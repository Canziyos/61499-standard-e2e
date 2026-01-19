Newer directional initiative: UniversalAutomation.org (UAO)

UAO positions its shared runtime as IEC 61499–based, with the explicit goal of **portable applications across heterogeneous hardware**.
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

* The **“URI-style ID” idea from ~2012** is **real in practice**, most clearly in **Eclipse 4diac FORTE**.
* **UAO** represents the **business-side realization** of the same portability dream.
* What never happened is a standardized “download FB types by URI” mechanism, a canonical **IEC 61499-5**

Buttools quietly implemented the useful parts anyway.
