### Semantics.md: Execution semantics and causality models

### 1. Scope and intent

This note collects **execution semantics and causality assumptions** for **IEC 61499** applications, emphasizing clarifications introduced with the **Second Edition (2012)**.
It focuses on **public, standard-aligned interpretations** useful for later **timing/causality model extraction**. Tool- or vendor-specific behaviors are excluded unless they reflect widely used reference practice.

---

### 2. Event–data separation and triggering

* IEC 61499 separates **events** (control) from **data** (values).
* **Events trigger execution and synchronize data usage**; **data changes alone do not trigger execution**.
* Data variables may be associated with an event via `WITH` so that the event defines **which inputs are relevant for that activation**.

---

### 3. Data sampling semantics (`WITH`)

* On delivery of an **input event**, the runtime shall perform **sampling (or equivalent)** of the **data inputs associated with that event via `WITH`**.
* The intent is a **consistent snapshot** of the associated data values for the algorithm(s) triggered by that event.
* This reduces timing-dependent behavior where different runtimes might otherwise read different input values for the same logical event activation.

---

### 4. Basic FB execution: single-event atomicity

* A **Basic Function Block instance** shall not be activated by **more than one input event at the same instant**.
* The resource must ensure **no concurrent delivery of multiple input events to the same FB instance**.
* Consequence: algorithm execution for one event activation is effectively **atomic with respect to that FB instance** (no overlapping algorithm runs inside the same FB).

This improves repeatability but **does not** define global scheduling, real-time behavior, or cross-device determinism.

---

### 5. Event semantics: “instantaneous occurrence” and consumption

* When an input event activates an ECC:

  * transition conditions of the active state are evaluated sequentially
  * the **input event is only considered valid for the first evaluation pass**
* After a transition is taken and a new state is entered:

  * further transitions in the same activation chain may only use **eventless conditions**
  * this prevents “sticky event” interpretations and avoids infinite looping from a single event occurrence

---

### 6. Execution Control Charts (ECCs) and run-to-completion behavior

* A Basic FB uses an **ECC** as an event-driven state machine controlling:

  * which algorithm(s) run
  * when output events are emitted
* Within an activation triggered by an input event, the ECC may take:

  * one transition driven by the triggering event
  * then a cascade of **eventless transitions** (if defined)
* Where multiple outgoing transitions exist, **ordering/priority of evaluation matters** (especially if transitions are not mutually exclusive). The Second Edition improves how this can be represented/understood; exact runtime handling still depends on the implementation conforming to the clarified rules.

---

### 7. State: temporary vs persistent

* `VAR_TEMP` variables (inside algorithms):

  * exist only during a single algorithm invocation
  * are created/initialized
  * do not persist between invocations
* Internal FB variables:

  * persist across event activations
  * define the FB’s durable state across executions

This distinction reduces accidental state and makes timing/causality reasoning cleaner.

---

### 8. Encapsulation and management visibility

* Management operations (e.g., `READ` / `WRITE`) are restricted to **externally visible interfaces** of FBs, resources, and devices.
* Internal variables and internal structure are **not** directly addressable through access-path mechanisms (removed to enforce encapsulation).
* Consequence: causality/timing models should treat internals as hidden unless explicitly exposed via interfaces.

---

### 9. Concurrency scope: resources, devices, and distribution

* IEC 61499 allows distribution of applications across:

  * multiple **resources** within a device
  * multiple **devices** across a network
* The standard does **not** fully define:

  * global scheduling across resources/devices
  * message latency bounds
  * ordering under network concurrency
* Therefore, inter-resource and inter-device causality depends on:

  * communication FB semantics (often via SIFBs)
  * runtime scheduling and communication infrastructure

---

### 10. Determinism, ordering, and what is not guaranteed

IEC 61499 clarifies local semantics (single-event delivery per FB, data sampling rules, event consumption), but it does **not** guarantee:

