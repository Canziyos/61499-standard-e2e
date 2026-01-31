
This file lists only the sources treated as core inputs to the thesis argument and requirements.
# Core Sources (Thesis spine — 12 non-negotiable)

These sources form the minimum backbone for concepts, semantics, artefact basis, and the extraction-to-analysis link.

## Scope anchor
- MDHThesisDetails246 — Defines the thesis goal and scope; used to seed baseline requirements (reaction time + data age; extraction from IEC 61499 / 4diac artefacts).

## E2E timing analysis (general)
- BeckerE2E2017 — Baseline cause–effect chain concepts and analysis inputs/assumptions (reaction time / data age style thinking).
- feiertag2009compositional — Shows how path/chain semantics affect computed end-to-end delay; motivates explicit chain semantics in the model.
- Guenzel2021AsyncChains — Asynchronous chain effects (buffering, update loss) that directly drive modelling assumptions.

## IEC 61499 semantics (primary + timing-relevant semantics)
- IEC61499(1)webstore — Primary architecture/artefact definitions (FBs, apps, event/data connections) that constrain what is extractable.
- RTSemantics61499Lindgren2015 — Real-time semantics interpretation needed to justify timing meaning from IEC 61499 behaviour.

## Timing reasoning applied to IEC 61499
- E2E61499ResponseTimeLindgren2017 — Concrete E2E response-time reasoning for IEC 61499 applications over Ethernet; anchors “E2E on 61499”.
- ModellevelWCET2013 — Model-level timing attribute derivation (WCET inputs etc.); supports where timing parameters can come from.

## Tooling / runtime artefact sources
- Eclipse4diac — Toolchain anchor; defines the engineering artefacts and exports used as extraction inputs.
- 61499RuntimeEnvironments — Runtime comparison; motivates that runtime differences imply explicit assumptions/constraints in extraction.

## Bridging: requirements → analyzable timing model
- MubeenE2ETimingTranslation — Direct blueprint for translating timing requirements into an analyzable timing model.
- MubeenTowardsExtraction — Extractability + interoperability expectations; supports the “systematic extraction” framing.
