# Idea Maturity

`idea-maturity` is a product-thinking skill for assessing, maturing, and prioritizing product initiatives.

It turns raw input - an idea, feature request, research finding, complaint, backlog item, or assignment - into a structured maturity object. The output names the current status, the one blocking gap, and the cheapest next action.

## What It Does

There are always more ideas than teams can build. Prioritization by gut feel appears when initiatives cannot be compared: one has a measured baseline, the next has an anecdote, and both are discussed as if they were equally mature.

This skill keeps maturity visible. It separates:

- what has been evidenced
- what has merely been assumed
- what is already solution work but rests on open lower stages
- what is ready to test, build, defer, or drop

It is not a scoring model. The skill never multiplies rough impact, effort, and confidence into one number. Initiatives are grouped by stage first and compared only within the same maturity group.

## Stage Sequence

| # | Stage | Question it settles |
|---|---|---|
| 0 | Input | What arrived, and which mandate applies? |
| 1 | Problem | Whose problem is this, and what evidence supports it? |
| 2 | Relevance | How big is the problem: reach, frequency, severity, baseline, value? |
| 3 | Intent | What should be true instead, and how will success be recognized? |
| 4 | Hypotheses | Which solution paths could reach that fixed intent? |
| 5 | Worth | Is the chosen path worth its effort against the best alternative? |

Stages 1-3 form the briefing. The briefing is solution-free and stands on its own. Only after it is complete does the skill compare solution hypotheses.

## Core Rules

- Stop at the first stage that cannot honestly be affirmed.
- Work exactly one primary stage per pass.
- Treat existing work above the blocking stage as `work_at_risk`.
- Give every material claim an evidence rating: `unknown`, `assumed`, `reported`, `observed`, or `validated`.
- Inherit confidence from the weakest link in the causal or effect chain.
- Never invent numbers. Write `unknown -> measure first` and attach owner and due date.
- Keep solutions out of stages 1-3 except in trace fields such as `input.raw_statement` and `problem.reformulated_from`.
- Compare discretionary, obligatory, and maintenance initiatives differently; do not rank obligatory work against discretionary upside.

## Install

### Codex Plugin

The package contains a Codex-compatible local plugin manifest:

```text
idea-maturity-repo_v2/
  .agents/plugins/marketplace.json
  plugins/idea-maturity/.codex-plugin/plugin.json
```

From a local checkout, add the package root as a marketplace, then install `idea-maturity` through the Codex plugin flow.

### Direct Skill Upload

For environments that accept a standalone skill folder, upload or zip:

```text
plugins/idea-maturity/skills/idea-maturity
```

The skill payload itself is Markdown only: no runtime scripts, no network calls, no filesystem writes.

## Use

Once installed, describe an initiative and ask for maturity, readiness, prioritization, or missing evidence:

> "Wir haben im Buchungsflow beobachtet, dass die Preisdarstellung inkonsistent ist. Aus 8 Interviews wissen wir, dass Nutzer das irritiert. Wir haben ein Konzept dafür - können wir das nächstes Quartal einplanen?"

The skill should answer with the current status, the blocking stage, the relevant fields for that stage, and one concrete next action.

Common trigger phrasing:

- "Where does this stand?"
- "Is this ready to build?"
- "What evidence is missing?"
- "Prioritize this backlog by readiness."
- "Was the idea wrong, or did the implementation fail?"

## Repository Layout

```text
idea-maturity-repo_v2/
  .agents/
    plugins/
      marketplace.json
  plugins/
    idea-maturity/
      .codex-plugin/
        plugin.json
      skills/
        idea-maturity/
          SKILL.md
          reference/
            input-triage.md
            block-problem.md
            block-relevance.md
            block-intent.md
            phase-hypotheses.md
            phase-worth.md
            template-spec.md
            mandate-systems.md
            edge-cases-and-workflows.md
            facilitation.md
            example-briefing.md
            glossary.md
  tests/
    test_skill_contract.py
  CHANGELOG.md
  README.md
```

`SKILL.md` contains shared routing and operating rules. Each primary stage file contains the detailed workflow for that stage. Support references are loaded only when their case applies.

## Validation

Run the skill validator:

```bash
python3 /Users/alexkeil/.codex/skills/.system/skill-creator/scripts/quick_validate.py plugins/idea-maturity/skills/idea-maturity
```

Run the repository contract tests:

```bash
python3 tests/test_skill_contract.py
```

If plugin metadata changed, also validate the plugin manifest:

```bash
python3 /Users/alexkeil/.codex/skills/.system/plugin-creator/scripts/validate_plugin.py plugins/idea-maturity
```

## Versioning

The plugin version lives in `plugins/idea-maturity/.codex-plugin/plugin.json`. Changes to `SKILL.md` frontmatter description are behavioral because they change automatic invocation. Treat them accordingly in `CHANGELOG.md`.

## License

Apache-2.0.
