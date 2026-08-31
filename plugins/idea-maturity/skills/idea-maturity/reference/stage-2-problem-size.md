# Stage 2 deep-dive — how big is the problem?

## Contents
- What must be produced
- The number-with-origin rule
- Sizing fast without faking
- When the baseline is unknown
- Probing questions
- Exit criteria

Read this when stage 2 is the blocking stage. This is where most ideas actually sit. Work it, then return to SKILL.md and re-state the status.

## What must be produced

Four values, each with an origin:

| Value | Question | Example |
|---|---|---|
| **Reach** | How many, absolute or as a share? | "20-30 % der Buchungsabbrecher" |
| **Frequency** | How often does it occur? | "in jedem Buchungsvorgang, im Schnitt 1,4× pro Sitzung" |
| **Severity** | What happens when it does? | "Abbruch, kein Umweg — Nutzer kommen nicht zurück" |
| **Baseline** | What is today's value of the damaged metric? | "Abbruchquote Schritt 3 = 34 %" |

Reach × severity is what makes ideas comparable in a backlog. Without both, prioritization falls back to whoever argues most confidently.

The tell-tale sentence at this stage is *"wir haben Research gemacht, wir wissen doch, dass es ein Problem ist."* True — and it leaves open how big, how many, how often. Say that plainly, without implying the research was bad.

## The number-with-origin rule

Every value is a **number plus where it came from**:

> "Betrifft geschätzt 20-30 % der Buchungsabbrecher, Herkunft: Funnel-Daten Q2 plus 8 Interviews."

A number without origin does not count — it becomes fact by repetition. An origin without a number does not count either — it is stage 1 material wearing a stage 2 label. **Never invent a plausible-looking figure to fill a gap.** An honest `unbekannt` outranks a confident guess, because the guess is what later gets quoted in a steering deck.

## Sizing fast without faking

An estimate is legitimate at this stage; only its origin is mandatory. Cheapest sources first:

1. **Funnel or event data already collected** — usually answers reach and baseline in an afternoon
2. **Support and complaint volume** — a lower bound on frequency; people who complain are a fraction of those affected
3. **Segment arithmetic** — share observed in a small sample × size of the affected segment, stated as a range, never a point value
4. **Sales or CS reports** — directional only, and rated `reported`
5. **A deliberate measurement** — when 1–4 come up empty, this becomes the next action rather than a gap in a card

Ranges are better than point values here. "20-30 %" invites a check; "24 %" invites belief.

## When the baseline is unknown

Write `unbekannt → zuerst messen` and make instrumenting it the next action. This is not a failure of the idea — it is the cheapest work on the whole path, and it usually unblocks several ideas at once. A backlog with three ideas blocked on the same missing baseline needs one measurement, not three debates.

Without a starting value, no effect can ever be proven later. Stage 5 will be unbuildable, and a post-launch argument about whether it worked is guaranteed.

## Probing questions

- "Wie viele Nutzer betrifft das — grob, zehn Prozent oder achtzig?"
- "Worauf stützt sich die Schätzung?"
- "Was ist der heutige Wert der Kennzahl, die darunter leidet?"
- "Wie oft tritt das pro Nutzer und Sitzung auf?"
- "Was passiert, wenn es auftritt — Umweg oder Abbruch?"

## Exit criteria

```
- [ ] Reach stated as a number or range, with origin
- [ ] Frequency stated, with origin
- [ ] Severity stated as a consequence, not an adjective
- [ ] Baseline measured, or `unbekannt → zuerst messen` with an owner and a date
- [ ] Estimates marked as estimates, never rounded into facts
```

If reach and severity together do not justify the effort, stop here and say so. Killing an idea at stage 2 costs a measurement; killing it after stage 4 costs a quarter.
