# Product Thinking Skills

Agent Skills for assessing, maturing and prioritizing product ideas.

Skills are folders of instructions that Claude loads when they become relevant. This repository holds one so far.

## `idea-maturity`

Determines **which stage an idea has reached**, works the one stage that blocks it, and produces the figures needed to rank it against other ideas.

There are always more ideas than people to build them, so prioritization is unavoidable. Prioritization by gut feel is what happens when ideas cannot be compared — and they cannot be compared when one has a measured baseline and the next has an anecdote. Maturity is what makes them comparable.

**The five stages**

| # | Stage | Question it settles |
|---|---|---|
| 1 | Problem exists | Does the problem exist, or do we only perceive it? |
| 2 | Problem is relevant | How big is it — reach, frequency, severity, baseline? |
| 3 | Solution fits | Does *this* solution solve *this* problem, and why this one? |
| 4 | It can be built | Technically, legally, organizationally? |
| 5 | Success is recognizable | Would we recognize whether it worked — and is this idea worth doing before the others? |

You go bottom-up and stop at the first stage you cannot honestly affirm. That is the status. Work above that stage does not raise it; it is work at risk.

Every claim carries a rating — `assumed` / `reported` / `observed` / `validated` — and the weakest link of the causal chain sets the confidence of the whole idea.

**What it is not:** a scoring model. The comparison figures are shown side by side, never multiplied into a single number. Two rough estimates and an inherited rating do not become precise by being multiplied.

### Language

The skill responds in the language of the conversation. Output templates ship with German field labels and are translated at runtime.

## Install

### Claude Code

```
/plugin marketplace add KLX389/Skills
/plugin install idea-maturity@klx389-skills
```

### Claude.ai

Zip the folder `plugins/idea-maturity/skills/idea-maturity` and upload it under Settings → Capabilities → Skills. See [Using skills in Claude](https://support.claude.com/en/articles/12512180-using-skills-in-claude).

### Claude API

Upload the skill folder via the Skills API. See the [Skills API quickstart](https://docs.claude.com/en/api/skills-guide).

## Use

Once installed, no invocation is needed — describe an idea and ask where it stands:

> "Wir haben im Buchungsflow beobachtet, dass die Preisdarstellung inkonsistent ist. Aus 8 Interviews wissen wir, dass Nutzer das irritiert. Wir haben ein Konzept dafür — können wir das nächstes Quartal einplanen?"

The skill names the stage, the one blocking gap, and the cheapest next action.

Other phrasings that trigger it: *where does this stand*, *is this ready to build*, *what's missing*, *how do we prioritize these*, *sort this backlog by readiness*.

## Repository layout

```
.claude-plugin/
  marketplace.json          plugin registry — required at repo root
plugins/
  idea-maturity/
    .claude-plugin/
      plugin.json           plugin metadata
    skills/
      idea-maturity/
        SKILL.md            router: classify, then route
        reference/
          stage-1-problem-evidence.md
          stage-2-problem-size.md
          stage-3-solution-fit.md
          stage-4-buildability.md
          stage-5-targets-and-priority.md
          facilitation.md
          example-card.md
          glossary.md
CHANGELOG.md
```

`glossary.md` carries one-line definitions of the vocabulary used across all stages, with sources named. `SKILL.md` holds only what is needed on every run. Exactly one stage file is loaded per pass — the one that is blocking. This keeps the context small and prevents the wall of questions the skill exists to avoid.

## Contains no executable code

Skills can run arbitrary code in Claude's environment, so read one before installing it. This one is markdown only: no scripts, no network calls, no filesystem writes.

## Versioning

Version numbers live in `plugin.json` and `marketplace.json` and must be bumped together. A skill's `description` controls when Claude triggers it, so changing it changes behavior — see `CHANGELOG.md` for how that maps to SemVer.

## Contributing

Issues and pull requests welcome. For changes to the stages themselves, please include the reasoning: which real situation the current wording handled badly.

## License

Apache-2.0. Add the licence text via GitHub's licence picker so the wording is the canonical one.
