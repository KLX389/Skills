# Changelog

All notable changes to the skills in this repository.

The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/); versions follow [SemVer](https://semver.org/).

Because a skill's `description` controls when Claude triggers it, treat description changes as **behavioral** changes, not cosmetic ones:

- **major** — the skill's scope or output contract changes; existing users will see different results
- **minor** — new stages, reference files or fields; existing behavior preserved
- **patch** — wording, typos, clarifications with no behavioral effect

## [0.3.0]

### Changed
- Narrowed the skill trigger description so ordinary implementation requests do not invoke the skill unless maturity, evidence, readiness, or prioritization is in question
- Clarified that one primary stage file is worked per pass while support references may be read for mandate, schema, facilitation, edge cases, examples, or terminology
- Made first-pass stage 0 behavior explicit: record and classify before reformulation, then route to the entry stage
- Separated user-near targets from worth thresholds in stage 3
- Clarified that `candidate_type: build` in stage 4 means eligible for stage 5, not approved for implementation
- Made required `unknown` values in stage 2 remain blocking until measurement or explicit non-convertible decision

### Added
- Codex-compatible plugin manifest under `plugins/idea-maturity/.codex-plugin/plugin.json`
- Local marketplace entry under `.agents/plugins/marketplace.json`
- Repository contract test for packaging, routing references, enums, and core methodology invariants

### Fixed
- README repository layout and validation commands now match the actual 0.3.0 file structure
- Solution-free briefing rule now permits trace fields to quote the original solution without contaminating active stage 1-3 fields

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
