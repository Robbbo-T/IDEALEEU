# CMP References — ATA-05 Time Limits and Maintenance Checks

## Configuration Management Program Reference Document

**Baseline ID**: ATA-05/BL-2025.10  
**Version**: 1.0  
**Date**: 2025-10-24  
**Status**: Active

---

## 1. Overview

This document establishes the Configuration Management Program (CMP) framework for ATA-05 Time Limits and Maintenance Checks, ensuring compliance with IDEALE-EU CMP-STD-1001 and industry best practices.

---

## 2. CMP-STD-1001 Compliance Matrix

| Requirement ID | Description | Implementation | Status |
|----------------|-------------|----------------|--------|
| CMP-1001-01 | Configuration Identification | IDENTIFICATION_CARD.json with unique baseline ID | ✅ Compliant |
| CMP-1001-02 | Configuration Control | CCB approval required for all changes | ✅ Compliant |
| CMP-1001-03 | Configuration Status Accounting | REVISION_HISTORY.yaml tracking | ✅ Compliant |
| CMP-1001-04 | Configuration Audit | Quarterly CCB reviews scheduled | ✅ Compliant |
| CMP-1001-05 | Traceability | UTCS anchors for all artifacts | ✅ Compliant |
| CMP-1001-06 | ESG Integration | ESG_DECLARATION.md per task category | ✅ Compliant |
| CMP-1001-07 | S1000D Integration | Data modules per S1000D Issue 5.0 | ✅ Compliant |
| CMP-1001-08 | Change Management | ECN process with 04-REVISIONS/ | ✅ Compliant |

---

## 3. CCB Approval History

### Initial Baseline Creation
- **ECN**: ECN-2025-05123
- **Date**: 2025-10-24
- **Description**: Establish ATA-05 baseline structure per new CMP framework
- **Status**: Approved
- **Approvers**: CMP Lead — ATA-05 (initial approval; full CCB review pending)

### Future Changes
All future changes will be documented here following CCB approval.

---

## 4. Change Control Procedures

### 4.1 Change Request Process
1. **Initiate**: Submit ECR to `/00-PROGRAM/CONFIG_MGMT/06-CHANGES/05-ECR/`
2. **Classify**: Determine change category (minor, major, emergency)
3. **Analyze**: Impact assessment on maintenance tasks, schedules, ESG
4. **Review**: CCB evaluation within 14 days (target: 7 days by 2027)
5. **Approve/Reject**: CCB decision with rationale
6. **Implement**: If approved, create ECN and update baseline
7. **Verify**: Post-implementation verification
8. **Close**: Document lessons learned

### 4.2 Emergency Changes
- **Trigger**: Safety-critical issue requiring immediate action
- **Authority**: Chief Engineer can authorize emergency change
- **Ratification**: CCB review within 48 hours post-implementation
- **Documentation**: Full ECN created retroactively

### 4.3 Change Categories

| Category | Definition | Approval Authority | Timeline |
|----------|------------|-------------------|----------|
| Minor | No impact on safety, schedule, or cost | CMP Lead — ATA-05 | 3 days |
| Major | Impacts safety, schedule, cost, or interfaces | Full CCB | 14 days |
| Emergency | Immediate safety or regulatory action required | Chief Engineer + CCB ratification | 24 hrs |

---

## 5. Interface with Other ATA Chapters

### 5.1 Direct Interfaces
| ATA Chapter | Interface Description | Coordination Point |
|-------------|----------------------|-------------------|
| ATA-04 | Airworthiness Limitations references time limits | Shared maintenance intervals |
| ATA-06 | Dimensions/Areas impact maintenance access | Maintenance task procedures |
| ATA-12 | Servicing intervals coordinated with checks | Scheduled maintenance alignment |
| ATA-20 | Standard Practices applied in all tasks | Common maintenance procedures |
| ATA-45 | Central Maintenance System schedules checks | AAMMPP integration |

### 5.2 Indirect Interfaces
All ATA chapters that contain maintenance-required systems interface through the scheduling and execution of A/B/C/D checks.

---

## 6. Traceability to Requirements

### 6.1 Regulatory Requirements
| Requirement | Source | Implementation |
|-------------|--------|----------------|
| Instructions for Continued Airworthiness | CS-25.1529 / Part 25.1529 | 02-DATA_MODULES/ S1000D procedures |
| Maintenance Program | CS-25 Subpart E | A/B/C/D check structure |
| Record Keeping | CS-25.1529(c) | REVISION_HISTORY.yaml + AAMMPP |

### 6.2 UTCS Traceability
All artifacts in this baseline are anchored to UTCS (Universal Traceability Coordinate System):

**Root Anchor**: `utcs://idealeeu.eu/02-AIRCRAFT/CONFIG_BASE/ATA-05/BL-2025.10`

**Sub-Anchors**:
- Maintenance Tasks: `utcs://idealeeu.eu/02-AIRCRAFT/CONFIG_BASE/ATA-05/BL-2025.10/TASKS`
- Data Modules: `utcs://idealeeu.eu/02-AIRCRAFT/CONFIG_BASE/ATA-05/BL-2025.10/DMC`
- ESG Declaration: `utcs://idealeeu.eu/02-AIRCRAFT/CONFIG_BASE/ATA-05/BL-2025.10/ESG`
- Revisions: `utcs://idealeeu.eu/02-AIRCRAFT/CONFIG_BASE/ATA-05/BL-2025.10/REV`

