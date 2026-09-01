# Changelog

All notable changes to the skills in this repository.

The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/); versions follow [SemVer](https://semver.org/).

Because a skill's `description` controls when Claude triggers it, treat description changes as **behavioral** changes, not cosmetic ones:

- **major** — the skill's scope or output contract changes; existing users will see different results
- **minor** — new stages, reference files or fields; existing behavior preserved
- **patch** — wording, typos, clarifications with no behavioral effect

## [0.2.0]

### Changed — breaking
- Restructured into stage 0 Input, a three-block briefing (Problem, Relevance, Intent), then Hypotheses and Worth
- Intent now precedes hypotheses: the goal is derived from problem and relevance, never from the solution
- Hypotheses are plural — several paths to one fixed goal, compared against each other
- Evidence rating extended to five levels: unbekannt, angenommen, berichtet, beobachtet, nachgewiesen
- Confidence is inherited from the weakest chain link and can never be raised by a later stage
- All field names, enum values and examples are English; labels are translated at runtime

### Added
- `reference/template-spec.md`: machine-readable field spec with closed enums and field ownership rules
- `reference/glossary.md`: 63 sourced one-line definitions
- Stage 0 produces a gap card and a calculated expectation statement
- Mandate (diskretionär / obligatorisch / erhaltend) determines which stages apply

## [0.1.0] — initial release

### Added
- `idea-maturity` skill: five-stage maturity assessment with bottom-up stage routing
- Four-level evidence rating: assumed / reported / observed / validated
- Per-stage deep-dive reference files, loaded one at a time
- Stage 5 produces six comparison figures for portfolio prioritization
- Facilitation guide for group sessions and backlog reviews
- Worked example card
