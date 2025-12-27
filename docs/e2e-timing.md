## **Analyzable Modeling of Legacy Communication in Component-Based Distributed Embedded Systems**

🔗 [https://doi.org/10.1109/SEAA.2011.43](https://doi.org/10.1109/SEAA.2011.43)

### **It establishes:**

* **End-to-end timing analysis in distributed hard real-time systems requires explicit communication modeling**; legacy protocols (e.g., CAN) introduce timing effects that cannot be abstracted away without losing analyzability.

* **Communication must be treated as a first-class execution concern**, not hidden behind middleware.

* **Analyzability is achieved through disciplined modeling and mechanical extraction of timing semantics**.

* **No existing approach simultaneously provides** explicit execution semantics, legacy communication support, and tight end-to-end timing analyzability.

* Communication is modeled using:

  * an explicit **network specification**, and
  * explicit **send (OSWC)** and **receive (ISWC)** execution steps.

* These steps make communication visible to timing analysis.

* **End-to-end timing paths are mechanically extracted** from trigger relations.

* **Standard response-time analysis** is then applied to compute worst-case end-to-end delays.

---

### **Relevance:**

* Direct analogue to **extracting timing semantics from event-driven IEC 61499 function block networks**.
* Motivates why **IEC 61499 requires an extraction-based timing approach**, rather than timing annotations alone.
* Core transferable insight:

  > **End-to-end timing analysis requires explicit extraction of execution and communication semantics from component-based architectures.**

> *Rubus needed explicit communication modeling to enable end-to-end timing analysis.
> IEC 61499 has the same structural problem.

---

## **Support for Holistic Response-Time Analysis in an Industrial Tool Suite**

🔗 [https://doi.org/10.1109/ECBS.2012.38](https://doi.org/10.1109/ECBS.2012.38)

It establishes:

* **End-to-end timing analysis (HRTA) is only possible if timing models are explicitly extracted**; component models do not provide all required parameters unambiguously.
* HRTA assumes explicit availability of WCETs, offsets, priorities, triggering semantics, message properties, and precedence relations — these must be **derived**, not assumed.
* **Distributed transactions (cause–effect chains) are not explicit** and must be **constructed** from model structure and communication mappings.
* **Timing inheritance is iterative**: response times propagate as jitter across task → message → task chains.
* **Design and deployment decisions affect analyzability**; careless allocation can introduce direct cycles that make analysis non-terminating.
* **Multi-network systems require staged analysis**, with timing results propagated across gateways as jitter.
* The **ACC case study** demonstrates feasibility on a realistic system and validates the extraction-based approach.
* The dominant engineering effort lies in **extraction, validation, error handling, and convergence control**, not in new analysis theory.

### **Relevance:**

* Direct analogue to **extracting timing models from IEC 61499 architectures**.
* Confirms that **end-to-end timing paths must be reconstructed**, not inferred from connections alone.
* Shows that **event-driven semantics require inference of transmission/activation types**.
* Demonstrates that **deployment rules and architectural constraints are necessary** for analyzability.
* Reinforces the core transferable insight:

  > **End-to-end timing analysis requires explicit extraction of execution and tracing semantics from the design model.**