# Stage 1 deep-dive — does the problem exist?

## Contents
- What must be produced
- Rating the evidence
- Two problems, one chain
- The hidden-solution trap
- Probing questions
- Exit criteria

Read this when stage 1 is the blocking stage. Work it, then return to SKILL.md and re-state the status.

## What must be produced

Three things, and none of them substitutes for another:

1. The **user problem** — what users cannot achieve, or what obstructs them
2. The **business problem** — missing revenue, higher cost, risk, inconsistency, maintenance load
3. The **causal chain** connecting the two, link by link

Only one of the first two means either building something users love that earns nothing, or the reverse.

## Rating the evidence

Every claim gets `assumed` / `reported` / `observed` / `validated`. Evidence carries two parts, always:

- the **source**, named concretely — not "research" but "8 interviews, März, Bestandskunden"
- the **observation type** — interview, analytics, support tickets, usability test, benchmark, complaint

Qualitative explains the *why*, quantitative proves the *whether*. Neither alone reaches `validated`:

| What you have | Rating | What is missing |
|---|---|---|
| A hunch, however senior the person holding it | assumed | Any observation at all |
| Benchmark — "competitors do it" | assumed | This is imitation, not evidence. It says nothing about *your* users. |
| Support tickets, sales reports, users telling you | reported | Firsthand observation. People report what they noticed, not what they did. |
| Interviews where users describe the problem | reported | Still secondhand: you heard it, you did not see it happen |
| Usability test or session recording of the behavior | observed | The quantitative side — how often, how many? |
| Analytics anomaly on its own | observed | The qualitative side — why does the number look like that? |
| Behavior data and qualitative picture agreeing | validated | Nothing at this stage |

The jump from `reported` to `observed` is the one teams skip. It is also the cheapest: five sessions of watching the behavior usually settle what a month of debate cannot.

A benchmark never raises a rating on its own. It is a source of hypotheses, not of proof.

## Two problems, one chain

Write the chain out and rate **each link separately**:

> Inkonsistente Darstellung `belegt` → fehlende Transparenz `beobachtet` → Unsicherheit beim Nutzer `berichtet` → weniger Buchungen `vermutet` → weniger Umsatz `vermutet`

The endpoints are usually the well-defended part. The guessing hides in the middle. Naming the **weakest link** specifically — not "there is some uncertainty" — is the main output of this stage, because that link is what stage 2 will have to measure.

Chains longer than about five links usually contain a second, separate problem. Split them.

## The hidden-solution trap

A problem stated as a missing feature is a solution in disguise, and it quietly forecloses stage 3:

| Hidden solution | Actual problem |
|---|---|
| "There's no filter" | Users can't find the right item in long lists and drop out |
| "We need a dashboard" | Team can't tell on Monday whether last week went well |
| "The onboarding needs a tutorial" | New users don't reach their first success and churn in week 1 |

Rewrite in the user's terms before going further. If the rewrite is impossible because nobody knows what users were trying to do, that is itself the finding: the problem is `assumed`.

## Probing questions

Pick the one or two that actually bite:

- "Wer hat das beobachtet, und woran genau?"
- "Steht das auch in den Daten — oder nur in den Interviews?"
- "Was verliert das Unternehmen konkret, wenn das so bleibt?"
- "Welches Glied in der Kette habt ihr wirklich gesehen, und welches ist geschlossen worden?"
- "Wäre das Problem noch da, wenn ihr die geplante Lösung nicht baut — und woran würdet ihr das merken?"

## Exit criteria

Stage 1 is cleared when all of these hold:

```
- [ ] User problem stated in user terms, not as a missing feature
- [ ] Business problem named with the metric it damages
- [ ] Both rated, each with source and observation type
- [ ] Causal chain written out, every link rated
- [ ] Weakest link named specifically
```

**The weakest link sets the rating of the whole chain** — this carries forward to stage 5, where it becomes the confidence value used for prioritization. If the weakest link is `assumed` and load-bearing, the honest status stays at stage 1 even when everything else is filled in. Return to SKILL.md, re-state the status, and route to stage 2 — where that link becomes the thing to size.
