# Stage 5 — Effort & Worth

## Contents
- Scope
- Effort and feasibility
- The business case
- Opportunity cost
- The payback threshold
- The judgement
- Exit criteria

For the chosen hypothesis only. This is where binding estimation is worth the time.

## Scope

Stage 4 produced a rough size for ordering. Here the estimate must hold: dependencies, prerequisites, resources, one named owner.

Two things of different kinds were deliberately separated. *Is it possible at all* — legally, contractually, technically — was answered as the k.-o. check in stage 0, where it costs five minutes. What remains here is *how big is it*, which is a number and belongs next to the value.

## Effort and feasibility

| Item | Standard |
|---|---|
| **Effort** | T-shirt size, estimated by those who would do the work |
| **Dependencies** | Named systems, teams, data sources, contracts — not "some backend work" |
| **Prerequisites** | What must exist before starting; each with an owner |
| **Owner** | One person, by name |
| **Reversibility** | `switchable` / `partial` / `irreversible` |

Sizes: XS under 1 week · S 1–2 weeks · M 3–6 weeks · L 1 quarter · XL do not estimate, decompose.

**The estimate must not come from the idea's author.** Not because they are wrong, but because it is unverifiable and nobody is surprised when it turns out optimistic. A one-line written answer from the responsible discipline is enough; a meeting where nobody objected is not.

A prerequisite with no owner and no date is the most common silent killer at this stage.

## The business case

**Compare against the best alternative, not against nothing.** This is the most common error in business cases. If a partial solution delivers 70 % of the effect for 20 % of the effort, the case for the full build is wrong — not miscalculated, but calculated against the wrong alternative. Stage 4 produced those alternatives; use them.

```
cost:          [amount]
benefit:       [amount per year, shared unit]
compared_with: [best alternative from stage 4]
payback:       [period]
confidence:    [← confidence of the chosen hypothesis]
```

**The case inherits the confidence of its effect chain's weakest link.** Two exact figures resting on an `assumed` remain a bet. Stating the confidence next to the numbers prevents the arithmetic from acquiring an authority its inputs do not have.

## Opportunity cost

**What do we drop to do this?** Under scarce capacity this is often the larger item, and it is the one most frameworks omit. A quarter is not only its cost in money; it is everything that does not happen in that quarter.

Name the specific initiative that gets displaced, not "other work".

## The payback threshold

Set in advance, not derived from the result: *"at a quarter of effort we accept at most 18 months."* Without a threshold, any payback period that is not absurd justifies the measure.

## The judgement

The stage is not finished when the numbers exist. Establishing effort and cost and then saying nothing is the most common dead end — the estimate is on the table, but nobody has stated whether it is worth it.

| Judgement | When |
|---|---|
| `build` | Value exceeds effort against the best alternative, confidence at least `reported` |
| `test` | Value plausible, but the effect chain's weakest link is `assumed` |
| `defer` | Worth it, but capacity is committed elsewhere — with a review date |
| `drop` | Effort exceeds value, or the worth threshold is unreachable |

Every judgement carries a reason. The object is kept in all four cases: a documented rejection stops the same idea returning unexamined two quarters later.

## Exit criteria

```
- [ ] Effort estimated by the responsible discipline, source named
- [ ] Dependencies and prerequisites listed, each prerequisite with an owner
- [ ] One named owner, reversibility stated
- [ ] Business case against the best alternative, not against nothing
- [ ] Confidence inherited and shown next to the figures
- [ ] Opportunity cost named specifically
- [ ] Payback threshold set in advance
- [ ] Judgement stated with a reason
```

With a judgement of `build`, the initiative is a build candidate and can be ranked. Everything up to here was discovery; everything after is delivery.

**Note on mandate:** For `discretionary`, the business case is cost vs. benefit, and all judgements are available. For `obligatory`, pick the cheapest compliant variant and ship on deadline. For `maintenance`, defer is risky; escalate if you cannot ship. See `mandate-systems.md` for how mandate affects this stage.

## After launch

When this initiative ships, return here after launch to validate the assumptions. See `edge-cases-and-workflows.md` — "Post-launch review: Was the idea wrong or the implementation?" for how to structure the retrospective and close the feedback loop.
