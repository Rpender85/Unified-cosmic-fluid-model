# Emergent Gravity from a Dynamic Fluid Spacetime

**Author:** Ralph Pender
**Date:** April 10 2026
**Status:** Simulations Verified (Bullet Cluster, Spiral Galaxies, Big Bang)

## 🌌 Overview
This project proposes a unified hydrodynamic model of spacetime where gravity emerges from the dynamics of a super-low viscosity fluid medium. Unlike geometric formulations of General Relativity (GR), this model treats spacetime as a dynamic fluid where:
- **Gravity** is a pressure gradient arising from fluid flow.
- **Black Holes** act as mass sinks and **vorticity sources**.
- **Quasars/Big Bangs** act as mass sources and **vorticity injectors**.
- **Dark Matter effects** (like the Bullet Cluster separation) emerge naturally from the collisionless nature of the fluid's vorticity field.

## ✅ Key Validations (Simulated)
We have successfully simulated three critical observational tests that typically require Dark Matter or complex GR corrections:

1.  **The Bullet Cluster:** The model reproduces the separation of "lensing mass" (vorticity) from "baryonic gas" (viscous fluid) during a cluster collision, without invoking invisible particles.
2.  **Spiral Galaxy Formation:** Spiral arms emerge naturally from the shear of a rotating disk and vorticity injection from a central supermassive black hole, without pre-defined density waves.
3.  **The Big Bang:** A "Cosmic Engine" cycle is simulated where a collapsing black hole reaches a critical density, triggering a phase transition (sink-to-source) that releases stored vorticity, creating an expanding, rotating universe.

## 📐 Governing Equations
The model is governed by a modified continuity equation coupled with a vorticity evolution equation.

### 1. Mass Continuity (Sink/Source Dynamics)
$$ \frac{\partial \rho}{\partial t} = \nabla \cdot \left[ \rho \left( \kappa \nabla \rho - \boldsymbol{\omega} \times \mathbf{r} \right) \right] - \alpha M_{BH} + \delta Q_{QS} $$

*   $\rho$: Fluid density (spacetime medium)
*   $\kappa$: Net diffusion/pressure coefficient
*   $\boldsymbol{\omega}$: Vorticity vector
*   $M_{BH}$: Black Hole sink term (mass removal)
*   $Q_{QS}$: Quasar source term (mass injection)

### 2. Vorticity Evolution (The Critical Fix)
Unlike standard baroclinic models where vorticity generation vanishes for barotropic fluids, this model introduces a direct source term driven by cosmic bodies:

$$ \frac{\partial \boldsymbol{\omega}}{\partial t} = (\mathbf{v} \cdot \nabla)\boldsymbol{\omega} + \sigma \left( M_{BH} + Q_{QS} \right) - \lambda \boldsymbol{\omega} $$

*   **$\sigma (M_{BH} + Q_{QS})$**: **Direct Vorticity Source.** Black Holes and Quasars actively generate spin in the fluid, bypassing the vanishing baroclinic term.
*   **$\lambda$**: Weak damping (viscosity).

### 3. Gravity & Auxiliary Relations
*   **Gravity from Pressure:** $\mathbf{a}_{grav} = -k \nabla \rho$
*   **Equation of State:** $p(\rho) = \frac{k}{2} \rho^2$
*   **Lensing (Refraction):** $c_{eff} = \frac{c_0}{\rho}$
*   **Time Dilation:** $\tau \propto \frac{1}{\rho}$

## 🧪 Simulation Results
The Python simulations included in this repository demonstrate:
- **Frame 1:** Two gas clouds colliding. The gas (viscous) stops in the center, while the vorticity (gravity) passes through, creating the "Bullet Cluster" separation.
- **Frame 2:** A rotating disk where vorticity injection from the center naturally winds up into spiral arms.
- **Frame 3:** A collapse-to-bang transition where density reaches a critical threshold, flipping the sink to a source and releasing a vorticity explosion.

## 📂 Repository Contents
- `/simulations`: Python scripts for Bullet Cluster, Spiral Galaxy, and Big Bang models.
- `/results`: Screenshots and data plots from successful runs.
- `/paper`: Draft manuscript and abstract.

## 📞 Contact & Collaboration
This work is open for peer review and collaboration. For inquiries, please contact ralphpender@gmail.com or open an issue.

---
*Note: This is a theoretical framework. All simulations are numerical approximations intended to validate the core physical mechanisms.*