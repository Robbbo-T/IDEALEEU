# SUBSYSTEM: 21-10_PACKS_AND_REFRIGERATION

**Under System:** 21-AIR-CONDITIONING • **Architecture:** BWB-H2-Hy-E • **Domain:** DDD-DRAINAGE-DEHUMIDIFICATION-DRYING

## Purpose

Unidades de refrigeración / packs (incl. ciclo sCO₂ o refrigeración por compresión). Gestiona los paquetes de acondicionamiento de aire y sistemas de refrigeración para control ambiental de cabina.

## Folder Contract

- `PLM/CAx/*` → design / reports / MOCs
- `PLM/EBOM_LINKS.md` → packaging / on & off-board bundles
- `CAE/` → simulation cases, smoke tests, baseline metrics
- `CAD/` → STEP AP242 geometry with PMI
- `MAINTENANCE_TASKS/` → S1000D work packages
- `PERFORMANCE/` → capacity curves, energy consumption data
- `VALIDATION/` → test plans and bench reports
- `INTERFACES/` → ICDs with other systems
- `META.json` + `inherit.json` → CAD/CAE/CAM only here

## Deliverables

1. EBOM mapping with part identification
2. CAD models in STEP AP242 format
3. CAE smoke test with baseline/metrics.json
4. Maintenance procedures (S1000D)
5. Performance tables and curves
6. Validation test reports
7. Interface control documents

## Rules

- **Verification:** see `README.md` + template provenance
- Contribute following CM: ECR → ECO → baselines + ICDs → *.
- Add docs & tests before models or code.

> Owner: Systems Lead — ATA-21 • Status: scaffold • Year: 2025
