# Project 2 — Text Classification

## Objective
Assign one or more labels to a piece of text based on its overall meaning.

## Example Label Sets

### Sentiment
- POSITIVE
- NEGATIVE
- NEUTRAL

### Intent
- INFO_REQUEST
- PRAISE
- CANCELLATION
- COMPLAINT
- REFUND
- FLAG

## Rules
- Base the label on the text itself, not assumptions about the writer.
- Use the dominant intent when the task is single-label.
- Use all supported labels when the task is multi-label.
- Do not add a second label simply because it is related.

See `classification_sample.csv`.
