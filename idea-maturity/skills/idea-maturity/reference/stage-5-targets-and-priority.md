# Stage 5 deep-dive — targets, and the data that makes ideas comparable

## Contents
- Two outputs, not one
- The target formula
- Where the target value comes from
- Stop criterion and attribution
- Acceptance is not success
- The six comparison figures
- The comparison card
- Ranking without a fake score
- Exit criteria

Read this when stage 5 is the blocking stage — which means **before** implementation starts. Afterwards this stage is worthless, because the metric gets chosen to fit the result.

## Two outputs, not one

Stage 5 produces two things, and the second is the reason the whole framework exists:

1. **Targets** — so that after launch, anyone can tell whether it worked.
2. **Comparison figures** — so that before launch, this idea can be ranked against the others competing for the same people and the same quarter.

The targets come first, because the comparison figures are derived from them. An idea without a target cannot be prioritized, only advocated for.

## The target formula

Every target is one sentence — **what changes, by how much, by when**:

> `[metric or behavior]` rises/falls from `[baseline]` to `[target]` by `[date]`.

> *"Die Abbruchquote in Buchungsschritt 3 sinkt von 34 % auf 28 % bis 8 Wochen nach Launch."*

If one of the three parts is missing, it is not a target:

| Missing | What it degrades into |
|---|---|
| **What** | An activity. "We launch X" is an output. The *what* must be a behavior or outcome change, not a delivery. |
| **How much** | Something unfalsifiable. "More bookings" is satisfied by a single extra booking. It needs **baseline and target** — both numbers. |
| **By when** | No moment of truth. The effect is awaited indefinitely and nothing is ever switched off. |

Three metric types, each with its own formula:

- **Leading indicator** — early signal, fast but a proxy: *"Anteil der Nutzer, die den neuen Vergleich öffnen, steigt von 0 auf über 15 % in Woche 1."*
- **Lagging indicator** — the actual result, reliable but slow: *"Buchungsabschlussquote steigt von 34 % auf 38 % bis 8 Wochen nach Launch."*
- **Guardrail** — what must not get worse, at least one is mandatory: *"Support-Tickets zum Buchungsflow steigen nicht über 120/Woche, gemessen über dieselben 8 Wochen."*

A guardrail without a number is decoration.

## Where the target value comes from

Not from what seems achievable, but from:

> **Above which value would the effort have been worth it?**

If that value lies above what is realistically achievable, the idea is already refuted — before anything was built, which is the cheapest possible moment to find out. Deriving the target from what looks reachable inverts this and guarantees a target that can always be declared met. An estimated target is fine when labelled `Vorschlag` or `bestätigt`.

This question is also what produces the value figure below, so answering it properly does double duty.

## Stop criterion and attribution

**Stop criterion** — which result would end the idea. Written before the start it is a decision rule; written afterwards it is an excuse. If nobody can name a result that would stop it, the idea is not being tested, it is being defended.

**Attribution** — how the effect is separated from seasonality, other launches and chance. Control group where possible, otherwise a clean before/after window with the confounders named. Attribution decided after the fact is attribution chosen to fit the outcome.

## Acceptance is not success

**Acceptance** means *built as specified*. **Success** means *the behavior moved*. Something can pass acceptance, ship on time, and still fail on outcome. Only when both are documented separately can anyone later distinguish **"the idea was wrong"** from **"the implementation was poor"** — the distinction most often missing, and why post-mortems stall in opinion.

## The six comparison figures

These are the figures that make two ideas comparable. Each is derived from a stage already worked, so none of them requires new analysis — if one cannot be filled, the stage it comes from was not actually cleared.

| # | Figure | Derived from | Standard |
|---|---|---|---|
| 1 | **Effect** | Stage 5 target | The delta in the metric's own unit: "34 % → 28 %" |
| 2 | **Value** | Stage 2 baseline × stage 5 delta | That delta converted into **one shared unit** for the whole portfolio, with its origin stated |
| 3 | **Effort** | Stage 4 | Order of magnitude — days, weeks, a quarter — plus which team is occupied |
| 4 | **Confidence** | Weakest link of the stage 1 chain | The chain's rating, lowered one level if stage 3's riskiest assumption is still untested |
| 5 | **Time to signal** | Stage 5 timeframes | When the leading indicator speaks, and when the lagging one does |
| 6 | **Reversibility** | Stage 4 | Can it be switched off, and at what cost |

**On figure 2 — the shared unit.** Ideas measured in different currencies cannot be compared: an abandonment rate and a support-ticket count have no common scale. Convert both into whatever single unit the organization already steers by, usually money per year. State the conversion and its origin. Where a conversion is genuinely impossible, write `nicht umrechenbar` and rank that idea separately rather than inventing a rate.

**On figure 4 — confidence is inherited, not scored.** It comes from the chain, not from someone's feeling on a scale of one to ten. A `vermutet` link anywhere load-bearing makes the whole idea a bet, no matter how precise the target looks. This is the figure that keeps a well-formatted guess from outranking a measured certainty.

**On figure 5 — under scarcity, speed of learning is value.** An idea whose lagging indicator lands in eight weeks frees the team to decide; one that takes a year occupies both the people and the decision.

## The comparison card

One block per idea, same fields every time, so a portfolio table can be built from them mechanically. In the conversation's language:

```
**Vergleich: [Idee in einem Satz]**
- Wirkung: [Kennzahl] [Baseline] → [Zielwert] bis [Datum]
- Wert: [Betrag in gemeinsamer Einheit] / [Zeitraum] — Herkunft: [Rechenweg]
- Aufwand: [Tage / Wochen / Quartal] — blockiert: [Team]
- Konfidenz: [Vermutet / Berichtet / Beobachtet / Belegt] — schwächstes Glied: [welches]
- Zeit bis Signal: Frühindikator [Zeitraum], Spätindikator [Zeitraum]
- Umkehrbarkeit: [abschaltbar / teilweise / irreversibel]
```

## Ranking without a fake score

Sort by **value against effort**. Use confidence, time to signal and reversibility as tiebreakers — and show them next to the ranking, never multiplied into it.

**Do not collapse the figures into a single number.** A score makes a `vermutet` idea and a `belegt` idea look identical whenever their products happen to match, which is precisely the confusion the four ratings exist to prevent. The number also acquires an authority its inputs do not have: two rough estimates and an inherited rating do not become precise by being multiplied. Show the figures side by side and let the room decide — the disagreement that surfaces is the useful part.

Two rules that decide most cases without argument:

- **A high-value, low-confidence idea is not a build candidate — it is a test candidate.** The next action is the cheapest test from stage 3, not a slot in the quarter.
- **Equal value and effort, unequal confidence → the better-evidenced idea goes first.** Not because it is more exciting, but because it is more likely to actually deliver the value it promises.

## Exit criteria

```
- [ ] One leading and one lagging indicator, each as a full target formula
- [ ] At least one guardrail with a numeric limit
- [ ] Baseline measured for every metric, or instrumented before launch
- [ ] Target value derived from worthwhileness, labelled Vorschlag or bestätigt
- [ ] Stop criterion stated
- [ ] Attribution method decided
- [ ] Acceptance criteria kept separate from success criteria
- [ ] All six comparison figures filled, each traceable to the stage it came from
- [ ] Value expressed in the same unit as the rest of the portfolio
```

When these hold, the idea is a build candidate and can be ranked. Everything before this point is discovery; everything after is delivery. For running the ranking with a group, see `facilitation.md`.
