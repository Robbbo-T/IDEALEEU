# 02-DATA_MODULES

## Purpose
Source Data Modules (DMCs) defining individual maintenance requirements and procedures.

## Overview
This directory contains the canonical S1000D Data Modules that define all maintenance requirements, intervals, and procedures for time-limited tasks and periodic checks under ATA Chapter 05.

## Data Module Structure
Each Data Module follows S1000D Issue 5.0 structure with:
- **DMC (Data Module Code)**: Unique identifier per S1000D schema
- **DMTitle**: Descriptive title of the maintenance requirement
- **Info Code**: Type of information (procedural, descriptive, fault isolation)
- **Issue Date**: Publication date and version
- **Applicability**: Aircraft models, serial number ranges, effectivity

## Content Types
### Procedural Data Modules
- Step-by-step maintenance procedures
- Inspection criteria and acceptance standards
- Calibration and test procedures
- Rigging and adjustment instructions

### Descriptive Data Modules
- Component identification and location
- System descriptions relevant to maintenance
- Servicing specifications
- Troubleshooting decision trees

### Scheduled Maintenance
- Calendar-based interval definitions
- Flight-hour-based interval definitions
- Cycle-based interval definitions
- Condition-based monitoring thresholds

## S1000D Compliance
- **Data Module Identification**: DMC-{Model}-{System}-{SubSystem}-{Type}-{Variant}-{Item}
- **XML Schema**: S1000D Issue 5.0 compliant XML
- **Common Source Database (CSDB)**: Integrated with publication pipeline
- **Technical Publications**: Export to PDF, HTML, IETP formats

## Integration
- **AAMMPP**: Maintenance planning and scheduling system
- **CMP**: Configuration Management Program
- **Digital Twin**: Maintenance event correlation
- **ESG Tracking**: Environmental impact per procedure

## Versioning
All Data Modules follow configuration control:
- Version tracked in DMC issue number
- Changes require ECN approval
- Baseline references in `03-IDENTIFICATION/`

## Compliance References
- **S1000D Issue 5.0**: International specification for technical publications
- **ASD S1000D**: Aerospace and Defence Industries Association of Europe
- **MSG-3**: Maintenance Steering Group logic (where applicable)

## Data Module Inventory

This directory contains the following S1000D Data Modules:

```
02-DATA_MODULES/
├── README.md
├── DMC-ATA_05-01-10-00-00-00-A-001-01.xml
├── DMC-ATA_05-01-20-00-00-00-A-002-01.xml
└── DMC-ATA_05-01-30-00-00-00-A-010-01.xml
```

### Data Module Details

| Data Module Code | Title | Description | Issue |
|-----------------|-------|-------------|-------|
| DMC-ATA_05-01-10-00-00-00-A-001-01.xml | Scheduled Maintenance Intervals | Defines calendar-, flight-hour-, cycle-, and condition-based maintenance intervals | 001-01 |
| DMC-ATA_05-01-20-00-00-00-A-002-01.xml | A/B/C/D Check Requirements | Details the scope, frequency, and requirements for major periodic maintenance checks | 001-01 |
| DMC-ATA_05-01-30-00-00-00-A-010-01.xml | Time Limits and Life Limits | Specifies mandatory time and life limits for safety-critical and life-limited components | 001-01 |

### DMC Naming Convention

The Data Module Codes follow S1000D standard naming:
- **Model Ident**: ATA_05 (ATA Chapter 05)
- **System Diff**: 01 (Standard configuration)
- **System Code**: 10, 20, 30 (Maintenance interval types)
- **Sub-system/Assy/Disassy**: 00-00-00 (General)
- **Disassy Code Variant**: A (Standard variant)
- **Info Code**: 001, 002, 010 (Information type)
- **Info Code Variant**: 01 (Standard issue)
- **Item Location**: A (Standard location)

### Usage

These Data Modules provide the technical foundation for:
1. **AAMMPP Integration**: Automated maintenance scheduling and work order generation
2. **Digital Passport Updates**: Component lifecycle tracking via AMSDP
3. **ESG Reporting**: Environmental and sustainability metrics per maintenance activity
4. **Regulatory Compliance**: Alignment with EASA/FAA continuing airworthiness requirements

## Status
Active — Baseline 1.0

## Contacts
- **Owner**: Technical Publications / CMP
- **Approver**: CMP Lead — ATA-05
- **Reviews**: CCB quarterly

---
**Last Updated**: 2025-10-24
