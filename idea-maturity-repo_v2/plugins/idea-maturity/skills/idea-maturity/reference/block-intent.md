# Stage 3 — Intent & Success Metrics

## Contents
- The fill-in-the-blank as acceptance test
- The target formula
- Which metric belongs in the intent
- The worth threshold
- Indicators, guardrails, stop criterion
- Two different dates
- Probing questions
- Exit criteria

Part three of the briefing, and the seal on it. Goal-bound and solution-free: the intent survives every discarded solution.

## The fill-in-the-blank as acceptance test

> [user group] should achieve [measurable result], without [current problem].

This is not a form. Every blank that cannot be filled names the block still open:

| Blank | Comes from | Empty means |
|---|---|---|
| User group | 1 · segment | You don't know who is affected |
| Current problem | 1 · user problem | You have a solution, not a problem |
| Measurable result | 2 · baseline | You cannot prove an effect later |

Whoever writes the sentence in one go has evidenced the blocks beneath it. Whoever stalls knows immediately where.

Example: *"Customers with complaints should receive a helpful resolution within 60 minutes, without having to follow up repeatedly."*

**No solution appears in this sentence.** If one does, the phase boundary has been breached — the artefact belongs in stage 4.

## The target formula

The binding part, written directly beneath the statement:

> [metric] from [baseline] to [target] by [date]

Missing any of the three parts and it is not a target:

| Missing | What it degrades into |
|---|---|
| **What** | An activity. "We launch X" is an output, not an outcome change. |
| **How much** | Unfalsifiable. "More bookings" is met by a single extra booking. Needs baseline *and* target. |
| **By when** | No moment of truth. The effect is awaited indefinitely and nothing is switched off. |

## Which metric belongs in the intent

**The user-near metric, not the business metric.** Revenue depends on too much to be attributed to one measure. Customer satisfaction, completion rate, resolution time — those move because of the initiative.

The business metric is the *why* behind the intent. The link between them is the effect chain in stage 4, and it carries its own confidence. Putting revenue in the intent hides that link and makes the target unattributable.

## The worth threshold

> **Above which value would it have been worth it?**

Derived from `relevance.problem_value` — what it is worth to be rid of the problem — **never from implementation cost**. This block must not read effort or cost fields at all. Otherwise the target adapts to what someone already wanted to build.

If the threshold lies above what is realistically achievable, the initiative is refuted here, before any hypothesis is formed. That is the cheapest possible moment. Record it and end.

An estimated target is fine when labelled `proposed` or `confirmed`.

## Indicators, guardrails, stop criterion

- **Leading indicator** — early signal, fast but a proxy: *"Share of users opening the new comparison rises from 0 to above 15 % in week 1."*
- **Lagging indicator** — the actual result, reliable but slow: *"Completion rate rises from 34 % to 38 % within 8 weeks of launch."*
- **Guardrail** — what must not get worse, at least one, with a numeric limit: *"Support tickets do not exceed 120 per week over the same period."* A guardrail without a number is decoration.
- **Stop criterion** — which *result* ends the initiative. Written before the start it is a decision rule; written afterwards it is an excuse. If nobody can name a result that would stop it, the initiative is not being tested but defended.
- **Attribution** — control group, or a clean before/after window with the confounders named. Decided afterwards, attribution is chosen to fit the outcome.

## Two different dates

`target.date` is the **measurement deadline** — when the target should be reached. `decision_date` is when someone decides on continuation. Usually the same, not necessarily. The stop criterion is a *result* and can occur at any time before either.

For `obligatory` demand the intent is given in advance: the obligation is the goal, its legal deadline the date. The block is then filled top-down and stages 1–2 only clarify scope.

## Probing questions

- "How should it be instead — in one sentence, without naming the solution?"
- "Which metric moves if this succeeds?"
- "Above which value would the effort have been worth it?"
- "What must not get worse in the process?"
- "Which result would convince you the idea was wrong?"
- "Who decides on this, and when?"

## Exit criteria

```
- [ ] Intent statement complete, naming no solution
- [ ] Target formula with metric, baseline, target, date
- [ ] Metric is user-near, not the business metric
- [ ] Worth threshold derived from the problem value, marked reachable or not
- [ ] At least one leading and one lagging indicator, each a full formula
- [ ] At least one guardrail with a numeric limit
- [ ] Stop criterion stated as a result
- [ ] Attribution decided
- [ ] Decider and decision date set
```

When these hold, **the briefing is complete**. It has an owner and a handover date, and it stands on its own even if no hypothesis is ever formed. Only now does stage 4 begin.

**Note on mandate:** For `discretionary`, intent is discovered in conversation. For `obligatory`, intent is given in advance (the obligation is the goal). For `maintenance`, intent is risk mitigation (return to normal). See `mandate-systems.md` for how mandate affects this stage.
