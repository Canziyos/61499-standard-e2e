
### 🔗 **[The IEC 61499 Function Block Standard: Software Tools and Runtime Platforms](https://www.researchgate.net/publication/235225083_The_IEC_61499_Function_Block_Standard_Software_Tools_and_Runtime_Platforms)**  
Christensen, J. H., Strasser, T. I., Valentini, A., Vyatkin, V., Zoitl, A.  
ISA Automation Week, 2012.  

Can we really build portable, configurable, multi-vendor distributed systems with this IEC 61499 Function Block Standard? The authors of the paper under discussion answer: **yes, but only if tools behave**, and that's the problem.

1. IEC 61499 promises three big things for distributed automation: **Portability**, **Configurability** and **Interoperability**.

2. **Parts 1 & 2 of the standard are not enough**.

3. **existing tools**: FBDK, ISaGRAF, 4diac, vendor runtimes:
  * Same FB model ≠ same runtime behavior.
  * Execution semantics differ.
  * XML portability exists *in theory*, not always in practice.

4. So, Just defining architecture + tool requirements does NOT guarantee systems will work together, therefore, different vendors can still interpret things differently, implement runtime behavior differently, or break portability while claiming compliance.

5. That’s why **Part 4** exists, the authoors say; **Part 4** It introduces Compliance Profiles, whose entire job is to **stop vendor bullshit**, by defining:

* *Which subset* of the standard is used.
* *How exactly* things behave.
* *What is mandatory vs optional*.

6. "open systems" have three properties:

a) **Portability**

- We can move function blocks and system models between tools.
- Reality: XML files alone don't guarantee behavior stays the same.

b) **Configurability**

- we can map software to devices/resources flexibly, across vendors.
- Reality: Toolchains often hard-code assumptions.

c) **Interoperability**

- Devices from different vendors actually cooperate at runtime.
- Reality: This is the hardest one, and often silently broken.

----
> Note 1: IEC 61499-2 defines **XML DTDs** (Annex A & B), which allow tools to exchange models. It requires profiles to specify **how strictly** those XML semantics are followed, because XML without semantic discipline = false portability (Same file ≠ same execution9.

> Note 2: **Event scheduling is underspecified**, IEC 61499 is *event-driven*, but:
* Does one event preempt another?
* Are events queued FIFO?
* Is execution atomic per FB?
* What happens if two events arrive “at the same time”?

Same model. Different order of execution. Different timing. Different behavior.

>Note 3: **Execution Control Chart (ECC) interpretation**

ECCs define *states and transitions*, but:

* When exactly is the algorithm executed?
* Are outputs visible immediately or at end-of-cycle?
* Are data updates synchronous with events?

Different runtimes answer these differently => emantic drift.


>note 4:. **Communication FBs hide runtime policy**; Publisher–subscriber FBs look identical in the model, but:

* One runtime uses buffered async messaging
* Another uses blocking sync calls
* Another batches network transfers

XML doesn’t say which => runtime decides.

note 5:. **Timing is not part of the model**, IEC 61499 (core) does **not model execution time**; So, same FB network/ Different CPU/ Different scheduler/ Different network => Execution *order* might match, but **latency won't** and for control systems, that’s already a behavior change.

> Note 5: **Compliance Profiles** are meant to say:

* This runtime executes events FIFO.
* This communication is time-triggered.
* This scheduling model applies.

(Without profiles, “IEC 61499-compliant” is *vibes-based engineering*.)

---
### Software Tools (IDEs)

* **commercial** (ISaGRAF, nxtSTUDIO) and **open-source** (FBDK, 4DIAC-IDE).
* **FBDK** acts as the original **reference tool**: semantically conservative, research-oriented, limited automation.
* **ISaGRAF Workbench** is commercially mature and TÜV-certified, but **confined to its own ecosystem**.
* **4DIAC-IDE** is open-source, extensible, and widely used in research; prioritizes **practical interoperability over certification**.
* **nxtSTUDIO** targets **system-level integration**, bundling control logic, HMI, hardware I/O, and documentation via CATs.
* Across tools, **portability and configurability are mostly “informally tested”**, not formally guaranteed.
* IDE features improve usability, but **do not define execution semantics**.
---

### Software / Firmware Platforms (Runtimes)

* Runtime platforms **determine actual system behavior** (event handling, scheduling, timing).
* **FBRT** is a early Java-based runtime used mainly for feasibility testing and education; embedded support is obsolete.
* **ISaGRAF Runtime** is TÜV-certified but **only interoperable within its own runtime**, using a vendor-specific compliance profile.
* **FORTE** is a small, portable, open-source runtime targeting embedded systems and real-time constraints.
* FORTE has been ported to multiple OSs and platforms and serves as a **de facto reference runtime**.
* **nxtRT61499F** is a commercial runtime built on FORTE, extended with additional services (e.g., OPC UA, web).
* Interoperability between runtimes is again **informally tested**, not formally certified.
* Overall pattern: **open runtimes enable real interoperability; certified runtimes favor isolation**.

The authors imply:
*“We now know what’s broken. Here’s how not to break IEC 61499’s neck on the way forward.”*

1. The core problem they diagnose.

Yes, there are now **many tools, runtimes, and libraries** for **IEC 61499**, but:

* No **multi-vendor compliance profiles**.
* No **shared test suites**.
* No **agreed certification procedures**.

Result:

* Vendors lock users into ecosystems. (like isagraf.)
* Early adopters face risk.
* “Choice” exists on paper, not in practice

2. Their proposed fix: generalize compliance profiles:

Take the **Feasibility Demonstration Compliance Profile (FDCP)** and:

* Remove **Java-specific assumptions** and **protocol-specific assumptions** (Make it **implementation-neutral**.)


3. They propose using **URI** strings for communication FBs:

Instead of hardcoding: Java, CANopen, DeviceNet, Custom protocols

```
canopen://...
devicenet://...
iec61499-fbdata://...
```
=>
* The **model stays generic**
* The **binding happens via the URI scheme**
* Semantics move from code → specification

> Let me say: this is a *very modern* idea (decoupling model from transport).

- They point out:

* There is **no standard way** to download FB types into devices.
* Current download mechanisms are implementation-dependent.
So 
> Use a URI to say *where* the type lives, not *how* it’s transferred.

This would improv portability, Reduce tool/runtime coupling amd make libraries more ecosystem-like


5. Even with better profiles, they admit:

> *Who certifies this, and how do we trust it?*

Their answer is:

* Open, shared **test configurations**
* Automated tests.
* Built as **open-source projects** (they even name **SourceForge**).

In other words:

> *Certification must be reproducible, not proprietary.* :)

