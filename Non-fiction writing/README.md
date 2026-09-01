# Zinsser Style Guardian

Ein Non-fiction-Writing-Skill für klare, knappe, aktive und menschliche Prosa. Er kann Texte diagnostizieren, direkt überarbeiten oder nur Feedback geben.

Der Skill ist von William Zinssers praktischen Schreibprinzipien inspiriert, ohne Buchpassagen zu kopieren oder seinen Stil zu imitieren.

## Struktur

```text
Non-fiction writing/
├── .agents/plugins/marketplace.json
├── plugins/zinsser-style-guardian/
│   ├── .codex-plugin/plugin.json
│   └── skills/zinsser-style-guardian/
│       ├── SKILL.md
│       ├── agents/openai.yaml
│       └── references/
├── scripts/
└── tests/
```

## Codex-Installation

Das Paket enthält einen repo-lokalen Marketplace-Eintrag unter `.agents/plugins/marketplace.json` und ein Codex-Plugin unter `plugins/zinsser-style-guardian`.

## Claude.ai-Installation

Claude erwartet einen ZIP-Upload, der den Skill-Ordner als oberstes Verzeichnis enthält. Erzeuge das Paket mit:

```bash
python3 scripts/build_claude_skill_zip.py
```

Danach kann `dist/zinsser-style-guardian-claude-skill.zip` in Claude über `Customize > Skills` als eigener Skill hochgeladen werden. Code Execution und Skills müssen im Claude-Konto aktiviert sein.

## Claude-Code-Installation

Für Claude Code kann der Skill als persönlicher Skill installiert werden:

```bash
python3 scripts/install_claude_code_skill.py --target ~/.claude/skills --force
```

Für ein einzelnes Projekt verwende stattdessen den Projektordner:

```bash
python3 scripts/install_claude_code_skill.py --target /path/to/project/.claude/skills --force
```

Der Installer kopiert nur die Claude-kompatiblen Skill-Dateien: `SKILL.md` und `references/`.

## Tests

```bash
python3 tests/test_skill_contract.py
python3 scripts/build_claude_skill_zip.py --output /tmp/zinsser-style-guardian-claude-skill.zip
```

## Quellen zur Claude-Kompatibilität

- Anthropic Help Center: https://support.claude.com/en/articles/12512198-how-to-create-custom-skills
- Anthropic Agent Skills Docs: https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview
