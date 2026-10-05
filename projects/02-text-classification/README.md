# Text Classification
Independent synthetic demonstration. Four examples; not a production dataset.

## Schema and rules
Sentiment: POSITIVE, NEGATIVE, NEUTRAL. Assess expressed sentiment, not whether the action is cancellation or refund. A polite procedural request with no judgement is NEUTRAL under this practice rule.

Intent: INFO_REQUEST, PRAISE, CANCELLATION, COMPLAINT, REFUND, FLAG. Multi-label tasks use every independently supported intent. REFUND requires an explicit request for money back; a billing complaint alone does not qualify.

For this single-label practice task, when both cancellation and refund are explicit, CANCELLATION is the primary intent. This tie-break is specific to this demonstration. Real project instructions override it.

See classification_sample.csv for labels and decision rationales.
