## The IEC 61499 Function Block Standard: Software Tools and Runtime Platforms

Christensen, J. H., Strasser, T. I., Valentini, A., Vyatkin, V., Zoitl, A.
ISA Automation Week, 2012.
Link: [https://www.researchgate.net/publication/235225083_The_IEC_61499_Function_Block_Standard_Software_Tools_and_Runtime_Platforms](https://www.researchgate.net/publication/235225083_The_IEC_61499_Function_Block_Standard_Software_Tools_and_Runtime_Platforms)

### Main position

The paper argues that IEC 61499 can support portable, configurable, interoperable multi-vendor distributed automation systems, but only if toolchains and runtimes implement sufficiently consistent semantics.

### IEC 61499 “open system” objectives

* **Portability:** transfer FB types and system models between tools. XML exchange supports this structurally, but identical files do not guarantee identical runtime behavior.
* **Configurability:** flexible mapping of software to devices/resources across vendors. In practice, toolchains often embed assumptions that restrict portability of deployment decisions.
* **Interoperability:** heterogeneous devices cooperate correctly at runtime. This is the most difficult objective and is typically undermined by runtime semantic differences.

### Why Parts 1 & 2 are insufficient

Parts 1 (architecture) and 2 (tool requirements, including XML formats) enable model exchange, but do not fully prevent behavioral divergence across runtimes. Structural portability can therefore exist without semantic portability.

### Recurring sources of semantic divergence

* **Event scheduling underspecification:** queue ordering, preemption, simultaneity handling, and atomicity assumptions can differ, leading to different execution orders and timing.
* **ECC interpretation differences:** runtimes may differ on when algorithms execute, when outputs become visible, and how data/event synchronization is realized.
* **Communication FB policy hidden in implementations:** publisher–subscriber and communication FBs can map to buffered asynchronous messaging, blocking synchronous calls, batching, etc., without the model explicitly constraining the policy.
* **Timing is outside the core model:** execution times and platform/network delays are not part of the architecture model; even if ordering matches, latency may differ and affect control behavior.

### Role of Part 4 (Compliance Profiles)

The paper motivates IEC 61499-4 as the practical enforcement mechanism to reduce semantic drift by specifying:

* the subset of the standard used,
* mandatory vs optional elements,
* precise execution and communication rules,
* constraints that make exchanged models behaviorally comparable (beyond XML syntax alone).

### Tooling landscape (as characterized)

* **IDEs/tools:** a mix of commercial and open/research tools (e.g., ISaGRAF, nxtSTUDIO, FBDK, 4diac). IDE capabilities improve usability and engineering workflow but do not define runtime semantics.
* **Runtimes/platforms:** runtimes determine observable behavior (event handling, scheduling, communication semantics, timing). Interoperability across runtimes is often validated informally rather than via shared certification procedures.

### Proposed directions

* Generalize the Feasibility Demonstration Compliance Profile (FDCP) toward implementation-neutral profiles (remove language/protocol-specific assumptions).
* Use **URI-based bindings** for communication FBs to keep models generic while making transport/protocol binding explicit through schemes (e.g., `canopen://...`, `devicenet://...`).
* Address lack of standardized mechanisms for distributing/downloading FB types and libraries to devices by using references that specify location/identity independently of transfer mechanism.
* Establish trust via shared, open test configurations and automated test suites to enable reproducible conformance checking.

### Post-2012 ecosystem notes (optional context)

* IEC 61499-1 and -2 second editions were published in 2012; IEC 61499-4 (compliance profiles) followed in 2013.
* Eclipse 4diac (IDE + FORTE runtime) became a widely used open ecosystem in research and practice.
* FBDK continued with updates; nxtSTUDIO/nxtControl reflects continued commercial investment; ISaGRAF remains active primarily within vendor ecosystems.

---

Newer directional initiative: UniversalAutomation.org (UAO)

UAO positions its shared runtime as IEC 61499–based**, with the explicit goal of **portable applications across heterogeneous hardware**.
  Source: [https://universalautomation.org/uao-technology/](https://universalautomation.org/uao-technology/)
* This directly mirrors the **Section V “open systems + network effects” vision**, but implemented as an **industry consortium**, not a standard part.

-Communication `ID` as a generic locator (idea → practice)

* The **`ID` input of standard IEC 61499 communication FBs** (`CLIENT`, `SERVER`, `PUBLISH`, `SUBSCRIBE`) is used to encode **protocol + addressing** in a single string.
* Conceptually equivalent to a **URI-like locator**:

  * one FB type
  * different transport/protocol stacks selected by the `ID` string
* The more speculative idea of using the `ID` as a **download locator for missing FB types** exists conceptually, but **is not standardized nor implemented**.

What exists in practice:!?

Eclipse 4diac FORTE — layered `ID` strings

* FORTE implements `ID` as a **stack of named communication layers with parameters**:

  * Syntax: `{protocol[layer_param].}protocol[layer_param]`
  * Ex: `fbdk[].ip[192.168.20.1:61499]`
* This is **not RFC 3986–compliant URI syntax**, but functionally equivalent in intent:
  **one string selects protocol stack + endpoint**.
* Source: [https://github.com/eclipse-4diac/4diac-forte](https://github.com/eclipse-4diac/4diac-forte)

---

OPC UA is a first-class communication layer in 4diac

* FORTE supports **OPC UA as a communication layer** (via open62541).
* Typical `ID` strings look like:

  * `opc_ua[READ;/Objects/1:Flip]`
  * `opc_ua[WRITE;/Objects/1:Flop]`
* This is fully integrated into **4diac workflows and tutorials**.
* S: [https://github.com/eclipse-4diac/4diac-forte](https://github.com/eclipse-4diac/4diac-forte)

---

Deployment via standard protocol endpoints

* 4diac can **deploy IEC 61499 applications over OPC UA**:

  * devices addressed via endpoints like `opc.tcp://host:4840`
  * FORTE exposes the deployment interface when built/run with OPC UA support
* This is **not “downloading FB types via URI”**, but:

  * deployment, management, runtime control
    are driven by **standardized endpoint strings**.
[https://github.com/eclipse-4diac/4diac-forte](https://github.com/eclipse-4diac/4diac-forte)

---

Containerization is officially supported

* FORTE is explicitly **Docker-deployable**:

  * official documentation
  * images including MQTT + OPC UA (+ security)
  * standard port exposure (61499, 4840)
* This aligns with **modern ops / platform portability**, not just academic demos.
[https://github.com/eclipse-4diac/4diac-forte](https://github.com/eclipse-4diac/4diac-forte)

---

Distributed runtime execution is operational

* 4diac tutorials demonstrate **splitting a single IEC 61499 application across multiple FORTE devices**.
* Communication FBs explicitly wire execution across devices.
* it’s a documented, first-class workflow.
See [https://github.com/eclipse-4diac/4diac-forte](https://github.com/eclipse-4diac/4diac-forte)

---

* **Portability reality check (2014)**
  *A Portability Study of IEC 61499: Semantics and Tools*
  [https://research.aalto.fi/fi/publications/a-portability-study-of-iec-61499-semantics-and-tools/](https://research.aalto.fi/fi/publications/a-portability-study-of-iec-61499-semantics-and-tools/)

* **Critical comparison vs IEC 61131 (2013)**
  [https://arxiv.org/pdf/1303.4761](https://arxiv.org/pdf/1303.4761)

* **Formal semantics work (composite FBs, 2018)**
  [https://arxiv.org/pdf/1805.08984](https://arxiv.org/pdf/1805.08984)

* **Library structuring problem persists (2022)**
  [https://epub.jku.at/obvulioa/download/pdf/7941912](https://epub.jku.at/obvulioa/download/pdf/7941912)

* **Industrial architecture & adoption challenges (2024)**
  [https://www.sciencedirect.com/science/article/pii/S2212827124014355](https://www.sciencedirect.com/science/article/pii/S2212827124014355)

* **Education / learning-curve barrier (2025)**
  [https://www.sciencedirect.com/science/article/pii/S2405896325006238](https://www.sciencedirect.com/science/article/pii/S2405896325006238)

---
implicit:

* The **“URI-style ID” idea from ~2012** is in practice, most clearly in **Eclipse 4diac FORTE**.
* **UAO** represents the **business-side realization** of the same portability dream.
* "Standardized, a canonical **IEC 61499-5**, download FB types by URI" mechanism never happened.

But tools quietly implemented the useful parts anyway.