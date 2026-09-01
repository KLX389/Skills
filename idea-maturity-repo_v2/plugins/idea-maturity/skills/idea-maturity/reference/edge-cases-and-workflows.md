# Edge Cases and Workflows

Scenarios that fall outside the standard single-initiative flow, and how to handle them.

## Contents

- Split: One problem or several?
- Re-triage: Later pass on a known initiative
- Rollback: When to change the blocking stage
- Tie-breaker: Equal-strength hypotheses
- Post-launch review: Was the idea wrong or the implementation?
- Lost entry point: Unknown blocks recovery

---

## Split: One problem or several?

### When to split

At any stage, you may discover that one initiative actually contains **two or more independent problems**, each with its own user group, business metric, or causal chain.

**Signal:** The causal chain branches (two unrelated causes → one user problem), or one user problem maps to two unrelated business metrics.

Example: "Checkout is too slow AND confusing" — two distinct problems (performance vs. comprehension) in different users (fast impatient users vs. inexperienced users).

### How to split

1. **In Stage 1:** If you recognize multiple problems, name them explicitly in `problem.cut.sub_problems: [problem 1, problem 2]` and set `cut.multiple_problems: true`.

2. **Create new objects:** Each sub-problem gets its own object with:
   - Unique `id` (parent.1, parent.2, etc., or new UUID)
   - Own `problem.reformulated_from` pointing to the original statement
   - Own gap card and entry stage

3. **Mark relationship:** In the parent object, add a note: "Split into [id.1], [id.2]". Keep the parent visible to avoid the same split being proposed twice.

4. **Status:** Parent object remains at the split point (stage 1, blocking). Do not advance it.

### Example workflow

**Input:** "Booking flow redesign — too slow and confusing"

**Stage 0:** Form = `solution_request`, mandate = `discretionary`, K.-o. = no

**Stage 1 discovery:**
- User problem A: Users get lost in multi-step checkout (segment: first-time mobile users)
- User problem B: Checkout takes 45 seconds vs. 15 seconds on competitor site (segment: experienced bookers)
- Business metric A: support tickets on checkout UI — cost + churn
- Business metric B: cart abandonment rate at final step — revenue

**Action:**
```
Status: stage 1 — problem blocking (decision: split)

Cut: multiple_problems = true
Sub-problems:
  1. "Confusing checkout UX" → id.checkout_ux
  2. "Slow checkout flow" → id.checkout_perf

Next: Assess each sub-problem independently
  - id.checkout_ux → proceed to stage 2 (relevance)
  - id.checkout_perf → proceed to stage 2 (relevance)
```

### Why split early

Splitting at stage 1 is cheap. Splitting after stage 3 means rewriting the intent. Splitting after stage 5 means discarding half a build plan.

---

## Re-triage: Later pass on a known initiative

### When to re-triage

- New information arrives (data that was `unknown` is now measured)
- Circumstances change (mandate, user segment, or business metric shifts)
- Status is disputed (someone thinks the blocking stage should be different)
- Timing: On request, not routinely. **Do not re-triage every cycle unless something actually changed.**

### First pass vs. later pass

| Item | First Pass (Stage 0) | Later Pass (Stage 0+) |
|------|------|------|
| **Input recording** | Full: raw statement, source, occasion, mandate, form, K.-o. | Update only if input changed; otherwise reuse |
| **Gap card** | Build from scratch | Update: which stage's status changed? Mark as `complete`, `partial`, or `open` |
| **Next action** | Calculate entry stage | Route to blocking stage (do not recalculate unless status changed) |

### How to update the gap card

The gap card is the **summary of what is still needed**. On a later pass:

1. **Do not rebuild it.** Add a dated note instead: "Update pass [date]: [what changed]"
2. **Mark stage status:**
   - `open` — nothing was done, preconditions are missing
   - `partial` — work exists but does not yet meet exit criteria
   - `complete` — all exit criteria are met
   - `not_applicable` — (mandate-dependent, see input-triage.md)

3. **Name the blocker:** Which stage cannot be honestly affirmed? That is your next target.

