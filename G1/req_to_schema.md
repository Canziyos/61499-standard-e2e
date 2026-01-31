## REQ-01 — E2E analysis support
Schema target(s): nodes[].timing; edges[]; assumptions.*; meta.time_unit
Status: planned

## REQ-02 — Explicit chain representation
Schema target(s): nodes[].id; edges[].src; edges[].dst; edges[].kind
Status: planned

## REQ-03 — Chain semantics must be explicit
Schema target(s): assumptions.resource_queue; assumptions.preemption; assumptions.comm_model; edges[].origin_semantics
Status: planned

## REQ-04 — Processing vs communication steps
Schema target(s): nodes[].kind; edges[].kind
Status: planned

## REQ-05 — Timing attributes for processing steps
Schema target(s): nodes[].timing
Status: planned
Notes: ensure nodes[].timing can represent WCET/activation/jitter/priority or document gaps.

## REQ-06 — Timing attributes for communication steps
Schema target(s): assumptions.comm_model; edges[].kind; edges[].origin_semantics
Status: planned
Notes: if per-edge delay attributes are needed, schema may require extension beyond current fields.

## REQ-07 — Deployment and allocation context
Schema target(s): nodes[].device_id; nodes[].resource_id
Status: planned

## REQ-08 — IEC 61499 artefact traceability
Schema target(s): nodes[].origin; edges[].origin_semantics (and/or extend edges with origin if required); meta.version
Status: planned

## REQ-09 — Assumption capture is mandatory
Schema target(s): assumptions.resource_queue; assumptions.preemption; assumptions.comm_model
Status: planned
Notes: assumptions are currently global; per-chain/per-element assumptions would require schema extension.

## REQ-10 — Extractability classification
Schema target(s): nodes[].origin; edges[].origin_semantics
Status: planned
Notes: provenance classification (extracted/derived/assumed/manual) may require adding explicit provenance fields.

## REQ-11 — Runtime/semantic variability
Schema target(s): assumptions.*; edges[].origin_semantics; meta.version
Status: planned

## REQ-12 — Consistency and integrity constraints
Schema target(s): timing_model/validators.py (node/edge id uniqueness, edge endpoints exist, required fields present)
Status: planned

## REQ-13 — Handling cyclic structures
Schema target(s): edges[].src; edges[].dst; assumptions.* (cycle-handling strategy may require explicit field)
Status: planned

## REQ-14 — Multiple chains and reuse
Schema target(s): nodes[].id; edges[].id
Status: planned
Notes: explicit multiple-chain grouping is not present; chains may be represented as selected paths over a shared graph.

## REQ-15 — Output/observation points
Schema target(s): nodes[].kind; nodes[].origin
Status: planned
Notes: observation points likely need explicit node kinds or a dedicated marker field.

## REQ-16 — Interoperability / export format
Schema target(s): timing_model/schema/timing-graph.schema.json; meta.version
Status: implemented

## REQ-17 — Reproducible extraction metadata
Schema target(s): meta.version; meta.time_unit (and/or extend meta with tool/version/config if required)
Status: planned

## REQ-18 — Boundaries of G1-derived requirements
Schema target(s): (documentation-only) requirements.md / method text
Status: planned
