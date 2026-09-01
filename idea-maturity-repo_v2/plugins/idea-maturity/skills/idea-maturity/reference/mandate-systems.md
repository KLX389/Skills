# Mandate System: What Applies and What Does Not

The mandate is what determines *whether* an initiative should go through the full briefing. It is the first classification decision in stage 0, and it affects which stages exist at all.

## Contents

- What is a mandate?
- The three types
- How to recognize each one
- What each mandate means for each stage
- Obligatory vs. Maintenance: common confusion
- Prioritization implications
- Workflows and examples

---

## What is a Mandate

A mandate answers: **Why does this matter enough to work on?**

The source of the mandate (internal choice, legal requirement, operational crisis) determines what evidence you need and how you measure success.

The mandate is **not** a feature. It is not a deadline. It is the category of decision.

---

## The Three Types

| Type | Source | Recognisable by | Reason it matters |
|------|--------|-----------------|------------------|
| `discretionary` | We choose it | No external sender, no deadline, only upside if built | Maximum evidence needed; we control whether to proceed |
| `obligatory` | Law, contract, platform, audit, security incident | External sender, deadline, consequence for inaction | Minimum evidence needed; the obligation replaces the "why"; we only choose how to comply |
| `maintenance` | Operational necessity | End-of-life, migration, outage risk, technical debt | Reduced evidence; the necessity is already accepted; we measure avoidance of damage |

### Discretionary

**Definition:** A self-assigned initiative. The organization chooses to work on it because it thinks it will create value.

**Examples:**
- "We should add a dark mode — I think users will like it"
- "Let's redesign the checkout flow to reduce drop-off"
- "Idea: experiment with a loyalty program"

**Recognition test:**
- Is there an external sender (law, contract, user demand at scale)? → No
- Is there a deadline imposed from outside? → No
- Is there a consequence for not doing it? → Only opportunity cost (we could do something else instead)

**Key principle:** If we are wrong, we lose nothing but the opportunity to work on something that would have been better. So the evidence bar is high.

### Obligatory

**Definition:** An external requirement that must be fulfilled, regardless of strategic value.

**Examples:**
- "GDPR compliance: we must delete user data on request"
- "Payment card industry standard (PCI): we must upgrade the payment system"
- "Major customer contract: we must deliver feature X by Q3 2027"
- "Platform ban: we must remove feature Y or lose app store access"

**Recognition test:**
- Is there a sender outside our team or organization? → Yes
- Is there a date or deadline? → Usually yes, often hard
- Is there a consequence for not doing it? → Legal, contractual, or market exclusion

**Key principle:** The obligation is a fact. We are not deciding whether to do it; we are deciding how quickly and how cost-effectively to comply. The "why" is not up for debate.

**Obligatory does not mean unimportant.** It means the decision has already been made by a higher authority. We inherit the decision and work backwards to find the cheapest compliant solution.

### Maintenance

**Definition:** A technical or operational necessity that prevents broader work.

**Examples:**
- "Our payment library is end-of-life — we must migrate"
- "Database performance is degrading — we must re-architect the query layer"
- "Security vulnerability in core library — we must patch"
- "Office lease ending — we must migrate to remote infrastructure"

**Recognition test:**
- Is there an external law or contract driving it? → No (obligatory)
- Is there an external customer demand? → No (discretionary)
- Does the system fail or become inoperable if we do not act? → Yes
- Is there a deadline set by technical reality, not business choice? → Yes

**Key principle:** The work is necessary to keep operations running. Success is measured by avoidance of damage (not degrading further), not by value creation.

---

## Stage-by-Stage Impact

### Stage 1 — Problem

| Mandate | What happens |
|---------|--------------|
| **discretionary** | Full evidence required: user problem + business problem + causal chain linking both. Show the gap with data. |
| **obligatory** | **Problem stage is omitted.** The obligation is the justification. Record who obligated you and why, but skip the evidence requirement. The question is not "is there a problem" but "what must we comply with." |
| **maintenance** | **Reduced problem.** Instead of user problem, record the operational risk. Example: "If we do not migrate the database, queries will time out and availability drops." No causal chain through users; the chain is infrastructure → availability → service. |

