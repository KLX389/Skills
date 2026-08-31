---
name: idea-maturity
description: Assesses the maturity of an idea, feature, or initiative — which stage it has reached, what evidence is missing, and whether it is ready to build — then routes into the deep-dive for the one stage that is blocking. Use whenever someone presents an idea, research finding, concept, or proposed solution and the real question is whether to do it, where it stands, what is missing, or whether it is ready. Applies especially when an idea jumps from an observation or research result straight to a concept; when someone says research proves there is a problem but cannot say how big it is or how many users it affects; when ideas are prioritized by gut feel; when a backlog needs sorting by readiness; when someone asks what must be true before starting; and when a group needs a shared, non-political way to assess ideas together. Also applies retrospectively when something shipped and it is unclear whether the idea was wrong or the implementation was.
---

# Idea Maturity

Determine which stage an idea has reached, then work the one stage that blocks it. Two jobs, in this order: **classify**, then **route**.

## Why this exists

There are always more ideas than people to build them, so prioritization is unavoidable. Prioritization by gut feel is what happens when ideas **cannot be compared** — and they cannot be compared when they sit at different levels of evidence. One has a measured baseline, the next has an anecdote, and the loudest advocate wins.

Maturity is what makes ideas comparable. **Ideas at the same stage compete on impact; ideas at different stages do not compete at all** — the lower one needs evidence, not a decision. Judging a stage-1 idea against a stage-4 idea and concluding the first is weak is the single most common prioritization error.

Two different things get prioritized, and conflating them wastes the scarcer resource:

- **What to build** — compare at stage 5, impact against effort.
- **What to mature next** — discovery capacity is scarce too. Spend it where the maturity gap is cheapest to close and the sized problem is largest.

**Not every idea should reach stage 5.** The funnel is supposed to narrow. An idea killed at stage 2 costs one measurement; the same idea killed after launch costs a quarter. Cheap death is the return on this framework, not a side effect.

The pattern it replaces: problem observed → research done → result treated as truth → straight into a concept → prioritized by gut feel → built. The leap from *observation* to *truth* to *concept* is never documented, so afterwards nobody can tell whether the idea was wrong, the assumption was wrong, the implementation was poor, or the wrong metric was watched.

For comparing several ideas against each other, see `reference/facilitation.md`.

## The core rule

Stages follow **what is still uncertain**. Each removes exactly one uncertainty, in order. Go **bottom-up** and stop at the first stage that cannot be **honestly** affirmed — that is the **blocking stage**.

The **status** is the highest **fully reached** stage, not the highest one someone has worked on. Detailed work above the blocking stage does not raise the status; it is work at risk.

## The five stages

| # | Stage | Question it settles | Cleared when |
|---|---|---|---|
| 1 | Problem exists | Does the problem exist, or do we only perceive it? | Problem is validated, not merely reported; the chain from user problem to business problem is written out |
| 2 | Problem is relevant | How big is it? | Reach, frequency, severity and a baseline all carry numbers with stated origins |
| 3 | Solution fits | Does *this* solution solve *this* problem? | Alternatives were rejected with reasons; the riskiest assumption is named with its cheapest test |
| 4 | It can be built | Can we build this — technically, legally, organizationally? | Dependencies, effort, blockers and one accountable owner are confirmed by the disciplines responsible |
| 5 | Success is recognizable | Would we recognize whether it worked, and is this idea worth doing before the others? | Every target names what changes, by how much, by when — plus guardrails, a stop criterion, and the comparison data that lets this idea be ranked against others |

Every claim carries a **rating**. Four levels, because the gap between hearsay and firsthand observation is where most overconfidence lives:

| Rating | Meaning |
|---|---|
| `assumed` | Plausible to someone. No observation behind it. |
| `reported` | Someone else said it — user, support, sales. Secondhand, unverified. |
| `observed` | We saw it ourselves, qualitatively — usability test, session recording, watching the behavior happen. |
| `validated` | Quantitative data confirms it, and the qualitative picture agrees. |

German labels: `Vermutet / Berichtet / Beobachtet / Belegt`. Most material sits at *reported*, and saying so is half the work. A benchmark ("competitors do it") never rises above `assumed`.

## Workflow

```
- [ ] 1 Map the material onto the five stages (internal, never shown)
- [ ] 2 State the status and name exactly one blocking stage
- [ ] 3 Read that stage's deep-dive file and work it
- [ ] 4 Fill the status card
- [ ] 5 Run the self-check, then give one concrete next action
```

**Respond entirely in the language of the conversation, from the first visible word.** Never show the internal mapping, never narrate that a skill is being applied, never leave English scaffolding in the output.

**Step 2** opens with one or two blunt lines: which stage, which blocker, why it matters. Example: *"Diese Idee steht auf Stufe 2. Die Lösung ist ausgearbeitet, aber wie groß das Problem ist, weiß niemand — damit ist die Priorisierung nicht belastbar."*

**Step 3 — routing.** Read exactly one deep-dive: the blocking stage's. Reading several at once reproduces the wall of questions this skill exists to prevent.

| Blocking stage | Read |
|---|---|
| 1 — Problem exists | `reference/stage-1-problem-evidence.md` |
| 2 — Problem is relevant | `reference/stage-2-problem-size.md` |
| 3 — Solution fits | `reference/stage-3-solution-fit.md` |
| 4 — It can be built | `reference/stage-4-buildability.md` |
| 5 — Success is recognizable | `reference/stage-5-targets-and-priority.md` |

The glossary is the one exception to reading a single file: it may be read alongside a deep-dive when a term is in dispute.

Each deep-dive ends with exit criteria. When they are met, return here, re-state the status, and route to the next stage. **One stage per pass** — do not chain two deep-dives in a single response.

Show the open path as a short numbered list before asking, so the whole way is visible, then ask only the 1–3 questions that unblock the current stage. Do not run a fixed questionnaire; read what is already there and probe only the gaps.

## Tone

Teams usually did good work. The research is often solid and the solution principles sound. What is typically missing is **one dimension**: the size of the problem and the measurability of the change.

> Not: "your research isn't enough."
> Instead: "we know the problem exists — we don't yet know how much it weighs."

Name gaps plainly and without hedging, but never imply the work was sloppy. The goal is that teams see the gap themselves.

## Output: the status card

Produce this inline, in the conversation's language, with the labels translated. One field per line, values a phrase rather than a paragraph. Fill the blocking stage in full; fill higher stages only where material already exists, marked *"noch nicht belastbar, weil Stufe [n] offen ist"*. Never drop the status line, the blocking stage, or the next action.

```
**Reifegrad: [Idee in einem Satz]**

**Status: Stufe [n] — [Bezeichnung]**
- Klartext: [ein blunter Satz: was steht, was blockiert]

**1. Problem**
- Nutzerproblem: [...] — [Vermutet / Berichtet / Belegt]
  - Beleg: [Quelle + Beobachtungsart | fehlt → welcher Beleg nötig wäre]
- Unternehmensproblem: [...] — [Vermutet / Berichtet / Belegt]
  - Beleg: [Quelle + Beobachtungsart | fehlt → welcher Beleg nötig wäre]
- Kausalkette: [Glied → Glied → Glied]
  - Schwächstes Glied: [welches, und warum]

**2. Relevanz**
- Reichweite: [Zahl + Herkunft | unbekannt → zuerst messen]
- Häufigkeit: [...]
- Schwere: [...]
- Baseline: [Wert | unbekannt → zuerst messen]

**3. Lösungspassung**
- Verworfene Alternativen: [1-3 mit Begründung | keine erwogen → Warnsignal]
- Wirkkette: [Lösung → Verhaltensänderung → Outcome]
- Riskanteste Annahme: [...]
- Billigster Test dafür: [...]

**4. Umsetzbarkeit**
- Abhängigkeiten: [...]
- Blocker: [was da sein muss / was nicht dagegenstehen darf]
- Aufwand: [Größenordnung]
- Owner: [eine Person]

**5. Erfolgserkennbarkeit**
- Ziel: [Kennzahl] von [Baseline] auf [Zielwert] bis [Datum] ([Vorschlag / bestätigt])
- Frühindikator: [Zielformel]
- Guardrail: [Kennzahl] bleibt [über/unter] [Grenze] im selben Zeitraum
- Stop-Kriterium: [Ergebnis, das die Idee beendet]
- Attribution: [Kontrollgruppe / Vorher-Nachher | ungeklärt]
- Priorisierungs-Eckdaten: [nur wenn Stufe 5 erreicht — siehe Vergleichskarte in der Stufe-5-Datei]

**Was für die nächste Stufe fehlt**
- [ ] [konkret fehlendes Stück] → [wie es zu beschaffen ist] → [wer]

**Nächster Schritt**
[eine konkrete, sofort machbare Handlung]
```

For a fully worked card and the level of bluntness expected, see `reference/example-card.md`.

## Self-check before sending

```
- [ ] No invented numbers — unknown is written `unbekannt → zuerst messen`
- [ ] Every claim rated assumed / reported / observed / validated
- [ ] Exactly one blocking stage named (a list of everything wrong is not a status)
- [ ] Exactly one deep-dive was read and worked
- [ ] No hedging: no "might", "perhaps", "could be worth exploring"
- [ ] Every gap has a concrete to-do attached
- [ ] Ends with one concrete next action
```

If any item fails, fix the card and check again. A response that names gaps but leaves the user guessing what to do has failed, however sharp the analysis. If an idea is genuinely well-formed, say so plainly and keep it short — do not pad.

## Shared vocabulary

`reference/glossary.md` holds one-line definitions of the terms used across all stages — output versus outcome, leading versus lagging, baseline, proxy, guardrail, attribution, MDE, Goodhart's law, and the qualitative-evidence terms behind the four ratings. Sources are named at the end of the file.

Read it when a term is being used loosely and the disagreement is really about definitions, when someone asks what a term means, or when a stage needs a precise word for something the team has been describing in paraphrase. Definitions are English; translate them into the conversation's language like every other output.

## Running it with a group

When the request is to facilitate a workshop, meeting, or backlog review rather than assess a single idea, read `reference/facilitation.md` for the session sequence, who needs to be in the room, and how to compare several ideas against each other.
