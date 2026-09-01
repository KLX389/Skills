# Template Specification

One object per initiative. Each stage writes only its own fields. When a required field is unknown, the stage remains blocking until the measurement or explicit decision closes the gap.

Field names and enum values are machine keys and stay in English. Human-facing labels may be translated at runtime.

## Rules

1. Field ownership: each stage writes only its own fields. Stage 3 does not edit `relevance.baseline_value`; stage 5 does not edit `intent.target`.
2. Enums are closed. No free text in enum fields.
3. `unknown` is a value, `null` is not. `null` means not yet worked. A worked but unknown required field gets `"unknown"` plus an item in `open_measurements`, and the stage remains blocking.
4. No number without an origin. Every numeric field has a sibling origin or derivation field. Missing origin means the value is unset.
5. Solution-free briefing: no active stage 1-3 field names a solution. Trace fields may quote the original solution: `input.raw_statement`, `problem.reformulated_from`, and `work_at_risk` notes.
6. Confidence is derived, not entered. It equals the weakest relevant link and can only stay equal or go down in later stages.
7. No single priority score. Sort by stage first, then compare impact, effort, and confidence side by side within the same stage.

## Enums

```text
mandate          discretionary | obligatory | maintenance
form             observation | complaint | problem_claim | solution_request | hypothesis | assignment
stage            0 | 1 | 2 | 3 | 4 | 5
block_status     open | partial | complete | not_applicable
evidence         unknown | assumed | reported | observed | validated
method           interview | analytics | tickets | usability_test | benchmark | operations | audit | other
indicator_type   leading | lagging
target_status    proposed | confirmed
attribution      control_group | before_after | unresolved
test_type        data_check | fake_door | prototype | wizard_of_oz | full_build_test | other
effort           XS | S | M | L | XL
reversibility    switchable | partial | irreversible
candidate_type   build | test
judgement        build | test | defer | drop
```

Effort reference: XS under 1 week; S 1-2 weeks; M 3-6 weeks; L 1 quarter; XL must be decomposed.

## Stage 0 - Input

Reads and records. Does not reformulate.

```yaml
id:                    string
title:                 string
created:               date
stage:                 0
input:
  raw_statement:       string
  source:              string
  occasion:            string
  mandate:             enum mandate
  mandate_reasoning:   string
  form:                enum form
  form_reasoning:      string
  ko_check:            bool            # true = known blocker exists
  ko_reason:           string | null
gap_card:
  - stage:             int
    status:            enum block_status
    reasoning:         string
    work_at_risk:      bool
entry_stage:           int
expectation:           string
closure:
  judgement:           enum judgement | null
  reason:              string | null
```

Required to advance: `mandate`, `form`, `ko_check`, `gap_card`, `entry_stage`, `expectation`.

Abort: `input.ko_check: true` -> `closure.judgement: drop`.

## Stage 1 - Problem

```yaml
problem:
  reformulated_from:   string | null
  user_problem:        string
  segment:             string
  business_problem:    string
  business_metric:     string
  causal_chain:
    - link:            string
      evidence:        enum evidence
      source:          string
      method:          enum method
  weakest_link:        int
  confidence:          enum evidence
  open_questions:      [string]
  cut:
    multiple_problems: bool
    sub_problems:      [string]
```

Required for `discretionary`: `user_problem`, `segment`, `business_problem`, `business_metric`, `causal_chain` with at least two links, `weakest_link`, `cut.multiple_problems`.

Derived: `confidence = causal_chain[weakest_link].evidence`.

Mandate: `obligatory` -> `gap_card.status: not_applicable`. `maintenance` -> use operational risk in `user_problem` and system/availability/cost in the chain.

Branch: `cut.multiple_problems: true` -> split; each sub-problem becomes its own object.

## Stage 2 - Relevance

```yaml
relevance:
  reach:               string | "unknown"
  reach_origin:        string
  frequency:           string | "unknown"
  frequency_origin:    string
  severity:            string | "unknown"
  severity_origin:     string
  baseline_metric:     string
  baseline_value:      number | "unknown"
  baseline_origin:     string
  baseline_period:     string
  problem_value:       number | "unknown" | "not_convertible"
  problem_value_unit:  string
  problem_value_origin: string
  open_measurements:
    - what:            string
      how:             string
      owner:           string
      due:             date
```

Required for completion: reach, frequency, severity, baseline, and problem value each set with origin. `unknown` required values keep stage 2 blocking and must have an `open_measurements` entry. `not_convertible` is complete only when the reason is stated in `problem_value_origin`.

