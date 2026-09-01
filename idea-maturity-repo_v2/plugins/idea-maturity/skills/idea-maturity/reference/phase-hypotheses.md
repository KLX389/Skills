# Stage 4 - Hypotheses

## Purpose

Stage 4 compares solution paths against a completed briefing. It is solution-bound and plural: one intent carries several hypotheses; one hypothesis serves exactly one intent.

Read this file when stage 4 is blocking. If the briefing is incomplete, route back to the first open stage in 1-3.

## What Changes Here

Stages 1-3 kept solutions out. Stage 4 brings solutions in deliberately. The discipline is now to avoid having only one.

Produce at least two plausible paths plus the null variant. A single hypothesis means the first idea stayed, not that comparison happened.

Reliable ways to generate alternatives:

- remove instead of add
- change sequence, timing, or defaults
- change who does the work: user, team, automation, partner
- reduce scope to the smallest target-contributing path

## Hypothesis Template

```text
HYPOTHESIS
If we [change], then [behavior or operational change] among [group], because [reasoning].

EFFECT CHAIN
[change]              - [evidence] · [source]
-> [behavior change]  - [evidence] · [source]
-> [intermediate]     - [evidence] · [source]
-> [business metric]  - [evidence] · [source]

Weakest link: [which] - [why]
Confidence: [rating of the weakest link, not above problem.confidence]

RISKIEST ASSUMPTION
[assumption whose falseness collapses the path]
Cheapest test: [type] - [effort] - [what it decides]

ROUGH EFFORT
[XS/S/M/L/XL, for ordering only]
TARGET CONTRIBUTION
[share of intent target, as range or phrase]
```

## Effect Chain

The effect chain must end on the business metric from stage 1 or the mandate consequence. Stopping at a behavior change leaves the business case unconnected.

Example:

```text
Pre-filled payment details `validated` - account data exists
-> booking time -10s `observed` - usability test
-> fewer payment-step exits `assumed` - not yet measured
-> completion rate +2 pp `assumed` - inferred
```

The weakest link is the current confidence. It cannot exceed stage 1 confidence. It may be lower if the solution path introduces a weaker assumption.

## Riskiest Assumption And Cheapest Test

The riskiest assumption is the one whose falseness collapses the path, not merely the one with the lowest evidence rating.

| Test | Typical effort | Use when |
|---|---|---|
| `data_check` | hours | behavior already happens and is logged |
| `fake_door` | days | demand or intent is unknown |
| `prototype` | days | comprehension or workflow fit is unknown |
| `wizard_of_oz` | 1-2 weeks | value can be tested manually before automation |
| `full_build_test` | quarter | cheaper tests cannot decide the assumption |

## Comparing Paths

Show confidence, effort, riskiest assumption, and target contribution side by side. Do not multiply them.

```text
Hypothesis              Effort  Confidence  Target contribution  Candidate
Pre-fill details        M       assumed     about 60%            test
Express checkout        L       observed    about 90%            build
Move payment later      S       assumed     unclear              test
Null variant            -       -           no change            baseline
```

The null variant is mandatory because it shows what happens if nothing changes. The final business case should still compare the chosen path against the best viable alternative, not automatically against null.

## Candidate Type

```text
confidence <= assumed  -> candidate_type: test
confidence >= reported -> candidate_type: build
```

`candidate_type: build` means the path is eligible for stage 5 worth assessment. It is not approval to schedule implementation. Stage 5 can still return `build`, `test`, `defer`, or `drop`.

A `test` candidate stops at stage 4. The next action is the cheapest test of the riskiest assumption. If the test succeeds, update the evidence and re-enter stage 4 or stage 5 as appropriate.

## Exit Criteria

```text
- [ ] At least two hypotheses plus the null variant.
- [ ] Each hypothesis maps to exactly one intent.
- [ ] Each effect chain ends on the business metric or mandate consequence.
- [ ] Every link has evidence and source.
- [ ] Weakest link and confidence are derived and not above problem confidence.
- [ ] Riskiest assumption and cheapest test are named per hypothesis.
- [ ] Rough effort and target contribution are shown per hypothesis.
- [ ] Candidate type is derived per hypothesis.
- [ ] One path is chosen for stage 5, or a test is scheduled.
```

If the chosen path is a test candidate, stop here. Otherwise route to stage 5 for the chosen path only.
