# Stage 0 - Input

## Purpose

Stage 0 records what arrived and decides how the maturity ladder applies. It does not reformulate the problem. Reformulation belongs to stage 1 so the original wording stays traceable.

Use this file on the first encounter with an initiative, or when a later pass explicitly reopens mandate or form classification.

## What This Stage Produces

- Raw statement, verbatim, with source and occasion
- Mandate and reasoning
- Form and reasoning
- Five-minute K.O. check
- Gap card across the applicable stages
- Entry stage and expectation statement

## Mandate

| Value | Source | Recognizable by |
|---|---|---|
| `discretionary` | internal choice | no binding external sender; upside or opportunity cost drives the work |
| `obligatory` | law, contract, platform, audit, regulator, formal security requirement | external sender, deadline, and consequence for non-compliance |
| `maintenance` | operational necessity | end-of-life, migration, degradation, outage risk, security exposure without a formal compliance mandate |

The mandate decides which stages exist. Do not send a legal deadline through the full discretionary evidence ladder. Do not label customer pressure `obligatory` unless a contract, platform rule, law, or comparable binding requirement exists.

| Stage | `discretionary` | `obligatory` | `maintenance` |
|---|---|---|---|
| 1 Problem | full | `not_applicable` - obligation replaces problem evidence | reduced to operational risk |
| 2 Relevance | full sizing | scope of obligation and consequence | risk, frequency, severity, damage value |
| 3 Intent | discovered from problem and relevance | given by obligation and deadline | return to normal or reduce risk |
| 4 Hypotheses | compare solution space | compare compliant paths only | compare stability paths |
| 5 Worth | value against effort | cheapest compliant path | avoided damage against effort and urgency |

Read `mandate-systems.md` when the classification is unclear or when a backlog mixes mandate types.

## Form

| Value | Recognizable by | Entry point |
|---|---|---|
| `observation` | a measured or witnessed state, no judgement and no proposal | stage 1 |
| `complaint` | emotion, dissatisfaction, or judgement, usually secondhand | stage 1 |
| `problem_claim` | shortfall in user or operational terms, no proposed artifact | stage 1 |
| `solution_request` | names an artifact, feature, process, or build request | stage 1, reformulate first |
| `hypothesis` | causal claim linking intervention and effect | stage 1, verify backwards |
| `assignment` | decision already taken, owner or deadline implied | stage 1 for discretionary/maintenance; stage 2 if obligatory |

Detection order: settled decision or deadline; binding mandate; artifact or build request; causal claim; measured or witnessed state; complaint; shortfall. A number does not make the input an `observation` if the same sentence asks for a solution.

## K.O. Check

Ask once: does anything already known make the initiative impossible or invalid - legally, contractually, technically, ethically, or organizationally?

This check is limited to known blockers. Do not estimate effort or dependencies here.

If a blocker is known, close the object immediately with a documented `drop` reason. Keep the object so the same initiative does not return without the blocker being addressed.

## Gap Card

Use the gap card to show which stages are complete, open, partial, not applicable, or work at risk.

```text
FINDING

Received:   "[raw statement, verbatim]"
            - [source], [occasion], [date]

Mandate:    [value] - [reasoning]
Form:       [value] - [recognition signal]
K.O.:       [no known blocker | blocker and reason]

GAP CARD

0 Input        complete     recorded and classified
1 Problem      open         [reasoning or not_applicable]
2 Relevance    open         [reasoning]
3 Intent       open         [reasoning]
4 Hypotheses   partial      [material exists but lower stages are open]
5 Worth        open         [depends on 3 and 4]

Entry: stage [n] - [what happens there]
```

Use `partial` only when material exists but fails the exit criteria. Use `work_at_risk: true` when material belongs above the blocking stage.

## Expectation Statement

Calculate the expectation from mandate, form, and open stages. It should say what arrived, which blocks remain, what the person will hold after those blocks are closed, and the first question of the entry stage.

Example:

> This is a solution request. The solution is explicit; the problem behind it is not. Three briefing blocks are still open: problem, relevance, and intent. We start at stage 1: what happens if you do not build the proposed overview?

Keep it short for obligatory work: the decision is not whether to comply, but how to do so.

## Exit Criteria

```text
- [ ] Raw statement recorded verbatim with source and occasion.
- [ ] Mandate set with reasoning.
- [ ] Form set with recognition signal.
- [ ] K.O. check answered.
- [ ] Gap card covers every applicable stage.
- [ ] Entry stage follows mandate and form.
- [ ] Expectation ends with the first question or next action for the entry stage.
- [ ] No problem reformulation was performed in stage 0.
```

## Special Cases

For a later pass on a known initiative, read `edge-cases-and-workflows.md` and update the existing gap card instead of rebuilding it.

If an `assignment` arrives and mandate is unclear, ask what happens if the team does not do it. Legal, contractual, platform, audit, or formal security consequence means `obligatory`; system degradation means `maintenance`; lost upside means `discretionary`.
