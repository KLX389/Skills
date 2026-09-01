---
name: idea-maturity
description: Assess product ideas, feature requests, research findings, complaints, assignments, or backlog items when the user asks whether to do them, where they stand, what evidence is missing, how to prioritize them, or whether shipped work failed by idea or implementation. Use for product discovery and initiative readiness; do not use for ordinary implementation requests unless readiness, evidence, problem framing, or prioritization is in question.
---

# Idea Maturity

Turn raw initiative input into a maturity object, then into one concrete next action. On every pass, do two jobs: classify the material and route to the first stage that cannot honestly be affirmed.

## Use When

Use this skill when the user asks about product maturity, readiness, prioritization, missing evidence, or post-launch learning. It is especially relevant when a request names a solution before the problem, cites research without sizing the problem, asks to sort a backlog by readiness, or needs a neutral workshop structure.

Do not use it for a direct delivery task whose problem, priority, and acceptance criteria are already settled, unless the user asks to challenge readiness.

## Stage Map

| Stage | Blocking question | Primary reference | Output |
|---|---|---|---|
| 0 Input | What arrived, and does the ladder apply? | `reference/input-triage.md` | finding, mandate, form, gap card, entry stage |
| 1 Problem | Whose problem is this, and do we know it? | `reference/block-problem.md` | user problem, business problem, causal chain, confidence |
| 2 Relevance | How big is it? | `reference/block-relevance.md` | reach, frequency, severity, baseline, problem value |
| 3 Intent | What should be true instead? | `reference/block-intent.md` | solution-free intent, target, indicators, guardrails, stop rule |
| 4 Hypotheses | What could get us there? | `reference/phase-hypotheses.md` | at least two paths plus null variant, effect chains, test/build candidates |
| 5 Worth | Is the chosen path worth it? | `reference/phase-worth.md` | binding effort, business case, opportunity cost, judgement |

Read exactly one primary reference per pass: the blocking stage's file. You may also read a support reference when it is directly relevant:

- `reference/template-spec.md` for structured output, enum values, field ownership, or external handoff.
- `reference/mandate-systems.md` when mandate classification is unclear or multiple mandate types are compared.
- `reference/facilitation.md` for workshops and backlog reviews.
- `reference/edge-cases-and-workflows.md` for split, re-triage, rollback, tie-breaker, lost entry point, or post-launch review.
- `reference/example-briefing.md` when tone or output shape is uncertain.
- `reference/glossary.md` when terminology is disputed.

## Operating Rules

Work bottom-up. The status is the highest fully completed stage, not the highest stage someone has worked on. Material above the blocking stage is `work_at_risk` and must be labelled as such.

On the first encounter with an initiative, run stage 0 before any reformulation. Record the raw statement verbatim, classify mandate and form, run the five-minute K.O. check, create the gap card, and route to the entry stage. If the user already provided enough evidence for the entry stage, work that one primary stage in the same pass; otherwise end with the first question for that stage.

On later passes, do not rebuild stage 0. Update the existing object and gap card, then work the current blocking stage.

One pass should advance or clarify one stage. Do not fill downstream stages just because material exists there.

## Mandates

Stage 0 sets the mandate:

- `discretionary`: internally chosen value creation; full evidence ladder applies.
- `obligatory`: law, contract, platform, audit, or security requirement; stage 1 is not applicable, and stages 4-5 compare compliant paths.
- `maintenance`: operational necessity; stages 1-3 use risk and return-to-normal framing.

Obligatory work is scheduled as a capacity block with a deadline before discretionary initiatives are ranked. Maintenance work escalates when deferral increases operational risk.

## Evidence And Confidence

Every material claim from stage 1 onward carries one evidence rating:

| Rating | Meaning |
|---|---|
| `unknown` | nobody checked; this is a gap |
| `assumed` | plausible, but not observed |
| `reported` | someone said it or a secondhand source records it |
| `observed` | seen firsthand, usually qualitative |
| `validated` | quantitative data and qualitative picture agree |

Each claim needs a concrete source and method. A benchmark never rises above `assumed` for your own users. Interviews are normally `reported` unless the team directly observed the behavior.

Confidence is inherited from the weakest rated link in the current causal or effect chain. Later stages can lower confidence, never raise it above the earlier chain. A well-worked solution cannot repair a weakly evidenced problem.

## Briefing Before Solution

Stages 1-3 are the briefing. They are solution-free by default.

Allowed trace exceptions: `input.raw_statement`, `problem.reformulated_from`, and explicit `work_at_risk` notes may quote the proposed solution because traceability matters. No active problem, relevance, target, or intent field may depend on that solution being built.

Intent comes before hypotheses. The goal is derived from problem and relevance, not from an existing solution. The worth threshold is set before effort is read, so the threshold cannot adapt to the cost of a favored build.

## Output Contract

Respond in the language of the conversation. Human-facing labels may be translated at runtime. Machine field names and enum values stay in English.

Always include:

```text
Status: stage [completed] - [completed name/status] complete · stage [blocking] [blocking name] blocking
```

When a mandate skips a stage, show it explicitly as `not_applicable` in the gap card and route to the next applicable stage. When the initiative is closed, replace the blocking part with the judgement and reason.

Then provide only the fields needed for the worked stage. Use one field per line; values should be phrases, not essays. Later-stage material can appear only as `work_at_risk`.

End with one concrete next action, including owner and due date when the next action depends on another person. If owner or due date is unknown, make assigning them the next action rather than inventing them.

## Self-Check Before Sending

Before responding, verify:

```text
- [ ] One blocking stage is named, or one closure judgement is named.
- [ ] Exactly one primary stage file was worked.
- [ ] Optional support files were used only for the current case.
- [ ] No invented numbers; missing values use `unknown -> measure first`.
- [ ] Every material claim is rated `unknown`, `assumed`, `reported`, `observed`, or `validated`.
- [ ] Confidence is inherited from the weakest link and never asserted independently.
- [ ] Stages 1-3 contain no solution except trace fields and `work_at_risk` notes.
- [ ] Gaps have concrete next actions, or the next action is assigning owner/date.
- [ ] The answer does not hedge the verdict with "might", "perhaps", or "could be worth exploring".
```

If any item fails, revise before sending.
