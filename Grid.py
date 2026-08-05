import numpy as np
import matplotlib.pyplot as plt
from pendulum_equations import _lambdifygenerated as accel


# 1. GRID GENERATION & SYSTEM CONSTANTS

# Number of pixels per axis (e.g., 200x200 = 40,000 pendulums simulated at once)
GRID_RES = 200  

L1 = L2 = L3 = 1.0
m1 = m2 = m3 = 1.0
g = 9.81

# Create ranges for the two angles to vary across the pixel axes
# I varied theta1 across the X-axis and theta2 across the Y-axis
theta1_range = np.linspace(-np.pi, np.pi, GRID_RES)
theta2_range = np.linspace(-np.pi, np.pi, GRID_RES)
T1, T2 = np.meshgrid(theta1_range, theta2_range)

# Initialize a grid: Shape is (GRID_RES, GRID_RES, 6)
state_grid = np.zeros((GRID_RES, GRID_RES, 6), dtype=float)

state_grid[:, :, 0] = T1           # X-axis of pixels maps to unique theta1 values
state_grid[:, :, 1] = T2           # Y-axis of pixels maps to unique theta2 values
state_grid[:, :, 2] = np.pi / 4    # Keep theta3 constant at 45 degrees for all
state_grid[:, :, 3] = 0.0          # omega1 = 0
state_grid[:, :, 4] = 0.0          # omega2 = 0
state_grid[:, :, 5] = 0.0          # omega3 = 0


# 2. VECTORISED DERIVATIVES & RK4

def vectorized_derivatives(state):
   
    t1 = state[:, :, 0]
    t2 = state[:, :, 1]
    t3 = state[:, :, 2]
    w1 = state[:, :, 3]
    w2 = state[:, :, 4]
    w3 = state[:, :, 5]

    a1, a2, a3 = accel(t1, t2, t3, w1, w2, w3, L1, L2, L3, m1, m2, m3, g)

 
    return np.stack([w1, w2, w3, a1, a2, a3], axis=-1)

def rk4_step(state, dt):
    k1 = vectorized_derivatives(state)
    k2 = vectorized_derivatives(state + 0.5 * dt * k1)
    k3 = vectorized_derivatives(state + 0.5 * dt * k2)
    k4 = vectorized_derivatives(state + dt * k3)
    return state + (dt / 6.0) * (k1 + 2.0 * k2 + 2.0 * k3 + k4)
# 3. CRITERIA TRACKING SIMULATION

dt = 0.0005
total_steps = 15000  # Total time window to monitor flipping / divergence

# To measure chaos vs stability, track the max velocity reached by each pendulum.
# Chaotic pendulums will violently whip around like Beyonce's gorgeous hair (high max velocity/flipping).
# Stable islands will stay tightly bound (very low max velocity).
max_omega_observed = np.zeros((GRID_RES, GRID_RES))

print(f"Simulating {GRID_RES}x{GRID_RES} ({GRID_RES**2}) pendulums simultaneously...")

for step in range(total_steps):
    state_grid = rk4_step(state_grid, dt)
    
    # Extract instantaneous absolute speeds of the middle and bottom bobs
    current_speeds = np.abs(state_grid[:, :, 4]) + np.abs(state_grid[:, :, 5])
    
    # Store the peak velocity hit by each specific coordinate pixel
    max_omega_observed = np.maximum(max_omega_observed, current_speeds)
    
    if step % 3000 == 0 and step > 0:
        print(f"  -> Progress: {int((step/total_steps)*100)}% complete...")

print("Simulation finished! Rendering your Stability Map...")

# 4. PLOTTING THE ISLANDS OF STABILITY

plt.figure(figsize=(8, 8))

# Logarithmic scaling brings out hidden geometric structures and fractal edges
stability_map = np.log1p(max_omega_observed)

plt.imshow(
    stability_map, 
    extent=[-np.pi, np.pi, -np.pi, np.pi], 
    origin='lower', 
    cmap='inferno'
)

plt.colorbar(label='Chaos Metric (Log Peak Angular Velocity)')
plt.xlabel(r'Initial $\theta_1$ (rad)')
plt.ylabel(r'Initial $\theta_2$ (rad)')
plt.title('Triple Pendulum Phase Map: Finding Islands of Stability')
plt.show()
