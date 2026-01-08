# 04-REVISIONS

## Purpose
Controlled change history and Engineering Change Notices for ATA-05 Configuration Baseline.

## Overview
This directory maintains the complete revision history of the ATA-05 Time Limits and Maintenance Checks configuration baseline, including all approved Engineering Change Notices (ECNs) and their impact documentation.

## Contents

### REVISION_HISTORY.yaml
Chronological record of all baseline revisions:
- Revision number and date
- Description of changes
- ECN references
- Approving authority
- Effectivity dates
- Impact summary

### Engineering Change Notices (ECNs)
Individual ECN records in JSON format following CMP change control procedures:
- ECN identifier
- Originator and date
- Problem statement
- Proposed solution
- Affected configuration items
- Impact assessment
- Approval signatures
- Implementation status

## Change Control Process
1. **Initiate**: ECN created in `00-PROGRAM/CONFIG_MGMT/06-CHANGES/05-ECR/`
2. **Review**: CCB evaluation and impact analysis
3. **Approve**: CCB decision and signature
4. **Document**: ECN record created in this directory
5. **Update**: REVISION_HISTORY.yaml updated
6. **Implement**: Changes applied to baseline
7. **Close**: ECN marked complete

## Naming Convention
ECN files follow the pattern: `ECN-{YYYY}-{NNNNN}.json`
- YYYY: Year
- NNNNN: Sequential number

Example: `ECN-2025-05123.json`

## Integration
- **CMP Changes**: Links to `00-PROGRAM/CONFIG_MGMT/06-CHANGES/`
- **CCB Records**: References `00-PROGRAM/CONFIG_MGMT/05-CCB/`
- **Baseline ID**: Updates `03-IDENTIFICATION/IDENTIFICATION_CARD.json`
- **Traceability**: UTCS anchors maintained

## Compliance
- **IDEALE-EU CMP-STD-1001**: Change control procedures
- **ISO 9001**: Quality management system requirements
- **AS9100**: Aerospace quality management
- **Configuration Management**: Industry best practices

## Retention
All revision records are permanent and maintained per:
- Regulatory requirements (minimum 10 years)
- Type certification data retention
- Audit trail requirements

## Status
Active — Baseline 1.0

## Contacts
- **Owner**: CMP Lead — ATA-05
- **CCB Authority**: Configuration Control Board
- **Change Coordinator**: CM Office

---
**Last Updated**: 2025-10-24
