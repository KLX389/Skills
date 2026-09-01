# Stage 1 - Problem

## Purpose

Stage 1 establishes the problem in user or operational terms and connects it to a business consequence. Read this file when stage 1 is blocking.

For `obligatory` mandates, stage 1 is `not_applicable`: the obligation replaces problem evidence. For `maintenance`, use operational risk instead of a user problem.

## Reformulate Before Judging

If the input was a `solution_request` or a discretionary `assignment`, translate the proposed artifact back into the problem it is meant to address. The test question is:

> What happens if we do not build it?

Keep the original wording in `problem.reformulated_from`. This is a trace field and may name the solution. The active problem fields must not.

| Hidden solution | Problem formulation |
|---|---|
| "There is no filter" | Users cannot find the right item in long lists and abandon the task |
| "We need a dashboard" | The team cannot tell on Monday whether last week went well |
| "Onboarding needs a tutorial" | New users do not reach first success and churn in week 1 |

If nobody can say what users or operations fail to achieve, the problem is `unknown`; do not infer one from the proposed solution.

## Required Outputs

Produce three things. None substitutes for another.

1. User problem plus precise segment: what the group cannot achieve.
2. Business problem plus damaged metric: revenue, cost, risk, compliance exposure, or maintenance load.
3. Causal chain linking the two, with evidence rating, source, and method for each link.

For maintenance, replace user problem with operational risk and write the chain as system state -> service effect -> business damage.

## Evidence Rating

Evidence always has source and method. "Research" is not a source. "8 interviews with existing customers in March" is.

| Material | Rating | Missing for the next rating |
|---|---|---|
| Nobody checked | `unknown` | any evidence at all |
| Hunch, senior opinion, or competitor benchmark | `assumed` | observation from your own context |
| User statements, interview reports, support tickets, sales reports | `reported` | firsthand observation of the behavior |
| Session recording, usability test, operational log, analytics anomaly | `observed` | triangulation with the other side of the picture |
| Quantitative data and qualitative explanation agree | `validated` | nothing at this stage |

The common skipped step is `reported` to `observed`: teams hear that something happens, then behave as if they have seen it. Name the gap without dismissing the research.

## Causal Chain

Write the chain link by link:

```text
Inconsistent price display `validated` - screenshots
-> final price not visible early `observed` - flow review
-> user uncertainty `reported` - 8 interviews
-> drop-off at step 3 `assumed` - not yet linked
-> lost revenue `assumed` - inferred from drop-off
```

The weakest link is the lowest-rated link whose failure would break the chain. Name it by index and reason. The confidence of stage 1 is exactly that rating.

Chains longer than about five links usually hide multiple problems. Run the cut check.

## Cut Check

Ask whether the initiative contains one problem or several. Split when the chain branches, the segment changes, or one problem maps to unrelated business metrics.

If it splits, create separate objects for the sub-problems and keep the parent at the split point. See `edge-cases-and-workflows.md` for the workflow.

## Probing Questions

- "Who is affected, specifically?"
- "What can they not achieve today?"
- "What does the business lose if this stays as it is?"
- "Which metric shows that loss?"
- "Which link did you observe, and which link is inferred?"
- "Would the problem still exist if the proposed solution disappeared?"

## Exit Criteria

```text
- [ ] User problem is in user terms, not a missing feature.
- [ ] Segment is precise.
- [ ] Business problem names the metric it damages.
- [ ] Causal chain has at least two links.
- [ ] Every link has evidence, source, and method.
- [ ] Weakest link is named specifically.
- [ ] Confidence is derived from the weakest link.
- [ ] Cut check is decided; if multiple, split into separate objects.
```

If the weakest link is `unknown`, stage 1 remains blocking and the next action is to get first evidence. Otherwise route to stage 2.
