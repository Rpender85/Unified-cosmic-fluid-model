import numpy as np
import matplotlib.pyplot as plt

class CosmicFluidSimulation:
    def __init__(self, grid_size, pressure_coefficient):
        self.grid_size = grid_size
        self.pressure_coefficient = pressure_coefficient
        self.density = np.zeros((grid_size, grid_size))
        self.pressure = np.zeros((grid_size, grid_size))
        self.mass_conservation_history = []
        self.pressure_history = []
        self.drainage_history = 0.0
        self.expelled_mass_history = 0.0
        self.quasar_events = []
        self.universe_creation_events = []

    def compute_pressure(self):
        self.pressure = self.pressure_coefficient * self.density

    def detect_expulsion_events(self, expulsion_threshold):
        local_avg_pressure = np.mean(self.pressure)
        expulsion_mask = self.pressure > (expulsion_threshold * local_avg_pressure)
        expelled_mass = np.sum(self.density[expulsion_mask])
        self.density[expulsion_mask] = 0
        self.expelled_mass_history += expelled_mass
        self.quasar_events.append(expelled_mass)

    def log_event(self, event_type, details):
        if event_type == 'quasar':
            self.quasar_events.append(details)
        elif event_type == 'new_universe':
            self.universe_creation_events.append(details)

    def update_mass_conservation(self):
        total_mass = np.sum(self.density)
        self.mass_conservation_history.append(total_mass)

    def visualize(self):
        fig, axs = plt.subplots(2, 2, figsize=(10, 10))
        axs[0, 0].imshow(self.density, cmap='viridis')
        axs[0, 0].set_title('Density Field')
        axs[0, 1].imshow(self.pressure, cmap='plasma')
        axs[0, 1].set_title('Pressure Field')
        axs[1, 0].plot(self.mass_conservation_history, label='Mass Conservation')
        axs[1, 0].set_title('Mass Conservation History')
        axs[1, 1].plot(self.pressure_history, label='Pressure Evolution')
        axs[1, 1].set_title('Pressure Evolution')
        plt.tight_layout()
        plt.show()

    def run_simulation(self, timesteps):
        for t in range(timesteps):
            self.compute_pressure()
            self.detect_expulsion_events(expulsion_threshold=1.0)
            self.update_mass_conservation()
            # Log pressure for visualization
            self.pressure_history.append(np.mean(self.pressure))
            # Implement logic for new universe creation events
            if t % 5 == 0:
                self.log_event('new_universe', {'time': t})

# Example Usage
if __name__ == '__main__':
    simulation = CosmicFluidSimulation(grid_size=100, pressure_coefficient=0.5)
    simulation.run_simulation(timesteps=100)
    simulation.visualize()