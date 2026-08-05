import numpy as np
from numpy import sin, cos
import matplotlib.pyplot as plt
from pendulum_equations import _lambdifygenerated as accel
import matplotlib.animation as animation

# 1. Define simulation constants
L1 = L2 = L3 = 1.0
m1 = m2 = m3 = 1.0
g = 9.81

# 2. Initial state vector: [theta1, theta2, theta3, omega1, omega2, omega3]
state = np.array([
    np.pi,   # theta1
    np.pi/6,   # theta2
    np.pi/2,   # theta3
    0.0,       # omega1
    0.0,       # omega2
    0.0        # omega3
], dtype=float)

# 3. Derivatives function evaluates 'accel'
def derivatives(state):
    theta1, theta2, theta3, omega1, omega2, omega3 = state

    
    alpha1, alpha2, alpha3 = accel(
        theta1, theta2, theta3,
        omega1, omega2, omega3,
        L1, L2, L3,
        m1, m2, m3, 
        g
    )

    return np.array([
        omega1,
        omega2,
        omega3,
        alpha1,
        alpha2,
        alpha3
    ])

# 4. RK4 Step
def rk4_step(state, dt):
    k1 = derivatives(state)
    k2 = derivatives(state + 0.5 * dt * k1)
    k3 = derivatives(state + 0.5 * dt * k2)
    k4 = derivatives(state + dt * k3)
    return state + (dt / 6) * (k1 + 2 * k2 + 2 * k3 + k4)

# 5. Time loop
dt = 0.0001
time = 0.0
history = []

for i in range(100000):
  
    history.append(np.copy(state)) 
    state = rk4_step(state, dt)
    time += dt

history = np.array(history)


# 6. ANIMATION TIME!!

print("Processing Cartesian coordinates for animation...")
theta1_hist = history[:, 0]
theta2_hist = history[:, 1]
theta3_hist = history[:, 2]

# Compute spatial positions for all 3 masses across all time steps
x1 = L1 * np.sin(theta1_hist)
y1 = -L1 * np.cos(theta1_hist)

x2 = x1 + L2 * np.sin(theta2_hist)
y2 = y1 - L2 * np.cos(theta2_hist)

x3 = x2 + L3 * np.sin(theta3_hist)
y3 = y2 - L3 * np.cos(theta3_hist)

# Setup the canvas figure window
fig, ax = plt.subplots(figsize=(6, 6))
max_length = L1 + L2 + L3
ax.set_xlim(-max_length - 0.5, max_length + 0.5)
ax.set_ylim(-max_length - 0.5, max_length + 0.5)
ax.set_aspect('equal')
ax.grid(True)

# Graphic element tracks
line, = ax.plot([], [], 'o-', lw=2, color='#1f77b4', markersize=8)  # Rods & Bobs
trace, = ax.plot([], [], '-', lw=1, color='red', alpha=0.4)         # Tip path trail
time_text = ax.text(0.05, 0.9, '', transform=ax.transAxes)

trail_x, trail_y = [], []
frame_skip = 200  

def init():
    line.set_data([], [])
    trace.set_data([], [])
    time_text.set_text('')
    return line, trace, time_text

def animate(i):
    idx = i * frame_skip
    if idx >= len(history):
        return line, trace, time_text

    
    this_x = [0, x1[idx], x2[idx], x3[idx]]
    this_y = [0, y1[idx], y2[idx], y3[idx]]
    

    trail_x.append(x3[idx])
    trail_y.append(y3[idx])
    if len(trail_x) > 200:  
        trail_x.pop(0)
        trail_y.pop(0)
        
    line.set_data(this_x, this_y)
    trace.set_data(trail_x, trail_y)
    time_text.set_text(f'Time = {idx * dt:.2f}s')
    return line, trace, time_text

print("Launching Real-Time Playback Window...")
ani = animation.FuncAnimation(
    fig, animate, 
    frames=len(history) // frame_skip,
    init_func=init, 
    interval=20,  
    blit=True
)

plt.show()
