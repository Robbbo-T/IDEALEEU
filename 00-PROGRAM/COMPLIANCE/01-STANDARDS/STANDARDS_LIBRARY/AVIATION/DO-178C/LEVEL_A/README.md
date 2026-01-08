# DO-178C Level A – Evidence Hub

## Purpose
Central repository for Level A compliance evidence for the certified item. Consolidates plans, baselines, verification results, structural coverage, CM/QA records, tool qualification, and certification artifacts.

## Scope
- Design Assurance Level: A (catastrophic failure condition)
- Full independence for verification + QA
- Structural coverage to Statement, Decision, and MC/DC (DO‑178C 6.4.4)
- Tool qualification as needed (DO‑330)
- Partitioning / resource isolation evidence (if hosted on IMA / mixed-criticality platform)

## Directory Layout
- `planning/` — PSAC, SDP, SVP, SQAP, SCMP
- `requirements/` — High-Level + Low-Level reqs, trace IDs
- `design/` — HLD, LLD, interfaces, partitioning assumptions
- `source/` — Tagged code baselines (immutable)
- `verification/` — Procedures, results, defects, coverage, `mcdc_justification/`
- `tools/` — DO‑330 qualification plans + evidence
- `cm/` — Baseline records, CCB minutes, PR/CR logs
- `qa/` — Audit reports, review logs, independence matrix
- `certification/` — SAS, Configuration Index, SOI minutes, authority checklists

## Entry Points
- Plan Set: `planning/PSAC.md`
- Traceability Index: `requirements/TRACE.md`
- Verification Index: `verification/INDEX.md`
- Certification Index: `certification/SAS.md`

## Objectives Mapping (DO-178C)
| Table | Area | Status | Evidence Path |
|-------|------|--------|---------------|
| A-1 | High-Level Requirements | … | requirements/HLR.md |
| A-2 | Low-Level Requirements | … | requirements/LLR.md |
| A-3 | Design | … | design/LLD/*.md |
| A-4 | Coding | … | source/ (tag vX.Y) |
| A-5 | Integration | … | verification/integration/ |
| A-6 | Verification of Outputs | … | verification/results/ |
| A-7 | Configuration Management / QA | … | cm/, qa/ |

(Keep a machine‑readable YAML mirror in `certification/objectives_status.yaml` for automation.)

## Roles & Independence
| Function | Primary | Independent Reviewer | Artifacts Reviewed |
|----------|--------|----------------------|--------------------|
| Requirements | Dev Lead | IV&V Lead | HLR, LLR, TRACE |
| Design | Dev Architect | Safety Engineer | HLD, LLD |
| Code | Implementer | Code Reviewer (independent) | source/, static analysis |
| Verification | Test Engineer | IV&V Lead | procedures, results |
| Coverage | Verification Tool Owner | QA | coverage reports |
| CM | CM/CCB Chair | QA | baselines, PR/CR logs |
| QA Surveillance | QA | — | audits, independence matrix |
| Tool Qualification | Tool Owner | QA / IV&V | tools/qualification/* |

## Traceability Model
Each requirement (REQ-XXXX) traces to:
- Design element(s): DES-XXXX
- Code module(s): `source/path/File.ts`
- Test case(s): TST-XXXX
- Coverage segments: auto-collected (file + line range)
Maintain a forward and backward complete mapping (see `requirements/TRACE.md`).

## Structural Coverage Process
1. Instrument build with coverage flags.
2. Run full regression test suite under defined environment.
3. Collect raw coverage (e.g., gcov/llvm-cov or language-specific tooling).
4. Normalize and merge into unified XML/JSON (`verification/coverage/merged_coverage.json`).
5. Check thresholds: Statement 100%, Decision 100%, MC/DC 100%.
6. Produce gap report (`verification/coverage/gaps.md`) listing each unachieved condition with justification (e.g., defensive code, unreachable partition fail-safes).
7. Sign-off: Independent review recorded in `qa/coverage_review_log.md`.

## Tool Qualification Matrix (DO-330)
| Tool | Purpose | Classification | TQL | Qualification Status | Evidence |
|------|---------|---------------|-----|----------------------|---------|
| Static Analyzer (CodeQL) | Verification (no automatic pass/fail insertion) | Development Support | TQL-5 | N/A (justification) | tools/codeql/ |
| Coverage Collector | Verification (affects structural coverage) | Verification | TQL-4 | Pending | tools/coverage/plan.md |
| Build System | Could insert errors | Development | TQL-4 | Assessment Complete | tools/build/assessment.md |
Justify any “No Qualification Required” decisions with criteria from DO‑330 Annex.

## Configuration & Baseline Policy
- Baselines: Requirements, Design, Source, Verification at major gates.
- Immutable tags: `baseline/REQ-v1`, `baseline/CODE-v1`, etc.
- Changes post-baseline require PR + CCB approval; record decision in `cm/ccb_minutes/{date}.md`.

## Defect / Problem Reporting Lifecycle
1. Log anomaly (PR-XXXX) in `verification/anomalies/PR-XXXX.md`.
2. Classify (Requirement / Design / Code / Test / Tool).
3. Disposition (Fix / Defer / Justify).
4. CCB review outcome appended + signature.
5. Trace closure in `verification/INDEX.md`.

## Gating
- FCR-1: Plans approved, trace skeleton complete, tool strategy baselined, test env qualified.
- FCR-2: All objectives satisfied, anomalies closed or justified, SAS ready for authority.

## Reproducibility
Include in every generated report footer:
```
Build SHA: <commit>
Baseline Tag: <tag>
Toolchain Versions: <compiler X.Y, coverage tool Z>
Environment Digest: <container image hash / OS / kernel>
Timestamp (UTC): <ISO-8601>
```
Canonical build script: `source/build_scripts/build_level_a.sh`.

## Current Status Snapshot
| Aspect | Metric | Target | Actual | Date |
|--------|--------|--------|--------|------|
| Statement Coverage | 100% | 100% | … | … |
| Decision Coverage | 100% | 99.8% | … | … |
| MC/DC Conditions | 100% | 99.2% | … | … |
| Open Anomalies | 0 | 2 | … | … |
(Automated nightly regeneration via CI.)

## Gaps & Justifications
List each outstanding MC/DC exception with ID, location, rationale, risk assessment, and approval signature.

## Glossary
- PSAC: Plan for Software Aspects of Certification
- SAS: Software Accomplishment Summary
- MC/DC: Modified Condition/Decision Coverage
- CCB: Configuration Control Board
- IV&V: Independent Verification & Validation
- TQL: Tool Qualification Level

## Contacts
- Dev Lead: …
- IV&V Lead (independent): …
- QA: …
- CM / CCB Chair: …
- Safety / Certification Engineer: …

## Authority Interaction Log
Maintain chronological SOI (Stage of Involvement) meeting minutes in `certification/soi_minutes/`.

## Rationale for Technology Choices
Explain language / framework safety approach, coding standards, static analysis coverage, data integrity mechanisms (in `planning/Technology_Rationale.md`).

---


