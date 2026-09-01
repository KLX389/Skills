# Output Modes

Choose the output shape from the user's request. Do not add mode explanations unless the user asks.

## Default Review And Rewrite

Use this when the user asks generally to improve, review, polish, tighten, clarify, or rewrite text.

German heading pattern:

```markdown
## Diagnose
- 3 bis 5 konkrete Punkte, priorisiert nach Wirkung.

## Überarbeiteter Text
[Der überarbeitete Text.]

## Wichtigste Änderungen
- Kurze Liste der wichtigsten Eingriffe.
```

English heading pattern:

```markdown
## Diagnosis
- 3 to 5 concrete points, ordered by impact.

## Revised Text
[The revised text.]

## Key Changes
- Short list of the most important edits.
```

## Feedback Only

Trigger phrases include `nur Feedback`, `nur Diagnose`, `nur kommentieren`, `don't rewrite`, and `feedback only`.

Return only concise feedback. Use specific examples from the text and name the most valuable next edits. Do not provide a full rewritten version.

## Direct Rewrite Only

Trigger phrases include `direkt überarbeiten`, `nur überarbeiteter Text`, `mach es direkt besser`, `rewrite only`, and `just rewrite`.

Return only the revised text. Do not add a preface, diagnosis, bullet list, or closing note. Preserve paragraph structure unless changing it clearly improves readability.

## Missing Or Ambiguous Source Text

If the user asks for an edit but provides no text, ask for the text and, if useful, whether they want feedback, a direct rewrite, or the default review-and-rewrite mode.

If the user provides multiple text blocks, treat each block independently unless they ask for a unified rewrite.
