# Project 5 — Annotation Quality Assurance

## Objective
Review annotation work before submission and reduce avoidable errors.

## QA Checklist

### Guideline Compliance
- Did I use only allowed labels?
- Did I apply the latest project guideline?
- Did I avoid personal assumptions?

### Span / Boundary Accuracy
- Are NER spans complete but not oversized?
- Are video boundaries placed on the correct frames?
- Are punctuation and possessives handled correctly?

### Classification Accuracy
- Does the selected class match the actual meaning?
- If multi-label, are all labels independently supported?
- Did I avoid adding a weak or speculative label?

### Relation Accuracy
- Is the relationship explicitly supported?
- Are head and tail entities in the correct direction?
- Should the example instead be `NO_RELATION`?

### Consistency
- Would I label a similar example the same way?
- Have I applied the same rule across the entire batch?

### Final Review
- Re-check difficult examples.
- Re-check all low-confidence decisions.
- Confirm that no confidential or restricted data is included.
