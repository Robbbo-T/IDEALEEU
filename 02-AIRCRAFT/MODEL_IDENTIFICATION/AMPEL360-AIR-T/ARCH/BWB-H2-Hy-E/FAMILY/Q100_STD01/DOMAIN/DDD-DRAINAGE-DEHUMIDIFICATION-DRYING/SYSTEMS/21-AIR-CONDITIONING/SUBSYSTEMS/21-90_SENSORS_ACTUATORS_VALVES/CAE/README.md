# CAE — 21-90_SENSORS_ACTUATORS_VALVES

## Purpose
This folder contains simulation cases, analysis results, and baseline metrics.

## Required Contents
1. **Smoke Test:** Quick validation case for CI pipeline
2. **Baseline Metrics:** `baseline/metrics.json` with standard keys
3. **Analysis Reports:** Detailed simulation results
4. **Mesh Files:** Input meshes and geometry

## Baseline Metrics Format
```json
{
  "mass": 0.0,
  "energy_kwh": 0.0,
  "peak_temp_C": 0.0,
  "mass_flow_kg_s": 0.0,
  "pressure_drop_kPa": 0.0
}
```

## Notes
- Smoke tests must complete in <10 minutes for CI
- Document solver settings and convergence criteria
- Include validation against test data when available

**Status:** Awaiting CAE cases
