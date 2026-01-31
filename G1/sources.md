# G1 Source Map.

This list supports a lightweight literature mapping (not a systematic/scoping review):
- map the relevant concepts,
- extract a concise requirement list (REQ-01..REQ-N),

---

## Seed & scope anchor
- MDHThesisDetails246 — Official thesis scope/goal; used to seed baseline requirements (E2E reaction time + data age, extraction from IEC 61499/its artefacts).

---

## 1) End-to-end timing analysis (general, not IEC 61499-specific)

### Core (recommended)
- BeckerE2E2017 — E2E timing analysis of cause–effect chains; good baseline for chain concepts and analysis inputs/assumptions.
- feiertag2009compositional — Path semantics for E2E delay calculation; motivates why “chain semantics” must be explicit.
- Guenzel2021AsyncChains — Timing analysis of asynchronized distributed cause–effect chains; highlights buffering/async effects.
- HeterogeneousChainsGuenzel2023 — Cause–effect chains with heterogeneous communication; pushes requirements for modelling link types.
- CyclicExecLednicki2014 — Cyclic execution paths in timing analysis; useful warning about cycles and modelling choices.

### Extras
- Himrane2022Response — Response time evaluation using discrete-event-system formalisms; alternative modelling/evaluation angle.
- Sarkar2016TimeEval — Time evaluation of technologies for distributed control; broad context, sometimes useful for motivation.
- MubeenExtendsCan2014 — CAN mixed messages with priority/FIFO; queueing/priority assumptions for network timing.

---

## 2) IEC 61499 standard and closely related semantics

### Primary standard documents
- IEC61499(1)webstore — Core architecture and definitions (apps, FBs, event/data connections, deployment artefacts).
- IEC61499(2)webstore — Tool requirements; what tools/artefacts are expected to provide.
- IEC61499(3)webstore — Tutorial information; terminology and interpretation support.
- IEC61499(4)Webstore — Compliance profiles; constraints relevant to portability and assumptions.
- 61499Overview — Overview of the second edition; terminology alignment and standard intent.

### Core semantics / modelling papers
- VyatkinIEC61499 — IEC 61499 foundations for embedded/distributed control design (background and terminology).
- VyatkinAsEnablerReview2011 — Review positioning IEC 61499 and typical challenges; motivation and framing.
- 61499Semanticstoolsportability — Semantics/tool portability study; supports “tool differences ⇒ extraction assumptions.”
- RTSemantics61499Lindgren2015 — Real-time semantics for IEC 61499; bridges behaviour to timing interpretation.
- FormalpersECCLindgren2015 — ECC semantics; clarifies behavioural interpretation relevant to extraction.
- ImplementationApproachesOf61499Apps — Execution-model implementation approaches; informs runtime assumptions.
- DeviceResourceExecutionModel61499 — Device/resource execution model; supports scheduling/execution context.
- ModellingExecOrderandRealtimeConstraints61499 — Execution order and real-time constraints; ordering constraints and assumptions.
- ConcurrentExec61499IndustrialEdgeApps — Concurrent execution semantics; timing implications of concurrency.
- FormalModel99Drozdov2021 — Formal model supporting time-aware computations; time-related semantics anchor.

### Extras (only if it becomes relevant)
- RefactoringECC2010 — ECC refactoring; software-structure angle.
- UnambiguousFBD2021 — Unambiguous modelling/equivalence testing; helps if “extractability” hinges on unambiguity.
- Thramboulidis2010Transformto61499 — IEC 61131-3 → IEC 61499 transformation; relevant if legacy migration artefacts are discussed.
- Pang2014MDE61499 — Model-driven engineering reference; background/supporting terminology.
- surveyComplexityOfStructuredText2023 — Structured Text complexity in IEC 61499 FBs; relevant only if complexity/maintainability becomes an issue.

---

## 3) Timing reasoning and timing constraints applied to IEC 61499 (incl. E2E within IEC 61499)

### Core
- E2E61499ResponseTimeLindgren2017 — E2E response time for IEC 61499 apps over switched Ethernet; network segment modelling.
- DeterminingWcetReactionTime61499 — Worst-case reaction time of IEC 61499 function blocks; node-level timing requirements.
- ModellevelWCET2013 — Model-level WCET analysis for IEC 61499; how timing attributes can be derived from models.
- DeviceUtilization — Early-stage utilisation analysis for IEC 61499 systems; supports resource-load assumptions.
- ModelBasedNetworkTimeCritical — Model-based network specification for time-critical IEC 61499 control; links network design to timing reasoning.
- TimingContractsSafety — Timing contracts/monitors for IEC 61499; formalising and checking timing constraints.

