# Stage 0 — Input

## Contents
- What this stage does and does not do
- Mandate
- Form
- K.-o. check
- The gap card
- The expectation statement
- Exit criteria

Reads and records. **Does not reformulate** — that is the first action in the problem block. Rewriting before recording destroys traceability: nobody can later tell whether a phrasing was received or translated.

## Mandate — determines the *whether*

| Value | Source | Recognisable by |
|---|---|---|
| `discretionary` | We choose it | No compulsion, only benefit |
| `obligatory` | Law, contract, platform, audit, security incident | External sender, deadline, consequence for inaction |
| `maintenance` | Operational necessity | End-of-life, migration, outage risk |

The mandate decides which stages apply at all. Sending a regulatory deadline through five stages burns discovery capacity on something that will happen regardless.

| Stage | discretionary | obligatory | maintenance |
|---|---|---|---|
| 1 Problem | full | **omitted** — the obligation replaces the evidence | reduced: outage risk instead of user problem |
| 2 Relevance | full | scope of the obligation: who and what is covered | risk and frequency |
| 3 Intent | is discovered | **given in advance** — the obligation is the goal, its deadline the date | avoided damage |
| 4 Hypotheses | full | full — only the *how*, never the *whether* | full |
| 5 Worth | value against effort | cheapest compliant variant | avoided damage against effort |

Obligatory demand does not compete with discretionary demand. It is deducted in advance as a capacity block with a deadline; what remains gets prioritized. Otherwise every deadline beats every idea and prioritization becomes a formality.

**See also:** `mandate-systems.md` for the full decision tree, recognizing each mandate type, common confusions, and workflows. Read this when mandate classification is unclear or when comparing multiple initiatives.

## Form — determines the *how*

| Value | Recognisable by | Entry point |
|---|---|---|
| `observation` | A state, no judgement, no proposal | Stage 1 |
| `complaint` | Emotion or judgement, usually secondhand | Stage 1 |
| `problem_claim` | A shortfall in user terms, no solution | Stage 1 |
| `solution_request` | Names an artefact: "we need a…" | Stage 1, reformulate first |
| `hypothesis` | Contains a causal "because" linking two things | Stage 1, verify backwards |
| `assignment` | Decision already taken, deadline set | Stage 1, verify backwards |

**Detection test — first matching question wins:**

```
Deadline or settled decision named?        → assignment
Artefact named ("a filter", "a tool")?     → solution_request
Causal "because" linking two things?       → hypothesis
A number given?                            → observation
Emotion or judgement?                      → complaint
Shortfall in user terms?                   → problem_claim
```

Two forms need care:

**`solution_request` is the most common input and the only one requiring rollback.** It looks mature because it is concrete, but it has skipped stages 1–3 and installed the solution as a premise.

**`assignment` is the most dangerous.** Formally the most advanced, it says nothing about evidence — someone decided, that is all. Do not challenge the decision; fill the stages backwards with what is already documented. If stage 1 stays empty, that is a visible fact rather than an objection.

## K.-o. check

One question: does anything already known stand hard against this — legally, contractually, technically? Five minutes, no effort estimation, no dependency analysis.

Yes → end with a reason. The object is kept; a documented rejection stops the same idea returning unexamined two quarters later.

This check sits here, not in stage 5, so that an initiative does not mature through four stages and then die on a contract clause that was known all along.

## The gap card

```
FINDING

Received:   "[raw statement, verbatim]"
            — [source], [occasion], [date]

Mandate:    [value], [reasoning]
Form:       [value] — [what it was recognised by]
K.-o.:      [no known blocker | reason]

GAP CARD

1 Problem      ○ open       [reasoning]
2 Relevance    ○ open       [reasoning]
3 Intent       ○ open       [reasoning]
4 Hypotheses   ◐ partial    [material exists but does not count — lower stages open]
5 Worth        ○ open       [depends on 3 and 4]

Entry:      Stage [n] — [what to do there]
```

Marking existing material as *work at risk* rather than ignoring it is more honest and less likely to be argued with.

## The expectation statement

Calculated, not recited. It states what arrived, how many stages remain, and what the person will hold at the end. Length follows the mandate: a discretionary solution request needs the full statement, an obligatory one two sentences.

> This is a solution request — the solution is settled, the problem behind it is not. Three blocks are missing before there is a complete briefing: problem, relevance, and intent with success metrics. At the end you will hold an evidenced problem with a size, and an intent statement with a target value and a deadline — the basis on which solution paths become comparable at all.
>
> We start at stage 1. One question first: what happens if you do *not* build the overview?

Ending on the first question of the next stage keeps the pass moving instead of pausing for approval.

## Exit criteria

```
- [ ] Raw statement recorded verbatim, with source and occasion
- [ ] Mandate set, with reasoning
- [ ] Form set, with what it was recognised by
- [ ] K.-o. check answered
- [ ] Gap card produced for all five stages
- [ ] Expectation stated, ending with the first question of the entry stage
- [ ] Nothing reformulated yet
```

## Special cases

**Re-triage (later pass on a known initiative):** See `edge-cases-and-workflows.md` — "Re-triage: Later pass on a known initiative". Do not rebuild the gap card; update it with a dated note of what changed.

**Assignment with uncertain mandate:** If an `assignment` arrives and the mandate is unclear (is this obligatory or discretionary?), ask before proceeding. The mandate determines which stages apply. See `edge-cases-and-workflows.md` — "Lost entry point: Unknown blocks recovery".
