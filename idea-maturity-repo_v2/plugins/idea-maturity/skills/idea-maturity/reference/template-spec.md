# Template Specification

One object per initiative. Each stage writes only into its own fields. When the object is complete, the initiative is ready to be ranked.

Field names and enum values are **machine keys and stay in English**. Labels shown to a person are translated at runtime.

## Rules

1. **Field ownership.** Each stage writes only its own fields. Stage 3 does not touch `relevance.baseline_value`; stage 5 does not touch `intent.target`. Otherwise the ordering rules can be bypassed.
2. **Enums are closed.** No free text in enum fields.
3. **`unknown` is a value, `null` is not.** `null` means "not yet worked". A worked but unknown field gets `"unknown"` plus an entry in `open_measurements`.
4. **No number without an origin.** Every numeric field has a sibling `*_origin`. Missing the origin, the value counts as unset.
5. **Solution-free briefing.** No field in stages 1–3 names a solution. If one appears, it belongs in stage 4.

## Enums

```
mandate          discretionary | obligatory | maintenance
form             observation | complaint | problem_claim | solution_request | hypothesis | assignment
stage            0 | 1 | 2 | 3 | 4 | 5
block_status     open | partial | complete | not_applicable
evidence         unknown | assumed | reported | observed | validated
method           interview | analytics | tickets | usability_test | benchmark | operations | other
indicator_type   leading | lagging
target_status    proposed | confirmed
attribution      control_group | before_after | unresolved
effort           XS | S | M | L | XL
reversibility    switchable | partial | irreversible
candidate_type   build | test
judgement        build | test | defer | drop
```

Size reference for `effort`: XS under 1 week · S 1–2 weeks · M 3–6 weeks · L 1 quarter · XL do not estimate, decompose.

---

## Stage 0 — Input

Reads and records. **Does not reformulate** — that is the first action in stage 1.

```yaml
id:                    string
title:                 string          # one sentence, derived from the raw input
created:               date
stage:                 0
input:
  raw_statement:       string          # verbatim, unchanged
  source:              string
  occasion:            string          # why now
  mandate:             enum mandate
  mandate_reasoning:   string
  form:                enum form
  form_reasoning:      string          # what it was recognised by
  ko_check:            bool            # true = known blocker exists
  ko_reason:           string | null
gap_card:
  - stage:             int
    status:            enum block_status
    reasoning:         string
    work_at_risk:      bool            # material exists, preconditions open
entry_stage:           int
expectation:           string          # calculated from open stages and mandate
```

**Required to advance:** `mandate`, `form`, `ko_check`, `gap_card`, `entry_stage`, `expectation`.
**Abort:** `ko_check: true` → end, `judgement: drop`.

---

## Stage 1 — Problem

```yaml
problem:
  reformulated_from:   string | null   # original wording, if reformulated
  user_problem:        string          # user terms, never a missing feature
  segment:             string          # precise group, not "users"
  business_problem:    string
  business_metric:     string          # which metric suffers
  causal_chain:
    - link:            string
      evidence:        enum evidence
      source:          string
      method:          enum method
  weakest_link:        int             # index into causal_chain
  confidence:          enum evidence   # derived, never entered
  open_questions:      [string]
  cut:
    multiple_problems: bool
    sub_problems:      [string]        # if true, each gets its own object
```

**Required:** `user_problem`, `segment`, `business_problem`, `business_metric`, `causal_chain` with at least two links, `weakest_link`, `cut.multiple_problems`.
**Derived:** `confidence` = `causal_chain[weakest_link].evidence`.
**Branch:** `multiple_problems: true` → split; each sub-problem becomes its own object with its own briefing.
**Mandate:** `obligatory` → `block_status: not_applicable`, the obligation replaces the evidence. `maintenance` → reduced: outage risk instead of user problem.

---

## Stage 2 — Relevance

```yaml
relevance:
  reach:               string          # number or range, range preferred
  reach_origin:        string
  frequency:           string
  frequency_origin:    string
  severity:            string          # a consequence, not an adjective
  severity_origin:     string
  baseline_metric:     string
  baseline_value:      number | "unknown"
  baseline_origin:     string
  baseline_period:     string          # measurement window
  problem_value:       number | "unknown" | "not_convertible"
  problem_value_unit:  string
  problem_value_origin: string         # the calculation, traceable
  open_measurements:
    - what:            string
      how:             string
      owner:           string
      due:             date
```

**Required:** `reach`, `frequency`, `severity`, `baseline_*` — each with an origin. Unknown values as `"unknown"` plus an entry in `open_measurements`.
**Handover:** `problem_value` is the sole basis of the worth threshold in stage 3.
**Mandate:** for `obligatory`, `reach` means the scope of the obligation and `problem_value` the avoided consequence, named rather than calculated from an invented probability.

---

## Stage 3 — Intent & Success Metrics

Goal-bound and solution-free. The fill-in-the-blank is the acceptance test for stages 1 and 2.