### Example: Re-triage after measurement

**First pass (2026-03-15):**
```
Stage 1 blocking
Gap card:
  Stage 1: open — problem known but no business metric named
  Stage 2: open — baseline unknown → measure first
  Stage 3: open — depends on 1 and 2
```

**Later pass (2026-04-20):**
```
Status: stage 1 — problem complete · stage 2 relevance blocking

Update (2026-04-20): Baseline measured, business metric named
Gap card:
  Stage 1: complete ✓ (updated 2026-04-20)
  Stage 2: open — frequency and severity not yet measured
  Stage 3: open — depends on 2
  
Measurement results:
  - Baseline (drop-off at step 3): 34% ✓
  - Reach: 20-30% of all abandoners (from 8 interviews) — origin set
  - Frequency: unknown → measure how often per user → [owner, due date]
```

**Next action:** Run frequency measurement (how often does this affect each user?), then route to stage 2 completion.

### What does NOT re-raise status

Work done above the blocking stage remains work-at-risk. If stage 2 is open and someone has produced stage 4 hypotheses, the status stays stage 1 blocking.

On a re-triage, do not ask: *"Should we promote the hypotheses now?"* Ask: *"What is still blocking the briefing from being complete?"*

---

## Rollback: When to change the blocking stage

### Downward rollback (late discovery of earlier problem)

You are at stage 3, producing the intent, when you discover: "Actually, we don't know if the business metric we named is the right one."

That is a stage 1 problem (causal chain incomplete). **Do not continue stage 3.**

**Action:**
1. Mark stage 3 as `work_at_risk` (material exists but preconditions are open)
2. Restate blocking stage as stage 1
3. Identify what stage 1 still needs
4. Next pass: work stage 1 only

**Example:**
```
Status (original): stage 2 complete · stage 3 intent blocking

Blocker discovered: The business metric (drop-off rate) was assumed, not validated.
We asked: "Do users abandon because of price confusion?" But we don't have evidence.
This is stage 1 — the causal chain is incomplete.

Status (after rollback): stage 2 complete · stage 1 problem blocking (reopened)
Work at risk: stage 3 intent output exists but rests on `assumed` evidence

Next action: Validate the causal link via [method], owner [name], due [date]
```

### What triggers rollback

- A weakest link is discovered to be weaker than stated
- Evidence is challenged and re-rated lower
- A causal link breaks (stage 1)
- A measurement contradicts the baseline (stage 2)
- An obligatory deadline is discovered to be legal or only organizational (mandate changes)

### What rollback is NOT

- Disagreement about the interpretation of evidence (that is a re-discussion, not a rollback)
- New information that strengthens a stage rather than weakening it (that is an update, not a rollback)
- Asking for more detail in the current stage (that is continuation, not rollback)

---

## Tie-breaker: Equal-strength hypotheses

### When hypotheses are equally strong

Stage 4 produces multiple hypotheses, each with:
- Same confidence level
- Same rough effort
- Different target contribution or different riskiest assumptions

How to decide?

### The tie-breaker sequence

1. **By confidence first** — higher rating wins. A hypothesis with `observed` evidence beats one with `assumed`, regardless of effort.

2. **By effort next** — cheaper wins. If confidence is equal, less effort is better (quicker feedback on the riskiest assumption).

3. **By riskiest assumption** — which one, if false, is more recoverable?
   - Assumption: "Users will adopt feature X" — if false, the whole thing fails
   - Assumption: "Implementation A is cheaper than B" — if false, you switch to B
   - The first is riskier; pick it second (after cheaper tests have eliminated other risks)

4. **By reversibility** — can you undo or pivot if wrong?
   - `switchable` — easy to turn off → OK to try
   - `partial` — some change sticks → higher bar
   - `irreversible` — committed → must be higher confidence

5. **By candidate type:**
   - `test` candidates (confidence ≤ `assumed`) are always cheaper first. Get evidence first, build later.
   - `build` candidates (confidence ≥ `reported`) only when you need the speed.

### What does NOT break ties

