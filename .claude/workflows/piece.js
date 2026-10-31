export const meta = {
  name: 'piece',
  description: 'Run one piece through its stages, in the order stage_gate.py allows, stopping at every human decision',
  whenToUse: 'Start or resume a piece by slug, after Decision 1 is recorded with stage_gate.py start <slug> --bank <id>. Re-run it after each decision; it picks up where the files say the piece stands.',
  phases: [
    { title: 'Gate', detail: 'stage_gate.py says where the piece stands; the workflow obeys it' },
    { title: 'Stage', detail: 'run the one stage the gate named' },
  ],
}

// Args: the piece slug, as a string ("<slug>" or "<slug> --no-screenshots") or { slug, noScreenshots }.
// --no-screenshots is passed through to stage_gate.py only when a person gives it; the gate also
// requires the batch's conditions block to record the waiver (runs/README.md#screenshots).
const argText = typeof args === 'string' ? args.trim() : ''
const slug = argText ? argText.split(/\s+/)[0] : (args && args.slug)
const noShots = argText ? /(^|\s)--no-screenshots(\s|$)/.test(argText) : !!(args && args.noScreenshots)
const GATE_FLAGS = noShots ? ' --no-screenshots' : ''
if (!slug || !/^[a-z0-9-]+$/.test(slug)) {
  return { stopped: 'no slug', reason: 'Run as /piece <slug>, with a slug of lowercase letters, digits and hyphens.' }
}

const MAX_STEPS = 30        // backstop; a whole piece is about 14 stages
const MAX_EDIT_ROUNDS = 2   // then a person

const GATE = {
  type: 'object',
  properties: { next: { type: 'string' }, state: { type: 'string' }, detail: { type: 'string' } },
  required: ['next', 'state', 'detail'],
}
const RESULT = {
  type: 'object',
  properties: { status: { type: 'string', enum: ['ok', 'fail', 'blocked'] }, summary: { type: 'string' } },
  required: ['status', 'summary'],
}
const REPORT = 'Reply with status ok if the stage finished, fail if it went wrong, or blocked if an input was missing or wrong, and a one-line summary.'

// The checkpoint. The workflow never decides where to start or what comes next: this does.
const gate = (i) => agent(
  `Run exactly this command from the repo root, and nothing else: python scripts/stage_gate.py ${slug} --json${GATE_FLAGS}\n` +
  'It exits 3 when a person is needed and 4 when blocked; that is expected, not an error. ' +
  'Copy the top-level "next", "state" and "detail" fields from its JSON output exactly. Change no file.',
  { label: `gate ${i}`, phase: 'Gate', schema: GATE, effort: 'low' })

const skill = (name, extra) => agent(
  `Read runs/${slug}-piece.json. Invoke the Skill tool with skill "${name}" and args "${slug}` +
  `${extra || ''}" (add " --practice" after the slug if the manifest has "practice": true and the skill takes it). ` +
  `Follow the skill to the end. ${REPORT}`,
  { label: name, phase: 'Stage', schema: RESULT })