### Extras
- zoitlEnhancedRT2006 — Enhanced real-time execution of IEC 61499 control software; execution semantics and timing implications.
- PrioritizedDeterministic61499Gao2025 — Prioritised deterministic execution; scheduling/priority assumptions.
- AvionicsDeterministicExecution — Deterministic execution for distributed avionics using IEC 61499; strong constraints and assumptions.
- RealtimeDataAcquisition2017 — Real-time data acquisition support for IEC 61499 CPS; timing needs around I/O.
- CommsChannels61499 — Communication channels within IEC 61499 component systems; helps when modelling comm channels explicitly.
- SoftwareMeasurmentOf61499 — Software measure for basic FBs; not timing per se, only include if software-structure metrics matter.

---

## 4) Tooling and runtime platforms (artefact sources + “what exists”)

### Core
- Eclipse4diac — Toolchain anchor; engineering artefacts and formats.
- Framework4DIAC — 4diac framework paper; tooling pipeline context.
- 4diacLearnIEC61499 — 4diac learning/tutorial material; practical modelling workflow reference.
- 61499Tools2012 — Tools and runtime platforms overview; what artefacts exist across the ecosystem.
- 61499RuntimeEnvironments — Runtime environment comparison; semantic differences affecting extraction.
- DefinitionExecutionFuber61499RuntimeEnv — Execution model in a concrete runtime; example of runtime-defined semantics.
- FormalDescriptionRuntime2007 — Formal description of runtime environment with real-time constraints.
- TowardsEvaluatingExecutionSemantics61499Runtime — Methodology for evaluating runtime semantics; useful for handling runtime variation.

### Extras
- ThreadedRuntimeLindner2015 — Threaded runtime towards IEC 61499 execution; execution model detail.
- RealTExecFunctionBlocksForIoT — Real-time FB execution using RTFM-kernel; alternative runtime semantics.
- FasterThanRTVytatkin — Faster-than-real-time testing with embedded simulation; tool-supported validation.
- Faqrizal2024_AdaptiveICS — IEC 61499 + runtime enforcement; only include if enforcement/monitoring matters.
- mubeenHolisticRTA — Industrial tool suite experiences for holistic response-time analysis; implementation/pipeline perspective.

---

## 5) Timing-model extraction / bridging patterns (general, method-relevant)

### Core
- MubeenE2ETimingTranslation — Translating E2E timing requirements into an analyzable timing model; direct “REQ → model” inspiration.
- MubeenImplementationEndtoendLatencyAnalysis — Implementation of E2E latency analysis in a toolchain; practical pipeline insight.
- MubeenLegacyCommunication — Analyzable modelling of legacy communication; supports assumption handling when artefacts are incomplete.
- MubeenTowardsExtraction — Extraction of interoperable timing models; “extractability” and traceability expectations.
- MubeenExtractComponentBased2018 — Timing model extraction in multi-criticality systems; concrete extraction patterns.
- MubeenRefinement2019 — Refinement of timing constraints to support analysis; how vague constraints become analysis-ready.

### Extras
- RubusICERTanalysis — Real-time analysis framework in Rubus-ICE; tool/platform context.
- MubeenRubusApproach — Predictable embedded software in industry; practical constraints and assumptions.
- Arcticus2026RubusProductLine — Product-line/platform reference; include only if the platform context is discussed.

---

## 6) Context / method references (not G1 requirement sources)
- BlessingChakrabarti2009DRM — Design research methodology reference (method section).
- Nunamaker1990SystemsDevelopment — Systems development / DSR framing (method section).
- Kopetz_Bauer — Time-triggered architecture (real-time foundations, background only).
- Industry4 — Industry 4.0 review (context only; not timing requirements).
- Xu2018IIoTSurvey — IIoT survey (context only).
- Adapting61499DesignPattern2018 — Reusable IEC 61499 patterns (software engineering background).
- ControlSoftware61499SimulationVerification — Dev method + simulation/formal verification (background).
- DeploymentProblem61499Hussin2008 — Deployment problem; include only if deployment artefacts become a primary extraction input.
