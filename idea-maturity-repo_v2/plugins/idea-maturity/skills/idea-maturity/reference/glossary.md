# Glossary

## Framework terms

Briefing: the completed stages 1 to 3; a deliverable with an owner, not a warm-up.

Stage: position in the test sequence; the highest one fully completed.

Blocking stage: the first stage that cannot be honestly affirmed; the only one worked per pass.

Work at risk: material produced above the blocking stage; does not raise the status.

Causal chain: problem-level links from user problem to business problem, each rated.

Effect chain: solution-level links from a change to a business metric, each rated.

Weakest link: the lowest-rated link in a chain; sets the confidence of the whole.

Confidence: inherited rating of the weakest link; a later stage can lower it, never raise it.

Problem value: what being rid of the problem is worth per year, in the portfolio's shared unit.

Worth threshold: value above which the effort is justified; derived from the problem value, never from cost.

Null variant: what happens if nothing is done; the comparison baseline for any business case.

Mandate: whether an initiative is chosen, obliged, or operationally necessary; decides which stages apply. Three types: `discretionary` (internal choice), `obligatory` (external requirement), `maintenance` (operational necessity). See `mandate-systems.md` for full details.

## Goals and intent

Output: what ships; fully controllable, easy to count, no measure of success.

Outcome: behaviour or business change following the output; only partly controllable.

Impact: long-term effect on company goals; rarely attributable to one initiative.

Business goal: outcome the company cares about because it moves money, growth, or position.

User goal: what a user group wants to achieve, stated as value for them.

Hypothesis: causal, falsifiable claim that X leads to Y because Z.

Assumption: something treated as true without evidence; harmless only while stated openly.

Riskiest assumption: the one whose falseness collapses the whole idea.

Falsification: concrete result that would end or redirect the idea.

## Metrics

Metric: defined, repeatable measurement; useful ones are comparative, understandable, and change behaviour.

KPI: metric selected for steering; an organisational status, not a technical property.

Signal: observable indicator that a goal is being reached; sits between goal and metric.

Baseline: measured value before the change; without it no effect can be proven.

Target: value a metric should reach by a stated date; no date, no target.

Timeframe: window over which the outcome is measured; distinct from the delivery deadline.

Leading indicator: early signal predicting the outcome; fast enough to steer by, but a proxy.

Lagging indicator: delayed metric confirming the outcome; trustworthy, often too late to act on.

Proxy metric: stand-in for something hard to measure; the gap to the real goal is its weakness.

Guardrail metric: value that must not get worse; meaningless without a numeric limit.

Vanity metric: number that only rises and prompts no action, such as total signups.

Actionable metric: usually a ratio, reacting to product changes and naming the lever.

## Evidence

Evidence: observations supporting a claim; complete only with source and observation type.

Unknown: rating for a claim nobody has checked; an absence, not a bet.

Assumed: rating for a claim someone finds plausible with no observation behind it.

Reported: rating for a claim someone else made; secondhand, unverified.

Observed: rating for a claim seen firsthand but only qualitatively.

Validated: rating for a claim confirmed by data with the qualitative picture agreeing.

Qualitative data: non-numeric material from interviews and observation; answers why, not how often.

Quantitative data: numeric material from analytics and scaled surveys; answers whether and how much, not why.

Triangulation: cross-checking a finding across sources, methods, or researchers; contradictions are themselves findings.

Saturation: point at which further interviews yield no new themes; the qualitative stopping rule.

Validity: degree to which a measurement captures what it intends to.

Reliability: consistency of a measurement on repetition; a consistent measure can still be wrong.

Construct validity: fit between the chosen metric and the concept meant; clicks are not satisfaction.

Hierarchy of evidence: ranking by reliability, controlled experiments above observational data above anecdote.

## Measurement and causality

Attribution: crediting a change to this intervention rather than seasonality, other launches, or chance.

Controlled experiment: random split into control and treatment to establish cause.

Confounder: third variable driving both cause and effect, faking a relationship.

Significance level: p-value threshold, conventionally 0.05; caps the false-positive rate.

Statistical power: probability of detecting a real effect, conventionally 0.8; calculated before the test.

MDE: smallest effect a test can reliably detect given sample, baseline, significance, and power.

Effect size: magnitude of the difference, independent of sample size.

Cohort: group entering at the same time and tracked onward; separates product change from mix change.

Novelty effect: temporary lift driven by curiosity, fading as attention normalises.

Primacy effect: temporary drop as existing users lose familiar behaviour.

## Failure modes

Goodhart's law: collapse of a measure's usefulness once it becomes a target.

Gameability: ease with which a metric can be lifted without improving the underlying goal.

Twyman's law: rule of thumb that the most surprising figure is the most likely error.

HARKing: forming the hypothesis after seeing the results.

Survivorship bias: analysis limited to those who remained; the departed hold the explanation.

## Delivery

Deliverable: the concrete thing that ships, scoped and assignable.

Owner: single person accountable for delivery; shared accountability is absent accountability.

Acceptance criteria: checks that the deliverable was built as specified; silent on whether it worked.

Constraints: limits the work must respect, such as budget, technology, legal, scope, dependencies.

Deadline: date the deliverable must ship; distinct from the window in which effect is measured.

## Sources

Croll & Yoskovitz, Lean Analytics, 2013 — metric quality, vanity versus actionable, leading versus lagging.

Kohavi, Tang & Xu, Trustworthy Online Controlled Experiments, 2020 — guardrails, gameability, Twyman's law, hierarchy of evidence.

Goodhart 1975, restated by Strathern 1997 — Goodhart's law.

Denzin and Patton — typology of triangulation in qualitative research.