const STAGES = {
  research: async () => {
    await agent(`Run exactly: python scripts/timing.py ${slug} research start`, { label: 'timing', phase: 'Stage', effort: 'low' })
    const r = await agent(
      `Run Stage 1 RESEARCH. The piece slug is ${slug}. The buyer question is "question" in runs/${slug}-piece.json, ` +
      `and its long form is that bank row's ai_form in bank/questions.csv. Write runs/${slug}-research.md as your ` +
      `instructions say, and nothing else. ${REPORT}`,
      { label: 'research', phase: 'Stage', schema: RESULT, agentType: 'researcher' })
    await agent(`Run exactly: python scripts/timing.py ${slug} research end`, { label: 'timing', phase: 'Stage', effort: 'low' })
    return r
  },
  truth: () => agent(
    `Write the truth spec for piece ${slug}, then compute it.\n` +
    `1. Run: python scripts/timing.py ${slug} truth start\n` +
    `2. Read section 7 of runs/${slug}-research.md, the docstring of scripts/ground_truth_from_spec.py, and specs/rehearsal-truth.json as an example of the format.\n` +
    `3. Write specs/${slug}-truth.json: one row per test question, worded exactly as in section 7, with its table, filter, formula, unit, grain, family and signals. ` +
    'Add a row, with "asked": false, for every plausible rival reading of a question (all orders vs delivered, with or without freight), so rival definitions are in before the run. ' +
    'Mark follow-ups with "follow_up_of". Every row is one number: if a test question would produce a table or list, stop and report blocked, naming it. Never set "reviewed_by": a person sets it.\n' +
    `4. Run: python scripts/ground_truth_from_spec.py specs/${slug}-truth.json\n` +
    `5. Run: python scripts/timing.py ${slug} truth end\n${REPORT}`,
    { label: 'truth', phase: 'Stage', schema: RESULT }),
  run: (detail) => agent(
    `Run the evidence run for piece ${slug}, as your instructions say. The gate says: "${detail}". ` +
    `The conditions block for this batch is already in runs/${slug}-run.md; don't change it. Ask every test question in ` +
    `section 7 of runs/${slug}-research.md that has no entry in this batch yet. ${REPORT}`,
    { label: 'run', phase: 'Stage', schema: RESULT, agentType: 'dot-runner' }),
  mark: (detail) => agent(
    `1. Run: python scripts/timing.py ${slug} mark start\n2. Run exactly the command in this gate detail: ${detail}\n` +
    `3. Run: python scripts/timing.py ${slug} mark end\nChange no other file. ${REPORT}`,
    { label: 'mark', phase: 'Stage', schema: RESULT, effort: 'low' }),
  outline: () => skill('outline'),
  draft: () => skill('draft'),
  'seo-geo': () => skill('seo-geo'),
  reviews: (detail) => agent(
    `1. Run: python scripts/timing.py ${slug} reviews start\n` +
    `2. The gate says: "${detail}". For each reviewer it names, one at a time, run: python scripts/run_reviewer.py <reviewer> ${slug}\n` +
    `3. Run: python scripts/timing.py ${slug} reviews end\n` +
    `Never start a reviewer any other way, and never add anything to what run_reviewer.py passes. ${REPORT}`,
    { label: 'reviews', phase: 'Stage', schema: RESULT }),
  revise: () => agent(
    `Revise piece ${slug} after its blind reviews.\n1. Run: python scripts/timing.py ${slug} revise start\n` +
    `2. Read reviews/${slug}/reader.md, fact-checker.md and lift-tester.md, then pieces/${slug}.md, figures/${slug}-figures.csv and runs/${slug}-run.md.\n` +
    `3. Fix all three of the reader's stopping points, and every fact-checker problem, in pieces/${slug}.md. ` +
    'Use only numbers in the figures file and quotes word for word from the run file. Never set or change title_approved_by.\n' +
    `4. Write reviews/${slug}/revisions.md: one line per point, saying how it was fixed, or one line on why it stands.\n` +
    `5. Run: python scripts/review_copy.py ${slug}\n6. Run: python scripts/timing.py ${slug} revise end\n${REPORT}`,
    { label: 'revise', phase: 'Stage', schema: RESULT }),
  edit: (detail, round) => agent(
    `Edit round ${round} of ${MAX_EDIT_ROUNDS} for piece ${slug}.\n1. Run: python scripts/timing.py ${slug} edit start\n` +
    `2. The gate reports these check_piece.py FAILs: ${detail}\n` +
    `3. Fix only those, in pieces/${slug}.md, using only numbers in figures/${slug}-figures.csv. Change nothing else.\n` +
    `4. Run: python scripts/check_piece.py pieces/${slug}.md and report what still FAILs.\n` +
    `5. Run: python scripts/timing.py ${slug} edit end\n${REPORT}`,
    { label: `edit ${round}`, phase: 'Stage', schema: RESULT }),
  linkedin: () => skill('linkedin'),
  export: () => skill('export'),
}

const steps = []
let last = null
let editRounds = 0

for (let i = 1; i <= MAX_STEPS; i++) {
  const g = await gate(i)
  if (!g) return { slug, stopped_at: 'gate', state: 'failed', reason: 'stage_gate.py could not be read', steps }
  log(`gate ${i}: ${g.next} (${g.state}) — ${g.detail}`)

  if (g.state === 'waiting' || g.state === 'blocked') {
    return { slug, stopped_at: g.next, state: g.state, reason: g.detail, steps }
  }
  if (g.state === 'done') return { slug, complete: true, steps }
  if (g.state !== 'next' || !STAGES[g.next]) {
    return { slug, stopped_at: g.next, state: g.state, reason: `the workflow has no stage "${g.next}"; a person decides`, steps }
  }

  if (g.next === 'edit') {
    editRounds += 1
    if (editRounds > MAX_EDIT_ROUNDS) {
      return { slug, stopped_at: 'edit', state: 'needs a person',
        reason: `FAILs remain after ${MAX_EDIT_ROUNDS} fix rounds: ${g.detail}`, steps }
    }
  } else if (last === `${g.next}|${g.detail}`) {
    return { slug, stopped_at: g.next, state: 'no progress',
      reason: `the ${g.next} stage ran, but the gate still says: ${g.detail}`, steps }
  }
  last = `${g.next}|${g.detail}`

  const r = await STAGES[g.next](g.detail, editRounds)
  steps.push({ stage: g.next, status: r ? r.status : 'agent failed', summary: r ? r.summary : '' })
  if (!r || r.status !== 'ok') {
    return { slug, stopped_at: g.next, state: r ? r.status : 'agent failed', reason: r ? r.summary : 'the stage agent did not return', steps }
  }
}
return { slug, stopped_at: 'step limit', state: 'needs a person', reason: `${MAX_STEPS} steps without reaching a stop`, steps }
