# Stage 5 - Effort And Worth

## Purpose

Stage 5 evaluates the chosen build-eligible hypothesis. This is where effort becomes binding and a judgement is made.

Read this file when stage 5 is blocking. Do not use it for every hypothesis; use it for the chosen path only.

## Scope

Stage 4 used rough effort for ordering. Stage 5 needs an estimate that can be acted on: dependencies, prerequisites, owner, reversibility, cost, benefit, confidence, opportunity cost, and judgement.

The K.O. check in stage 0 already handled known impossibility. Stage 5 handles cost, capacity, sequencing, and worth.

## Effort And Feasibility

| Item | Standard |
|---|---|
| Effort | T-shirt size estimated by the responsible discipline |
| Dependencies | named systems, teams, data sources, vendors, contracts |
| Prerequisites | each with owner; add due date when it gates start |
| Owner | one accountable person |
| Reversibility | `switchable`, `partial`, or `irreversible` |

Size reference: XS under 1 week; S 1-2 weeks; M 3-6 weeks; L 1 quarter; XL must be decomposed.

The binding effort estimate must not come only from the idea author. A written one-line estimate from the responsible discipline is enough. A meeting where nobody objected is not.

## Business Case

Compare against the best viable alternative from stage 4, not automatically against doing nothing. If a partial path delivers most of the target for a fraction of the effort, the full build is not worth it yet.

```text
cost:          [amount]
benefit:       [amount per year, shared unit]
compared_with: [best viable alternative]
payback:       [period]
confidence:    [confidence of chosen hypothesis]
```

The business case inherits the chosen hypothesis confidence. Exact cost and benefit figures resting on `assumed` links remain a bet.

For `obligatory`, the business case compares compliant paths by cost, deadline risk, operational risk, and residual compliance risk. Compliance itself is not justified by ROI.

## Opportunity Cost

Name what gets displaced. "Other work" is not enough. Under scarce capacity, the displaced initiative is often the real cost.

If nothing specific is displaced because capacity is already reserved for this mandate, say so and name the reservation.

## Payback Or Decision Threshold

For discretionary and maintenance work, the acceptable payback or effort threshold must be set before reading the result. Without a threshold, almost any non-absurd payback can be defended.

For obligatory work, use compliance deadline and minimum acceptable compliant scope instead of payback.

## Judgement

| Judgement | When |
|---|---|
| `build` | value exceeds effort against best alternative, confidence is at least `reported`, and capacity tradeoff is accepted |
| `test` | value is plausible but a material assumption still needs evidence before build |
| `defer` | worth doing, but capacity is committed elsewhere; requires review date |
| `drop` | effort exceeds value, threshold is unreachable, or no compliant/feasible path exists |

Every judgement carries a reason. Keep the object in all cases so the decision is traceable.

## Exit Criteria

```text
- [ ] Effort is estimated by the responsible discipline, source named.
- [ ] Dependencies and prerequisites are listed; each prerequisite has an owner.
- [ ] One accountable owner is named.
- [ ] Reversibility is stated.
- [ ] Business case compares against the best viable alternative.
- [ ] Confidence is inherited and shown next to figures.
- [ ] Opportunity cost is specific, or reserved mandate capacity is named.
- [ ] Payback, decision threshold, or compliance deadline is explicit.
- [ ] Judgement is stated with reason.
```

With `judgement: build`, the initiative is ready to rank among other stage-5 build candidates. Everything before this point was discovery; everything after is delivery.

After launch, use `edge-cases-and-workflows.md` for the post-launch review: whether the idea was wrong, the implementation failed, or the evidence rating was too optimistic.
