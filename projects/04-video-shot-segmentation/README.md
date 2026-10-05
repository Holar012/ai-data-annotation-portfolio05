# Video Shot and Transition Annotation
Independent synthetic demonstration. The repository currently contains illustrative frame annotations, not the source video or a CVAT export. These examples demonstrate conventions; their visual accuracy cannot be independently verified without footage.

## Practice schema
Allowed transition labels: CUT, DISSOLVE, FADE, NO_TRANSITION.
- CUT: immediate editorial change. boundary_frame is the first frame of the new shot. No separate transition-frame interval is assigned.
- DISSOLVE: visible overlap between shots. Record the inclusive transition interval separately from the stable shot intervals.
- FADE: progressive darkening or brightening; this demonstration uses a combined class. A production task may require FADE_IN and FADE_OUT separately.
- NO_TRANSITION: a continuous take. Camera movement, zoom or subject movement alone does not establish an editorial boundary.

Frame numbers are zero-based and ranges are inclusive. Scene grouping is separate from shot counting. number_of_scenes is UNKNOWN until supported by footage and a scene definition.

## QA
Check that stable shots and transition intervals do not overlap, all frame ranges are ordered, and no frame is accidentally omitted. Confirm CUT boundary_frame equals the new shot's start. Rewatch source footage before treating the illustrative ranges as verified annotations.
