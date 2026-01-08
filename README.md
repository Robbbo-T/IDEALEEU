# IDEALEEU

> Unified, audit‑ready platform for multi‑vehicle aerospace programs.
>
> Reference apps: **AMSDP** (Aerospace Material & Software Digital Passports) and **AAMMPP** (Aerospace Assets Management, Maintenance & Procurement Platform).

[![Status](https://img.shields.io/badge/status-alpha-yellow)](#)
[![License](https://img.shields.io/badge/license-Apache--2.0-blue)](LICENSE)

---

## TL;DR

**IDEALEEU** is a design and governance framework that turns ESG principles into **executable data contracts**, **workflows**, and **models**. It composes:

* **Reference services**: AMSDP and AAMMPP.
* **LLM layer**: provider‑agnostic gateway, RAG, guardrails.

**Outcomes**: auditable architectures, artifacts, and APIs that are reusable across programs.

**Tagline**: *Design responsibly. Prove it.*

---

## What IDEALE‑EU is

An ESG‑first, standards‑anchored framework to design next‑generation aerospace systems. It runs common LLMs via a provider‑neutral gateway with retrieval and guardrails. AMSDP and AAMMPP implement the framework as reference applications.

### Principles

* **ESG‑first**: evidence and metrics embedded in every artifact.
* **LLM‑enabled, model‑agnostic**: common models through a neutral gateway.
* **Standards‑anchored**: W3C VC, EPCIS, ASD S‑Series, ISO 15288.
* **Replaceable components**: stores, queues, and models are swappable.

---

## Positioning

### What it is

* A modular framework to **design responsibly**: architectures, models, and processes with ESG baked in.
* A set of **methods and data contracts** that make traceability, auditability, and lifecycle stewardship measurable.
* A **governance layer (MAL)** that encodes policy, risk controls, and evidence collection. *MAL = Master Application Layer/Logic; the PLC of each domain.*

### What it is not

* Not an aircraft or engine program; no product claims.
* Not a certification declaration; it **collects evidence** to support audits.
* Not a token or marketplace; commercial exchanges (A360Exchanges‑TT) are adjunct.

### ESG‑first pillars

1. **Environment**: decarbonization, energy efficiency, circularity, end‑of‑life.
2. **Social**: safety, human‑in‑the‑loop oversight, fair labor, accessibility.
3. **Governance**: transparency, explainability, anti‑tamper audit, supply‑chain trust.

### Value

* Unified digital thread from requirements to operations.
* Interoperability with industry standards; vendor‑neutral interfaces.
* **Responsible AI**: QPLC human‑governed automation with guardrails and evidence.
* Lower cost‑of‑change via versioned contracts and contract tests.

**Primary users**: OEMs, Tier‑n suppliers, MROs, regulators, research programs.

**Success metrics**: emissions impact, safety outcomes, interop conformance, audit completeness, time‑to‑evidence, total cost of quality.

---

## Table of contents

* [Mission & Scope](#mission--scope)
* [Core Capabilities](#core-capabilities)
* [Architecture Overview](#architecture-overview)
* [Standards & Interop Targets](#standards--interop-targets)
* [Repository Layout](#repository-layout)
* [Quickstart (Developer)](#quickstart-developer)
* [Configuration](#configuration)
* [Component Taxonomy](#component-taxonomy)
* [Circularity and MRO](#circularity-and-mro)
* [Data Contracts](#data-contracts)
* [APIs](#apis)
* [Security Model](#security-model)
* [CI/CD](#cicd)
* [Releases & Changelog](#releases--changelog)
* [LLM Playground](#llm-playground)
* [Collaborative DevOps Licensing](#collaborative-devops-licensing)
* [Deployment](#deployment)
* [Packs & Engineering Constructs](#packs--engineering-constructs)
* [Operations](#operations)
* [Governance](#governance)
* [Contributing](#contributing)
* [Roadmap](#roadmap)
* [License](#license)
* [Security Policy](#security-policy)
* [Support](#support)
* [Sustainable energy systems](#sustainable-energy-systems-for-passenger-aircraft)
* [Extended materials](#extended-materials)

---

## Mission & Scope

**Mission**: Deliver certified, serial‑ready aerospace systems with a closed‑loop digital thread from concept to fleet operations.

**Scope**: End‑to‑end lifecycle: requirements → design → verification & certification → industrialization & production → operations → continuous improvement.

---

## Core Capabilities

* **Traceability & provenance**: part pedigree, software build lineage, conformity statements, audit trails.
* **Configuration control**: baselines, EOs/ECNs, effectivity, serialization, configuration state.
* **Digital Passports (AMSDP)**: issue, verify, revoke, and transfer credentials for material/part/software.
* **Lifecycle Ops (AAMMPP)**: item master, maintenance plans, work orders, reliability, inventory, procurement.
* **Data contracts**: typed schemas with versioning, backward‑compat rules, conformance tests.
* **Interoperability**: opinionated mappings to aerospace and supply‑chain standards.
* **Audit‑ready**: tamper‑evident logs, SBOMs, build provenance, retention policies.
* **Circularity & MRO**: repair, rework, requalification, return‑to‑service with evidence written to passports and configuration.
* **Collaborative DevOps licensing**: mixed seat+usage entitlements with governed redistribution across partner orgs.

---

## Architecture Overview

* **Identity & Trust**: issuer registry, key management, verifiable attestations, RBAC/ABAC.
* **Control Layer (MAL)**: the PLC of each domain; orchestrates workflows and policies.
* **Data Plane**: schema registry, contract testing, lineage catalog, event store.
* **Services**:

  * **AMSDP**: credential service, passport vault, verifier, revocation registry.
  * **AAMMPP**: item master, configuration, MRO, procurement, inventory.
  * **API Gateway**: REST/GraphQL ingress, OAuth2/OIDC.
  * **Events**: async bus for integrations and workflows.
* **Storage**: OLTP store, object storage for artifacts, append‑only audit log.
* **Integrations**: PLM/ERP/MES, certification authorities, supplier portals, operator systems.

> Diagrams and sequences: `/docs/architecture/`.

---

## Standards & Interop Targets

* **Identity & Credentials**: W3C Verifiable Credentials/Presentations.
* **Supply Chain Events**: GS1 EPCIS 2.0 + CBV.
* **Tech Pubs & Procurement**: ASD S‑Series (S1000D, S2000M).
* **Software Assurance**: SBOM (CycloneDX), SLSA provenance.
* **Lifecycle & Systems**: ISO/IEC/IEEE 15288, INCOSE guidance.
* **Aero Certification References**: DO‑178C/DO‑330, DO‑254, ARP4754A/ARP4761 (alignment targets, not declarations of compliance).

---

## Repository Layout

```
/                      # Monorepo root
/docs/                 # Documentation site and guides
/00-PROGRAM/           # Governance and engineering core
  platform/            # Executable platform (code & services)
    amsdp/             # Digital passports (issue/verify/revoke)
    aammpp/            # Item master, maintenance, procurement
    api/               # OpenAPI, GraphQL schemas, gateway config
    schemas/           # JSON/Avro/Proto contracts + tests
    clients/           # SDKs and examples
    infra/             # IaC, Docker, Helm, GH Actions
    tools/             # CLIs, generators, loaders
    llm/               # Provider-agnostic gateway, guardrails, eval
      gateway/
      embed/
      rag/
      guardrails/
      eval/
    playground-ui/     # Tenant playground (UI)
    vector/            # Vector DB adapters (pgvector, Qdrant)
    service/           # RMA, repair, requalification, RTS flows
    licensing/         # Entitlements, allocations, transfers
/01-FLEET/             # Operational data hub, MRO, federated learning
/02-AIRCRAFT/          # AIR-T baselines, domain integration, twin
/03-SPACECRAFT/        # STA baselines, domain integration, AIT/mission
/04-SATELLITES/        # Satellite product structures
/05-TELESCOPES/        # Observatory payload/domain structures
/06-PROBES/            # Deep-space probes
/07-DRONES/            # UAS/UAM product lines
/08-LAUNCHERS/         # Launch vehicles
/09-STM-SPACE-STATION-MODULES/ # Station modules/segments
/10-BUSINESS/          # Market, partnerships, finance
```

> Platform lives under `/00-PROGRAM/platform`. PLM and MRO are distributed per product under `/0X-*/…/{PLM|MRO}/`.

---

## Quickstart (Developer)

### Prerequisites

* Git, Docker, Docker Compose, Make
* Node 20+ and Python 3.11+ (tooling and SDKs)

### Bootstrap

```bash
git clone https://github.com/robbbo-t/idealeeu
cd idealeeu
make bootstrap        # install tooling, pre-commit hooks
make build            # docker compose build
make up               # docker compose up -d
make test             # run unit and contract tests
```

### Useful Targets

```bash
make up down logs lint fmt test test-contracts sbom provenance release
```

---

## Configuration

Set via environment or `.env`.

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

---

## Component Taxonomy

Canonical classes and required passport claims.

### Classes (enum)

* `primary_structure`
* `secondary_structure`
* `installation_hardware`
* `information_hardware`
* `software`
* `model`
* `firmware`
* `sensor_antenna`

### Common identifiers

* `componentClass` (enum above)
* `componentType` (controlled vocab, e.g., `wing_spar`, `fastener_rivet`, `lru_fms`, `uC_firmware`, `fem_model`, `gnss_antenna`)
* `ciId` (configuration item ID)
* `partNumber` (canonical PN)
* `serialNumber` (where applicable)
* `effectivity` (tail numbers, lots, ranges)
* `asDesignedId` • `asPlannedId` • `asBuiltId`

### Minimum passport claims by class

**primary_structure**: material spec/process; ply/stack or forging route; heat/lot; NDI results; dimensional report; CoC/CoA; stress justification ref; surface treatment.

**secondary_structure**: material/finish; lot; inspection record; CoC; torque/installation spec if relevant.

**installation_hardware**: standard ref (NAS/MS/EN/AS); grip/size/finish; lot/heat; torque/bakeout spec; CoC.

**information_hardware**: LRU model/P/N; CPU/FPGA ID; interfaces; PSU range; firmware baseline; calibration certs; environmental quals (DO‑160/EN 2282) refs.

**software**: version; build hash; target LRU(s); SBOM (CycloneDX) and SLSA provenance; safety level target (e.g., DO‑178C A–E) and approval trail.

**model**: model type (CAD/FEM/CFD/MBSE); toolchain/version; source dataset; V&V evidence; export‑control tag.

**firmware**: target device; bootloader reqs; image digest; SBOM/provenance; signing chain; rollback policy.

**sensor_antenna**: type; band; pattern/ref; calibration certificate; serial; environmental quals.

### Lifecycle states (all classes)

`draft` → `released` → `fabricated_or_loaded` → `inspected` → `installed` → `in_service` → `retired_or_scrapped`

### Relationships

Assemblies ↔ subassemblies ↔ parts via EBOM/MBOM. Serialized BOM for `asBuilt` with trace to passports and work orders.

### Schemas and location

* `/00-PROGRAM/platform/schemas/components/common/Component.v1.json` (base)
* `/00-PROGRAM/platform/schemas/components/<class>/Passport.v1.json` (per class)
* `/00-PROGRAM/platform/schemas/bom/` (EBOM/MBOM/SerializedBOM)

---

## Circularity and MRO

**Distributed model**: MRO data and procedures live under each product portfolio path, not centrally.

Portfolio placement per product:

```
/0X-*/DOMAIN_INTEGRATION/PRODUCTS/<PRODUCT>/MODELS/<MODEL>/VERSION/<Qn>/MRO/
```

Service flow:

1. **Repair order / RMA** → intake and diagnostics.
2. **Repair / rework** under approved procedures.
3. **Tests / NDI** and functional verification.
4. **Requalification / recertification** with e‑signatures and SOF.
5. **Digital passport update** and configuration state update.
6. **Release** and **return to service**; order closure.

Minimum evidence: inspection reports; NDI results; calibration certificates; firmware/software baseline; **SBOM + provenance**; hours/cycles; EBOM/MBOM impact.

Supported operations: rotable pools; controlled cannibalization; redistribution across fleets; CCB approval; segregation of duties.

EPCIS events: *Commission*, *Observation*, *Transformation*, *Aggregation* for each transition.

---

## Data Contracts

* Contracts live in `/00-PROGRAM/platform/schemas` with versioned folders.
* Compatibility policy: **backward‑compatible minor**, **breaking major**.
* Contract tests run in CI; producers and consumers must pass.

Example: minimal material passport (JSON)

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "MaterialPassport.v1",
  "type": "object",
  "required": ["materialId", "lot", "issuer", "claims"],
  "properties": {
    "materialId": {"type": "string"},
    "lot": {"type": "string"},
    "issuer": {"type": "string", "format": "uri"},
    "claims": {"type": "object"}
  }
}
```

**New contracts**

* `/00-PROGRAM/platform/schemas/service/RMA.v1.json`
* `/00-PROGRAM/platform/schemas/service/RepairOrder.v1.json`
* `/00-PROGRAM/platform/schemas/service/RequalificationReport.v1.json`
* `/00-PROGRAM/platform/schemas/service/Reintroduction.v1.json`
* `/00-PROGRAM/platform/schemas/licensing/Entitlement.v1.json`
* `/00-PROGRAM/platform/schemas/licensing/Assignment.v1.json`
* `/00-PROGRAM/platform/schemas/licensing/Transfer.v1.json`

---

## APIs

* **REST/GraphQL** via gateway. OpenAPI in `/00-PROGRAM/platform/api/openapi.yaml`. Async events in `/00-PROGRAM/platform/api/asyncapi.yaml`.

Example flow:

1. Obtain token via OIDC.
2. `POST /amsdp/v1/passports` to issue.
3. `POST /amsdp/v1/verify` with credential or reference.
4. `POST /amsdp/v1/revoke` to revoke.

**Service & Licensing endpoints**

* `POST /service/v1/rma` — create return‑material authorization
* `POST /service/v1/repairs` — register repair/rework
* `POST /service/v1/requalifications` — attach test results and approvals
* `POST /service/v1/reintroductions` — mark return‑to‑service
* `GET  /service/v1/work-orders/{id}` — status and evidence bundle
* `POST /licensing/v1/entitlements` — declare entitlements (seat/usage)
* `POST /licensing/v1/allocations` — allocate to users/orgs/projects
* `POST /licensing/v1/transfers` — governed redistribution between partners
* `GET  /licensing/v1/entitlements/{id}` — retrieve entitlement state

---

## Security Model

* Zero‑trust defaults; least‑privilege RBAC/ABAC.
* Keys managed via KMS/HSM; rotation enforced.
* Tamper‑evident append‑only audit log.
* Supply‑chain hardening: SBOM, vuln scanning, provenance attestations on releases.
* Threat modeling with STRIDE; findings tracked in `SECURITY.md`.
* **Crypto**: PQC‑ready design; see `SECURITY.md` for algorithms and status.

> This repository does **not** assert regulatory compliance. Evidence and alignment targets support audits.

---

## CI/CD

* GitHub Actions: build, lint, tests, contract tests, CodeQL, container scan.
* Release: semantic versioning, changelog, signed containers/artifacts, SBOM attach, SLSA provenance.

---

## Releases & Changelog

See `CHANGELOG.md` and GitHub Releases.

---

## LLM Playground

Multi‑tenant sandbox for trained, contextualized AI over IDEALE‑EU data.

* **Components**: `/00-PROGRAM/platform/playground-ui`, `/00-PROGRAM/platform/llm/gateway`, `/00-PROGRAM/platform/llm/embed`, `/00-PROGRAM/platform/llm/rag`, `/00-PROGRAM/platform/llm/guardrails`, `/00-PROGRAM/platform/vector`.
* **APIs**: `POST /llm/chat`, `POST /llm/embed`, `POST /knowledge/sync`, `POST /contexts`.
* **Security**: tenant/project namespaces; KMS‑backed keys; full prompt/tool/output audit.
* **Eval**: golden sets; EM/F1; groundedness; latency; cost; shadow runs.

---

## Collaborative DevOps Licensing

* Mixed seats+usage with budgets per project and phase.
* Governed redistribution of rights across program partners; traceable and expiring.
* Isolation by `{tenant}/{project}`; scopes by repo/pipeline/environment.
* Full audit of assignments and usage; only entitlement metadata shared.

---

## Deployment

### Local (Docker Compose)

```bash
docker compose up -d
```

### Images

* ghcr.io/robbbo-t/idealeeu-api:latest
* ghcr.io/robbbo-t/idealeeu-gateway:latest
* ghcr.io/robbbo-t/idealeeu-playground:latest

> Replace with your registry if different.

### Kubernetes (Helm)

```bash
# If you publish charts under your GitHub user, adjust accordingly, e.g.:
# helm repo add ideale https://robbbo-t.github.io/charts
# helm upgrade --install ideale ideale/idealeeu \
#   --namespace ideale --create-namespace \
#   -f infra/helm/values.dev.yaml
```

Readiness/liveness probes, HPA, and resource limits are defined in the Helm chart.

---

## Operations

* **Observability**: structured logs, metrics, traces. Prometheus and OTLP exporters by default.
* **Backups & DR**: PITR for databases; object store lifecycle rules.
* **Retention**: defaults in `/docs/governance/retention.md`.
* **Runbooks**: `/docs/runbooks/` for common incidents.

---

## Governance

* **CODEOWNERS** for critical paths.
* **ADRs** in `/docs/adr/` with status and decision context.
* **Change Control**: RFC issue template; review gates; affected‑system checklist.
* **Commit Convention**: Conventional Commits.

---

## Contributing

See `CONTRIBUTING.md` for setup, coding standards, commit rules, and DCO/CLA if applicable.

---

## Roadmap

* **v0.1**: Public repo, schemas, bootstrap, compose, basic AMSDP issue/verify.
* **v0.2**: AAMMPP item master, inventory, basic work orders, GraphQL façade.
* **v0.3**: EPCIS event ingest, supplier onboarding flows.
* **v1.0**: Pilot hardening, signed releases, docs and runbooks.

> Detailed milestones tracked in GitHub Projects.

---

## License

Apache‑2.0. See `LICENSE`.

---

## Security Policy

Report security issues to **[security@idealeeu.eu](mailto:security@idealeeu.eu)**. Do not file public issues. See `SECURITY.md`.

---

## Support

Questions: open a GitHub Discussion or an issue using the template.

---

## Sustainable energy systems for passenger aircraft

The platform tracks energy architectures across hydrogen, battery‑electric, SAF, and advanced propulsion. Summary below. A multi‑energy architecture proposal supports product roadmaps and certification planning.

| Energy Technology       | Description                                               | Target Aircraft / Routes        | Notes                                                                                           |
| :---------------------- | :-------------------------------------------------------- | :------------------------------ | :---------------------------------------------------------------------------------------------- |
| **Hydrogen**            | Hydrogen combustion or fuel cells. Water vapor emissions. | Short‑ to medium‑haul regional. | High infra and storage cost; lightweight tanks are the challenge. ZEROe timelines under review. |
| **Battery‑Electric**    | Batteries power electric motors.                          | Short‑haul ≤ ~500 km.           | Energy density limits; mass is the constraint. Fuel‑cell hybrids improve range.                 |
| **SAF**                 | Drop‑in bio/e‑fuels for current engines.                  | All types.                      | Scalable but feedstock‑limited. Best near‑term lever.                                           |
| **Advanced Propulsion** | Open Fan and new cores.                                   | Next‑gen fleets.                | >20% fuel‑burn/CO₂ reduction vs. current efficient engines. Compatible with SAF and future H₂.  |

**Ecosystem**

* Airports as energy hubs: ≥ 1 MW per charger; on‑site generation/storage recommended.
* Innovation: OEMs iterate platforms; startups drive radical concepts with certification risk.
* Policy: tighter CO₂ standards, jet‑fuel taxation, and R&D funding drive adoption.

**TFA mapping**: CQH, EEE, PPP, IIF.

### Technical Note: AMPAS (Multi‑Energy‑Agnostic Propulsion)

**Purpose**: integrate solid‑state batteries, liquid hydrogen (LH₂), SAF/e‑SAF, and high‑efficiency **Open Fan**.

**Functional sketch**

* **Takeoff**: batteries + H₂ fuel cells for peak power.
* **Climb/initial cruise**: transition to Open Fan on H₂ or SAF; electric assistance.
* **Cruise**: thermal mode (H₂ or SAF).
* **Descent/taxi**: partial regeneration and recharge.

**Controller**: **EDPICS** manages power flows, cryogenics, and G‑H₂ recirculation.

**Benefits**: up to **85%** CO₂/NOₓ reduction with SAF; **>95%** with green H₂. **20–25%** lower consumption vs. LEAP‑1A.

**Challenges**: thermal management (−253 °C to hot‑fuel circuits), certification baselines for hybrid‑cryogenic systems, acoustic/structural complexity of Open Fan, dual infrastructure at airports.

**Outlook**: viable for **100–200‑seat** aircraft with **transcontinental** range by **2040–2045** (subject to program risk and infra build‑out).

**References**: see numbered links in the original README for background sources.

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

### Repository Index and Navigation

**Top‑Level**: [/00‑PROGRAM](./00-PROGRAM/) · [/01‑FLEET](./01-FLEET/) · [/02‑AIRCRAFT](./02-AIRCRAFT/) · [/03‑SPACECRAFT](./03-SPACECRAFT/) · [/04‑SATELLITES](./04-SATELLITES/) · [/05‑TELESCOPES](./05-TELESCOPES/) · [/06‑PROBES](./06-PROBES/) · [/07‑DRONES](./07-DRONES/) · [/08‑LAUNCHERS](./08-LAUNCHERS/) · [/09‑STM‑SPACE‑STATION‑MODULES](./09-STM-SPACE-STATION-MODULES/) · [/10‑BUSINESS](./10-BUSINESS/)

**Reference points**: Governance → [`/00-PROGRAM/GOVERNANCE/`](./00-PROGRAM/GOVERNANCE/); Config Mgmt → [`/00-PROGRAM/CONFIG_MGMT/`](./00-PROGRAM/CONFIG_MGMT/); ECR/ECO/CCB → `06-CHANGES/` and `05-CCB/`; Digital Thread (MBSE) → `/00-PROGRAM/DIGITAL_THREAD/04-MBSE/`; Digital Twin → `/00-PROGRAM/DIGITAL_THREAD/05-DIGITAL_TWIN/`; UTCS Registry → `/00-PROGRAM/CONFIG_MGMT/10-TRACEABILITY/UTCS/`.

**Index maintenance**: automated updates with structure changes; manual review quarterly; baseline snapshots at milestones.