* real-time scheduling or deadlines
* global ordering of events across multiple FBs/resources/devices
* bounded network latency
* system-wide determinism across different runtimes/platforms
* standardized internal behavior of SIFBs

Any such guarantees require **platform assumptions**, **profiles**, or explicit engineering constraints.

---

### 11. Causality graph and timing-model extraction hooks

* An IEC 61499 application defines an explicit **event-causality graph**:

  * event connections define directed “may-trigger” relations between FB instances
* A **causal chain** (sensor → processing FBs → actuator) supports end-to-end latency modeling by composing:

  * algorithm execution times (e.g., WCET estimates)
  * event-queueing / dispatch delays (implementation/platform dependent)
  * communication delays across segments/devices (network dependent)
* Practical timing models therefore require attaching external parameters:

  * per-algorithm execution bounds
  * scheduling assumptions per resource
  * communication latency assumptions per link/segment

---

### 12. Event-triggered vs time-triggered interpretations

* IEC 61499 is fundamentally **event-triggered**.
* Time-triggered behavior can be modeled by:

  * periodic event sources (timers, cyclic triggers)
  * platforms that schedule event processing in fixed cycles/partitions
* Timing semantics in such cases come from the **event source** and/or **platform scheduling**, not from the core architecture alone.

---

### Terminology (semantic-focused)

* **Function Block (FB) type vs instance**

  * **Type**: the reusable definition (interface + internal structure/behavior).
  * **Instance**: a concrete occurrence of a type inside an application, with its own state.

* **Basic Function Block (Basic FB)**
  An FB instance that contains **algorithms** and an **ECC** to decide which algorithm(s) run in response to events.

* **Composite Function Block (Composite FB)**
  An FB type defined as a **network of internal FB instances** with event/data connections; behavior emerges from internal event flow (not from an ECC inside the composite itself, in the usual interpretation).

* **Service Interface Function Block (SIFB)**
  An FB representing interaction with **services outside the application model** (I/O, OS services, communication). Semantics are partly defined by the SIFB’s declared interface/contract, but internal behavior is typically platform-dependent.

* **Event**
  A control signal representing an **instantaneous occurrence** used to trigger execution and synchronize data sampling/usage. Not a persistent boolean state.

* **Data variable**
  A value carried on data inputs/outputs. **Does not trigger execution by itself**.

* **`WITH` association**
  A declaration-level binding that associates **specific data inputs/outputs** with an **event**, defining which data is sampled/considered on event delivery.

* **Execution Control Chart (ECC)**
  The event-driven state machine inside a Basic FB that controls:

  * state transitions based on conditions
  * which algorithms run
  * which output events are emitted

* **Resource**
  An execution context within a device that hosts FB instances and executes part of the application. Commonly maps to a task/thread/process or runtime container, but the standard leaves scheduling details to the implementation.

* **Device**
  A physical or virtual node containing one or more resources and communication interfaces. Devices host the distributed deployment of an IEC 61499 system.

* **Application**
  A network of FB instances connected by **event** and **data** connections, describing control logic independent of physical deployment (deployment maps instances to resources/devices).

* **System configuration**
  The deployment-level description that maps applications/FB instances to **devices/resources** and specifies communication structure between devices.

* **Event connection / data connection**
  A directed link between FB instances:

  * **event connection** defines triggering/causality potential
  * **data connection** carries values, typically synchronized via events

* **Causality graph**
  The directed graph induced primarily by **event connections** (and their associated data), describing “who can trigger whom”.

* **Causal chain (end-to-end path)**
  A selected path through the causality graph from a source (e.g., sensor SIFB/event) to a sink (e.g., actuator SIFB/event), used for end-to-end latency and response-time reasoning.

* **Dispatch / event queueing (implementation concept)**
  The runtime mechanism by which delivered events are stored/ordered and then processed. IEC 61499 constrains semantic outcomes (e.g., no simultaneous event delivery to the same FB), but does not mandate a single queue policy globally.

---
