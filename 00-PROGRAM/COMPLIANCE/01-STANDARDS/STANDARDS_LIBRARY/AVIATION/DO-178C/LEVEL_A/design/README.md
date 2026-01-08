# Design Evidence – Level A

Purpose:
Centralizes software architecture (HLD), detailed component design (LLD), interface contracts, and partitioning assumptions for the certified item.

Traceability:
- Each HLD section references high-level requirements (REQ-).
- Each LLD file (DES-XXXX) refines one or more low-level requirements (REQ-).
- Each interface file (INT-XXXX) references schema sources in `/00-PROGRAM/platform/schemas/**`.
- Partitioning assumptions link to platform evidence (e.g., memory protection, scheduling segregation).

Contents:
- `HLD.md` — System and software architectural overview
- `lld/` — Component-level design details
- `interfaces/` — Interface and protocol contracts (versioned)
- `partitioning/` — Assumptions + verification strategy for segregation
- `safety_architecture.md` — Hazard mitigation design measures
- `diagrams/` — Source diagrams (Draw.io / PlantUML). Rendered exports stored alongside.

Design ID Rules:
- HLD logical sections use anchors: `# HLD-SEC-<N>`
- LLD artifacts: `DES-<4 digits>-<short-name>` (e.g., `DES-0123-command-router`)
- Interface artifacts: `INT-<4 digits>-<name>` (if traced) or stable slug if not required to be numbered
- Partitioning assumptions: `PART-<N>` enumerations in assumptions.md

Independence:
Design reviews logged in `qa/` with reviewer distinct from original author.

Checklist (Before Baselining Design):
- All DES-XXXX mapped to at least one REQ-XXXX
- No orphan REQ-XXXX lacking a DES-XXXX (unless justified: trivial or directly implemented)
- Interface version recorded (SEMVER) and schema hash
- Resource + timing assumptions captured with planned verification method
- Safety mitigations traced to hazard controls (HAZ-XXXX) in safety file
