# ATA-06 — Dimensions & Areas  
**Configuration Baseline**

This baseline defines the reference configuration for all **aircraft dimensional data, stationing, areas, zones and access/clearance definitions** under ATA Chapter 06.

---

## Scope
Covers all items required to define the aircraft external and internal geometry used for design, certification, manufacture, production, maintenance and ground handling:
- Stationing, buttock/wing/fuselage stations and waterlines  
- Reference datum definitions and coordinate system conventions  
- External dimensions (length, span, height) and area envelopes (doors, cargo bays, service zones)  
- Access and service areas, clearances and maintenance panels  
- Zones for systems routing, safety zones and fire/ventilation envelopes  
- Integration with PLM geometry references (CAD part IDs, CAD revision pointers)  

---

## Directory Overview

| Folder | Purpose |
|--------|---------|
| `01-GEOMETRY_DEFINITIONS/` | Master geometry files and coordinate frame definitions (CAD exports, STEP AP242, neutral geometry). |
| `02-STATIONING/` | Station tables, buttock/wing/fuselage waterlines, reference datums and offsets (CSV/JSON). |
| `03-AREAS_ZONES/` | Defined areas: doors, cargo bays, service areas, equipment zones, safety exclusion zones. |
| `04-ACCESS_CLEARANCES/` | Door apertures, escape routes, maintenance access clearances and tooling interfaces. |
| `05-IDENTIFICATION/` | Baseline identification, CMP references and ESG notes. |
| `06-REVISIONS/` | Revision history and linked ECNs (CMP-controlled). |

---

## Configuration Items
| CI ID | Description | Owner | Source |
|-------|-------------|-------|--------|
| `ATA-06/BL-2025.10` | Dimensions & Areas baseline | CMP / Geometry Lead | `05-IDENTIFICATION/IDENTIFICATION_CARD.json` |
| `ECN-2025-06-001` | Initial ATA-06 baseline creation | CMP | `06-REVISIONS/ECN-2025-06-001.json` |

---

## Conventions & Notes
- **Coordinate system**: Right-handed aircraft coordinate system. Origin defined at datum plane. Documented in `01-GEOMETRY_DEFINITIONS/reference_datum.md`.  
- **Units**: SI units (mm for lengths). Any non-SI must be explicitly called out.  
- **Stationing**: Use fuselage station (FS), buttock line (BL) and waterline (WL) conventions documented in `02-STATIONING/`.  
- **CAD linkage**: All geometry items must reference CAD part IDs and STEP AP242 exports, with EBOM mappings where applicable.  
- **Access definitions**: Define minimum clearances for maintenance tasks and ground handling. Link these to ATA-05 maintenance tasks where relevant.  
- **Change control**: Any change to dimensional baselines must follow CMP change process. Coordinate with PLM and Production Engineering for downstream impact.

---

## Compliance References
- **ATA iSpec 2200 / iSpec 42** — Data exchange and electronic tech data standards  
- **S1000D** — Structured data modules (where used for maintenance or dimensional data)  
- **ASME Y14.5** — GD&T conventions (where applicable for manufacturing-critical features)  
- **EASA CS-25 / FAA 14 CFR Part 25** — Certification implications for dimensions and envelope definitions  
- **IDEALE-EU CMP-STD-1001** — Configuration and baseline management

---

## Version Control
All modifications follow CMP governance. Each revision must update:
- `REVISION_HISTORY.yaml` in `06-REVISIONS/`  
- Linked ECN JSON record  
- `baselineId` and `date` in `05-IDENTIFICATION/IDENTIFICATION_CARD.json`

---

**Baseline Owner:** `CMP Lead — ATA-06`  
**Date:** 2025-10-24  
**Status:** Active (Baseline 1.0)


## Key Interfaces

- **ATA-92**: EWIS (all wiring)

## Related Documents

- [Configuration Rules](../ATA-00_GENERAL/RULES.md)
- [Global Change Log](../ATA-00_GENERAL/GLOBAL_CHANGE_LOG.csv)

## Contacts

- **System Owner**: Systems Engineering
- **Configuration Owner**: Configuration Management

---

**Last Updated**: 2024-01-15
