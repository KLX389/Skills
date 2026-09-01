# Worked example

Read this when unsure how blunt the verdict should be, how short field values should be, or how to handle a stage where nothing is known.

## Input

> "We need a price overview in the booking flow. The price display is inconsistent across the steps, sometimes with fees, sometimes without. From our 8 interviews we know this irritates users. We'd like to schedule it for next quarter."

## Stage 0 output

**FINDING**

Received: "We need a price overview in the booking flow." — Product Owner, retro on 12 March

- Mandate: **discretionary**, self-assigned, no external sender
- Form: **solution_request** — names an artefact ("price overview"), not the problem. The interviews supply supporting material but do not change the form.
- K.-o.: no known blocker

**GAP CARD**

```
1 Problem      ○ open       solution given, the problem behind it unnamed
2 Relevance    ○ open       no number, no baseline
3 Intent       ○ open       depends on 1 and 2
4 Hypotheses   ◐ partial    "price overview" is one — no effect chain, no alternatives
5 Worth        ○ open       depends on 3 and 4
```

Entry: stage 1

**EXPECTATION**

> This is a solution request — the solution is settled, the problem behind it is not. Three blocks are missing before there is a complete briefing: problem, relevance, and intent with success metrics. At the end you will hold an evidenced problem with a size, and an intent statement with a target value and a deadline — the basis on which solution paths become comparable at all.
>
> We start at stage 1. One question first: what happens if you do *not* build the overview?

## Stage 1 output, after the answer

**Status: stage 0 — input complete · stage 1 problem blocking**

Plainly: the irritation is reported, not observed, and the business problem has not been named. The concept therefore rests on a stage it has not reached.

- Reformulated from: "We need a price overview"
- User problem: users only recognise the final price late in the flow and have to work backwards — **reported**
  - Evidence: 8 interviews, March, existing customers (method: interview). For `observed`, seeing the behaviour itself is missing.
- Segment: first-time bookers without an account
- Business problem: not formulated — **unknown**
  - Evidence: missing → which metric suffers, revenue or support cost?
- Causal chain:
  1. Price display changes between steps — `validated` (screenshots)
  2. Final price only visible late — `observed` (flow analysis)
  3. User uncertainty — `reported` (interviews)
  4. Drop-off at step 3 — `assumed`
  5. Lost revenue — `assumed`
- Weakest link: **4** — the interviews show irritation, not abandonment. That uncertainty causes the drop-offs is conjecture; the final price itself would do as well.
- Confidence: **assumed**
- Cut: one problem

**Missing for stage 2**

- [ ] Drop-off rate per booking step from the funnel → analytics query → Data, week 12
- [ ] Name the business problem: which metric concretely suffers → Product
- [ ] Check whether support tickets on pricing exist → Support

**Next step**

Run the funnel query. Two days, and it decides whether link 4 holds — before the concept is developed any further.

## What this demonstrates

- The verdict comes first and is blunt. It does not open with praise.
- Stage 0 records the original wording; stage 1 reformulates and keeps `reformulated_from`.
- Status stays 0 even though a concept exists — work above the blocking stage does not raise it.
- Unknowns are written as unknown, never smoothed into a plausible estimate.
- The weakest link is named by number and reason, not as "some uncertainty".
- Confidence is the weakest link's rating, not an assessment.
- Stages 2–5 are omitted entirely — filling them with stage 1 open would be noise.
- The next step is one action, cheap, and decides the blocking stage.