```yaml
intent:
  statement:           string          # [group] should achieve [result], without [problem]
  user_group:          string          # ← problem.segment
  result:              string
  current_problem:     string          # ← problem.user_problem
  target:
    metric:            string          # user-near, NOT the business metric
    baseline:          number          # ← relevance.baseline_value
    target_value:      number
    target_status:     enum target_status
    date:              date            # measurement deadline
  worth_threshold:
    value:             number
    unit:              string
    derivation:        string          # from relevance.problem_value
    reachable:         bool            # false → drop, no hypotheses
  indicators:
    - metric:          string
      type:            enum indicator_type
      baseline:        number
      target_value:    number
      period:          string
  guardrails:
    - metric:          string
      limit:           number
      direction:       "not above" | "not below"
      reasoning:       string
  stop_criterion:      string          # a result, not a date
  attribution:         enum attribution
  decider:             string
  decision_date:       date
```

**Required:** `statement`, complete `target`, `worth_threshold`, at least one `leading` and one `lagging` indicator, at least one guardrail, `stop_criterion`, `decider`, `decision_date`.
**Lock:** this block must not read any effort or cost field. The target value is derived from `relevance.problem_value`, never from implementation cost.
**Check:** `worth_threshold.reachable: false` → `judgement: drop`, without stages 4 and 5.
**Mandate:** for `obligatory` the intent is given in advance; `date` is the legal deadline.

---

## Stage 4 — Hypotheses

Solution-bound and plural. Requires a completed briefing.

```yaml
hypotheses:
  - id:                string
    statement:         string          # If [X], then [Y] among [group], because [Z]
    effect_chain:                      # must end on a business metric
      - link:          string
        evidence:      enum evidence
        source:        string
    weakest_link:      int
    confidence:        enum evidence   # derived; never above problem.confidence
    riskiest_assumption: string
    cheapest_test:
      type:            string          # data_check | fake_door | prototype | wizard_of_oz
      effort:          enum effort
      decides:         string
    rough_effort:      enum effort     # for comparison only
    target_contribution: string
    candidate_type:    enum candidate_type   # derived from confidence
null_variant:
  consequence:         string          # what happens if nothing is done
chosen_hypothesis:     string          # id
```

**Required:** at least two hypotheses plus `null_variant`. A single hypothesis is a warning sign, not a result.
**Derived:** `candidate_type` = `test` when `confidence` ≤ `assumed`, otherwise `build`.
**Branch:** `candidate_type: test` → skip stage 5; the next step is `cheapest_test`.

---

## Stage 5 — Effort & Worth

For `chosen_hypothesis` only.

```yaml
worth:
  effort:              enum effort
  effort_source:       string          # must not be the idea's author
  dependencies:        [string]
  prerequisites:
    - what:            string
      owner:           string
  owner:               string          # one person
  reversibility:       enum reversibility
  business_case:
    cost:              number
    benefit:           number
    unit:              string          # the portfolio's shared unit
    compared_with:     string          # best alternative, never "do nothing"
    payback:           string
    threshold:         string          # set in advance
    confidence:        enum evidence   # ← chosen hypothesis
  opportunity_cost:    string          # the specific initiative displaced
  judgement:           enum judgement
  judgement_reasoning: string
```

**Required:** `effort` with `effort_source`, `owner`, complete `business_case`, `opportunity_cost`, `judgement`.
**Lock:** `effort_source` must not be the idea's author.
**Derived:** `business_case.confidence` = confidence of the chosen hypothesis. Two exact figures resting on an `assumed` remain a bet.

---

## Derived fields for prioritization

Calculated, never entered. These are the sort keys for an external backlog tool.

```yaml
prioritization:
  stage:               0..5            # highest fully completed stage
  blocking_stage:      int             # stage + 1
  impact_amount:       number          # ← worth.business_case.benefit
  impact_unit:         string
  impact_relative:     string          # "completion rate +4 pp"
  impact_origin:       string
  effort:              enum effort
  confidence:          enum evidence
  next_step:
    action:            string
    owner:             string
    due:               date
  comparable:          bool            # false when the benefit cannot be converted
```

**Sort rule:** group by `stage` first, then within the group by `impact_amount` against `effort`. Initiatives at different stages do not compete — the lower one needs evidence, not a decision.

**Never form a single score.** As soon as `stage 1 · assumed · high` and `stage 5 · validated · medium` produce the same number, the stage column is worthless.

---

## Completion

The briefing is **complete** when all required fields of stages 1–3 are set. Only then does stage 4 begin.

```yaml
briefing:
  status:              enum block_status
  open_blocks:         [string]
  confidence:          enum evidence   # ← problem.confidence
  owner:               string
  completed:           date | null
  handover_to:         string          # who forms the hypotheses
```

An initiative is **ready to rank** when `stage = 5` and `worth.judgement` is set.

It is **closed without implementation** when one of these holds:

```
input.ko_check = true                     → drop, known blocker
intent.worth_threshold.reachable = false  → drop, target above what is achievable
problem.confidence = unknown              → paused until measured
hypothesis.candidate_type = test          → test first, stage 5 stays open
worth.business_case.cost > benefit        → drop, effort exceeds value
capacity committed elsewhere              → defer, with a review date
```

In every case the object is kept. A documented rejection stops the same idea returning unexamined two quarters later.

**What the briefing hands to stage 4:**

| Field | Becomes |
|---|---|
| `intent.statement` | The fixed goal that paths are compared against |
| `intent.target` | The yardstick for each hypothesis's target contribution |
| `intent.worth_threshold` | The ceiling for defensible effort |
| `problem.causal_chain` | Points of attack — each link is a possible lever |
| `problem.confidence` | Starting value; a hypothesis can only lower it, never raise it |
| `relevance.problem_value` | The ceiling of achievable benefit |
