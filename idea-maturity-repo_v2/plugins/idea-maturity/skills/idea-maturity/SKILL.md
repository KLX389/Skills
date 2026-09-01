---
name: idea-maturity
description: Turns raw input — an idea, feature request, research finding, complaint, or assignment — into a structured briefing with a documented problem, its size, and an intent statement with success metrics, then into compared solution paths and a build-or-test judgement. Use whenever someone presents something to work on and the real question is whether to do it, where it stands, what evidence is missing, or whether it is ready. Applies especially when a request names a solution but no problem; when someone says research proves there is a problem but cannot say how big it is or how many users it affects; when ideas are prioritized by gut feel; when a backlog needs sorting by readiness; and when a group needs a shared, non-political way to assess initiatives together. Also applies retrospectively when something shipped and it is unclear whether the idea was wrong or the implementation was.
---

# Idea Maturity

Turn raw input into a briefing, the briefing into compared solution paths, and those into a judgement. Two jobs on every pass: **classify**, then **route**.

## Why this exists

There are always more ideas than people to build them, so prioritization is unavoidable. Prioritization by gut feel is what happens when initiatives **cannot be compared** — and they cannot be compared when one has a measured baseline and the next has an anecdote.

**Initiatives at the same stage compete on impact; initiatives at different stages do not compete at all** — the lower one needs evidence, not a decision. Judging a stage 1 initiative against a stage 4 initiative and concluding the first is weak is the most common prioritization error.

Not every initiative should reach stage 5. The funnel narrows on purpose: killed at stage 2 it costs a measurement, killed after launch it costs a quarter.

## The sequence

Not a causal chain but a **test sequence**: each stage falls away if the previous one does not hold.

| | Stage | Question | Falls away if |
|---|---|---|---|
| **0** | Input | What is this, does the ladder apply? | — |
| **1** | Problem | Whose problem, and do we know it? | there is no problem |
| **2** | Relevance | How big is it? | it is too small |
| **3** | Intent | How should it be instead, and how would we know? | we cannot say what we want |
| **4** | Hypotheses | What could get us there? | no path leads there |
| **5** | Worth | Is the path worth it, and can we take it? | effort exceeds benefit |

**Stages 1–3 together form the briefing** — the structured, complete version of what arrived as input. It is a deliverable in its own right, with an owner and a handover, not a warm-up for stage 4.

**The status** is the highest fully completed stage, not the highest anyone has worked on. Work above the blocking stage does not raise it; it is work at risk.

**Two orderings carry the whole structure:**

- **Intent before hypotheses.** The goal is derived from problem and relevance, never from the solution. Otherwise the goal gets worded so the existing solution fits.
- **Target value before effort.** The worth threshold is fixed before anyone knows the cost. Otherwise the target adapts to the effort.

## Evidence rating

Every claim carries one. Applies from stage 1 and propagates to stage 5.

| Rating | Meaning |
|---|---|
| `unknown` | Nobody checked — a gap |
| `assumed` | Someone finds it plausible — a bet |
| `reported` | Someone said it, secondhand |
| `observed` | Seen firsthand, qualitatively |
| `validated` | Data confirms it and the qualitative picture agrees |

A benchmark ("competitors do it") never rises above `assumed`. Most material sits at `reported`, and saying so is half the work.

**Confidence is inherited, never scored.** It is the rating of the weakest link in the causal chain. A later stage can lower it, never raise it — a well-worked solution cannot improve the evidence for a weakly evidenced problem.

## Workflow

```
- [ ] 1 Map the material onto the stages (internal, never shown)
- [ ] 2 First pass only: work stage 0 — finding, gap card, expectation
- [ ] 3 Read the blocking stage's file and work it
- [ ] 4 Update the object, run the self-check, give one concrete next action
```

**Step 2 runs once per initiative.** On a first encounter the blocking stage is 0, so stage 0 is worked and the pass ends with the first question of the entry stage. On every later pass the object already carries a finding and a gap card: skip to step 3, and update the gap card rather than rebuilding it. Re-triaging a known initiative wastes a turn and re-asks answered questions.

**Respond entirely in the language of the conversation, from the first visible word.** Field labels, stage names and ratings are translated at runtime; the field names and enum values in `template-spec.md` stay as written, because they are machine keys. Never show the internal mapping and never narrate that a skill is being applied.

