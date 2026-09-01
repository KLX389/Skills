# Stage 4 — Hypotheses

## Contents
- What changes now
- The hypothesis template
- The effect chain
- Riskiest assumption and cheapest test
- Comparing the paths
- Build candidate or test candidate
- Exit criteria

Solution-bound, and **plural**. One intent carries several hypotheses; a hypothesis serves exactly one intent. When a hypothesis falls, the intent stands and the next one builds on the same briefing.

Requires a completed briefing. Without a fixed goal, hypotheses cannot be compared — only advocated for.

## What changes now

Stages 1–3 forbade naming solutions. Here solutions are the content. The discipline shifts: not *whether* to name one, but never to name only one. A single hypothesis is a warning sign, not a result — it means nobody chose, the first idea simply stayed.

Three directions that reliably produce alternatives:

- **Remove instead of add** — can the problem disappear by taking something away?
- **Change the sequence** — same elements, different order or timing
- **Change who does it** — automate, delegate, or let the user decide

## The hypothesis template

```
HYPOTHESIS
If we [change], then [behaviour change] among [group], because [reasoning].

EFFECT CHAIN
[change]              — [evidence] · [source]
  ↓
[behaviour change]    — [evidence] · [source]
  ↓
[intermediate effect] — [evidence] · [source]
  ↓
[business metric]     — [evidence] · [source]

Weakest link: [which] — [why]
Confidence: [rating of the weakest link]

RISKIEST ASSUMPTION
[The one assumption whose falseness breaks the chain]
Cheapest test: [type] — [effort] — [what it decides]

ROUGH EFFORT
[T-shirt size, for comparison only]
TARGET CONTRIBUTION
[share of the intent's target, roughly]
```

## The effect chain

**It must end on a business metric**, not on the behaviour change. This closes the hole that otherwise opens between stages 3 and 5: seconds get measured, money gets calculated, and the link between them appears nowhere.

> Pre-filled payment details `validated` → booking time −10 s `observed` → fewer drop-offs at the payment step `assumed` → completion rate +2 pp `assumed`

Here the third link is the bet: the tests show time saved, not abandonment behaviour. That the duration *causes* the drop-offs is assumption — price or trust would do as well.

**Confidence is the weakest link's rating.** It can never exceed `problem.confidence` from stage 1: a well-worked solution cannot improve the evidence for a weakly evidenced problem. A later stage may lower confidence, never raise it.

## Riskiest assumption and cheapest test

The riskiest assumption is the one that, if false, leaves nothing standing — not the most uncertain, not the easiest to check. Find it by asking of each link: *if this is wrong, does anything survive?*

| Test | Costs | Use when |
|---|---|---|
| Data check | hours | The behaviour already happens and is already logged |
| Fake door | days | The assumption is about demand or intent |
| Prototype with 5 users | days | The assumption is about comprehension |
| Wizard of Oz | 1–2 weeks | The assumption is about value and the mechanics are expensive |
| Full build | a quarter | Only when the above cannot answer the question |

## Comparing the paths

Effort here is **rough and only for ordering**. Estimating precisely would be wasted, because most hypotheses drop out. The binding estimate belongs to stage 5, for the chosen path only.

| Hypothesis | Effort | Weakest link | Target contribution |
|---|---|---|---|
| Pre-fill payment details | M | `assumed` | ~60 % of the target |
| Express checkout | L | `observed` | ~90 % |
| Show payment step later | S | `assumed` | unclear |
| Do nothing | — | — | comparison baseline |

**"Do nothing" is mandatory.** A business case without a null variant compares against nothing.

Effort alone does not sort the list. A cheap hypothesis resting on `assumed` is not better than an expensive one resting on `validated` — it is cheaper *and* less certain. Both values are read together.

**If two hypotheses are equally strong,** apply the tie-breaker sequence: confidence first, effort next, riskiest assumption, reversibility, candidate type. See `edge-cases-and-workflows.md` — "Tie-breaker: Equal-strength hypotheses".

## Build candidate or test candidate

```
confidence ≤ assumed   → candidate_type: test
confidence ≥ reported  → candidate_type: build
```

A test candidate skips stage 5. The next step is the cheapest test of its riskiest assumption, not implementation. If that test succeeds, confidence rises and the hypothesis re-enters as a build candidate.

This is the rule that stops well-formatted guesses from being scheduled.

## Exit criteria

```
- [ ] At least two hypotheses plus the null variant
- [ ] Each with a full effect chain ending on a business metric
- [ ] Each link rated; weakest link named
- [ ] Confidence derived, and not higher than problem.confidence
- [ ] Riskiest assumption and cheapest test per hypothesis
- [ ] Rough effort and target contribution per hypothesis
- [ ] Candidate type derived for each
- [ ] One path chosen, or a test scheduled
```

If the chosen path is a test candidate, stop here: the next action is the test. Otherwise route to stage 5 for the chosen hypothesis only.

**Note on mandate:** For `discretionary`, hypotheses compare full solution space. For `obligatory`, hypotheses compare only the "how" — multiple compliant paths, not whether to comply. For `maintenance`, hypotheses compare paths to system stability. See `mandate-systems.md` for how mandate affects this stage.
