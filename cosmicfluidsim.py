import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import gaussian_filter

# =====================================================
# EXACT CODE USED FOR THE SIMULATION RESULTS SHOWN
# (Vortex/spiral/galaxy-like clustering version)
# =====================================================

N = 256
L = 60.0
dx = L / N
dt = 0.004

beta = 0.38
gamma = 0.15
k = 2.8
alpha = 0.85
omega_z = 0.085
drain_radius = 1.8

n_steps = 650
plot_every = 35
n_particles = 350

x = np.linspace(-L / 2, L / 2, N)
y = np.linspace(-L / 2, L / 2, N)
X, Y = np.meshgrid(x, y)
R = np.sqrt(X**2 + Y**2)

r_vec = np.zeros((N, N, 3))
r_vec[:, :, 0] = X
r_vec[:, :, 1] = Y

rho = np.ones((N, N)) * 1.0
rho += np.random.normal(0, 0.08, (N, N))

# Vortex seed for spirals
theta = np.arctan2(Y, X)
rho += 0.035 * np.sin(3 * theta) * np.exp(-R / 12)

rho = np.clip(rho, 0.05, None)

particles = np.random.uniform(-L / 2, L / 2, (n_particles, 2))


def gradient(f):
    df = np.zeros((N, N, 2))
    df[:, 1:-1, 0] = (f[:, 2:] - f[:, :-2]) / (2 * dx)
    df[:, 0, 0] = (f[:, 1] - f[:, 0]) / dx
    df[:, -1, 0] = (f[:, -1] - f[:, -2]) / dx
    df[1:-1, :, 1] = (f[2:, :] - f[:-2, :]) / (2 * dx)
    df[0, :, 1] = (f[1, :] - f[0, :]) / dx
    df[-1, :, 1] = (f[-1, :] - f[-2, :]) / dx
    return df


def divergence(v):
    div = np.zeros((N, N))
    div[:, 1:-1] += (v[:, 2:, 0] - v[:, :-2, 0]) / (2 * dx)
    div[:, 0] += (v[:, 1, 0] - v[:, 0, 0]) / dx
    div[:, -1] += (v[:, -1, 0] - v[:, -2, 0]) / dx
    div[1:-1, :] += (v[2:, :, 1] - v[:-2, :, 1]) / (2 * dx)
    div[0, :] += (v[1, :, 1] - v[0, :, 1]) / dx
    div[-1, :] += (v[-1, :, 1] - v[-2, :, 1]) / dx
    return div


def black_hole_sink():
    dist = np.sqrt(X**2 + Y**2)
    return alpha / (dist**2 + drain_radius**2)


plt.ion()
fig, ax = plt.subplots(figsize=(10, 8))

for step in range(n_steps + 1):
    grad_rho = gradient(rho)
    grad_ln_rho = grad_rho / (rho[..., np.newaxis] + 1e-8)

    v = beta * grad_rho - gamma * grad_ln_rho
    omega_cross = np.cross([0, 0, omega_z], r_vec)[:, :, :2]
    v -= omega_cross

    flux = rho[..., np.newaxis] * v
    div_flux = divergence(flux)
    sink = black_hole_sink()
    rho_new = rho - dt * (div_flux + sink)
    rho = np.clip(rho_new, 0.05, None)

    if step % 8 == 0:
        rho = gaussian_filter(rho, sigma=0.7)

    if step % 4 == 0:
        grad_at_p = np.zeros((n_particles, 2))
        for i in range(n_particles):
            ix = int((particles[i, 0] + L / 2) / dx)
            iy = int((particles[i, 1] + L / 2) / dx)
            ix = np.clip(ix, 1, N - 2)
            iy = np.clip(iy, 1, N - 2)
            grad_at_p[i] = grad_rho[iy, ix]

        acc = -k * grad_at_p
        particles += acc * dt * 8

    if step % plot_every == 0 or step == n_steps:
        ax.clear()
        im = ax.imshow(
            rho.T,
            extent=[-L / 2, L / 2, -L / 2, L / 2],
            origin="lower",
            cmap="inferno",
            vmin=0.05,
            vmax=4.0,
            interpolation="nearest",
        )
        ax.scatter(particles[:, 0], particles[:, 1], s=6, c="cyan", alpha=0.85)
        ax.set_title(f"Your Unified Fluid Model — Step {step}")
        ax.set_xlabel("x (kpc)")
        ax.set_ylabel("y (kpc)")
        plt.colorbar(im, ax=ax, label="Cosmic Fluid Density ρ\n(Low = Gravity)")
        plt.pause(0.08)

plt.ioff()
plt.show()