- Whoever advocated loudest
- How polished the concept is
- How long the team has worked on it
- Organizational politics

---

## Post-launch review: Was the idea wrong or the implementation?

### When to run this

After launch, when results differ from the intent.

**Question:** Did stage 5's `judgement: build` rest on correct assumptions, or did we build the right thing wrong (or wrong thing right)?

### What to check

Return to the template object and answer:

1. **Was intent hit?** Did the target metric reach the target value by the deadline?
   - Yes → Implementation worked. Assumptions held.
   - No → Either the intent was wrong, or the build was incomplete.

2. **Did guardrails hold?** Did any metric get worse than the limit?
   - Yes → Unintended side effect. The execution had issues.
   - No → Build did what was intended.

3. **Which stage 4 hypothesis was chosen?** Does the effect chain still hold?
   - Check each link: Did the behaviour change occur? Did it drive the metric?
   - A link breaking means stage 4's assumptions were weaker than stated.

4. **Did confidence track?** Was the weakest link in stage 1 actually the risk?
   - If confidence was `assumed` and the link held, that is good luck, not vindication.
   - If confidence was `assumed` and a later stage broke, that is what `assumed` means.

### Outputs for retrospective

Write a new object entry, parallel to the original:

```
id: [original_id]_postlaunch
launched: [date]
results:
  intent_met: yes | no
  target_value: [actual]
  guardrails_held: yes | no | [specific breaches]
  effect_chain_held: 
    - link 1: held / broken / untested
    - link 2: held / broken / untested
    - ...
  confidence_prediction_accuracy: [weakest link assumed, turned out true/false]
  
what_changed:
  stage_1_revision: [if problem understanding shifted]
  stage_2_revision: [if sizing was off]
  stage_4_revision: [if chosen hypothesis was wrong]

lessons:
  - [What did you learn about this domain?]
  - [What would you do differently?]
  - [What is still unknown?]
```

This becomes a data point for future initiatives in the same domain.

---

## Lost entry point: Unknown blocks recovery

### Scenario

You are at stage 3, producing the intent. You need stage 2's `problem_value` to set the `worth_threshold`. But stage 2 was never completed — nobody can say how big the problem is.

Now what?

### Forward recovery

1. **Pause stage 3.** Mark intent as `work_at_risk`.
2. **Route to stage 2.** Read `block-relevance.md`.
3. **Identify the cheapest measurement.** Is it funnel data? A query? A count?
4. **Name an owner and a due date.** "Measure X by [date], owner [name]."
5. **Come back to stage 3 after that measurement.**

You have not lost progress. You have clarified the path.

### Backward recovery (if entry stage is also unknown)

Scenario: An assignment arrives. Stage 0 is done. But mandate is misclassified (`discretionary` when it should be `obligatory`), so entry stage was calculated wrong.

**Discovery point:** Stage 1 exits with "We don't actually know whose problem this is" — everyone assumes it is someone else's.

**Action:**
1. Reopen stage 0. Re-classify the mandate.
2. Recalculate entry stage.
3. Produce new gap card.
4. Start over at the correct entry stage.

This is rare (mis-classifying mandate), but it happens when assignment details are unclear.

---

## Preventing edge-case confusion

### Checklist for ambiguous situations

```
- [ ] Is there one problem or more? (Split check)
- [ ] Is this a first pass or re-triage? (Update approach)
- [ ] Has a stage broken? (Rollback to lower stage)
- [ ] Are two paths truly equal? (Apply tie-breaker sequence)
- [ ] Has this shipped? (Post-launch review needed)
- [ ] Is an entry point missing? (Forward or backward recovery)
```

If none of these apply, work the blocking stage as normal.

### Communication

When an edge case emerges, **name it explicitly.** Do not pretend it does not exist or route around it.

Example:
> "This is a split point. The initiative contains two independent problems: X and Y. I'm creating two separate objects and proceeding with X first."

Or:
> "This is a rollback. We discovered stage 1's causal chain is incomplete. Restarting at stage 1, marking stage 3 work as provisional."

This makes the path visible and prevents confusion later.