Handover: `problem_value` is the basis for the stage 3 worth threshold. `baseline_value` is the basis for the target formula.

Mandate: for `obligatory`, reach means scope of the obligation and problem value means avoided consequence.

## Stage 3 - Intent And Success Metrics

```yaml
intent:
  statement:           string
  user_group:          string
  result:              string
  current_problem:     string
  target:
    metric:            string
    baseline:          number
    target_value:      number
    target_status:     enum target_status
    date:              date
  worth_threshold:
    value:             number | "not_applicable"
    unit:              string | null
    derivation:        string
    reachable:         bool | null
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
  stop_criterion:      string
  attribution:         enum attribution
  decider:             string
  decision_date:       date
```

Required for completion: solution-free `statement`, complete `target`, leading and lagging indicators, at least one guardrail, stop criterion, attribution, decider, and decision date.

For `discretionary` and `maintenance`, `worth_threshold.value`, `unit`, `derivation`, and `reachable` are required. For `obligatory`, use `value: "not_applicable"`, `reachable: null`, and derive success from compliance scope and deadline.

Lock: stage 3 must not read effort or cost. The target is user-near or operation-near; the threshold comes from `relevance.problem_value`.

Branch: `worth_threshold.reachable: false` -> close with `judgement: drop` before stage 4.

## Stage 4 - Hypotheses

```yaml
hypotheses:
  - id:                string
    statement:         string
    effect_chain:
      - link:          string
        evidence:      enum evidence
        source:        string
    weakest_link:      int
    confidence:        enum evidence
    riskiest_assumption: string
    cheapest_test:
      type:            enum test_type
      effort:          enum effort
      decides:         string
    rough_effort:      enum effort
    target_contribution: string
    candidate_type:    enum candidate_type
null_variant:
  consequence:         string
chosen_hypothesis:     string | null
```

Required: at least two hypotheses plus `null_variant`. Each effect chain ends on the business metric or mandate consequence.

Derived: `confidence` is the weakest link, capped by `problem.confidence` when stage 1 applies. `candidate_type = test` when confidence is `unknown` or `assumed`; `candidate_type = build` when confidence is `reported`, `observed`, or `validated`.

Branch: `candidate_type: test` -> skip stage 5 until the cheapest test updates evidence. `candidate_type: build` means eligible for stage 5, not approved for implementation.

## Stage 5 - Effort And Worth

```yaml
worth:
  effort:              enum effort
  effort_source:       string
  dependencies:        [string]
  prerequisites:
    - what:            string
      owner:           string
      due:             date | null
  owner:               string
  reversibility:       enum reversibility
  business_case:
    cost:              number
    benefit:           number
    unit:              string
    compared_with:     string
    payback:           string | null
    threshold:         string
    confidence:        enum evidence
  opportunity_cost:    string
  judgement:           enum judgement
  judgement_reasoning: string
```

Required: effort with source, dependencies, prerequisites, owner, reversibility, complete business case, opportunity cost, judgement, and judgement reasoning.

Lock: `effort_source` must not be only the idea author. `business_case.confidence` inherits the chosen hypothesis confidence.

For `obligatory`, `business_case.threshold` is the compliance deadline or minimum compliant scope rather than ROI payback.

## Derived Fields For Prioritization

Calculated, never entered:

```yaml
prioritization:
  stage:               0..5
  blocking_stage:      int | null
  impact_amount:       number | null
  impact_unit:         string | null
  impact_relative:     string
  impact_origin:       string
  effort:              enum effort | null
  confidence:          enum evidence
  next_step:
    action:            string
    owner:             string | "unknown"
    due:               date | "unknown"
  comparable:          bool
```

Sort rule: group by stage first. Within one stage, compare impact, effort, and confidence side by side. Never create a single score.

## Completion

The briefing is complete when all applicable required fields of stages 1-3 are complete. For obligatory mandates, stage 1 is `not_applicable` and the briefing can complete after stages 2-3.

An initiative is ready to rank when stage 5 is complete and `worth.judgement` is set.

Closed without implementation when one of these holds:

```text
input.ko_check = true                     -> drop, known blocker
intent.worth_threshold.reachable = false  -> drop, target value unreachable
stage 1 required evidence = unknown       -> pause until first evidence
stage 2 required size = unknown           -> measure first
hypothesis.candidate_type = test          -> test first, stage 5 stays open
worth.business_case.cost > benefit        -> drop, effort exceeds value
capacity committed elsewhere              -> defer, with review date
```

In every case, keep the object. A documented rejection prevents the same idea from returning unexamined.
