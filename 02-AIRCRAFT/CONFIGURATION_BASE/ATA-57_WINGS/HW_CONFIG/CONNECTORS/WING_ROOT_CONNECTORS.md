# Wing Root Connectors

## Document Control

| Field | Value |
|-------|-------|
| Document ID | ATA-57-CONN-WR-001 |
| Type | Connector Specification |
| Revision | 1.0 |
| Date | 2026-01-08 |

## 1. Overview

This document defines electrical and hydraulic connectors at the wing root interface.

## 2. Electrical Connectors

### 2.1 Main Power Connector

#### Connector Specification
| Parameter | Value |
|-----------|-------|
| Connector Type | [Manufacturer/Series] |
| Part Number | [P/N] |
| Shell Size | [Size] |
| Contact Count | [Number] pins |
| Current Rating | [A] per contact |
| Voltage Rating | [V] |

#### Pin Assignment

| Pin | Signal Name | Wire Gauge | Function | Reference |
|-----|-------------|------------|----------|-----------|
| A | +28VDC_BUS1 | 16 AWG | Primary power | [ATA-24](../../ATA-24_ELECTRICAL_POWER/) |
| B | +28VDC_BUS2 | 16 AWG | Backup power | [ATA-24](../../ATA-24_ELECTRICAL_POWER/) |
| C | GND | 16 AWG | Power return | [ATA-92](../../ATA-92_EWIS/) |
| D | AILERON_CMD | 22 AWG | Command signal | [ATA-27](../../ATA-27_FLIGHT_CONTROLS/) |
| E | AILERON_POS | 22 AWG | Position feedback | [ATA-27](../../ATA-27_FLIGHT_CONTROLS/) |
| ... | ... | ... | ... | ... |

### 2.2 Data Bus Connector

#### Connector Specification
| Parameter | Value |
|-----------|-------|
| Connector Type | MIL-DTL-38999 Series III |
| Part Number | [P/N] |
| Shell Size | [Size] |
| Contact Count | [Number] pins |

#### Pin Assignment
| Pin | Signal Name | Function | Bus Standard |
|-----|-------------|----------|--------------|
| A | ARINC_429_HI | Data high | ARINC 429 |
| B | ARINC_429_LO | Data low | ARINC 429 |
| C | SHIELD | Shield ground | - |

## 3. Hydraulic Connectors

### 3.1 Hydraulic Supply

#### Connector Specification
| Parameter | Value |
|-----------|-------|
| Connector Type | MS33656 |
| Size | -8 (1/2") |
| Pressure Rating | 3000 PSI |
| Fluid | MIL-PRF-83282 |
| System | [ATA-29 Hydraulic System](../../ATA-29_HYDRAULIC_POWER/) |

### 3.2 Hydraulic Return

#### Connector Specification
| Parameter | Value |
|-----------|-------|
| Connector Type | MS33656 |
| Size | -10 (5/8") |
| Pressure Rating | 500 PSI |
| System | [ATA-29 Hydraulic System](../../ATA-29_HYDRAULIC_POWER/) |

## 4. Installation Requirements

### 4.1 Electrical Connector Installation
1. Inspect connector for damage
2. Apply dielectric grease to contacts
3. Align connector and engage
4. Torque coupling ring per specification: [TBD] in-lbs
5. Install safety lock wire
6. Verify continuity per [ATA-92 EWIS](../../ATA-92_EWIS/)

### 4.2 Hydraulic Connector Installation
1. Inspect O-rings and replace if damaged
2. Lubricate O-rings with compatible lubricant
3. Hand-tighten fitting
4. Torque to specification: [TBD] ft-lbs
5. Safety wire per specification
6. Perform leak check per [ATA-29](../../ATA-29_HYDRAULIC_POWER/)

## 5. Maintenance

### 5.1 Inspection Intervals
- Visual inspection: Every A-Check
- Connector cleaning: Every C-Check
- O-ring replacement: Every [TBD] flight hours

### 5.2 Inspection Criteria
- Check for corrosion
- Verify coupling ring engagement
- Check safety wire condition
- Inspect for hydraulic leaks

## 6. Related Documents

- [Control Surface Connectors](CONTROL_SURFACE_CONNECTORS.md)
- [Sensor Connectors](SENSOR_CONNECTORS.md)
- [HW_CONFIG Overview](../README.md)
- [ATA-92 EWIS](../../ATA-92_EWIS/) - Complete wiring documentation
- [ATA-29 Hydraulic Power](../../ATA-29_HYDRAULIC_POWER/)
- [ATA-27 Flight Controls](../../ATA-27_FLIGHT_CONTROLS/)

## 7. Revision History

| Revision | Date | Description | Author |
|----------|------|-------------|--------|
| 1.0 | 2026-01-08 | Initial release (Genesis) | @copilot prompted by @AmedeoPelliccia |

---

**Document Status**: Template  
**Classification**: Company Confidential
