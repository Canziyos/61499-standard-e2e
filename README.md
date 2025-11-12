# IEC 61499 → Timing IR (E2E Chains)

This repo extracts timing models from IEC 61499 applications to enable end-to-end analysis (reaction time and data age) across devices. It implements rule-based extraction (R1, R2, .., etc), a clean intermediate representation (IR), and minimal "golden" projects to lock behavior.

First adapter targets Eclipse 4diac (IDE/FORTE); others can plug in via the adapter interface.
