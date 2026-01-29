## Common ground across the papers

* **Architecture/component models are not directly analyzable.** Timing analysis requires a **separate analysis model** produced by **systematic extraction/translation**.
* End-to-end timing is a **chain property** (tasks + messages + causality), not a single-task property.
* A usable model separates **node execution**, **network communication**, and **explicit linking** (cross-domain causality).
* **Extraction ≠ analysis.** Extraction produces the analyzable model; analysis consumes it unchanged.
* Missing information must be stated as **explicit assumptions**.

---

## 1) SEAA 2011 — *Analyzable Modeling of Legacy Communication…*

* Legacy communication (e.g., CAN) cannot be abstracted away without losing analyzability → **communication must be modeled explicitly** and treated as execution.
* Communication is made visible using:

  * an explicit **Network Specification**, and
  * explicit **send/receive execution steps** (OSWC/ISWC-style: communication becomes schedulable work).
* End-to-end paths are extracted mechanically from **trigger relations**, then **standard response-time analysis** is applied to compute worst-case end-to-end delays.
* Same structural issue appears in IEC 61499: timing is scattered and communication semantics are not fully represented by connections alone.

---

## 2) ECBS 2012 — *Support for Holistic Response-Time Analysis in an Industrial Tool Suite*

* HRTA requires explicit derivation of analysis parameters (WCET, offsets, priorities, triggering, precedence, message properties), which design models rarely provide unambiguously.
* **Distributed transactions / cause–effect chains** must be constructed from structure plus deployment/mapping.
* Response times propagate as **jitter** along task → message → task chains.
* Analyzability pitfalls:

  * poor deployment can introduce **direct cycles** and lead to non-termination,
  * **multi-network** systems require staged analysis and propagation across gateways as jitter.
* Feasibility is demonstrated via an **ACC case study**.
* Deployment rules and architectural constraints can be necessary for analysis to terminate.

---

## 3) 2014 (Rubus/RCM) — *Extracting End-to-End Timing Models from Component-Based Distributed Embedded Systems*

* End-to-end timing behavior emerges during **code generation and deployment**, making it an **engineering reconstruction problem**.
* Two-part analyzable model:

  * **System Timing Model:** node timing + network timing (local behavior)
  * **System Linking Model:** explicit reconstruction of task ↔ message ↔ task chains
* Core difficulty occurs at **node boundaries** (trigger → signal → message; buffering/bundling), which breaks naïve triggering assumptions.
* Tool-supported pattern:

  * explicit send/receive boundary entities (OSWC/ISWC concept),
  * a central **Network Specification** with signal↔message mapping and linking pointers,
  * pipeline via an intermediate representation (e.g., ICCM) → auto-extraction → analysis → feedback.
* Separating timing and linking is necessary because node/network timing alone does not define end-to-end chains.

---

## 4) *Communications-oriented development…* (linking-focused synthesis)

* **Linking is the main difficulty:** timing attributes are insufficient without unambiguous causality links.
* **Trigger dependency** (Dependent vs Independent) is extracted semantics used to:

  * classify chains (trigger/data/mixed),
  * prevent metric misuse before analysis.
* **Inter-domain crossings** require explicit timing entities (entry/exit points), conceptually matching OSWC/ISWC while remaining portable.
* Message attributes inherit from sender execution unless explicitly specified, reducing contradictory multi-source annotations.
* Incomplete architectures / external traffic remain analyzable by modeling stand-alone messages.
* IEC 61499 mapping: device/resource boundaries and SIFBs function as timing boundaries; explicit entry/exit semantics are needed to keep delays bounded and visible.

---

## 5) Paper A — *Translating End-to-End Timing Requirements to Timing Analysis Models…*

* **Trigger chains vs data chains** is a semantic split that determines which metrics are meaningful:

  * Trigger chain → holistic response time
  * Data chain → latency / data age / first reaction
* For data chains, latency has multiple semantics (FIFO/FILO/LIFO/LILO), so end-to-end latency is not a single quantity unless semantics are fixed.
* Mixed chains and merges are common; chain type may require tracing the full distributed chain.
* Introduces a **trigger map** (dependent/independent between neighbors) as an extraction artifact; ambiguous cases are treated conservatively.
* Extraction must include **chain semantics**, not only entities, to avoid analyzing the wrong requirement.

---

## 6) Paper B — *Towards Extraction of Interoperable Timing Models…*

* Focus shifts to **interoperability across abstraction levels and tools** (design → implementation).
* **Early timing analysis** is motivated; implementation-level discovery is costly to correct.
* Design-level obstacles are made explicit:

  * missing priorities/jitter/transmission types,
  * unclear triggering and control-vs-data separation,
  * hidden linking across nodes,
  * duplicated/ambiguous timing annotations.
* Two strategies are proposed:

  1. extend design languages/tools, or
  2. define a **restricted, well-defined execution interpretation** (practical route).
* Supports defining a restricted interpretation plus explicit assumptions to make extraction unambiguous in IEC 61499 contexts.

---

## 7) 2018 — *Component-Based Multi-Criticality Vehicular Embedded Systems*

### What it adds (beyond 2014)

* **Multi-criticality** at application/partition level: node → **partitions** → transactions → tasks; partitions provide isolation and host one criticality level (ASIL A–D).
* End-to-end model expanded to three parts:

  1. timing model
  2. linking model
  3. **timing requirements model**
* Requirements are **chain-level**: Age, Reaction, Output Synchronization, Input Synchronization (AUTOSAR/TADL2-aligned).
* Richer network coverage: CAN-family and switched Ethernet families; multi-hop links; active vs passive network behavior.

### Extraction philosophy

* Information is either explicitly specified or implicitly inferred; missing information is handled via **explicit assumptions**.
* Many message parameters are derived (payload/bandwidth → transmission time, CAN ID → priority, sender RT bounds → jitter, sender triggering → periodic/sporadic/mixed).
* Reinforces the three-artefact structure: **timing + linking + requirements**, with explicit handling of missing data.

---

## IEC 61499 implication

IEC 61499 timing-model extraction requires: **(1) timing entities**, **(2) linking (causality)**, **(3) chain semantics**, and **(4) chain-level requirements**, supported by explicit assumptions and potentially a restricted execution interpretation.

---

## Glossary (RT / DA / CEC)

* **Reaction time (RT):** initiation → effect occurrence (responsiveness, not freshness).
* **Data age (DA):** production → consumption of the same data instance (freshness, not speed).
* **Cause–effect chain (CEC):** causally connected computations and communications from cause to effect; invalid when causality or data-instance traceability is ambiguous (e.g., merges, forks without semantics, temporal ordering assumptions).
