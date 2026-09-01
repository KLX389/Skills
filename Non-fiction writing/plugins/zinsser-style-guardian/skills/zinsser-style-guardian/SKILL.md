---
name: zinsser-style-guardian
description: Review or rewrite non-fiction prose when the user wants clearer, tighter, more active, human writing; avoid for fiction, poetry, legal drafting, or edits that must preserve wording.
---

# Zinsser Style Guardian

Use this skill to review or rewrite non-fiction prose in the spirit of William Zinsser's practical style principles: clear, brief, active, concrete, and human.

Use it for essays, articles, memos, reports, newsletters, speeches, web copy, product writing, internal updates, and other factual prose. Do not use it for fiction, poetry, legal drafting, compliance wording, or copyedits where the exact original phrasing must be preserved unless the user explicitly asks for stylistic intervention.

## Operating Modes

Read [references/output-modes.md](references/output-modes.md) before answering. Select the mode from the user's wording:

- Default review and rewrite: provide `Diagnose`, `Überarbeiteter Text`, and `Wichtigste Änderungen`.
- `nur Feedback`: give feedback only; do not rewrite the full text.
- `direkt überarbeiten`: return only the revised text, without diagnosis or explanation.

Use the user's language for headings and prose. For German input, write German output. For English input, write English output.

## Editing Principles

Read [references/style-rules.md](references/style-rules.md) when reviewing or rewriting text.

Core standard: `Klar. Knapp. Aktiv. Menschlich.`

When revising:

1. Preserve the author's factual meaning, intent, constraints, and useful voice.
2. Remove clutter: filler, throat-clearing, inflated transitions, redundant qualifiers, and bureaucratic padding.
3. Prefer active subjects and strong verbs over passive constructions and nominalizations.
4. Make abstract claims concrete when the source provides concrete material. If evidence is missing, flag it instead of inventing it.
5. Strengthen the opening and ending when they are weak, vague, or delayed.
6. Vary sentence rhythm so the text is readable aloud, not merely shorter.
7. Replace institutional or hedged language with plain human phrasing while preserving real uncertainty.

Do not over-polish. Keep necessary technical terms, quoted text, legal obligations, numbers, names, and domain-specific distinctions intact. A shorter sentence is not better if it becomes less true.

Before finalizing a long, sensitive, or publication-bound edit, use [references/editing-checklist.md](references/editing-checklist.md).