They openly credit **open technologies** for:

* Making the standard feasible
* Stress-testing compliance profiles
* Exploring runtime semantics
* Training engineers
* Seeding commercial products

Then comes the shift; As IEC 61499 matures, open source will move from: **innovation engine** → **risk mitigation layer**!.


>Message to industry: Open source isn't free to maintain.
> If you profit from IEC 61499, **you should help fund the ecosystem**.

---


## Tools: what survived and what evolved post-2012

* **IEC 61499-1 (Architecture) — 2nd edition is 2012** (replaces 2005). [IEC 61499-1:2012](https://webstore.iec.ch/en/publication/5506)

* **IEC 61499-2 (Software tool requirements) — 2012**.
  [IEC 61499-2:2012](https://webstore.iec.ch/en/publication/5507)

* **IEC 61499-4 (Compliance profiles) — 2013**.
  [IEC 61499-4:2013](https://webstore.iec.ch/en/publication/5508)

**Part 5 (“Proposed Extensions”)** shows up as a planned/standardization activity (trial-use extensions) in EU standardization reporting,
[European Commission standardization report](https://ec.europa.eu/research/participants/documents/downloadPublic?appId=PPGMS&documentIds=080166e5c80a8099)

> Part 5 was proposed, discussed, and fed by projects — but nothing was released so far.

---

### Eclipse 4diac (open source) became the center of gravity.

* Still very alive: **4diac IDE + FORTE runtime** are actively maintained. [Eclipse 4diac FORTE repository](https://github.com/eclipse-4diac/4diac-forte)

* Big signal: **Eclipse 4diac 3.0** is positioned as a massive ecosystem update (IDE + FORTE + new build environment). [Eclipse 4diac 3.0 release announcement](https://eclipse.dev/4diac/news/2025/2025/eclipse-4diac-3.0-released/)

the open-source “risk mitigation + reference implementation” role from Section V, from previous paper, basically came true in some sense.

---

### Holobloc FBDK/FBRT didn't die — modernized quietly

* FBDK has ongoing updates and explicitly supports proposed extensions (e.g., library management ideas).
  [FBDK – What’s New](https://www.holobloc.com/fbdk8/whatsnew.htm)

* Download page (FBDK 11 page updated in 2023).
  [FBDK 11 – Function Block Development Kit](https://www.holobloc.com/fbdk.htm)

---

### nxtSTUDIO / nxtControl: corporate gravity happened

* nxtControl was acquired by **Schneider Electric (2017)**. [Schneider Electric acquisition of nxtControl](https://www.arcweb.com/blog/why-did-schneider-electric-acquire-nxtcontrol)

* Schneider keeps pushing IEC 61499 messaging (white papers/blogs), which is a real adoption signal even if “perfect portability” still is not guaranteed.
  [Schneider Electric IEC 61499 white paper](https://www.se.com/ww/en/download/document/998-21041914/)

---

### ISaGRAF: still around, but mostly in its own universe

* Rockwell still documents ISaGRAF technology/toolkit.
  [ISaGRAF technology – Rockwell Automation](https://www.rockwellautomation.com/en-se/support/documentation/technical-data/isagraf_20190326-0743.html)

* multiple “ISaGRAF flavors” supported by vendors (e.g., ISaGRAF 3.47 / ISaGRAF Open in an HMS/Sixnet context).
  [ISaGRAF – HMS Support Portal](https://support.hms-networks.com/hc/en-us/articles/27220881951250-ISaGRAF)

---
