# SUBSYSTEMS — ATA-21 Air Conditioning (ECS) — Domain DDD

## Propósito
Carpeta que contiene los subsistemas de ATA-21 aplicables a Drainage / Dehumidification / Drying en el Q100. Cada subsistema debe mantener su propio conjunto PLM/CAx/CAE/Mantenimiento/Validación y enlazar con el baseline del sistema.

## Lista de subsistemas recomendados
- **21-10_PACKS_AND_REFRIGERATION** — Unidades de refrigeración / packs (incl. ciclo sCO₂ o refrigeración por compresión).  
- **21-20_AIR_DISTRIBUTION_DUCTS_VALVES** — Conductos, compuertas, válvulas y routing de aire.  
- **21-30_PRESSURIZATION_CONTROL** — Sistema de presurización, outflow valves y lógica de control.  
- **21-40_CABIN_ENVIRONMENT_CONTROL_CONTROLS** — Controladores HVAC, lógica BMS/ECS, UI.  
- **21-50_RECIRCULATION_VENTILATION** — Recirculación de aire, blowers y filtros de cabina.  
- **21-60_HUMIDITY_CONTROL_DEHUMIDIFIERS** — Unidades de deshumidificación (adsorbente / refrigerated).  
- **21-70_HEAT_EXCHANGERS_RECUPERATORS** — Recuperadores, intercambiadores CHT y diseño de superficies.  
- **21-80_FILTERS_WATER_SEPARATORS** — Filtros, trampas de agua y separadores; gestión de condensados.  
- **21-90_SENSORS_ACTUATORS_VALVES** — Sensórica, actuadores, válvulas de control y solenoides.  
- **21-99_COMMON** — Estándares, interfaces y plantillas comunes.

## Entregables mínimos por subsistema
Cada carpeta de subsistema debe contener como mínimo:
1. `README.md` del subsistema (alcance, owner, contactos).  
2. `PLM/EBOM_MAPPING.csv` o `metadata.yaml` por pieza.  
3. `CAD/` con STEP AP242 + `export_recipe.txt` y thumbnails.  
4. `CAE/` con caso *smoke* y `baseline/metrics.json`.  
5. `MAINTENANCE_TASKS/` (S1000D work-packages o equivalent).  
6. `PERFORMANCE/` (tablas rendimiento, curvas de capacidad, consumos).  
7. `VALIDATION/` (plan de ensayos y al menos un informe de banco de pruebas).  
8. `INTERFACES/INTERFACES.md` (ICD con otros sistemas: ECS, BMS, fuel/cryogenics, electrical).  
9. `TEMPLATE_METADATA.yaml` y `META.json` local.

## Convenciones
- Nombres: `{ATA}-{NN}_{DESCRIPTION}` (p. ej. `21-10_PACKS_AND_REFRIGERATION`).  
- Metadatos: usar `TEMPLATE_METADATA.yaml` con campos `part_id, ebom_id, cad_system, revision`.  
- Formatos: STEP AP242 con PMI para geometry; S1000D/XML para tareas de mantenimiento; CSV/JSON para tablas numéricas.  
- Unidades SI: mm, °C, kPa, kg, kW. Documentar excepciones en `21-99_COMMON/STANDARDS.md`.  
- CI/QA: cada `CAE` debe exponer un *smoke* ensayable en CI y `baseline/metrics.json` con claves `mass`, `energy_kwh`, `peak_temp_C`, `mass_flow_kg_s`.

## Enlaces útiles
- Plantilla de metadatos: `TEMPLATE_METADATA.yaml` (en esta carpeta).  
- Estándares y requisitos generales: `21-99_COMMON/STANDARDS.md`.

**Owner del conjunto de subsistemas:** Systems Lead — ATA-21  
**Contacto:** systems-ddd@idealeeu.eu
