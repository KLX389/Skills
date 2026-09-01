# Stage 2 - Relevance

## Purpose

Stage 2 sizes the problem. This is where many initiatives actually sit: the problem exists, but nobody knows how much it weighs.

Read this file when stage 2 is blocking.

## Required Outputs

| Value | Question | Standard |
|---|---|---|
| Reach | How many users, accounts, sessions, systems, or cases are affected? | number or range with denominator |
| Frequency | How often does it occur? | count per user, session, week, month, incident, or release |
| Severity | What happens when it occurs? | consequence, not adjective |
| Baseline | Today's value of the damaged metric | measured value, period, and origin |
| Problem value | What is being rid of the problem worth? | shared portfolio unit, usually money/year, with calculation |

Reach and severity make initiatives comparable. Without both, prioritization falls back to persuasion.

## Number-With-Origin Rule

Every numeric or sized field needs value, origin, and measurement window:

```text
Reach: 20-30% of checkout abandoners
Origin: Q2 funnel data plus 8 interviews with first-time bookers
Window: 2026-04-01 to 2026-06-30
```

A number without origin does not count. An origin without a number is stage 1 material. Use ranges when precision is not earned.

Never invent plausible figures. Use `unknown -> measure first` and add an `open_measurements` item with method, owner, and due date.

## Fast Sizing Without Faking

Use the cheapest valid source first:

1. Existing funnel, event, revenue, reliability, or operations data.
2. Ticket, complaint, sales, or support volume as lower bound.
3. Segment arithmetic: observed share in small sample times affected population, stated as range.
4. Existing research or CS reports as directional evidence.
5. A deliberate measurement when none of the above answers the field.

## Problem Value

Convert the sized problem into the portfolio's shared unit and show the calculation. This value is the ceiling for the worth threshold in stage 3; it is not a solution business case.

If conversion is genuinely impossible, write `not_convertible` and rank the initiative separately. Do not invent a conversion rate to force comparability.

For `obligatory`, problem value is the avoided consequence of non-compliance: fine, contract loss, app store exclusion, audit failure. Name the consequence rather than inventing a probability. For `maintenance`, use avoided operational damage.

## Unknown Baseline Or Value

A measurement plan is useful, but it does not complete stage 2. If reach, frequency, severity, baseline, or problem value is `unknown`, stage 2 remains blocking until the measurement or explicit non-convertible decision exists.

Write:

```text
Baseline: unknown -> measure first
Open measurement: query checkout_step_abandonment by step; owner Data; due 2026-09-08
```

Without a baseline, stage 3 cannot set a falsifiable target. Without problem value or an explicit `not_convertible`, stage 3 cannot set a worth threshold.

## Probing Questions

- "How many are affected - ten percent or eighty?"
- "What is that estimate based on?"
- "What is today's value of the metric that suffers?"
- "How often does it occur per user, session, or period?"
- "What happens when it occurs - detour, abandonment, cost, risk, or outage?"
- "What would it be worth to be rid of this problem?"

## Exit Criteria

```text
- [ ] Reach as number or range, with denominator, origin, and period.
- [ ] Frequency with origin and period.
- [ ] Severity as consequence, with origin.
- [ ] Baseline metric and value measured, with origin and period.
- [ ] Problem value calculated in the shared unit, or explicitly `not_convertible`.
- [ ] Estimates marked as estimates and kept as ranges where appropriate.
- [ ] No required value is `unknown` unless stage 2 remains blocking with an open measurement.
```

If reach and severity together do not justify further effort, close with `drop` at stage 2. If new sizing contradicts the stage 1 chain, read `edge-cases-and-workflows.md` and roll back to stage 1.