### 6.3 Requirements Traceability Matrix
Full RTM maintained in: `/00-PROGRAM/CONFIG_MGMT/10-TRACEABILITY/UTCS/`

---

## 7. Integration with AAMMPP

### 7.1 Maintenance Planning
- **Data Flow**: S1000D Data Modules → AAMMPP maintenance planning module
- **Scheduling**: AAMMPP generates work orders based on calendar/FH/cycle triggers
- **Execution**: Work packages from 01-MAINTENANCE_TASKS/ executed via AAMMPP
- **Recording**: Completion data flows back to configuration state

### 7.2 Configuration State
- **As-Maintained**: AAMMPP records reflect actual maintenance performed
- **Baseline Comparison**: Deviations trigger review process
- **Effectivity**: Serial number effectivity tracked per maintenance action

---

## 8. S1000D Integration

### 8.1 Data Module Management
- **CSDB**: Common Source Database for all ATA-05 data modules
- **Publication**: Automated export to PDF, HTML, IETP formats
- **Version Control**: Data Module Code (DMC) includes issue number
- **Applicability**: Data modules tagged with aircraft model/effectivity

### 8.2 Maintenance Task Coding
Standard DMC structure for ATA-05:
```
DMC-{ModelCode}-{ATA-05}-{SubSystem}-{InfoCode}-{Variant}-{Item}-{Issue}
```

Example: `DMC-AMPEL360-05-00-00-00A-A_CHECK_PROCEDURES-001-01`

---

## 9. Quality Assurance

### 9.1 Reviews
| Review Type | Frequency | Participants | Deliverables |
|-------------|-----------|--------------|--------------|
| Technical Review | Per ECN | Subject matter experts | Technical approval memo |
| CCB Review | Monthly (or as-needed) | CCB members | CCB meeting minutes |
| Quarterly Audit | Quarterly | CM Office + QA | Audit report with findings |
| Annual Assessment | Annual | Executive leadership | Annual CM performance report |

### 9.2 Metrics
- **Configuration Accuracy**: Target 99.5%, measured quarterly
- **Change Processing Time**: Target 7 days average by 2027
- **UTCS Completeness**: Target 99%, measured monthly
- **Audit Findings**: Target <5 open findings

---

## 10. Training and Competency

### 10.1 Required Training
All personnel working with ATA-05 baseline must complete:
- CMP-STD-1001 fundamentals
- S1000D basics (for technical authors)
- UTCS traceability system
- ECN/ECO process
- AAMMPP maintenance planning module

### 10.2 Competency Assessment
- **Frequency**: Annual
- **Method**: Knowledge check + practical assessment
- **Records**: Training records in HR system + AAMMPP

---

## 11. Audit and Compliance

### 11.1 Internal Audits
- **Frequency**: Quarterly
- **Scope**: Configuration accuracy, process compliance, UTCS traceability
- **Auditor**: CM Office
- **Findings**: Tracked to closure in `/00-PROGRAM/CONFIG_MGMT/11-AUDITS/`

### 11.2 External Audits
- **Frequency**: Annual (minimum)
- **Auditors**: Regulatory authorities (EASA, FAA), customer audits
- **Preparation**: Pre-audit checklist and evidence packages
- **Response**: Corrective action plans for findings

### 11.3 Certification Authorities
- **Type Certification**: ATA-05 data supports Type Certificate Data Sheet
- **Production Certificates**: Baseline used for production approval
- **Continued Airworthiness**: Ongoing compliance demonstration

---

## 12. Continuous Improvement

### 12.1 Lessons Learned
- Post-change reviews capture lessons learned
- Best practices shared across ATA chapters
- Process improvements submitted as ECNs to CMP-STD-1001

### 12.2 Technology Evolution
- S1000D Issue updates evaluated annually
- AAMMPP integration improvements ongoing
- UTCS system enhancements as needed

---

## 13. Document Control

**Owner**: CMP Lead — ATA-05  
**Approver**: CCB Chair  
**Review Frequency**: Annual or with major CMP-STD-1001 changes  
**Next Review**: 2026-10-24  

---

## 14. References

### Internal Documents
- `/00-PROGRAM/CONFIG_MGMT/01-CM_PLAN.md`
- `/00-PROGRAM/CONFIG_MGMT/10-TRACEABILITY/UTCS/README.md`
- `/00-PROGRAM/GOVERNANCE/MAL-EEM/`

### External Standards
- **IDEALE-EU CMP-STD-1001**: Configuration and Maintenance Planning Standard
- **S1000D Issue 5.0**: International specification for technical publications
- **EASA CS-25**: Certification Specifications for Large Aeroplanes
- **FAA Part 25**: Airworthiness Standards: Transport Category Airplanes
- **ASD S2000M**: International specification for material management
- **MSG-3**: Maintenance Steering Group methodology

---

## 15. Contact Information

**CMP Lead — ATA-05**: cmp-ata05@idealeeu.eu  
**CCB Chair**: ccb-chair@idealeeu.eu  
**CM Office**: cm-office@idealeeu.eu  
**Technical Support**: support@idealeeu.eu

---

**Document Control**
- **Version**: 1.0
- **Status**: Active
- **Classification**: Internal
- **Retention**: Permanent

---

*This reference document is maintained in alignment with CMP-STD-1001 and is updated as the configuration management framework evolves.*
