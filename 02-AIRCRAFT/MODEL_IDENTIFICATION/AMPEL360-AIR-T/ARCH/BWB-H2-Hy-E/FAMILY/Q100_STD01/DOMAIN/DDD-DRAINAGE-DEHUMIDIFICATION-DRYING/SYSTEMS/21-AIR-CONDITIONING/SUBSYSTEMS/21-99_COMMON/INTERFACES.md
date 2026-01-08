# ATA-21 System-Level Interfaces — 21-99_COMMON

## Purpose
This document defines system-level interfaces for ATA-21 Air Conditioning that apply across all subsystems. Subsystem-specific interfaces are documented in each subsystem's `INTERFACES/INTERFACES.md`.

## Overview
The ATA-21 Air Conditioning system interfaces with multiple aircraft systems to provide environmental control for the cabin and equipment bays.

## External System Interfaces

### ATA-24: Electrical Power
- **Interface Type:** Electrical
- **Description:** Power supply for ECS components
- **Specifications:**
  - Primary: 115 VAC, 400 Hz, 3-phase
  - Secondary: 28 VDC
  - Power consumption: TBD kW (peak), TBD kW (cruise)
- **Interface Control Document:** ICD-21-24-001
- **Status:** DRAFT

### ATA-28: Fuel System (H2 Cryogenics)
- **Interface Type:** Thermal/Mechanical
- **Description:** Heat rejection to LH2 tanks for heat exchanger cooling
- **Specifications:**
  - Heat load: TBD kW
  - Temperature interface: -253°C to +20°C
  - Flow rates: TBD kg/s
- **Interface Control Document:** ICD-21-28-001
- **Status:** DRAFT

### ATA-31: Instruments
- **Interface Type:** Data
- **Description:** Sensor data for cabin pressure, temperature, humidity
- **Specifications:**
  - Protocol: ARINC 429
  - Data rate: 12.5 kbps or 100 kbps
  - Update rate: 1-10 Hz (sensor dependent)
- **Interface Control Document:** ICD-21-31-001
- **Status:** DRAFT

### ATA-32: Landing Gear
- **Interface Type:** Logical/Control
- **Description:** Weight-on-wheels signal for ground/flight mode selection
- **Specifications:**
  - Signal type: Discrete (ground/flight)
  - Voltage: 28 VDC discrete
- **Interface Control Document:** ICD-21-32-001
- **Status:** DRAFT

### ATA-36: Pneumatic
- **Interface Type:** Fluid/Mechanical
- **Description:** Bleed air supply for ECS (if applicable; BWB may use electric)
- **Specifications:**
  - Pressure: TBD kPa
  - Temperature: TBD °C
  - Flow rate: TBD kg/s
- **Interface Control Document:** ICD-21-36-001
- **Status:** DRAFT
- **Note:** BWB-H2-Hy-E may use all-electric ECS; verify architecture

### ATA-49: APU
- **Interface Type:** Fluid/Electrical
- **Description:** APU bleed air or electrical power for ground operations
- **Specifications:**
  - Ground power: 115 VAC, 400 Hz
  - Bleed air: TBD kPa, TBD °C (if used)
- **Interface Control Document:** ICD-21-49-001
- **Status:** DRAFT

### ATA-73/75: Engine Systems
- **Interface Type:** Fluid/Thermal
- **Description:** Engine bleed air or thermal interface (architecture dependent)
- **Specifications:**
  - TBD based on propulsion system (H2 fuel cell or turbine)
- **Interface Control Document:** ICD-21-73-001
- **Status:** DRAFT

## Internal Subsystem Interfaces

### 21-10 ↔ 21-20: Packs to Air Distribution
- **Interface:** Conditioned air outlet from packs to distribution ducts
- **Specifications:**
  - Temperature: TBD °C
  - Pressure: TBD kPa
  - Flow rate: TBD kg/s

### 21-20 ↔ 21-30: Air Distribution to Pressurization
- **Interface:** Cabin inflow and outflow valve coordination
- **Specifications:**
  - Control signals: ARINC 429 or discrete
  - Pressure regulation: 75-101 kPa cabin

### 21-60 ↔ 21-80: Dehumidifiers to Water Separators
- **Interface:** Condensate drainage and water management
- **Specifications:**
  - Condensate flow: TBD kg/h
  - Drainage path: Gravity or pump-assisted

### 21-70 ↔ 21-10: Heat Exchangers to Packs
- **Interface:** Heat rejection from refrigeration cycle
- **Specifications:**
  - Heat load: TBD kW
  - Coolant: Air, glycol, or LH2 (architecture dependent)

### 21-90 ↔ All Subsystems: Sensors/Actuators
- **Interface:** Sensing and control for all ECS subsystems
- **Specifications:**
  - Sensor types: Temperature, pressure, humidity, flow
  - Actuator types: Valves, dampers, pumps
  - Communication: ARINC 429, CAN, discrete

## Interface Matrix Summary

| Subsystem | External Interfaces | Internal Interfaces | Critical Dependencies |
|-----------|---------------------|---------------------|----------------------|
| 21-10 | ATA-24, ATA-28 | 21-20, 21-70, 21-90 | Electrical power, cooling |
| 21-20 | — | 21-10, 21-30, 21-50, 21-90 | Conditioned air supply |
| 21-30 | ATA-31, ATA-32 | 21-20, 21-90 | Weight-on-wheels, sensors |
| 21-40 | ATA-31, ATA-24 | All subsystems | Control and monitoring |
| 21-50 | — | 21-20, 21-80, 21-90 | Air distribution |
| 21-60 | — | 21-80, 21-90 | Condensate removal |
| 21-70 | ATA-28 | 21-10, 21-90 | Heat rejection sink |
| 21-80 | — | 21-60, 21-90 | Water drainage |
| 21-90 | ATA-31 | All subsystems | Sensing and control |

## Interface Development Process

### Documentation Requirements
1. Each interface must have a unique ICD number
2. ICDs must include:
   - Functional description
   - Physical specifications
   - Electrical/mechanical drawings
   - Data formats and protocols
   - Test and verification requirements
3. ICDs must be reviewed and approved via ECR/ECO process

### Change Management
- Interface changes are high-risk and require cross-functional review
- Affected subsystems must be notified via CCB (Configuration Control Board)
- Regression testing required for interface modifications

## References

### Internal Documents
- System architecture: `../INTEGRATION_VIEW.md`
- Subsystem interfaces: See each subsystem's `INTERFACES/INTERFACES.md`
- Standards: `21-99_COMMON/STANDARDS.md`

### External Standards
- ARINC 429: Digital data bus standard
- DO-160G: Environmental testing
- CS-25: Certification specifications

## Contacts
See `21-99_COMMON/CONTACTS.md` for interface points of contact.

**Owner:** Systems Lead — ATA-21  
**Contact:** systems-ddd@idealeeu.eu  
**Last Updated:** 2025-10-24  
**Status:** DRAFT
