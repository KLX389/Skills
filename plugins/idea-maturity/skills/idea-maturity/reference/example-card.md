# Worked example

Read this when unsure how blunt the verdict should be, how short the field values should be, or how to handle a stage where nothing is known.

## Input

> "Wir haben uns den Buchungsflow angeschaut. Die Preisdarstellung ist über die Schritte hinweg inkonsistent, mal mit, mal ohne Gebühren. Aus unseren 8 Interviews wissen wir, dass Nutzer das irritiert. Wir haben ein Konzept für eine durchgängige Preiskomponente gebaut und würden das gern ins nächste Quartal einplanen."

## Output

**Reifegrad: Durchgängige Preiskomponente im Buchungsflow**

**Status: Stufe 1 — Problem existiert (berichtet)**
- Klartext: Das Problem ist berichtet, nicht belegt, und wie viele es betrifft, weiß niemand. Das Konzept steht auf Stufe 3, die Grundlage darunter auf Stufe 1 — damit ist die Quartalsplanung nicht belastbar.

**1. Problem**
- Nutzerproblem: Preisdarstellung wechselt zwischen Schritten, Nutzer verlieren den Überblick — **Berichtet**
  - Beleg: 8 Interviews (qualitativ). Für „Belegt" fehlt die quantitative Seite: Abbruchraten je Schritt.
- Unternehmensproblem: nicht formuliert — **Vermutet**
  - Beleg: fehlt → welche Kennzahl leidet, Umsatz oder Supportkosten?
- Kausalkette: Inkonsistente Preise → Intransparenz → Unsicherheit → Abbruch → weniger Umsatz
  - Schwächstes Glied: „Unsicherheit → Abbruch". Die Interviews zeigen Irritation, nicht Abbruch. Genau hier wird geraten.

**2. Relevanz**
- Reichweite: unbekannt → zuerst messen
- Häufigkeit: betrifft strukturell jeden Buchungsvorgang, Auswirkung aber ungemessen
- Schwere: unbekannt → zuerst messen
- Baseline: unbekannt → zuerst messen (Abbruchquote je Buchungsschritt)

**3. Lösungspassung** — *noch nicht belastbar, weil Stufe 1 offen ist*
- Verworfene Alternativen: keine erwogen → Warnsignal. Eine durchgängige Komponente ist eine Lösung; Gebühren früher ausweisen oder eine Zwischensumme einblenden wären andere.
- Wirkkette: Konsistente Preise → Nutzer versteht Endpreis früher → weniger Abbruch
- Riskanteste Annahme: Die Irritation verursacht die Abbrüche — und nicht der Endpreis selbst.
- Billigster Test dafür: Abbruchraten der Schritte mit und ohne Gebührenwechsel vergleichen. Zwei Tage Analyse statt eines Quartals Umsetzung.

**Was für die nächste Stufe fehlt**
- [ ] Abbruchquote je Buchungsschritt aus dem Funnel → Analytics-Abfrage → Data
- [ ] Unternehmensproblem benennen: welche Kennzahl leidet konkret → Product
- [ ] Prüfen, ob Support-Tickets zum Thema Preis existieren → Support

**Nächster Schritt**
Die Funnel-Abfrage stellen, bevor das Konzept weiter ausgearbeitet wird. Sie kostet zwei Tage und entscheidet, ob die Idee Stufe 2 überhaupt erreicht.

## What this example demonstrates

- The verdict is blunt and comes first. It does not open with praise.
- The status is stage 1 even though a concept exists — work above the blocking stage does not raise the status.
- Stage 3 is filled in because the material exists, but explicitly marked as not yet reliable.
- Unknowns are written as `unbekannt → zuerst messen`, never smoothed over with a plausible-sounding estimate.
- The weakest link in the causal chain is named specifically, not described as "some uncertainty".
- The next step is one action, cheap, and decides the blocking stage.
- Stages 4 and 5 are omitted entirely — with stage 1 open, filling them would be noise.