**The expectation statement is not optional on the first pass.** Say what was received, how many stages remain, and what the person will hold at the end. It is calculated from the number of open stages and the mandate, not recited from a fixed script.

**Step 3 — routing.** Read exactly one file: the blocking stage's.

| Blocking stage | Read |
|---|---|
| 0 — Input | `reference/input-triage.md` |
| 1 — Problem | `reference/block-problem.md` |
| 2 — Relevance | `reference/block-relevance.md` |
| 3 — Intent | `reference/block-intent.md` |
| 4 — Hypotheses | `reference/phase-hypotheses.md` |
| 5 — Worth | `reference/phase-worth.md` |

Also available, read only when needed: `reference/template-spec.md` for field names and enums, `reference/example-briefing.md` for a worked pass, `reference/glossary.md` for terminology, `reference/facilitation.md` for group sessions.

The glossary is the one exception to reading a single file: it may be read alongside when a term is in dispute.

Each file ends with exit criteria. When they are met, re-state the status and route to the next stage. **One stage per pass** — never chain two.

Show the open path as a short numbered list before asking, then ask only the 1–3 questions that unblock the current stage. Do not run a fixed questionnaire; read what is there and probe only the gaps.

## The object

Every stage writes into one shared object. `reference/template-spec.md` holds the field names, enums, ownership rules, and completion conditions.

Read it when producing structured output, when a field's permitted values matter, or when the object will be handed to another system. For conversational work the prose fields in each stage file are enough.

All enum fields must stay inside their permitted values; everything else may be prose. Four of them are what an external backlog tool sorts on — `stage`, `evidence`, `effort`, `judgement` — so an out-of-range value there breaks ranking, not just tidiness.

## Tone

Teams usually did good work. The research is often solid and the solution principles sound. What is typically missing is **one dimension**: the size of the problem and the measurability of the change.

> Not: "your research isn't enough."
> Instead: "we know the problem exists — we don't yet know how much it weighs."

Name gaps plainly and without hedging, but never imply the work was sloppy. The goal is that teams see the gap themselves.

## Output

Produce the current state of the object inline, in the conversation's language. One field per line, values a phrase rather than a paragraph.

The status line has a fixed shape — the completed stage and the blocking stage are different numbers and both must appear:

```
Status: stage [n] — [name of stage n] complete · stage [n+1] [name] blocking
```

At the very start that reads *"stage 0 — input complete · stage 1 problem blocking"*. Naming only one of the two is the most common way this gets misread. Fill the blocking stage in full; fill later stages only where material already exists, marked *"not yet reliable — stage [n] is open"*. Never drop the status line, the blocking stage, or the next action.

Each stage file carries the fields it owns. `reference/example-briefing.md` shows a full worked pass and the level of bluntness expected.

## Self-check before sending

```
- [ ] No invented numbers — unknown is written `unknown → measure first`
- [ ] Every claim rated unknown / assumed / reported / observed / validated
- [ ] Confidence inherited from the weakest link, never asserted
- [ ] Exactly one blocking stage named
- [ ] Exactly one stage file was read and worked
- [ ] No solution named anywhere in stages 1–3
- [ ] No hedging: no "might", "perhaps", "could be worth exploring"
- [ ] Every gap has a concrete to-do with an owner
- [ ] Ends with one concrete next action
```

If any item fails, fix the output and check again. A response that names gaps but leaves the person guessing what to do has failed, however sharp the analysis. If an initiative is genuinely well-formed, say so plainly and keep it short.

## Shared vocabulary

`reference/glossary.md` holds one-line definitions of the terms used across all stages — output versus outcome, leading versus lagging, baseline, proxy, guardrail, attribution, MDE, Goodhart's law, and the five evidence ratings with the research terms behind them. Sources are named at the end.

Read it when a term is used loosely and the disagreement is really about definitions, or when a stage needs a precise word for something being described in paraphrase.

## Running it with a group

When the request is to facilitate a workshop, meeting, or backlog review rather than assess a single initiative, read `reference/facilitation.md` for the session sequence, who needs to be in the room, and how to compare several initiatives.
