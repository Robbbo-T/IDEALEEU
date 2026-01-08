# 06-REVISIONS

Revision history and linked ECNs (CMP-controlled).

## Purpose

This directory contains:
- Revision history for ATA-06 baseline
- Engineering Change Notice (ECN) records
- Configuration Management Plan controlled changes
- Baseline update tracking

## Contents

- **REVISION_HISTORY.yaml**: Complete revision history
- **ECN Records**: Individual ECN JSON files
- **Baseline Snapshots**: Historical baseline references

## Revision Control

All modifications must:
1. Follow CMP governance process
2. Update REVISION_HISTORY.yaml
3. Create linked ECN JSON record
4. Update baselineId and date in 05-IDENTIFICATION/

## ECN Naming Convention

ECN files follow the pattern: `ECN-YYYY-06-NNN.json`
- YYYY: Year
- 06: ATA chapter
- NNN: Sequential number

## Change Process

1. Submit ECR through CCB process
2. Upon approval, create ECN record
3. Update configuration files
4. Document in revision history
5. Update identification card

## References

- [ATA-06 README](../README.md)
- [Identification](../05-IDENTIFICATION/)
- [00-PROGRAM/CONFIG_MGMT/06-CHANGES](../../../../00-PROGRAM/CONFIG_MGMT/06-CHANGES/)

---

**Last Updated**: 2025-10-24  
**Status**: Active