**Key decision point:** In stage 0, you classified the mandate. If `obligatory`, you know you will not ask "is this a real problem?" You will ask "what does compliance mean?"

**Common mistake:** Treating `obligatory` like `discretionary` and building a user-facing problem statement for something that is legally required. This wastes time; the problem is already given.

### Stage 2 — Relevance

| Mandate | What happens |
|---------|--------------|
| **discretionary** | Full sizing: reach (how many users), frequency (how often), severity (what happens), baseline (today's metric). Four pieces, all with origins. |
| **obligatory** | **Scope of the obligation:** Who must comply? What must they do? Example: "GDPR deletion on request applies to all users with accounts in EU. We have 200K such users. Average deletion request takes 2 hours of manual work." Scope replaces reach. |
| **maintenance** | Risk and frequency: How often does the system fail? How bad is the failure? Example: "Query timeout occurs 3× daily, blocking 10–20 users for 30+ seconds each time." Severity is operational impact, not user frustration. |

**The problem value calculation:** 
- `discretionary`: What it is worth to solve this (money per year)
- `obligatory`: What the consequence is of *not* complying (fine, contract loss, market exclusion). Name the consequence, do not invent a probability.
- `maintenance`: What damage occurs if the system keeps degrading (revenue loss from downtime, customer churn, data loss)

### Stage 3 — Intent & Success Metrics

| Mandate | What happens |
|---------|--------------|
| **discretionary** | Intent is **discovered** in conversation. Goal comes from stages 1–2. Example: "Users should be able to find items in 5 seconds instead of 45, without having to refine their search." |
| **obligatory** | Intent is **given in advance.** The obligation defines the goal. Example: GDPR says the goal is "delete all user data within 30 days of request." The intent is not negotiable. |
| **maintenance** | Intent is **risk mitigation.** Goal comes from avoiding the named damage. Example: "Queries should respond within 2 seconds 99% of the time, without degrading further." |

**The target value (metric + baseline + target date):**
- `discretionary`: Derived from `relevance.problem_value`. You control the target.
- `obligatory`: The deadline is the legal deadline, not a measurement window. Example: "All deletions must be completed within 30 days." The target date is often fixed by law, not by your business choice.
- `maintenance`: The target is the "normal" state, not an improvement. Example: "Queries return in <2s" is the baseline requirement, not an improvement target.

**Worth threshold:**
- `discretionary`: How much value would justify the effort? (Comes from problem value)
- `obligatory`: Not asked. Compliance is not negotiable. The only question in stage 5 is "what is the cheapest compliant way?"
- `maintenance`: How much effort is justified to avoid the damage? (Comes from damage value)

### Stage 4 — Hypotheses

| Mandate | What happens |
|---------|--------------|
| **discretionary** | Full hypothesis space: 2+ paths to the goal, all compared. Test cheapest uncertain ones first. |
| **obligatory** | **Only the "how", never the "whether".** Multiple paths to compliance exist (full delete vs. anonymize vs. archive). Hypotheses compare solutions, not whether to solve. |
| **maintenance** | Full hypothesis space, but constrained by feasibility. Example: "We can migrate to DB X or DB Y" — both solve the uptime problem, but with different trade-offs. |

### Stage 5 — Effort & Worth

| Mandate | What happens |
|---------|--------------|
| **discretionary** | Full business case: cost vs. benefit, ROI, payback period. Build if value > effort (against best alternative). |
| **obligatory** | **Cheapest compliant variant.** Compare only among paths that fulfill the obligation. Example: "Full deletion costs 2 quarters, anonymization costs 4 weeks. Both are compliant. Pick anonymization and ship it." Cost-benefit is not the question; compliance is. |
| **maintenance** | Cost vs. damage avoidance. Example: "Migration costs 1 quarter and prevents 100K/quarter in downtime costs. Worth it." Urgency is higher (we cannot defer indefinitely). |

**Judgement:**
- `discretionary`: `build` / `test` / `defer` / `drop` — all available
- `obligatory`: Usually `build` (compliance is mandatory) or `drop` (if impossible, but rare). `defer` is risky (deadline approaches).
- `maintenance`: Usually `build` (necessary) or `defer with a review date` (kick the can). `test` is rare (maintenance does not usually need validation).

---

## When Obligatory Meets Discretionary

### Deduction model

**Obligatory demand is deducted in advance as a capacity block.** Otherwise every deadline beats every idea and prioritization becomes a formality.

**Process:**
1. List all obligatory initiatives with their deadlines
2. Estimate effort for each (stage 5 binding estimate)
3. Deduct total effort from quarterly capacity
4. Remaining capacity is available for discretionary work
5. Rank discretionary work within the remaining budget

**Example:**
- Quarterly capacity: 4 quarters of work (team of 4)
- Obligatory: GDPR deletion (2 quarters) + Payment upgrade (1.5 quarters) = 3.5 quarters deducted
- Remaining: 0.5 quarters for discretionary work
- Result: Only the cheapest 0.5-quarter discretionary initiatives compete for time

This prevents the scenario where an obligatory deadline always wins against discretionary ideas, even when the discretionary work would create more value.

### What happens in a backlog review?

When sorting multiple initiatives (mix of mandates):

1. **Separate by mandate** — Do not rank obligatory against discretionary
2. **Schedule obligatory first** — with deadlines
3. **Rank discretionary** within remaining capacity — by stage + impact
4. **Maintenance** goes where it fits, but escalates if system risk rises

---

## Common Confusions

### Confusion 1: Obligatory vs. Maintenance

Both are "externally driven." What is the difference?

| Aspect | Obligatory | Maintenance |
|--------|-----------|-------------|
| **Sender** | External: law, contract, platform, customer | Internal: technical reality (end-of-life, outage risk) |
| **Consequence** | Legal, contractual, market exclusion | Technical failure, data loss, service degradation |
| **Example** | "GDPR compliance" | "Database library end-of-life" |
| **Deadline** | Often hard (legal date) | Softer, but urgent (before system fails) |
| **How to tell** | Is someone outside forcing us? → Obligatory | Is the system breaking? → Maintenance |

**Rule of thumb:** If you could legally choose to *not* do it, it is maintenance. If the law says you must, it is obligatory.

### Confusion 2: Obligatory ≠ Unimportant

Obligatory work can create enormous value incidentally. Example: GDPR migration required moving to new database architecture, which also improved query speed. The obligation drove it, but the value was real.

Do not downrank obligatory work just because it was mandated. Stage 5 still produces cost and (incidental) benefit. Just do not expect benefit to justify the work; the obligation already does.

### Confusion 3: Discretionary ≠ Optional

Discretionary means we chose it, not that it is low priority. A discretionary initiative can be higher priority than an obligatory one if:
- The discretionary work creates much more value
- The obligatory deadline is far away (capacity is available)
- The obligatory work is very small

Deduction model still applies: obligatory goes in the calendar first (with dates), then discretionary is ranked.

### Confusion 4: Maintenance deadline is soft

Maintenance has no external deadline, but it has an internal one: the point at which the system fails.

Example: "Database library is end-of-life" has a soft deadline (whenever the vendor stops supporting it), but when security patches stop coming, the deadline becomes hard (ship or lose customers).

Do not confuse soft deadline with no urgency.

---

## Recognizing the Mandate at Entry

### Decision tree for stage 0

```
Is there an external sender?
  ├─ YES: Law, contract, platform, customer demand
  │  └─ Can we legally choose not to do it?
  │     ├─ NO → obligatory
  │     └─ YES → (still not obligatory; see next)
  │
  └─ NO: We thought this up
     └─ Is the system breaking or at risk of breaking?
        ├─ YES → maintenance
        └─ NO → discretionary
```

### Checklist for stage 0

When someone presents an initiative:

```
- [ ] Is there a legal, contractual, or platform requirement? 
       If yes: obligatory
       
- [ ] Is there a hard deadline set by someone outside our team?
       If yes: probably obligatory
       
- [ ] Is the system or data at risk if we do not act?
       If yes: maintenance (or obligatory, if also legally required)
       
- [ ] Are we choosing this because we think it will create value?
       If yes: discretionary
       
- [ ] Is there ambiguity?
       Ask the source: "What happens if we do not do this?"
       - Legal/market consequence → obligatory
       - System breaks → maintenance
       - Lost opportunity → discretionary
```

---

## Stage Presence by Mandate

**Quick reference: which stages actually exist?**

| Stage | discretionary | obligatory | maintenance |
|-------|---------------|-----------|-------------|
| 0 | ✓ | ✓ | ✓ |
| 1 Problem | ✓ | **N/A** (omitted) | ✓ (reduced) |
| 2 Relevance | ✓ | ✓ (scope) | ✓ (risk) |
| 3 Intent | ✓ (discovered) | ✓ (given) | ✓ (risk-based) |
| 4 Hypotheses | ✓ | ✓ (solution only) | ✓ |
| 5 Worth | ✓ | ✓ (cheapest path) | ✓ |

**To read this table:** If blocking stage is 3 and mandate is obligatory, the intent is **given in advance**. You do not discover it; it is provided by the obligation.

---

## Workflows by Mandate

### Discretionary initiative workflow

```
Stage 0 → classify as discretionary
          ↓
Entry Stage 1
          ↓
Stage 1 → gather evidence, build causal chain
   ↓ (if blocked)
   ↓ Stage 2 → size the problem
   ↓ (if blocked or too small) stop
   ↓ Stage 3 → define target from problem value
   ↓ Stage 4 → produce 2+ hypotheses
   ↓ Stage 5 → estimate cost, calculate ROI, decide build/test/defer/drop
   ↓
Judgement made
```

### Obligatory initiative workflow

```
Stage 0 → classify as obligatory
          Record: who, what, deadline
          ↓
Entry Stage 2 (Stage 1 omitted)
          ↓
Stage 2 → clarify scope: who and what is covered, consequences
          ↓
Stage 3 → Intent given by obligation, record deadline
          Target metrics from compliance, not from problem value
          ↓
Stage 4 → Compare compliant solution paths
          (Not: "Should we do this?" but "How do we comply?")
          ↓
Stage 5 → Pick cheapest compliant variant
          Effort v. implementation complexity, not ROI
          ↓
Schedule with deadline as constraint
```

### Maintenance initiative workflow

```
Stage 0 → classify as maintenance
          Record: what is at risk, degradation timeline
          ↓
Entry Stage 1 (reduced form) or Stage 2
          ↓
Stage 1 → Problem is operational: uptime, data integrity, cost
          Causal chain: degradation → damage
          ↓
Stage 2 → Risk and frequency: how often? how bad?
          Problem value: cost of inaction
          ↓
Stage 3 → Intent: return to normal state (not: improve beyond normal)
          Success metric: "X does not degrade further"
          ↓
Stage 4 → Paths to stability (e.g., migrate vs. patch vs. rewrite)
          ↓
Stage 5 → Cost vs. damage avoidance, but with urgency
          Defer is risky; defer requires escalation and review date
          ↓
Schedule to prevent system failure
```

---

## Scenario Examples

### Scenario 1: "We need a dark mode"

**Input:** "Users like dark mode. Other apps have it. Let's add it."

**Stage 0 analysis:**
- External sender? No
- System at risk? No
- Self-assigned value creation? Yes
- **Mandate: discretionary**

**Stages applied:**
- Stage 1: What users are affected? Is there evidence they want dark mode?
- Stage 2: How many would use it? Would it reduce support tickets or increase engagement?
- Stage 3: Target: X% of daily active users switch to dark mode
- Stage 4: Native dark mode vs. CSS filter vs. operating-system detect
- Stage 5: Effort vs. benefit

**Outcome:** If benefit > effort and confidence is high enough, `build`. Otherwise `defer` or `drop`.

---

### Scenario 2: "GDPR deletion compliance"

**Input:** "Regulators say we must delete user data on request within 30 days."

**Stage 0 analysis:**
- External sender? Yes (regulators, law)
- Legal consequence for not doing it? Yes (fines)
- **Mandate: obligatory**

**Stages applied:**
- Stage 1: **Omitted.** The obligation replaces the evidence. Record: "GDPR article 17, 30-day deadline, EU users (200K accounts)."
- Stage 2: **Scope.** Who is covered? All EU users. What must happen? Full deletion of personal data within 30 days.
- Stage 3: **Intent given.** All deletion requests must be processed within 30 days, complying with GDPR. Deadline: set by law.
- Stage 4: Full delete vs. anonymize vs. archive. Which one is compliant and cheapest?
- Stage 5: Compare cost of each compliant path. Pick cheapest. Ship by legal deadline.

**Outcome:** Likely `build` because it is mandatory. Stages 4–5 are about "how fast, how cheap" not "whether."

---

### Scenario 3: "Database library end-of-life"

**Input:** "Our database driver is end-of-life. Vendor stops supporting it in 6 months. We should plan a migration."

**Stage 0 analysis:**
- External sender? Vendor (end-of-life is external technical reality)
- System at risk? Yes (patches will stop, security issues will emerge)
- **Mandate: maintenance**

**Stages applied:**
- Stage 1: **Reduced problem.** Risk is query timeout and security vulnerabilities. Consequence: data loss, customer churn.
- Stage 2: Risk frequency: How often does the old driver fail? Severity: How bad? (data loss, downtime, security exposure)
- Stage 3: Intent: Migrate to a driver that is actively maintained, before end-of-life date.
- Stage 4: Migrate to Driver X, Driver Y, or rewrite with Driver Z.
- Stage 5: Cost vs. avoided damage (data loss, churn). Urgency is high (deadline is end-of-life).

**Outcome:** Likely `build` because maintenance is necessary. Defer only if escalated with a risk acceptance.

---

## Mandate in Retrospect

After an initiative ships, the mandate helps interpret results:

- **Discretionary:** Success is measured against the target. Did the value materialize?
- **Obligatory:** Success is compliance. Did we ship by the deadline? Did we comply with the requirement?
- **Maintenance:** Success is system stability. Did we prevent the predicted failure?

Example: An obligatory GDPR deletion feature ships late and over budget. That is bad project execution. But it succeeded in the mandate sense: users can now delete data, and compliance is met. Do not conflate project success with mandate satisfaction.

---

## Troubleshooting

### "I classified this as discretionary but it feels obligatory"

Likely cause: External pressure that is not yet formalized as a contract or law.

Example: "A major customer is threatening to leave unless we build X."

**Test:** Is there a contract penalty if we do not deliver? If yes, it is obligatory. If not (they might leave, but there is no written consequence), it is discretionary with urgency. Treat it as discretionary but escalate in stage 5 to account for churn risk.

### "This is obligatory but feels discretionary"

Likely cause: The obligation is assumed rather than written.

Example: "We just always upgrade to the latest version of our framework."

**Test:** Is there a written requirement? A contract? A security advisory? If no, it is maintenance, not obligatory. Maintenance still needs doing, but it does not get the obligatory deduction priority.

### "This started as discretionary but became obligatory"

Possible during execution: A discretionary initiative becomes mandatory mid-way (e.g., regulatory announcement).

**Action:** Re-classify in stage 0. Update the object. Stages 1–3 may stay the same (evidence still matters for choosing *how* to comply), but stages 4–5 shift to "cheapest compliant variant."

---

## References

See `input-triage.md` for the mandate classification in stage 0.

See the stage files for how each mandate type affects that specific stage:
- `block-problem.md` — how problem is defined by mandate
- `block-relevance.md` — how sizing differs
- `block-intent.md` — how intent is derived or given
- `phase-hypotheses.md` — how solution space is constrained
- `phase-worth.md` — how success is measured
