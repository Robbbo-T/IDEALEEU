# idealeeu

> Unified, audit‑ready platform for multi‑vehicle aerospace programs.  
> Reference applications: **AMSDP** (Aerospace Material & Software Digital Passports) and **AAMMPP** (Aerospace Assets Management, Maintenance & Procurement Platform).

[![Status](https://img.shields.io/badge/status-alpha-yellow)](#)
[![License](https://img.shields.io/badge/license-Apache--2.0-blue)](LICENSE)

**Tagline**: *Design responsibly. Prove it.*

---

## 0. Compliance & Responsibility Disclaimer

idealeeu is an **alignment and evidence collection framework**. It does **not** itself assert airworthiness or regulatory compliance (DO‑178C, DO‑254, ARP4754A, EU AI Act, etc.).  
It aggregates artifacts, provenance, and traceability to support certification, ESG audits, and responsible AI assessments. Implementers remain responsible for regulatory engagements.

---

## 1. TL;DR

idealeeu turns ESG and assurance principles into **executable data contracts**, **workflows**, **LLM governance**, and **traceable artifacts**.  
It composes:

- **Reference services**: AMSDP (digital passports) & AAMMPP (lifecycle, MRO, procurement)
- **LLM layer**: provider‑agnostic gateway, retrieval (RAG), guardrails, eval harness
- **Governance layer (MAL)**: policies, evidence threads, risk controls

**Outcomes**: auditable architectures, reusable contracts, accountable automation.

---

## 2. Mission & Scope

**Mission**: Deliver certified, serial‑ready aerospace systems with a closed‑loop digital thread from concept → fleet operations.

**Scope**: Full lifecycle: requirements → design → verification & certification → industrialization → operations → continuous improvement, with sustainability & safety evidence integrated.

---

## 3. Principles

| Pillar | Description |
|--------|-------------|
| ESG‑first | Embed environment, social, governance metrics in artifacts |
| Standards‑anchored | W3C VC, EPCIS 2.0, ASD S‑Series, ISO/IEC/IEEE 15288, SBOM/SLSA |
| Responsible AI | Human‑governed LLM actions, auditability, guardrails |
| Traceability | Strict ID patterns and contract tests; end‑to‑end data lineage |
| Replaceable components | Storage, queue, model, and embedding adapters are swappable |
| Typed & secure | Schemas drive validators; logs redacted; provenance tracked |
| Dependency‑light | Avoid unnecessary third‑party libraries; justify each addition |

---

## 4. Positioning

**What it is**:  
A modular framework and method set for designing aerospace software & data ecosystems with provable stewardship, safety, and sustainability.

**What it is not**:  
- Not a product certification statement  
- Not an aircraft or propulsion program deliverable  
- Not a token economy or marketplace core (commerce adjunct lives separately)

---

## 5. Architecture Overview

Layers (see diagrams in `docs/architecture/`):
1. Gateway (REST / GraphQL ingress, AuthN/Z)
2. Control Layer (MAL orchestration & policy engine)
3. Domain Services (passports, item master, configuration, licensing, MRO flows)
4. Data Plane (schema registry, lineage catalog, event & audit stores)
5. Storage (PostgreSQL OLTP, object storage, vector DB adapters)
6. Observability & Security (structured logs, metrics, traces, integrity chain)
7. LLM & Retrieval (gateway, embeddings, RAG, guardrails, eval harness)
8. Infrastructure (Docker Compose / Kubernetes, IaC, CI/CD pipelines)

Diagram references:
- `docs/architecture/context.puml`
- `docs/architecture/components.puml`
- `docs/architecture/sequence_passport_issue.puml`

---

## 6. Standards & Interoperability Targets

| Domain | Standards / References |
|--------|------------------------|
| Identity & Credentials | W3C VC / VP |
| Supply Chain Events | GS1 EPCIS 2.0 + CBV |
| Tech Publications & Procurement | ASD S‑Series (S1000D, S2000M) |
| Software Assurance | SBOM (CycloneDX), SLSA provenance |
| Systems Lifecycle | ISO/IEC/IEEE 15288, INCOSE guidance |
| Aero Safety Alignment | DO‑178C / DO‑330, DO‑254, ARP4754A / ARP4761 (targets only) |
| Responsible AI | EU AI Act (high‑risk preparedness), ISO/IEC 24027 |

---

## 7. Repository Layout (Monorepo)

```
/                      # Root
/docs/                 # Documentation & guides
/00-PROGRAM/           # Governance & platform core
  platform/
    amsdp/             # Digital passport issuance/verify/revoke
    aammpp/            # Item master, MRO, procurement
    api/               # OpenAPI & GraphQL schemas
    schemas/           # JSON/Avro/Proto contracts + tests
    clients/           # SDKs/examples
    infra/             # IaC, Docker, Helm, GH Actions
    tools/             # CLIs, generators, loaders
    llm/               # Gateway, embeddings, RAG, guardrails, eval
    playground-ui/     # Multi-tenant UI
    vector/            # pgvector/Qdrant adapters
    service/           # RMA/repair/requalification flows
    licensing/         # Entitlements & allocations
/01-FLEET/             # Ops data hub, MRO, federated learning
/02-AIRCRAFT/          # AIR-T baselines; domain integration
/03-SPACECRAFT/        # Spacecraft (STA) baselines
/04-SATELLITES/        # Satellite product structures
/05-TELESCOPES/        # Observatory payload structures
/06-PROBES/            # Deep-space probes
/07-DRONES/            # UAS / UAM product lines
/08-LAUNCHERS/         # Launch vehicles
/09-STM-SPACE-STATION-MODULES/ # Station modules
/10-BUSINESS/          # Market, partnerships, finance layer
```

Platform root for reusable services: `/00-PROGRAM/platform`.

---

## 8. Quickstart (Developer)

### Prerequisites
- Git, Docker, Docker Compose
- Node 20+ (TypeScript strict mode) & Python 3.11+ (mypy strict)
- Make, OpenSSL (hashing/provenance), optional PlantUML

### Bootstrap
```bash
git clone https://github.com/robbbo-t/idealeeu
cd idealeeu
make bootstrap
make build
make up
make test
```

### Common Targets
```bash
make up down logs lint fmt test test-contracts sbom provenance release
```

---

## 9. Configuration

```ini
IDEALEEU_ENV=dev
IDEALEEU_LOG_LEVEL=info
IDEALEEU_DB_URL=postgresql://user:pass@db:5432/ideale
IDEALEEU_OBJECT_STORE=s3://bucket/prefix
OIDC_ISSUER_URL=https://auth.example.com/
OIDC_AUDIENCE=ideale-api
JWT_SIGNING_KEY=change-me
EVENT_BUS_URL=nats://nats:4222
```

See `.env.example` for a complete template with descriptions.

A Python configuration module is available in the `config/` directory for easy access to settings:

```python
from config import get_settings

settings = get_settings()
print(f"Environment: {settings.env.value}")
print(f"Database: {settings.db_url}")
```

Secrets must be injected via the orchestrator secret store. Do not commit secrets.
Inject secrets via orchestrator/KMS; never commit them.

---

## 10. Component Taxonomy & Passports

Classes: `primary_structure`, `secondary_structure`, `installation_hardware`, `information_hardware`, `software`, `model`, `firmware`, `sensor_antenna`.

Lifecycle: `draft → released → fabricated_or_loaded → inspected → installed → in_service → retired_or_scrapped`

Schemas live under `/00-PROGRAM/platform/schemas/components/`.

---

## 11. Evidence Threads

| Flow | Core Artifacts | Tests | Audit Outputs |
|------|----------------|-------|---------------|
| Passport Issue | Passport.v1, SBOM, provenance, signature bundle | Contract + functional + policy | Credential hash, audit event |
| Repair & Requalification | RMA, RepairOrder, RequalificationReport | Flow + EPCIS + policy | EPCIS log, passport delta |
| Licensing Entitlement | Entitlement, Assignment, Transfer | Policy invariants | Allocation ledger |
| Configuration Change | Change request, baseline tag manifest | Diff & trace tests | CCB minutes, baseline manifest |
| LLM Interaction | Prompt log, guardrail config, eval metrics | Safety rule tests | Redacted prompt + decision log |

Each exposes schema version, artifact hash, correlationId chain, and signature/provenance reference.

---

## 12. Data Contracts & Schema Governance

- Source of truth: `/00-PROGRAM/platform/schemas/**`
- SemVer: MAJOR (breaking → filename bump), MINOR (compatible additions), PATCH (non-structural)
- Deprecations: `x-deprecated: true` for ≥1 MINOR before removal
- Manifest: `schemas/manifest.yaml` (id, path, hash, owners, tests)
- CI: generate types & validators on diff; run contract tests

---

## 13. APIs

Gateway provides REST & GraphQL (OpenAPI & AsyncAPI specs under `/00-PROGRAM/platform/api/`).

Examples:
- OIDC authenticate → issue passport `POST /amsdp/v1/passports`
- Verify `POST /amsdp/v1/verify`
- Revoke `POST /amsdp/v1/revoke`
- Service endpoints: RMA, repair, requalification, return-to-service
- Licensing: entitlements, allocations, transfers

---

## 14. Security Model & Logging Contract

| Control | Mechanism |
|---------|-----------|
| AuthN | OIDC JWT |
| AuthZ | RBAC + ABAC policies (MAL) |
| Audit | Append-only, tamper-evident chain (ADR in progress) |
| Logging | Structured; mandatory fields: timestamp, service, tenant, project, correlationId, action, result, severity |
| Redaction | `x-sensitive: true` fields → `<redacted>` |
| Supply Chain | SBOM, CodeQL, provenance attestations |
| Secrets | KMS / secret store |
| PQC Readiness | Tracked in `docs/crypto/pqc.md` |

No PII or secrets in logs.

---

## 15. Responsible AI Boundary

LLM subsystem:
- Cannot autonomously alter schemas, policies, or entitlements
- All prompts/tool calls logged with correlationId & redactions
- Guardrails (EPE) enforce safety/ethics rules
- Human approval for privileged actions

Artifacts: `QPLC_DEFINITION.md`, `ETHICAL_POLICIES/`.

---

## 16. CI/CD

- Actions: build, lint, unit, contract, integration, CodeQL, image scan, SBOM, provenance
- Gates: schema compatibility, policy invariants, coverage thresholds on critical paths
- Release: signed images, SBOM + provenance attached, semver auto-bump via Conventional Commits

---

## 17. Operations

| Capability | Location |
|------------|----------|
| Observability | Logs, metrics, traces (OTLP + Prometheus) |
| Backups | PITR for DB; object store retention |
| Integrity | Artifact footers embed build SHA & schema hash |
| Runbooks | `/docs/runbooks/` |
| Performance | Instrumented endpoints; latency SLO tests |
| Retention | `docs/governance/retention.md` |

---

## 18. Governance

- CODEOWNERS enforce independent review
- ADRs: `/docs/adr/`
- Change Control: RFC issues, CCB minutes, baseline tags
- Traceability registry: `/00-PROGRAM/CONFIG_MGMT/10-TRACEABILITY/UTCS/`
- Index auto-refresh; quarterly manual audit

---

## 19. Contributing

See `CONTRIBUTING.md`.

Flow:
1. RFC (if non-trivial)
2. Schema change → manifest update → regenerate types/tests
3. Implementation + tests (unit, contract, integration)
4. Docs + README updates
5. Ensure SBOM & provenance pass
6. CODEOWNERS review → merge

---

## 20. Roadmap (Indicative)

| Version | Focus |
|---------|-------|
| v0.1 | Public repo, core schemas, passport issue/verify |
| v0.2 | AAMMPP item master, inventory, work orders, GraphQL façade |
| v0.3 | EPCIS ingest, supplier onboarding |
| v1.0 | Hardening, signed releases, full evidence threads, AI guardrails maturity |

---

## 21. Sustainable Energy Systems (Summary)

Tracks hydrogen, battery‑electric, SAF, advanced propulsion architectures for sustainability metrics (emissions, noise, energy efficiency). Multi‑energy hybrid concept (AMPAS) integrating cryogenic + electric power flows; outlines CO₂/NOx reductions & infrastructure challenges.

Extended notes: `docs/energy/`.

---

## 22. BWB-H2-HY-E-THERMAL-CRYO-001 (Snapshot)

Development plan for blended wing body hydrogen hybrid-electric aircraft (cryogenic thermal management integrated). Staged phases from concept → certification → EIS. Full plan path under `/02-AIRCRAFT/.../BWB-H2-Hy-E/`.

---

## 23. TFA Domains

Canonical domain mapping (AAA, CQH, PPP, EEE, LCC, IIF, etc.) for cross‑discipline traceability. Reference: `docs/tfa/domains.md`.

---

## 24. Licensing & Entitlements

Collaborative DevOps licensing:
- Mixed seat + usage entitlements
- Allocation, transfer, expiry ledger
- Isolation by `{tenant}/{project}`
Schemas at `/00-PROGRAM/platform/schemas/licensing/`.

Policy tests validate invariants (no negative allocation, expiry enforcement).

---

## 25. Index & Navigation

Top-level anchors:  
[`/00-PROGRAM`](./00-PROGRAM/) · [`/01-FLEET`](./01-FLEET/) · [`/02-AIRCRAFT`](./02-AIRCRAFT/) · [`/03-SPACECRAFT`](./03-SPACECRAFT/) · [`/04-SATELLITES`](./04-SATELLITES/) · [`/05-TELESCOPES`](./05-TELESCOPES/) · [`/06-PROBES`](./06-PROBES/) · [`/07-DRONES`](./07-DRONES/) · [`/08-LAUNCHERS`](./08-LAUNCHERS/) · [`/09-STM-SPACE-STATION-MODULES`](./09-STM-SPACE-STATION-MODULES/) · [`/10-BUSINESS`](./10-BUSINESS/)

Governance: [`/00-PROGRAM/GOVERNANCE/`](./00-PROGRAM/GOVERNANCE/)  
Config Mgmt: [`/00-PROGRAM/CONFIG_MGMT/`](./00-PROGRAM/CONFIG_MGMT/)  
Digital Thread (MBSE): `/00-PROGRAM/DIGITAL_THREAD/04-MBSE/`

---

## 26. Security Policy

Report security issues to [security@idealeeu.eu](mailto:security@idealeeu.eu). Do not file public issues. See `SECURITY.md`.

---

## 27. Support

Use GitHub Discussions or issue templates (non-security). Partner onboarding: `/docs/onboarding/`.

---

## 28. License

Apache‑2.0. See [LICENSE](LICENSE).

---

## 29. Next Steps (Contributor Checklist)

1. `make bootstrap`
2. Confirm schema changes → update manifest → run `make test-contracts`
3. Implement feature with typed code (TS strict / Python with type hints)
4. Add/adjust tests (unit, contract, integration)
5. Regenerate SBOM & provenance
6. Update docs (README, sequence diagrams if impacted)
7. Request independent review
8. Merge upon green gates

---

## 30. Glossary

| Term | Meaning |
|------|--------|
| MAL | Master Application Layer (policy orchestration) |
| Passport | Verifiable credential & lifecycle metadata |
| Evidence Thread | Group of artifacts proving a lifecycle flow |
| UTCS | Unified Traceability & Configuration Set registry |
| SLSA | Supply-chain Levels for Software Artifacts |
| QPLC | Human‑governed AI oversight framework |
| EPCIS | Supply chain event standard |
| RAG | Retrieval-Augmented Generation |

---

**Document Version**: 1.0  
**Date**: October 24, 2025  
**Status**: Initial Development Requirements

**TFA Domain Mapping**: This development plan integrates across CQH (Cryogenics-Quantum-H2), PPP (Propulsion), AAA (Airframes-Aerodynamics-Airworthiness), EEE (Electrical-Endocircular-Energization), LCC (Linkages-Control-Communications), and IIF (Industrial-Infrastructure-Facilities).

**Repository References**:
* Configuration details: `/02-AIRCRAFT/MODEL_IDENTIFICATION/AMPEL360-AIR-T/ARCH/BWB-H2-Hy-E/`
* Domain systems: `/02-AIRCRAFT/MODEL_IDENTIFICATION/AMPEL360-AIR-T/ARCH/BWB-H2-Hy-E/FAMILY/Q100_STD01/DOMAIN/`
* UTCS traceability: `/00-PROGRAM/CONFIG_MGMT/10-TRACEABILITY/UTCS/`

---

## Extended materials

### TFA Canonical Domains

| Code | Domain                                 | Focus                                  |
| ---- | -------------------------------------- | -------------------------------------- |
| AAA  | Airframes‑Aerodynamics‑Airworthiness   | Structure, aero, certification         |
| AAP  | Airport‑Adaptable‑Platforms            | Ground ops, GSE                        |
| CCC  | Cockpit‑Cabin‑Cargo                    | Flight deck, passenger, freight        |
| CQH  | Cryogenics‑Quantum‑H2                  | H₂ systems, quantum tech               |
| DDD  | Drainage‑Dehumidification‑Drying       | Moisture control                       |
| EDI  | Electronics‑Digital‑Instruments        | Avionics, sensors                      |
| EEE  | Electrical‑Endocircular‑Energization   | Power, energy harvesting               |
| EER  | Environmental‑Emissions‑Remediation    | Fire, pollution, sustainability        |
| IIF  | Industrial‑Infrastructure‑Facilities   | Manufacturing, tooling                 |
| IIS  | Information‑Intelligence‑Systems       | Software, AI, cybersecurity            |
| LCC  | Linkages‑Control‑Communications        | Flight controls, datalinks             |
| LIB  | Logistics‑Inventory‑Blockchain         | Supply chain, evidence anchoring       |
| MMM  | Mechanical‑Material‑Modules            | Materials, mechanical, MRO             |
| OOO  | Operations‑Optimizations‑Orchestration | Fleet ops, optimization, backends, UIs |
| PPP  | Propulsion‑Power‑Plants                | Engines, thrust, fuel                  |

### Documentation links

* Digital Passport Dashboard → `/docs/digital-passport/`
* Quick Start Guide → `/docs/quick-start/`
* TFA Domains Reference → `/docs/tfa/domains.md`
* CAx Lifecycle Overview → `/docs/cax-lifecycle/`
* API Reference → `/docs/api/`

### QPLC: Human‑Governed AI Framework

**Principles**: human sovereignty; safety‑bounded; full traceability; federated ethics learning.

**Key components**

| Component           | Description                  | Location                                                                |
| ------------------- | ---------------------------- | ----------------------------------------------------------------------- |
| QPLC Definition     | Framework spec               | `/00-PROGRAM/GOVERNANCE/QPLC_DEFINITION.md`                             |
| EPE Rules           | Ethical Policy Engine schema | `/00-PROGRAM/GOVERNANCE/MAL-EEM/ETHICAL_POLICIES/EPE-v1.0.yaml`         |
| Human‑First Policy  | Ethical principles           | `/00-PROGRAM/GOVERNANCE/MAL-EEM/ETHICAL_POLICIES/HUMAN_FIRST_POLICY.md` |
| Human Review Portal | Interface spec               | `/00-PROGRAM/GOVERNANCE/QPLC_GOVERNANCE/HUMAN_REVIEW_PORTAL.md`         |
| PLUMA Integration   | Workflow orchestration       | `/00-PROGRAM/GOVERNANCE/QPLC_GOVERNANCE/PLUMA_INTEGRATION.md`           |

**EPE rules (excerpt)**: HUM‑SAFE‑01 Safety > cost/schedule; PRIVACY‑05 Data minimization; TRANS‑06 Explainability; AUTON‑09 Human oversight.

**Compliance refs**: DO‑178C, EU AI Act (high‑risk), ISO/IEC 24027, CS‑25.1309.

### Program folders

* **/00-PROGRAM/** governance, CM, QMS, standards, supply chain

  * **/00-PROGRAM/BUSINESS/AAMMPP/** canonical AAMMPP
* **/01-FLEET/** ops data hub, MRO, federated learning
* **/02‑AIRCRAFT/** AIR‑T baselines, domain integration, twin
* **/03‑SPACECRAFT/** STA baselines, domain integration, AIT/mission
* **/04‑SATELLITES/** product structures
* **/05‑TELESCOPES/** payload/domain structures
* **/06‑PROBES/** deep‑space probes
* **/07‑DRONES/** UAS/UAM product lines
* **/08‑LAUNCHERS/** launch vehicles
* **/09‑STM‑SPACE‑STATION‑MODULES/** station modules/segments
* **/10‑BUSINESS/** market, partnerships, finance

  * **/10‑BUSINESS/A360‑EXCHANGES‑TT/** commercial layer on AAMMPP

**Core path pattern**

```
DOMAIN_INTEGRATION/PRODUCTS/<PRODUCT>/MODELS/<MODEL>/VERSION/<Qn>/SYSTEMS/…
```

Example

```
/02-AIRCRAFT/DOMAIN_INTEGRATION/PRODUCTS/AMPEL360-AIR-T/
  MODELS/BWB-H2-Hy-E/VERSION/Q100/
```

**ESG and Green Performant Tools (GPT)**

```
/00-PROGRAM/COMPLIANCE/12-ESG_SUSTAINABILITY/
  ├── 01-ESG_FRAMEWORK/
  ├── 02-GREEN_PERFORMANT_TOOLS/
  ├── 03-KEY_INDICATORS/
  ├── 04-TRANSFORMATION_VALUE/
  ├── 05-REPORTING/
  └── 06-CERTIFICATIONS/
```

**ATA-05 Maintenance Tasks Structure**

```
02-AIRCRAFT/CONFIGURATION_BASE/ATA-05_TIME_LIMITS_MAINT_CHECKS/01-MAINTENANCE_TASKS/
├── 05-01-00_MAINTENANCE_TASKS_general.md
├── ATA_05-01-10_A_Check.xml
├── ATA_05-01-20_B_Check.xml
└── ATA_05-01-30_Daily_Check.xml
```

### Repository Index and Navigation

**Top‑Level**: [/00‑PROGRAM](./00-PROGRAM/) · [/01‑FLEET](./01-FLEET/) · [/02‑AIRCRAFT](./02-AIRCRAFT/) · [/03‑SPACECRAFT](./03-SPACECRAFT/) · [/04‑SATELLITES](./04-SATELLITES/) · [/05‑TELESCOPES](./05-TELESCOPES/) · [/06‑PROBES](./06-PROBES/) · [/07‑DRONES](./07-DRONES/) · [/08‑LAUNCHERS](./08-LAUNCHERS/) · [/09‑STM‑SPACE‑STATION‑MODULES](./09-STM-SPACE-STATION-MODULES/) · [/10‑BUSINESS](./10-BUSINESS/)

**Reference points**: Governance → [`/00-PROGRAM/GOVERNANCE/`](./00-PROGRAM/GOVERNANCE/); Config Mgmt → [`/00-PROGRAM/CONFIG_MGMT/`](./00-PROGRAM/CONFIG_MGMT/); ECR/ECO/CCB → `06-CHANGES/` and `05-CCB/`; Digital Thread (MBSE) → `/00-PROGRAM/DIGITAL_THREAD/04-MBSE/`; Digital Twin → `/00-PROGRAM/DIGITAL_THREAD/05-DIGITAL_TWIN/`; UTCS Registry → `/00-PROGRAM/CONFIG_MGMT/10-TRACEABILITY/UTCS/`.

**Index maintenance**: automated updates with structure changes; manual review quarterly; baseline snapshots at milestones.

