# Unified-cosmic-fluid-model
Unified cosmic fluid theory to explain the universe structure.
# Unified Universal Fluid Model: Emergent Gravity from Density Gradients and Black-Hole Drains

A toy cosmological model where gravity emerges as low-pressure zones in a cosmic fluid, driven by black holes acting as drains. No dark matter or separate gravitational field is required — clustering, rotation curves, galactic spirals, and large-scale structure arise from fluid dynamics alone.

This is a personal exploration / alternative framework inspired by analogue gravity, vortex cosmologies, and black-hole baby universe ideas. It is **not** a replacement for general relativity or ΛCDM, but a simple, simulatable PDE that reproduces several qualitative observations.

## Core Idea

- The universe is modeled as a compressible cosmic fluid with density ρ.
- Black holes act as sinks/drains (−α M(x) term) that create deep low-ρ funnels.
- Matter collects in these low-pressure zones → emergent "gravity" via a = −k ∇ρ.
- Gradient terms (β ∇ρ and γ ∇(ln ρ)) drive clustering and anti-diffusion.
- Rotation (ω × r) produces vortices and maintains orbits.
- A successful drain threshold can "birth" new universes with inherited spin (explaining axis-of-evil alignment).

## The Locked Field Equation

The evolution of the cosmic fluid density ρ is governed by:

∂ρ/∂t = ∇ · [ ρ (β ∇ρ − γ (∇ρ)/ρ − ω × r) ] − α M(x)

with effective gravitational acceleration for test particles:

a = −k ∇ρ

(For numerical stability, the flux is rewritten to avoid division instability when ρ → 0 near drains.)

## Features Demonstrated in Simulation

- Central black-hole drain carves low-ρ funnel
- Spiral arms and vortex formation from rotation + gradients
- Matter particles cluster and orbit in low-pressure zones
- Qualitative flat-ish rotation curves and galactic structure without dark matter

## Requirements

- Python 3.x
- NumPy
- Matplotlib
- SciPy (for gaussian_filter)

Install with:

```bash
pip install numpy matplotlib scipy
