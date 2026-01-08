# Aileron Actuator - Technical Specifications

## Document Control

| Field | Value |
|-------|-------|
| Document ID | ATA-57-LRU-AA-SPEC-001 |
| Revision | 1.0 |
| Date | 2026-01-08 |
| Status | Active |
| Owner | Systems Engineering |

## 1. General Information

### 1.1 LRU Identification
- **LRU Name**: Aileron Actuator
- **ATA Chapter**: 57 - Wings
- **Function**: Roll control actuation
- **Type**: Hydraulic/Electric linear actuator
- **Location**: Wing aileron hinge line

### 1.2 Applicable Aircraft
- Model: [Aircraft Model]
- Configuration: [Configuration ID]
- Effectivity: [Effectivity Range]

## 2. Performance Specifications

### 2.1 Operational Parameters
| Parameter | Value | Units | Tolerance |
|-----------|-------|-------|-----------|
| Maximum Force | TBD | N | ±5% |
| Maximum Stroke | TBD | mm | ±2mm |
| Maximum Velocity | TBD | mm/s | ±10% |
| Response Time | TBD | ms | ±50ms |
| Operating Pressure | TBD | bar | ±5% |
| Operating Voltage | 28 | VDC | ±4V |

### 2.2 Environmental Specifications
| Parameter | Minimum | Maximum | Units |
|-----------|---------|---------|-------|
| Operating Temperature | -55 | +71 | °C |
| Storage Temperature | -55 | +85 | °C |
| Altitude | 0 | 50,000 | ft |
| Humidity | 0 | 95 | %RH |
| Vibration | - | Per DO-160 | - |
| Shock | - | Per DO-160 | - |

## 3. Physical Characteristics

### 3.1 Dimensions
| Dimension | Value | Units |
|-----------|-------|-------|
| Length (extended) | TBD | mm |
| Length (retracted) | TBD | mm |
| Diameter | TBD | mm |
| Weight | TBD | kg |

## 4. Interface Specifications

### 4.1 Mechanical Interfaces
- **Upper Attachment**: [Interface specification]
- **Lower Attachment**: [Interface specification]
- **Mounting Hardware**: See [Installation Manual](INSTALLATION.md)

### 4.2 Electrical Interfaces
- **Connector Type**: [Connector P/N]
- **Pinout**: See [Connector Documentation](../CONNECTORS/CONTROL_SURFACE_CONNECTORS.md)
- **Wiring**: Reference [ATA-92 EWIS](../../ATA-92_EWIS/)

### 4.3 Hydraulic Interfaces
- **Port Size**: [Size specification]
- **Fluid Type**: [Fluid specification per [ATA-29](../../ATA-29_HYDRAULIC_POWER/)]
- **Pressure**: [Operating pressure range]

## 5. Related Documents

### 5.1 Component Documentation
- [Installation Manual](INSTALLATION.md)
- [Part Numbers](PART_NUMBERS.csv)
- [Test Procedures](TEST_PROCEDURES.md)
- [LRU Overview](README.md)

### 5.2 Aircraft Component Manuals
- [Master ACM](ACM/ACM_AILERON_ACTUATOR.md)
- [Component Breakdown](ACM/COMPONENT_BREAKDOWN.md)
- [Maintenance Manual](ACM/MAINTENANCE_MANUAL.md)
- [Illustrated Parts Catalog](ACM/ILLUSTRATED_PARTS_CATALOG.md)
- [Troubleshooting Guide](ACM/TROUBLESHOOTING_GUIDE.md)

### 5.3 Subcomponents
- [Actuator Motor](SUBCOMPONENTS/ACTUATOR_MOTOR.md)
- [Control Valve](SUBCOMPONENTS/CONTROL_VALVE.md)
- [Position Sensor](SUBCOMPONENTS/POSITION_SENSOR.md)
- [Mounting Brackets](SUBCOMPONENTS/MOUNTING_BRACKETS.md)

### 5.4 System Documentation
- [ATA-27 Flight Controls](../../ATA-27_FLIGHT_CONTROLS/)
- [ATA-29 Hydraulic Power](../../ATA-29_HYDRAULIC_POWER/)
- [ATA-92 EWIS](../../ATA-92_EWIS/)

### 5.5 Configuration Management
- [HW_CONFIG Overview](../README.md)
- [Configuration Rules](../../ATA-00_GENERAL/RULES.md)
- [Part Numbering](../../../../00-PROGRAM/CONFIG_MGMT/02-PART_NUMBERING.md)

## 6. Revision History

| Revision | Date | Description | Author |
|----------|------|-------------|--------|
| 1.0 | 2026-01-08 | Initial release (Genesis) | @copilot prompted by @AmedeoPelliccia |

---

**Document Status**: Template - To be populated with actual data  
**Classification**: Company Confidential
