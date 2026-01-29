## Common ground across the whole set of the papers below.

* **Architecture/component models are not directly analyzable.** Timing analysis needs a **separate analysis model** produced by **systematic extraction/translation**, not vibes.
* End-to-end timing is a **chain property** (tasks + messages + causality), not a single-task property.
* A usable model must separate domains: **node execution**, **network communication**, plus **explicit linking** (causality across domains).
* **Extraction ≠ analysis.** Extraction builds the analyzable model; analysis consumes it unchanged.
* Any missing info must become **explicit assumptions** (hidden assumptions = fake certainty).

---

## 1) SEAA 2011 — *Analyzable Modeling of Legacy Communication…*

* Legacy communication (e.g., CAN) cannot be “abstracted away” without losing analyzability → **communication must be explicit** and treated as execution.

* Makes communication visible using:

  * an explicit **Network Specification**, and
  * explicit **send/receive execution steps** (OSWC/ISWC-style idea: comm becomes schedulable work).
* **Mechanical path extraction** from **trigger relations**, then **standard response-time analysis** to compute worst-case end-to-end delays.

* Same structural pain: timing is scattered + comm semantics aren’t “in the wires” → you need **extraction of execution + communication semantics**, not just annotations.

---

## 2) ECBS 2012 — *Support for Holistic Response-Time Analysis in an Industrial Tool Suite*

* HRTA only works if analysis parameters are **derived explicitly** (WCET, offsets, priorities, triggering, precedence, message properties). Design models rarely give these unambiguously.

* **It contributes**

* **Distributed transactions / cause–effect chains must be constructed** from structure + deployment/mapping.
* **Iterative jitter propagation** along task → message → task.
* **Analyzability pitfalls**:

  * bad deployment introduces **direct cycles** → possible non-termination,
  * **multi-network** requires staged analysis and gateway jitter propagation.
* Validated via a realistic **ACC case study**.


* Strong support for “extraction-first,” plus a concrete warning: **deployment rules/constraints matter for analysis to even terminate**.

---

## 3) (Rubus/RCM) 2014 — *Extracting End-to-End Timing Models from Component-Based Distributed Embedded Systems*

* End-to-end timing behavior **emerges during codegen + deployment** → it’s an **engineering reconstruction problem**, not “read it from the diagram.”

**It contributes**

* Two-part analyzable model:

  * **System Timing Model** = node timing + network timing (local behavior)
  * **System Linking Model** = explicit task↔message↔task chain reconstruction
* Pinpoints the core distributed break: **node boundaries** (trigger→signal→message, buffering/bundling, etc.) destroy naïve triggering semantics.
* Tool-supported pattern:

  * explicit send/receive boundary entities (OSWC/ISWC concept),
  * a central **Network Specification** containing signal↔message mapping + linking pointers,
  * pipeline via an intermediate representation (e.g., ICCM) → auto-extraction → analysis → feedback.

* The backbone: **timing + linking** as separate artefacts, because node+network timing alone can’t give end-to-end chains.

---

## 4) *Communications-oriented development…* (your “linking-focused” take)


* **Linking is the real hard problem**: without unambiguous causality links, timing attributes are useless.
* **Trigger dependency is extracted semantics** (Dependent vs Independent) used to:

  * classify chains (trigger/data/mixed),
  * prevent metric misuse before analysis.
* **Inter-domain crossings need explicit timing entities** (entry/exit points) → same abstract role as OSWC/ISWC, but portable to other ecosystems.
* **Message attributes inherit from sender execution unless explicitly specified** → avoids contradictory “annotate everything everywhere.”
* **Incomplete architectures / external traffic** must still be analyzable (stand-alone message modeling).

* Perfect mapping to IEC 61499: device/resource boundaries + SIFBs are natural **timing boundaries**; you’ll need explicit **entry/exit semantics** to keep delays bounded and visible.

---

## 5) Paper A — *Translating End-to-End Timing Requirements to Timing Analysis Models…*

* **Trigger chains vs data chains** is a hard semantic split that determines **which metric is meaningful**:

  * Trigger chain → holistic response time
  * Data chain → latency/data age/first reaction
* For data chains, **“latency” has multiple semantics** (FIFO/FILO/LIFO/LILO).
  → End-to-end latency is **not one number** unless chain semantics are fixed.
* Mixed chains + merges are normal; chain type may only be resolvable after tracing the **full distributed chain**.
* Introduces **trigger map** (dependent/independent between neighbors) as an extraction artefact; ambiguous cases treated conservatively.

* Extraction must include **chain semantics**, not only entities. Otherwise you risk “correct analysis of the wrong requirement.”

---

## 6) Paper B — *Towards Extraction of Interoperable Timing Models…*

* Shifts focus to **interoperability across abstraction levels/tools** (design → implementation).
* Argues for **early timing analysis**: implementation-level extraction is too late to fix.
* Makes design-level pain explicit:

  * missing priorities/jitter/transmission types,
  * unclear triggering & control-vs-data,
  * hidden linking across nodes,
  * duplicated/ambiguous timing annotations.
* Offers two viable strategies:

  1. extend design languages/tools, or
  2. define a **restricted, well-defined execution interpretation** (practical route).


* Direct justification for your IEC 61499 stance: you’re allowed (and basically forced) to define a **restricted interpretation** + explicit assumptions to make extraction unambiguous.

---

## 7) 2018 — *Component-Based Multi-Criticality Vehicular Embedded Systems*

**What it adds (beyond 2014)**

* **Multi-criticality** at application/partition level (not task-level mixed-criticality): node → **partitions** → transactions → tasks; partitions provide isolation and host one criticality level (ASIL A–D).
* Expands the model into **three parts**:

  1. timing model
  2. linking model
  3. **timing requirements model**
* Requirements are **chain-level** with a small, sharp set: **Age, Reaction, Output sync, Input sync** (AUTOSAR/TADL2-aligned).
* Richer network model coverage (CAN + switched Ethernet families; multi-hop links; active vs passive networks).

**Extraction philosophy**

* Two sources of info: **explicit** + **implicit inferred**, with missing info handled via **explicit assumptions**.
* Many message parameters are **derived** (payload/bandwidth → tx time, CAN ID → priority, sender RT bounds → jitter, sender triggering → periodic/sporadic/mixed).

* Reinforces the “three artefacts” story: **timing + linking + requirements**, plus a clean pattern for being honest about missing info.

---

* IEC 61499 needs extraction of **(1) timing entities**, **(2) linking (causality)**, **(3) chain semantics**, and **(4) chain-level requirements**, with **explicit assumptions** and possibly a **restricted execution interpretation** for analyzability.

---

## Glossary (RT / DA / CEC)

* **Reaction time (RT):** initiation → effect occurrence (responsiveness, not freshness).
* **Data age (DA):** production → consumption of the *same data instance* (freshness, not speed).
* **Cause–effect chain (CEC):** causally connected computations+communications from cause to effect; invalid if causality/data instance traceability is ambiguous (merges, forks without semantics, “temporal folklore,” etc.).

