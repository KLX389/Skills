# Stage 3 deep-dive — does this solution fit this problem?

## Contents
- What must be produced
- Why alternatives are mandatory
- The effect chain
- The riskiest assumption and its cheapest test
- Probing questions
- Exit criteria

Read this when stage 3 is the blocking stage. Work it, then return to SKILL.md and re-state the status.

## What must be produced

1. **Two or three rejected alternatives**, each with the reason it was rejected
2. **The effect chain**: solution → behavior change → outcome
3. **The riskiest assumption**, plus the cheapest test that could disprove it

## Why alternatives are mandatory

A single solution is a warning sign, not a result. When only one option was ever on the table, the team did not choose it — it was the first thing that came to mind, and everything since has been elaboration.

Generating alternatives is also the cheapest quality lever available: it costs an hour and regularly surfaces an option that is a tenth of the effort. Three useful directions to force:

- **Remove instead of add** — can the problem disappear by taking something away?
- **Change the sequence** — same elements, different order or timing
- **Change who does it** — automate, delegate, or let the user decide

Record the rejected options with reasons. Six months later, this is the artifact that prevents relitigating the same debate, and it makes the chosen option defensible without appealing to authority.

## The effect chain

State what people will **do differently**, and **who exactly**:

> Konsistente Preisdarstellung → Nutzer erkennt den Endpreis vor Schritt 3 → weniger Abbrüche in Schritt 3 → mehr abgeschlossene Buchungen

A chain that jumps straight from the solution to the business outcome has skipped the behavior — and the behavior is the only part the solution can actually touch. If the behavior change cannot be named, the idea is not ready for stage 4 regardless of how detailed the concept is.

Name the group precisely. "Nutzer" is rarely the right unit; "Erstbucher ohne Kundenkonto" is.

## The riskiest assumption and its cheapest test

The riskiest assumption is the one that, if false, collapses the whole idea — not the one that is most uncertain, and not the one that is easiest to check. Find it by asking of each link in the effect chain: *if this is wrong, does anything survive?*

Then pick the cheapest test that could disprove it, in this order:

| Test | Costs | Use when |
|---|---|---|
| **Data check** | hours | The assumption is about behavior that is already happening and already logged |
| **Fake door / painted door** | days | The assumption is about demand or intent |
| **Prototype in front of 5 users** | days | The assumption is about comprehension or usability |
| **Wizard of Oz** | 1-2 weeks | The assumption is about value, and the mechanics would be expensive to build |
| **Full build** | a quarter | Only after the above have been ruled out as unable to answer the question |

If a cheap test can check the core bet, it beats the full build — and the argument that "we'll learn more by shipping it" is only true when the measurement from stage 5 is already in place.

## Probing questions

- "Welche zwei anderen Lösungen habt ihr erwogen, und warum sind sie rausgeflogen?"
- "Was genau tun Nutzer danach anders als heute — und welche Nutzer?"
- "Welche Annahme muss stimmen, damit das funktioniert? Und wenn sie falsch ist, bleibt dann irgendetwas übrig?"
- "Was ist der billigste Weg, diese eine Annahme zu widerlegen?"
- "Was wäre die Lösung, die zehnmal weniger Aufwand kostet — und warum reicht sie nicht?"

## Exit criteria

```
- [ ] Two or three alternatives named with rejection reasons
- [ ] Effect chain written: solution → behavior change → outcome
- [ ] The changed behavior is named, and so is the group that changes it
- [ ] Riskiest assumption named as one sentence
- [ ] Cheapest test named, with its rough cost
```

If the cheapest test is materially cheaper than the build, the honest next action is the test, not stage 4. Say so directly.
