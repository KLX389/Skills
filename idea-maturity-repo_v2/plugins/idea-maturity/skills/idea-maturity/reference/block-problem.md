# Stage 1 — Problem

## Contents
- Reformulating first
- What must be produced
- Rating the evidence
- The causal chain
- The cut
- Probing questions
- Exit criteria

Part one of the briefing. Read this when stage 1 is blocking.

## Reformulating first

If the input was a `solution_request` or `assignment`, the solution has to be translated back into a problem before anything else. The test question:

> **What happens if we do not build it?**

The answer is the problem. Keep the original wording in `reformulated_from` so the translation stays visible.

| Hidden solution | Actual problem |
|---|---|
| "There's no filter" | Users can't find the right item in long lists and drop out |
| "We need a dashboard" | The team can't tell on Monday whether last week went well |
| "Onboarding needs a tutorial" | New users don't reach their first success and churn in week 1 |

If the rewrite is impossible because nobody knows what users were trying to do, that is the finding: the problem is `unknown`.

## What must be produced

Three things, none substituting for another:

1. **User problem** plus **segment** — what users cannot achieve. "Users" is rarely the right unit; "first-time bookers without an account" is.
2. **Business problem** plus the **metric that suffers** — missing revenue, higher cost, risk, maintenance load.
3. **The causal chain** connecting the two, link by link.

Only one of the first two means either building something users love that earns nothing, or the reverse.

## Rating the evidence

Evidence carries two parts, always: the **source**, named concretely — not "research" but "8 interviews, March, existing customers" — and the **method**.

| What you have | Rating | What is missing |
|---|---|---|
| A hunch, however senior | `assumed` | Any observation at all |
| Benchmark — "competitors do it" | `assumed` | Says nothing about *your* users |
| Support tickets, sales reports, users telling you | `reported` | Firsthand observation |
| Interviews describing the problem | `reported` | Still secondhand: you heard it, you did not see it |
| Usability test or session recording of the behaviour | `observed` | The quantitative side — how often, how many |
| Analytics anomaly on its own | `observed` | The qualitative side — why the number looks like that |
| Behaviour data and qualitative picture agreeing | `validated` | Nothing at this stage |

Nobody has checked at all → `unknown`. The gap between `unknown` and `assumed` matters: the first is an absence, the second is a bet, and they lead to different next steps.

The jump from `reported` to `observed` is the one teams skip, and the cheapest to close: five sessions of watching the behaviour usually settle what a month of debate cannot.

## The causal chain

Write it out and rate **each link separately**:

> Inconsistent price display `validated` → final price not visible early `observed` → user uncertainty `reported` → drop-off at step 3 `assumed` → lost revenue `assumed`

The endpoints are the well-defended part. The guessing hides in the middle. Naming the **weakest link** specifically — not "there is some uncertainty" — is the main output of this stage: that link is what stage 2 will measure, and its rating becomes the confidence of the whole initiative.

Chains longer than about five links usually contain a second problem. Split them.

## The cut

**One problem or several?** If several, split: each part becomes its own object with its own id and its own briefing. Without this rule the question is decorative.

The signal is a chain that branches, or a user problem that maps to two unrelated business metrics. Splitting early is cheap; splitting after stage 3 means redoing the intent.

## Probing questions

- "Who observed that, and by what exactly?"
- "Does it show in the data too, or only in the interviews?"
- "What does the business concretely lose if this stays as it is?"
- "Which link in the chain did you see, and which one was closed by inference?"
- "Would the problem still be there if you did not build the planned solution?"

## Exit criteria

```
- [ ] User problem in user terms, not a missing feature
- [ ] Segment named precisely
- [ ] Business problem named with the metric it damages
- [ ] Causal chain written out, every link rated with source and method
- [ ] Weakest link named specifically
- [ ] Confidence derived from it, not asserted
- [ ] Cut decided; if several problems, split into separate objects
```

If the weakest link is `unknown`, the briefing pauses here until it is measured. Otherwise route to stage 2, where that link is what gets sized.
