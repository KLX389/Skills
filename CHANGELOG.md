# Changelog

All notable changes to the skills in this repository.

The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/); versions follow [SemVer](https://semver.org/).

Because a skill's `description` controls when Claude triggers it, treat description changes as **behavioral** changes, not cosmetic ones:

- **major** — the skill's scope or output contract changes; existing users will see different results
- **minor** — new stages, reference files or fields; existing behavior preserved
- **patch** — wording, typos, clarifications with no behavioral effect

## [Unreleased]

### Added
- `reference/glossary.md`: 63 sourced one-line definitions covering goals, metric types, evidence, causality, target-system failure modes, and delivery terms

## [0.1.0] — initial release

### Added
- `idea-maturity` skill: five-stage maturity assessment with bottom-up stage routing
- Four-level evidence rating: assumed / reported / observed / validated
- Per-stage deep-dive reference files, loaded one at a time
- Stage 5 produces six comparison figures for portfolio prioritization
- Facilitation guide for group sessions and backlog reviews
- Worked example card
