---
name: idea-maturity
description: Turns raw input — an idea, feature request, research finding, complaint, or assignment — into a structured briefing with a documented problem, its size, and an intent statement with success metrics, then into compared solution paths and a build-or-test judgement. Use whenever someone presents something to work on and the real question is whether to do it, where it stands, what evidence is missing, or whether it is ready. Applies especially when a request names a solution but no problem; when someone says research proves there is a problem but cannot say how big it is or how many users it affects; when ideas are prioritized by gut feel; when a backlog needs sorting by readiness; and when a group needs a shared, non-political way to assess initiatives together. Also applies retrospectively when something shipped and it is unclear whether the idea was wrong or the implementation was.
---

# Idea Maturity

Turn raw input into a briefing, the briefing into compared solution paths, and those into a judgement. Two jobs on every pass: **classify**, then **route**.

---

## ⚡ Quick Start

**What this is:** A six-stage test sequence that takes initiatives from raw input → evidenced problem → sized impact → fixed intent → compared solutions → go/test/defer/drop judgement.

**When to use it:**
- Someone presents an idea or feature request — you need to know *where it stands*
- A backlog needs sorting by readiness, not gut feel
- The request names a solution but the problem is unnamed
- Claims exist without evidence or without size ("research proves it" but you don't know how big)
- A group needs a non-political way to assess multiple initiatives together

**The core loop:**
1. Classify the input (form: observation / complaint / problem / solution / hypothesis / assignment)
2. Route to the blocking stage (the one that cannot be affirmed)
3. Work only that stage (read one file, ask 1–3 questions, move on)
4. Repeat on next input — one stage per pass

**First question?** What happens if you do not build what was just proposed?

---

## 📍 Navigation & Routing

**Blocking stage determines your route.** Find your stage below, read its file, ask the gaps.

| Stage | Blocking Question | Read This | Output |
|-------|-------------------|-----------|--------|
| **0** | What is this? | `input-triage.md` | Gap card + entry stage |
| **1** | Do we know the problem? | `block-problem.md` | Reformulated problem + causal chain |
| **2** | How big is it? | `block-relevance.md` | Reach, frequency, severity, baseline, problem value |
| **3** | What should it be instead? | `block-intent.md` | Intent statement + target + worth threshold |
| **4** | What could get us there? | `phase-hypotheses.md` | 2+ paths vs. null variant + riskiest assumption |
| **5** | Is the path worth it? | `phase-worth.md` | Effort, cost, benefit, confidence, judgement |

**One rule:** Read exactly one stage file per pass. Work above the blocking stage does not raise the status.

**Also available** (read only when needed):
- `template-spec.md` — field names, enums, ownership rules (needed for structured output)
- `mandate-systems.md` — decision tree and stage-by-stage impact of each mandate type (read in stage 0 or when mandate is unclear)
- `example-briefing.md` — worked pass showing how blunt the verdict should be
- `glossary.md` — 63 sourced definitions (read alongside when a term is disputed)
- `facilitation.md` — session sequence and group dynamics (read for backlog reviews or workshops)
- `edge-cases-and-workflows.md` — split, re-triage, rollback, tie-breaker, post-launch, and lost-entry-point scenarios

---

## Why This Exists

Prioritization by gut feel is what happens when initiatives **cannot be compared** — and they cannot be compared when one has a measured baseline and the next has an anecdote.

**Initiatives at the same stage compete on impact; initiatives at different stages do not compete** — the lower one needs evidence, not a decision. Judging a stage 1 initiative against a stage 4 initiative and concluding the first is weak is the most common prioritization error.

Not every initiative should reach stage 5. The funnel narrows on purpose: killed at stage 2 it costs a measurement, killed after launch it costs a quarter.

## The Test Sequence

Not a causal chain but a **test sequence**: each stage falls away if the previous one does not hold.

| | Stage | Question | Falls away if |
|---|---|---|---|
| **0** | Input | What is this, does the ladder apply? | — |
| **1** | Problem | Whose problem, and do we know it? | there is no problem |
| **2** | Relevance | How big is it? | it is too small |
| **3** | Intent | How should it be instead, and how would we know? | we cannot say what we want |
| **4** | Hypotheses | What could get us there? | no path leads there |
| **5** | Worth | Is the path worth it, and can we take it? | effort exceeds benefit |

### Briefing = Stages 1–3

**Stages 1–3 together form the briefing** — the structured, complete version of what arrived as input. It is a deliverable in its own right, with an owner and a handover, not a warm-up for stage 4.

A complete briefing allows solutions to be compared. Without it, you are advocating for artefacts, not evaluating them.

### Status vs. Work-at-Risk

**The status** is the highest fully completed stage, not the highest anyone has worked on. Work above the blocking stage does not raise it; it is work at risk.

If a concept exists at stage 4 but stage 2 is open, the status is stage 1 — blocking. Work at stage 4 is provisional.

---

## The Core Principles

### Two orderings carry the structure

- **Intent before hypotheses.** The goal is derived from problem and relevance, never from the solution. Otherwise the goal gets worded so the existing solution fits.
- **Target value before effort.** The worth threshold is fixed before anyone knows the cost. Otherwise the target adapts to the effort.

### Evidence rating

Every claim carries one. Applies from stage 1 onwards and propagates to stage 5.

| Rating | Meaning |
|---|---|
| `unknown` | Nobody checked — a gap |
| `assumed` | Someone finds it plausible — a bet |
| `reported` | Someone said it, secondhand |
| `observed` | Seen firsthand, qualitatively |
| `validated` | Data confirms it and the qualitative picture agrees |

A benchmark ("competitors do it") never rises above `assumed`. Most material sits at `reported`, and saying so is half the work.

### Confidence is inherited, never raised

**Confidence is the rating of the weakest link in the causal chain.** A later stage can lower it, never raise it — a well-worked solution cannot improve the evidence for a weakly evidenced problem.

If stage 1 rests on `assumed` evidence, the entire initiative has confidence `assumed`. Stage 4 cannot fix that; it can only acknowledge it.

---

## The Workflow — Four Steps Per Pass

```
- [ ] 1 Map the material onto the stages (internal, never shown)
- [ ] 2 First pass only: work stage 0 — finding, gap card, expectation
- [ ] 3 Read the blocking stage's file and work it
- [ ] 4 Update the object, run the self-check, give one concrete next action
```

### Step 1: Classify

What form did this arrive in? (observation / complaint / problem / solution_request / hypothesis / assignment)

Two forms require care:
- **`solution_request`** is the most common and the only one requiring rollback. Test question: *"What happens if we do not build it?"* The answer is the problem.
- **`assignment`** is the most dangerous. A decision was made, that is all. It says nothing about evidence. Do not challenge the decision; fill the stages backwards with what is documented.

### Step 2: First Pass Only

Work stage 0 if this is the first encounter. Produce: raw statement (verbatim), mandate, form, K.-o. check, gap card, entry stage, expectation statement.

**On every later pass:** Skip stage 0. The object already carries a finding and a gap card. Update the gap card rather than rebuilding it. Re-triaging wastes a turn.

### Step 3: Route by Blocking Stage

Read exactly one file — the blocking stage's. Use the routing table at the top of this document.

**One stage per pass** — never chain two. Each stage file ends with exit criteria. When they are met, restate the status and route to the next stage.

### Step 4: Produce & Self-Check

Respond entirely in the language of the conversation. Field labels and stage names are translated at runtime; field names and enum values stay English (they are machine keys).

Run the self-check below. If any item fails, fix and check again. A response that names gaps but leaves the person guessing what to do has failed.

---

## On Every Pass

### Tone

Teams usually did good work. The research is often solid and the solution principles sound. What is typically missing is **one dimension**: the size of the problem and the measurability of the change.

> Not: "your research isn't enough."
> Instead: "we know the problem exists — we don't yet know how much it weighs."

Name gaps plainly and without hedging, but never imply the work was sloppy. The goal is that teams see the gap themselves.

### Output Format

Produce the current state of the object inline, in the conversation's language. One field per line, values a phrase rather than a paragraph.

**The status line has a fixed shape.** The completed stage and the blocking stage are different numbers and both must appear:

```
Status: stage [n] — [name of stage n] complete · stage [n+1] [name] blocking
```

At the very start that reads *"stage 0 — input complete · stage 1 problem blocking"*. Naming only one of the two is the most common way this gets misread. Fill the blocking stage in full; fill later stages only where material already exists, marked *"not yet reliable — stage [n] is open"*.

Never drop the status line, the blocking stage, or the next action.

### Self-Check Before Sending

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

If any item fails, fix the output and check again.

---

## The Object

Every stage writes into one shared object. **`reference/template-spec.md`** holds the field names, enums, ownership rules, and completion conditions.

Read it when producing structured output, when a field's permitted values matter, or when the object will be handed to another system. For conversational work the prose fields in each stage file are enough.

**All enum fields must stay inside their permitted values.** Four of them are what an external backlog tool sorts on — `stage`, `evidence`, `effort`, `judgement` — so an out-of-range value breaks ranking.

**Key rules:**
- Field ownership: each stage writes only its own fields. Stage 3 does not touch `relevance.baseline_value`; stage 5 does not touch `intent.target`.
- No number without an origin. Every numeric field has a sibling `*_origin`.
- Solution-free briefing: no field in stages 1–3 names a solution. If one appears, move it to stage 4.

---

## For Single Initiatives

When assessing one idea:
1. Classify and route to the blocking stage
2. Read that stage's file and work it
3. One question drives the pass: What is blocking this from advancing?

**Example:** A solution request arrives. Stage 0 completed, entry stage is 1. Read `block-problem.md`, ask what happens if it is not built, reformulate to a problem. One pass.

---

## For Groups & Backlogs

When facilitating a review or session, read **`reference/facilitation.md`** for:
- Session sequence
- Who needs to be in the room
- How to compare several initiatives
- Common failure modes

Key principle: **Initiatives at the same stage compete. At different stages they do not.**

---

## Terminology

**`reference/glossary.md`** holds 63 sourced one-line definitions of the terms used across all stages — output vs. outcome, leading vs. lagging, baseline, proxy, guardrail, attribution, MDE, Goodhart's law, and the five evidence ratings with the research terms behind them.

Read it when a term is used loosely and the disagreement is really about definitions.
