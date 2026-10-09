# Flood Decision Intelligence

Interactive flood decision digital twin prototype combining an Earth-first location workflow, live data connectors, adaptive 3D/2.5D hydraulics, statistics, AI-assisted screening and intervention analysis.

## v1.1 robust-mechanistic

This version fixes the live terrain acquisition hang seen in the earlier prototype. The root cause was a recursive Streamlit cache wrapper for the public DEM connector. Live acquisition is now bounded, parallel and fail-safe.

### Live acquisition

- Open-Meteo weather / rainfall
- public Copernicus GLO-90 elevation fallback
- OpenTopography COP30 / SRTM / NASADEM when an API key is supplied
- OpenStreetMap / Overpass critical assets and limited building exposure
- hard connector timeouts and an overall acquisition budget
- optional-source failure does not block the workspace
- deterministic terrain fallback if a public DEM service is unavailable
- acquisition timing and source provenance shown in the UI

### Mechanistic hydraulic core

The default routing engine now uses:

- adaptive 2.5D storage prisms with fine-DEM hypsometric storage
- local-inertial shallow-water face momentum
- Manning friction
- Horton time-varying infiltration
- CFL-style adaptive timesteps
- conservative volume transfer
- wetting-front Froude limiter for numerical stability
- mass-balance, Froude and runoff diagnostics

The previous instantaneous diffusive-wave approximation is no longer the only mechanism driving lateral flow.

### Decision intelligence

The app also includes:

- 3D flood visualisation and time slider
- asset exposure and prototype depth-damage consequences
- intervention sandbox for retention basins, drainage channels and raised defences
- before/after physics verification
- benefit-cost screening
- uncertainty ensembles and exceedance maps
- Bayesian sensor reweighting
- AI surrogate acceleration with cross-validation
- return-period / GEV exploration
- "why flooded?" terrain-contributing-area explainability

## Windows

Extract the application package and double-click `run.bat`.

The launcher:

1. reuses an existing `.venv` if available;
2. finds or bootstraps Python 3.12 when necessary;
3. installs missing dependencies;
4. validates the app;
5. finds a free port starting at 8517;
6. starts Streamlit and opens the browser.

If the Python environment becomes damaged, run `repair_environment.bat`.

## Release package in this repository

The complete v1.1 local application is stored under `release/` as Base64 parts because the connected GitHub writer is text-oriented.

Run:

```bash
python release/assemble_release.py
```

This creates:

```text
FloodDecisionIntelligence-v1.1.zip
```

Extract the ZIP and double-click `run.bat`.

## Important limitation

This is a research/product-development prototype. It is not yet calibrated or validated for statutory flood mapping, emergency life-safety decisions, insurance pricing or engineering sign-off.
