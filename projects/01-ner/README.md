# Project 1 — Named Entity Recognition

## Objective
Identify and label named entities in text using a fixed schema.

## Labels
- `PERSON`
- `ORG`
- `LOCATION`
- `DATE`
- `MONEY`

## Annotation Rules
- Label the smallest complete span that represents the entity.
- Do not include unnecessary punctuation.
- Keep possessive endings outside the entity when required by the project rule.
- Relative dates such as “next Friday” should be labelled only when the guideline defines them as `DATE`.
- Do not guess an entity type when the text is genuinely ambiguous.

## Example
Text: `Aisha joined Microsoft in London in March 2026.`

Entities:
- Aisha → PERSON
- Microsoft → ORG
- London → LOCATION
- March 2026 → DATE

See `ner_sample.jsonl` for additional examples.
