# Stage 4 deep-dive — can this actually be built?

## Contents
- What must be produced
- Blockers come in two kinds
- Who is allowed to answer
- Effort, sized honestly
- Probing questions
- Exit criteria

Read this when stage 4 is the blocking stage. Work it, then return to SKILL.md and re-state the status.

This is the shortest stage, and the one most often skipped because it feels like paperwork. It is not: an idea that clears stages 1–3 and then dies on a legal constraint wasted the most expensive discovery work in the sequence.

## What must be produced

| Item | Standard |
|---|---|
| **Dependencies** | Named systems, teams, data sources, contracts — not "some backend work" |
| **Effort** | An order of magnitude, agreed by the people who would do it |
| **Blockers** | Split into prerequisites and obstacles (below) |
| **Owner** | One person, by name |

An owner that is a team or a committee is not an owner. Shared accountability is absent accountability, and it is the reason ideas sit at this stage for months without anyone noticing they have stopped.

## Blockers come in two kinds

Teams usually list only the second kind and are then surprised by the first.

- **Prerequisites** — what must be in place before starting: a data field that isn't collected yet, a contract clause, a design system component, a migration that has to land first.
- **Obstacles** — what must not stand in the way: a freeze period, a conflicting roadmap item, a legal review, a dependency team's own quarter.

Write both lists. A prerequisite with no owner and no date is the most common silent killer at this stage.

## Who is allowed to answer

Evidence comes from the **discipline responsible**: engineering from engineering, legal from legal, data protection from data protection. The idea author's own assessment of feasibility does not count here, however senior they are — not because they are wrong, but because the assessment is unverifiable and nobody will be surprised when it turns out optimistic.

A one-line written answer from the responsible discipline is enough. A meeting where nobody objected is not.

## Effort, sized honestly

An order of magnitude is sufficient: days, weeks, or a quarter. Precision at this stage is false precision, because the solution can still change at stage 3 feedback or fail its stage 5 target definition.

What matters more than the number is the **ratio** — effort against the reach and severity from stage 2. An idea affecting 3 % of users for a quarter of work is not blocked by feasibility; it is blocked by arithmetic, and that belongs in the status card as plainly as any technical dependency.

## Probing questions

- "Welche Systeme und welche Teams müssen dafür etwas tun?"
- "Was muss vorher da sein, damit ihr überhaupt anfangen könnt?"
- "Wer aus Technik/Legal hat das eingeschätzt — und was hat die Person gesagt?"
- "Tage, Wochen oder ein Quartal?"
- "Wer ist die eine Person, die dafür geradesteht?"

## Exit criteria

```
- [ ] Dependencies named concretely
- [ ] Prerequisites listed, each with an owner
- [ ] Obstacles listed, each with the discipline that confirmed it
- [ ] Effort sized to an order of magnitude by the people who would do the work
- [ ] Exactly one named owner
- [ ] Effort checked against stage 2 reach and severity
```

If effort is disproportionate to the sized problem, say so here rather than letting it surface as a prioritization argument later.
