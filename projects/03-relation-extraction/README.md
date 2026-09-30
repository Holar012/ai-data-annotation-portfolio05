# Project 3 — Relation Extraction

## Objective
Identify valid relationships between already-recognised entities.

## Relation Labels
- `WORKS_FOR`
- `STUDIES_AT`
- `LIVES_IN`
- `LOCATED_IN`
- `FOUNDED_BY`

## Rules
- Create a relation only when the sentence supports it.
- Do not infer a relation from world knowledge.
- Use `NO_RELATION` when the entities are present but the required relationship is not stated.
- Historical or uncertain relationships should follow the project guideline exactly.

See `relations_sample.jsonl`.
