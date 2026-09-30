# Project 4 — Video Shot & Transition Annotation

## Objective
Identify shot boundaries and classify visual transitions.

## Transition Types
- `CUT`
- `DISSOLVE`
- `FADE_IN`
- `FADE_OUT`

## Key Rules
- Camera movement alone does not create a new shot.
- Zooming alone does not create a new shot.
- A `CUT` is an immediate transition from one shot to another.
- A `DISSOLVE` contains visible blending between two shots.
- A `FADE` involves progressive darkening or brightening.
- Shot boundaries should be recorded at the correct frames.

## Practice Examples
The CSV contains demonstration cases based on frame-level annotation practice.

See `shot_annotations.csv`.
