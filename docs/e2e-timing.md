### Analyzable Modeling of Legacy Communication in Component-Based Distributed Embedded Systems

🔗 [https://doi.org/10.1109/SEAA.2011.43](https://doi.org/10.1109/SEAA.2011.43)

* End-to-end timing analysis in distributed hard real-time systems requires explicit communication modeling; legacy protocols (e.g., CAN) introduce timing effects that cannot be abstracted away without losing analyzability.

* Communication must be treated as a first-class execution concern, not hidden behind middleware.

* Analyzability is achieved through disciplined modeling and mechanical extraction of timing semantics.

* No existing approach simultaneously provides explicit execution semantics, legacy communication support, and tight end-to-end timing analyzability.

* Communication is modeled using:
  * an explicit **network specification**, and
  * explicit **send (OSWC)** and **receive (ISWC)** execution steps.

* These steps make communication visible to timing analysis.

* End-to-end timing paths are mechanically extracted from trigger relations.

* Standard response-time analysis is then applied to compute worst-case end-to-end delays.
---

### **Thoughts:**

* Analogue to **extracting timing semantics from event-driven IEC 61499 function block networks**.
* Motivates why **IEC 61499 requires an extraction-based timing approach**, rather than timing annotations alone.

> End-to-end timing analysis requires explicit extraction of execution and communication semantics from component-based architectures.

> Rubus needed explicit communication modeling to enable end-to-end timing analysis. IEC 61499 has the same structural problem.

---

## Support for Holistic Response-Time Analysis in an Industrial Tool Suite

🔗 [https://doi.org/10.1109/ECBS.2012.38](https://doi.org/10.1109/ECBS.2012.38)

* holistic End-to-end timing analysis (HRTA) is only possible if timing models are explicitly extracted; component models do not provide all required parameters unambiguously.

* HRTA assumes explicit availability of WCETs, offsets, priorities, triggering semantics, message properties, and precedence relations — these must be **derived**, not assumed.

* Distributed transactions (cause–effect chains) are not explicit and must be **constructed** from model structure and communication mappings.

* Timing inheritance is iterative: response times propagate as jitter across task → message → task chains.

* Design and deployment decisions affect analyzability; careless allocation can introduce direct cycles that make analysis non-terminating.

* Multi-network systems require staged analysis with timing results propagated across gateways as jitter.

* The **ACC case study** demonstrates feasibility on a realistic system and validates the extraction-based approach.

#### **Thoughts:**

* Direct analogue to **extracting timing models from IEC 61499 architectures**.
* Confirms that **end-to-end timing paths must be reconstructed**, not inferred from connections alone.
* Shows that **event-driven semantics require inference of transmission/activation types**.
* Demonstrates that **deployment rules and architectural constraints are necessary** for analyzability.

> End-to-end timing analysis requires explicit extraction of execution and tracing semantics from the design model.
---

## Extracting End-to-End Timing Models from Component-Based Distributed Embedded Systems” (2014)

* Rubus component model RCM properties enabling extraction:

  * explicit separation of **control flow (triggers)** and **data flow (signals)**,
  * run-to-completion SWC semantics,
  * tasks and schedules are *derived* by code generation.

* Problem source: distributed timing behavior **emerges during code generation and deployment**, not from architecture diagrams.

* end-to-end timing is an **engineering reconstruction problem**, not a modeling-language problem.

* Distributed transactions consist of:

  * **trigger chains**, **data chains**, or **mixed chains**.
* Different chain types require **different timing constraints** → chain type must be identified explicitly.

* End-to-end timing paths are **implicit and fragmented** in distributed systems.

* Core difficulty arises at **node boundaries**:

  * triggers become signals,
  * signals become messages,
  * messages may be buffered, bundled, or delayed.
* Network communication **breaks direct triggering semantics**.

* Key missing semantics:

  * who triggers the destination SWC,
  * when it is triggered after message reception.

* Required (but missing) information:

  * sender/receiver node IDs,
  * sender/receiver task IDs,
  * signal–message mapping.
* Existing RCM components are **insufficient for linking distributed chains**.

* Needed concepts:

  * explicit **linking objects**,
  * **entry and exit points** between node and network models.
* end-to-end timing chains cannot be inferred from architectural connections alone; they must be explicitly reconstructed. (again)

* End-to-End Timing Model

* Purpose: represent **all timing properties, requirements, and dependencies** needed for end-to-end timing analysis in distributed embedded systems.

* The model is split into **two complementary parts**:

  * **System Timing Model**
  * **System Linking Model**

* System Timing Model (what has timing behavior)

* Composed of:

  * **Node Timing Models**
  * **Network Timing Models**
* Captures *local* timing behavior before chains are linked end-to-end.

* Node Timing Model
* Based on **transaction models with offsets**.
* A node contains multiple **transactions**, each activated by:

  * periodic events (period (T_i)), or
  * sporadic events (minimum inter-arrival time (T_i)).
* Transactions are **independently phased**.
* Each transaction consists of **tasks** ( \tau_{ij} ).
* Each task is characterized by:

  * priority (P_{ij}),
  * WCET (C_{ij}),
  * offset (O_{ij}),
  * release jitter (J_{ij}),
  * optional deadline (D_{ij}),
  * blocking time (B_{ij}),
  * worst-case response time (R_{ij}).

* No restrictions on relationships between period, offset, deadline, or jitter.

* Network Timing Model

* Captures timing behavior of **inter-node communication**.
* Supports CAN and CAN-based protocols.
* Tasks communicate by **queueing messages** for network transmission.
* Each message is defined by:

  * unique ID,
  * priority,
  * transmission type (periodic / sporadic / mixed),
  * transmission time,
  * inherited release jitter,
  * payload size,
  * period (T_m) and/or minimum update time (MUT_m),
  * blocking time,
  * worst-case response time (R_m).

* System Linking Model (what connects timing behavior)

* Required because **transactions span multiple nodes**.
* Represents **how tasks and messages are connected** into distributed chains.
* A task chain:

  * is an ordered sequence of tasks,
  * has a common ancestor,
  * may propagate **triggers, data, or both**.

* Neighboring tasks in a chain may:

  * reside on different nodes,
  * communicate via network messages.
* So, End-to-end timing analysis requires:

  * explicit **linking information** between tasks and messages,
  * not just local timing parameters.
* Linking extraction is **significantly more complex** than in single-node systems.

* **Timing parameters alone are insufficient**.
* End-to-end timing analysis requires:

  * a **system timing model** (nodes + networks), and
  * a **system linking model** that explicitly reconstructs distributed chains.


* Purpose: **resolve linking and extraction problems** identified earlier and show a **tool-supported solution** in Rubus-ICE.
* Approach demonstrated on a **two-node distributed RCM application**.

* Introduce special-purpose SWCs:

  * **OSWC (Output Software Circuit)**: one per outgoing network message.
  * **ISWC (Input Software Circuit)**: one per incoming network message.
* Each OSWC/ISWC is translated into a **runtime task**.
* Introduce **Network Specification (NS)**:

  * one per network protocol,
  * models communication semantics explicitly.
* NS contains **signal–message mapping**:

  * signal packing into messages,
  * encoding/decoding rules,
  * message composition.
* OSWC acts as **exit point** from node model to network.
* ISWC acts as **entry point** from network to node model.
* Trigger ports of OSWCs/ISWCs are referenced in NS → enables **bounded end-to-end delays**.

* Each task is annotated with a **trigger dependency attribute**:

  * `independent` → triggered by clock or external event,
  * `dependent` → triggered by predecessor task.
* Precedence constraints added for dependent tasks.
* Chain classification:

  * all dependent (except first) → **trigger chain**,
  * more than one independent → **data chain**.

* Linking information stored **centrally in NS**.
* NS holds **pointers** to:

  * trigger in-ports of OSWCs,
  * trigger out-ports of ISWCs.
* Pointer arrays link **neighboring components across nodes**.
* Enables reconstruction of distributed trigger chains.
* Supports protocol-specific behavior (e.g., CAN):

  * send queues,
  * interrupts vs polling,
  * message reception and triggering.
* ISWC:

  * decodes message,
  * extracts signals,
  * places data on ports,
  * triggers next SWC using NS linking.
* OSWC/ISWC together form **explicit node boundaries**.

* System modeled in **Rubus Designer**.
* Compiled into **ICCM (Intermediate Compiled Component Model)**.
* ICCM contains:

  * component structure,
  * timing parameters,
  * linking information.
* End-to-end timing model is **automatically extracted** from ICCM.
* Extracted models:

  * node timing model,
  * network timing model,
  * system linking model.
* Rubus Analysis Framework computes:

  * task response times,
  * message response times,
  * end-to-end response times and delays,
  * network utilization.
* Results fed back into Rubus-ICE.

## Component-Based Multi-Criticality Vehicular Embedded Systems (2018)

* Distinguishes **multi-criticality** from classic mixed-criticality:

  * mixed-criticality (Vestal): criticality assigned to **tasks**,
  * **multi-criticality (this paper)**: criticality assigned to **applications**, not individual tasks.
* Inspired by:
  * **ISO 26262** (automotive functional safety),
  * **DO-178C** (aerospace).

* Compatible with component models using **pipe-and-filter communication**.
* Timing requirements model aligned with:

  * **TIMMO2USE / TADL2** timing constraints.
* Extends prior work by supporting **multi-criticality**, not just single-criticality systems.

* End-to-end timing model contains all information required by timing analysis engines.
* Consists of **three parts**:

  1. **Timing model**
  2. **Linking model**
  3. **Timing requirements model**
* Explicitly separates:

  * software architecture,
  * timing model,
  * timing analysis engines.

* This paper **generalizes the 2014 extraction work** by adding:

  * multi-criticality awareness,
  * richer timing requirements,
  * alignment with safety standards,
  * broader network protocol support.

* System (S) consists of:

  * **nodes (ECUs)** and **networks**.
* End-to-end timing model consists of **three parts**:

  1. **Timing model**
  2. **Linking model**
  3. **Timing requirements model**

* Based on **transactional task model with offsets**.
* Nodes are divided into **partitions**:

  * partitions provide **time and space isolation**,
  * each partition hosts software of **one criticality level**.
* Criticality levels follow **ISO 26262 (ASIL A–D)**.
* Node → partitions → transactions → tasks hierarchy.

* Activated by **independent events** (periodic or sporadic).
* Period (T) or minimum inter-arrival time defined.
* Tasks inside a transaction may have **offsets**, defining release dependencies.

* Each task characterized by:

  * WCET,
  * period,
  * offset,
  * priority,
  * release jitter,
  * blocking time,
  * response time,
  * deadline.
* No restrictions between period, deadline, offset, or jitter.

* Supports **multiple vehicular real-time protocols**:

  * CAN, CANopen, HCAN, AUTOSAR COMM,
  * switched Ethernet (AVB, HaRTES, TSN).
* Network model includes:

  * bandwidth,
  * switches and links (for multi-hop networks),
  * traffic shaping parameters (slopes, time windows),
  * set of messages.

* messages Can be **periodic, sporadic, or mixed**.
* Message attributes include:

  * priority,
  * transmission time,
  * payload size,
  * period / minimum update time,
  * offset,
  * jitter,
  * blocking time,
  * response time.
* Message properties derived from:

  * sender task behavior,
  * network protocol characteristics.

* Systems are modeled as **chains of tasks and messages**.
* Chains:

  * have one initiator and one terminator,
  * may be local or distributed.
* Tasks may receive:

  * trigger,
  * data,
  * or both.
* Messages:

  * may be task-triggered (passive networks),
  * or network-triggered (active networks).
* Multi-hop networks introduce multiple links per message.
* Linking model captures:

  * trigger flow,
  * data flow,
  * mapping of tasks ↔ messages ↔ links.
* Linking information is **essential for end-to-end analysis**.

* Timing requirements specified **on chains**, not individual tasks/messages.
* Each requirement has:

  * type,
  * MIN value,
  * MAX value.
* Only **four chain-level constraints** considered:

  * **Age**
  * **Reaction**
  * **Output Synchronization**
  * **Input Synchronization**
* Constraints aligned with **AUTOSAR / TADL2** semantics.

* Extraction Philosophy:

* Two types of extracted information:

  1. **Explicitly specified** by user.
  2. **Implicit**, inferred from architecture.
* Missing information handled via **explicit assumptions**.

* Some network/message parameters are user-defined.
* Others are derived:

  * transmission time from payload + bandwidth,
  * message priority from ID (CAN) or user attribute,
  * blocking time from lower-priority messages,
  * message jitter from sender task response-time bounds.
* Message type (periodic/sporadic/mixed) derived from sender triggering.

* Each distributed chain captured as an **ordered reference set**:

  * references to tasks, messages, ports.
* Tasks assigned **trigger dependency attribute**:

  * `Independent` (clock/event-triggered),
  * `Dependent` (triggered by predecessor).
* Precedence constraints added for dependent triggering.
* Multi-hop networks:

  * extract set of traversed links per message.

* Constraints specified using **start/end objects** on chains.
* MAX extracted from end object.
* MIN defaults to zero if unspecified.
