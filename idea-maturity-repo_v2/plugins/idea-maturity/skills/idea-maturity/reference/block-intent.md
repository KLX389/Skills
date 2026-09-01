# Stage 3 - Intent And Success Metrics

## Purpose

Stage 3 completes the briefing. It states what should be true instead, without naming a solution, and defines how success will be recognized.

Read this file when stage 3 is blocking. If the baseline or problem value from stage 2 is missing, route back to stage 2 instead of inventing a target.

## Intent Statement

Use this fill-in-the-blank as an acceptance test for stages 1 and 2:

```text
[user group] should achieve [measurable result], without [current problem].
```

| Blank | Source | Empty means |
|---|---|---|
| user group | `problem.segment` | affected group is unknown |
| current problem | `problem.user_problem` or maintenance risk | problem is still a solution in disguise |
| measurable result | `relevance.baseline_metric` and baseline | effect cannot be proven later |

Example:

```text
Customers with complaints should receive a helpful resolution within 60 minutes, without having to follow up repeatedly.
```

No solution appears in this sentence. If one does, move it to stage 4 as a hypothesis.

## Target Formula

The target is the measurable result, written directly under the statement:

```text
[metric] from [baseline] to [target] by [measurement date]
```

The metric should be user-near or operation-near: completion rate, resolution time, error rate, availability, time to first success. The business metric remains the reason the work matters, not the intent metric itself, unless the problem is already directly financial.

Missing pieces degrade the target:

| Missing | Degrades into |
|---|---|
| metric | activity or output |
| baseline | unfalsifiable wish |
| target value | direction without decision threshold |
| measurement date | no moment of truth |

## Worth Threshold

Ask:

> Above which problem value would this have been worth pursuing?

The worth threshold comes from `relevance.problem_value` or maintenance damage value. It must be set before reading effort or cost. Otherwise the threshold adapts to the effort of a favored solution.

The threshold is not the same as the user-near target. The target says what should change; the threshold says how valuable that change needs to be.

For `obligatory`, the threshold is `not_applicable`: compliance is not optional. Stage 5 will compare compliant paths by cost, risk, and deadline.

If the threshold is above the achievable problem value, close the initiative with `drop` before forming hypotheses.

## Indicators, Guardrails, Stop Criterion

- Leading indicator: early proxy that can steer action before the lagging target matures.
- Lagging indicator: the actual outcome measure or the closest attributable confirmation.
- Guardrail: metric that must not get worse, with numeric limit and direction.
- Stop criterion: result that ends or redirects the initiative. It is not a date.
- Attribution: control group, or a clean before/after window with confounders named.

Examples:

```text
Leading: share of affected users reaching price confirmation rises from 0% to 15% in week 1.
Lagging: checkout completion rises from 34% to 38% within 8 weeks.
Guardrail: refund-related support tickets do not rise above 120 per week.
Stop criterion: if completion stays below 35% after 8 weeks and guardrails hold, stop this path.
Attribution: before_after, excluding campaign weeks and payment outage days.
```

## Two Dates

`target.date` is the measurement deadline. `decision_date` is when someone decides whether to continue, change, or stop. They are often the same date, but not always.

For `obligatory`, the obligation supplies the target and legal deadline. Stages 1-2 only clarify scope and consequence.

## Probing Questions

- "How should it be instead - in one sentence, without naming the solution?"
- "Which user-near or operation-near metric moves if this succeeds?"
- "What is the current baseline and where does it come from?"
- "What target value would make the change meaningful?"
- "What must not get worse?"
- "Which result would stop or redirect the initiative?"
- "Who decides, and on what date?"

## Exit Criteria

```text
- [ ] Intent statement is complete and solution-free.
- [ ] Target formula has metric, baseline, target value, and measurement date.
- [ ] Metric is user-near or operation-near, not a broad business metric by default.
- [ ] Worth threshold is derived from problem value before effort is read, or `not_applicable` for obligatory work.
- [ ] Worth threshold is marked reachable or unreachable.
- [ ] At least one leading and one lagging indicator each has metric, baseline, target, and period.
- [ ] At least one guardrail has numeric limit and direction.
- [ ] Stop criterion is stated as a result.
- [ ] Attribution approach is decided or explicitly `unresolved`.
- [ ] Decider and decision date are set.
```

When these hold, the briefing is complete. It has an owner and handover target. Only now does stage 4 begin.
