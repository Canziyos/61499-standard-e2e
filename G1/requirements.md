# G1 Requirements (v0)
Requirements for defining and extracting an analyzable End-to-End Timing Model (E2ETM) from IEC 61499 / 4diac artefacts, sufficient to support end-to-end timing analysis (reaction time + data age).

---

## Scope and intent
These requirements describe what the extracted model must represent and what assumptions must be recorded when information is not directly available in engineering artefacts. The goal is analysis support and traceability, not perfect behavioural simulation.

Primary analysis outputs:
- Reaction time (cause → effect latency)
- Data age (age of data at a consumption point)

---

## REQ-01 — E2E analysis support
The extracted E2ETM shall contain sufficient information to compute end-to-end delays, specifically **reaction time** and **data age**, for IEC 61499 / 4diac-based distributed software architectures.

Sources: MDHThesisDetails246; BeckerE2E2017

---

## REQ-02 — Explicit chain representation
The E2ETM shall explicitly represent end-to-end chains as ordered sequences of processing and communication steps, enabling unambiguous traversal from cause to effect.

Sources: BeckerE2E2017; feiertag2009compositional

---

## REQ-03 — Chain semantics must be explicit
The E2ETM shall explicitly declare the chain semantics used for analysis (e.g., trigger/event-driven vs data-driven interpretations, sampling/update assumptions), so computed delays are meaningfully defined.

Sources: feiertag2009compositional; Guenzel2021AsyncChains

---

## REQ-04 — Model elements for processing and communication
The E2ETM shall include distinct element types (or equivalent attributes) for:
- processing steps (software execution), and
- communication steps (data/event transfer between resources/devices).

Sources: BeckerE2E2017; MubeenE2ETimingTranslation

---

## REQ-05 — Timing attributes for processing steps
For each processing step, the E2ETM shall support timing attributes required for analysis, including (as applicable):
- execution time bounds (e.g., WCET; optionally BCET),
- activation pattern (periodic / sporadic / event-triggered),
- jitter or release variability (if used),
- scheduling-relevant attributes (e.g., priority) when assumptions require it.

Sources: ModellevelWCET2013; RTSemantics61499Lindgren2015

---

## REQ-06 — Timing attributes for communication steps
For each communication step, the E2ETM shall support timing attributes required for analysis, including (as applicable):
- delay bounds / latency distribution assumptions (at least worst-case bounds),
- buffering/queueing assumptions (e.g., FIFO vs priority),
- message/update semantics (overwrite vs queue),
- loss/drop assumptions when relevant.

Sources: Guenzel2021AsyncChains; HeterogeneousChainsGuenzel2023

---

## REQ-07 — Deployment and allocation context
The E2ETM shall represent deployment/allocation context sufficient to distinguish:
- device/resource boundaries,
- where each processing step executes,
- where each communication step occurs (intra-resource, inter-resource, inter-device).

Sources: IEC61499(1)webstore; 61499RuntimeEnvironments

---

## REQ-08 — IEC 61499 artefact traceability
Each E2ETM element shall provide traceability back to originating IEC 61499 / 4diac artefacts, at minimum via stable identifiers or references (e.g., FB instance, event/data connection, device/resource mapping).

Sources: IEC61499(1)webstore; Eclipse4diac

---

## REQ-09 — Assumption capture is mandatory
When required information is not extractable from artefacts, the E2ETM shall record explicit assumptions, including:
- what was assumed,
- why the assumption was needed,
- which model elements are affected.

Sources: MubeenTowardsExtraction; 61499RuntimeEnvironments

---

## REQ-10 — Extractability classification
For each required E2ETM attribute that is used in analysis, the extraction result shall be classifiable as one of:
- extracted directly,
- derived (computed from artefacts),
- provided externally (manual input),
- assumed (explicitly recorded).

Sources: MubeenTowardsExtraction; MubeenE2ETimingTranslation

---

## REQ-11 — Support for runtime/semantic variability
The E2ETM shall support recording the assumed execution semantics/runtime interpretation used during extraction (e.g., event scheduling semantics, concurrency interpretation), to handle variability across runtimes.

Sources: 61499RuntimeEnvironments; RTSemantics61499Lindgren2015

---

## REQ-12 — Consistency and integrity constraints
The extracted E2ETM shall support basic integrity checks, such as:
- all chain steps reference existing elements,
- referenced deployments/resources exist,
- timing attributes required by the chosen analysis mode are present or explicitly assumed.

Sources: MubeenE2ETimingTranslation; MubeenTowardsExtraction

---

## REQ-13 — Handling cyclic structures
If cyclic execution paths or cyclic dependencies are present in the source architecture, the E2ETM shall either:
- represent cycles explicitly, or
- record a cycle-handling strategy/assumption used to enable analysis.

Sources: CyclicExecLednicki2014

---

## REQ-14 — Multiple chains and reuse
The E2ETM shall support representing multiple chains within the same system model and reuse of shared elements across chains (e.g., a shared processing step used by multiple chains).

Sources: BeckerE2E2017

---

## REQ-15 — Output points and observation points
The E2ETM shall represent observation points needed to interpret data age and reaction time results (e.g., where data is produced, where it is consumed/effect is observed).

Sources: BeckerE2E2017; Guenzel2021AsyncChains

---

## REQ-16 — Minimal interoperability / export format
The E2ETM shall be serializable in a machine-readable format (e.g., JSON) suitable for downstream analysis, while preserving identifiers and traceability fields.

Sources: MubeenTowardsExtraction; Eclipse4diac

---

## REQ-17 — Reproducible extraction metadata
The extraction output shall include metadata sufficient to reproduce the extraction result, including:
- tool/version identifiers when available,
- extraction configuration (key parameters),
- timestamp or run identifier.

Sources: Eclipse4diac; MubeenImplementationEndtoendLatencyAnalysis

---

## REQ-18 — Boundaries of G1-derived requirements
The requirement set shall remain focused on representational needs for E2E timing analysis and extractability; requirements for implementing a full runtime, full formal verification, or performance benchmarking are out of scope for G1 unless explicitly motivated by analysis needs.

Sources: MDHThesisDetails246

---

## Notes
- Requirements are intentionally analysis-driven (reaction time + data age) and traceability-driven (artefact links + assumptions).
- The set is expected to be refined when mapping rules (G3) and schema design (G2) are finalized.
