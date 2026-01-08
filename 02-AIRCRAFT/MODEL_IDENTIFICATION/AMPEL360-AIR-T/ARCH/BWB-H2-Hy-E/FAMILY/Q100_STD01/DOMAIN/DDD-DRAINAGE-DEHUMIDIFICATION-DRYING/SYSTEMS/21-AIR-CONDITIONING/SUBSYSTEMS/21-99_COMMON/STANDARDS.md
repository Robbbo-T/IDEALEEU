# ATA-21 Air Conditioning Standards — 21-99_COMMON

## Purpose
This document defines common standards, conventions, and requirements for all ATA-21 Air Conditioning subsystems within the DDD domain.

## Naming Conventions

### Parts and Assemblies
- Format: `{ATA}-{NN}-{XXX}` where:
  - `{ATA}` = ATA chapter (21)
  - `{NN}` = Subsystem code (10-90)
  - `{XXX}` = Sequential part number (001-999)
- Example: `21-10-001` (First part in PACKS_AND_REFRIGERATION)

### Subsystems
- Format: `{ATA}-{NN}_{DESCRIPTION}`
- Use underscores for multi-word descriptions
- All caps for description portion
- Example: `21-10_PACKS_AND_REFRIGERATION`

## Units and Measurements

### Standard SI Units
All measurements must use SI units unless explicitly documented as exceptions:

- **Length:** mm (millimeters)
- **Temperature:** °C (Celsius) or K (Kelvin)
- **Pressure:** kPa (kilopascals)
- **Mass:** kg (kilograms)
- **Power:** kW (kilowatts)
- **Flow Rate:** kg/s (kilograms per second) or m³/s
- **Energy:** kWh (kilowatt-hours) or J (joules)

### Temperature Conversions
When using Kelvin:
- Standard day: 288.15 K (15°C)
- Cabin target: 293.15 K (20°C)
- Cryogenic (LH2): 20 K (-253.15°C)

## File Formats

### CAD Models
- **Primary:** STEP AP242 with PMI (Product Manufacturing Information)
- **Export Recipe:** Include `export_recipe.txt` describing export parameters
- **Thumbnails:** PNG or JPEG, max 1920×1080 px
- **Naming:** `{part_id}-{description}_R{revision}.step`

### CAE Models
- **Mesh:** ANSYS .cdb, OpenFOAM mesh, or equivalent
- **Results:** JSON format for metrics
- **Baseline:** `baseline/metrics.json` with standard keys:
  - `mass` (kg)
  - `energy_kwh` (kWh)
  - `peak_temp_C` (°C)
  - `mass_flow_kg_s` (kg/s)
  - `pressure_drop_kPa` (kPa)

### Documentation
- **Maintenance:** S1000D XML or equivalent structured format
- **Performance:** CSV or JSON for tabular data
- **Reports:** Markdown (.md) or PDF

## Metadata Requirements

### Required Fields (TEMPLATE_METADATA.yaml)
- `part_id`: Unique identifier
- `description`: Human-readable description
- `revision`: Revision code (R001, R002, etc.)
- `author`: Responsible engineer
- `cad_system`: CAD software used
- `cad_version`: Software version
- `file_name`: Primary file name
- `units`: Units dictionary
- `ebom_id`: Engineering BOM identifier
- `mass_kg`: Component mass
- `approval_status`: DRAFT | REVIEW | APPROVED | OBSOLETE
- `last_updated`: ISO date (YYYY-MM-DD)

## Design Standards

### Dehumidification Performance
- Target cabin humidity: 40-50% RH
- Condensate removal capacity: TBD kg/h
- Operating altitude: 0-45,000 ft
- Cabin pressure: 75-101 kPa

### Air Distribution
- Temperature uniformity: ±3°C cabin-wide
- Airflow rates: Per DO-160G environmental standards
- Noise levels: <65 dBA at passenger locations

### Pressurization
- Max cabin altitude: 8,000 ft (2,438 m) equivalent
- Pressure rate of change: <500 ft/min (2.5 m/s)
- Emergency descent: Per CS-25 requirements

## Quality and Compliance

### CI/QA Gates
Each subsystem CAE must include:
1. Smoke test executable in CI pipeline
2. `baseline/metrics.json` with all required keys
3. Validation against previous baseline (regression check)

### Configuration Management
- All changes require ECR (Engineering Change Request)
- Approval via ECO (Engineering Change Order)
- Baseline updates tracked in `00-PROGRAM/CONFIG_MGMT`
- UTCS traceability mandatory for all deliverables

### Verification and Validation
- Design verification: Analysis + bench test
- Validation: Ground test + flight test (as applicable)
- Documentation: V&V reports in `VALIDATION/` folder

## Interface Standards

### Electrical
- Power: 28 VDC or 115 VAC 400 Hz
- Signals: ARINC 429, CAN bus, or discrete
- EMI/EMC: Per DO-160G Section 20-21

### Mechanical
- Mounting: ISO metric fasteners
- Sealing: Per AS3578 or MIL-G-5514
- Materials: Aluminum alloys (2024, 7075), composites, titanium

### Fluid
- Air connections: MS fittings or equivalent
- Pressure ratings: 1.5× max operating pressure
- Leak rate: <1 SCCM at max pressure

## References

### Primary Standards
- **ATA Spec 100:** Air Transport Association numbering
- **CS-25 / FAR Part 25:** Certification requirements
- **DO-160G:** Environmental conditions and test procedures
- **S1000D:** Technical publications specification
- **STEP AP242:** CAD data exchange standard

### Internal References
- Configuration Management: `00-PROGRAM/CONFIG_MGMT`
- UTCS Traceability: `00-PROGRAM/CONFIG_MGMT/10-TRACEABILITY/UTCS`
- System Interfaces: `../INTERFACE_MATRIX`

## Revision History

| Revision | Date       | Author           | Changes                |
|----------|------------|------------------|------------------------|
| R001     | 2025-10-24 | Systems Lead ATA-21 | Initial release       |

**Owner:** Systems Lead — ATA-21  
**Contact:** systems-ddd@idealeeu.eu  
**Status:** DRAFT
