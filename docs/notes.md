### System execution models (high-level families)

1. **Event-triggered architectures**

   * External/internal events occur → interrupts/callbacks/handlers run.
   * Execution order emerges at runtime.
   * Timing is emergent rather than guaranteed.
     Examples: RTOS with interrupts, message queues, callbacks.

2. **Time-triggered architectures**

   * Actions occur at predefined times.
   * Communication and execution slots are scheduled offline.
   * Timing is an explicit design artifact.
     Examples: avionics, safety-critical automotive, fly-by-wire.

3. **Time-driven / cyclic architectures**

   * Fixed scan cycles.
   * Read inputs → compute → write outputs.
   * Time is implicit in the cycle period.
     Examples: PLC-style control loops.

4. **Dataflow / synchronous-reactive architectures**

   * Computation is driven by data availability under strict logical-time rules.
   * Physical-time behavior is obtained only after mapping/scheduling.
     Examples: Simulink (modeling), Lustre, Esterel.

5. **Best-effort / throughput-oriented architectures**

   * No timing guarantees.
   * Latency is observed rather than specified.
     Examples: cloud systems, microservices.

**Key point:** Even without explicit timing models, systems still exhibit timing behavior; the difference is whether timing is controlled or merely observed.

---

### Dependable systems (dependability)

A system is **dependable** if it delivers its service correctly, continuously, and predictably, including in the presence of faults (Laprie / Avizienis tradition). Key attributes commonly associated with dependability include:

* **Correctness:** produces the intended service.
* **Timeliness:** produces the service within required time bounds (late can be equivalent to wrong).
* **Availability:** service is present when needed.
* **Reliability:** failures are infrequent.
* **Safety:** failures, if they occur, are controlled and non-harmful.

**Key point:** Dependability is primarily about **worst-case guarantees**, not typical or average behavior. A system may be functionally correct yet not dependable, or fast on average yet not dependable.

---

### Three notions often conflated

1. **Physical time**

   * Real-world cause → effect progression (independent of computation).

2. **Clocks (hardware time bases)**

   * Oscillators/timers used to measure and approximate physical time (imperfectly).

3. **Software notions of time**

   * Ticks, scheduling order, message arrival order, logical-time abstractions (interpretations built on top of clocks).

**Key point:** Physical time exists independently of the computer system; clocks only approximate it, and software constructs are derived interpretations. Treating ordering as time, or local clock readings as “the” time, leads to inconsistent system views and unsafe conclusions.
