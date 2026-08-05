# Chaos

Hi! Welcome to the README for Chaos! Chaos theory is a branch of mathematics focusing on nonlinear systems that are highly sensitive to initial conditions, meaning small changes can lead to vastly different outcomes. For example, if you went and slapped Tom Holland on the face in Iceland, you could be the cause of a minion uprising against kangaroos in Australia. It's just like that, but with tiny bit more realistic constraints. You may know it as "the butterfly effect"! n-pendulums work based on a similar principle. While single pendulums move via simple harmonic motion governed and constrained by mathematical equations, double, triple, quadruple pendulums listen to chaos theory. They're completely random, and completely unpredictable! With my project, you can simulate a triple pendulum by messing around with the initial conditions (such as the initial angles etcetera), and then plot a 'phase map.'

# The Phase Map
The Phase Map is a grid which attempts to find "islands of stability." The idea is, that even in a sea of chaos, there are small islands of stability that follow predictable patterns with extremely specific initial conditions. By drawing inspiration from Veritasium and other Youtubers, this phase grid runs on the concept of each pixel in the map representing a single pendulum, wher every neighboring pixel has an identical but slightly different pendulum based on intiial conditions (for example, 0.0001 degrees different from the one before).

# Prerequisites
Ensure you have python installed along with libraries numpy, sympy, and matplotlib

```
bash
pip install numpy scipy matplotlib
```
# Installation of the Pendulum
First, you're going to run Triple_Pendulum.py: this finds the Lagrangian equations for the triple pendulum (which are EXTREMELY long). They've already been saved in pendulum_equations.py, which you should keep open as another tab. Finally, open simulation.py and locate this section of the code:

``` 
# 1. Define your simulation constants
L1 = L2 = L3 = 1.0 #YOU CAN CHANGE THIS!
m1 = m2 = m3 = 1.0 #YOU CAN CHANGE THIS!
g = 9.81

# 2. Initial state vector: [theta1, theta2, theta3, omega1, omega2, omega3]
state = np.array([
    np.pi,   # theta1; YOU CAN CHANGE THIS!
    np.pi/6,   # theta2; YOU CAN CHANGE THIS!
    np.pi/2,   # theta3; YOU CAN CHANGE THIS!
    0.0,       # omega1; YOU CAN CHANGE THIS!
    0.0,       # omega2; YOU CAN CHANGE THIS!
    0.0        # omega3; YOU CAN CHANGE THIS!
], dtype=float)

```
Anywhere that I've yelled at you saying "YOU CAN CHANGE THIS!" is a variable you can edit. Remember, all values of theta are in radians, so for ease, write them in terms of pi. For example, 90 degrees is pi/2 radians, so to change theta1 to pi/2 radians, you edit the row with #theta 1 with:
np.pi/2. The greater the engle, the more chaotic your system is likely to be.

Now, find this part of the code:

```
# 5. Time loop
dt = 0.0001
time = 0.0
history = []

for i in range(100000): #This means that the code runs for 10 seconds

    history.append(np.copy(state)) 
    state = rk4_step(state, dt)
    time += dt
```
The "i in range (100000)" means the pendulum will run a loop for 10 seconds. You can change this to different limits based on your preference (for example, 70000 for 7 seconds). But note that the longer you keep the time range, the longer it takes for the code to run. So, you'll have to be patient! The code at 100000 already takes about a few minutes to run.

# Installing the Grid

This is an optional step, but the outcome is really cool! However, the code is extremely heavy and it might be best to run this code on a desktop server if your laptop can't handle it. On my Mac, this code took about 2 days to complete.
To run it, all you have to do is run Grid.py. You can leave the conditions as they are in the code, OR you can edit the initial conditions in this too:
```
# Number of pixels per axis (e.g. 200x200 = 40,000 pendulums simulated at once)
GRID_RES = 200  

L1 = L2 = L3 = 1.0
m1 = m2 = m3 = 1.0
g = 9.81
```
Like before, you can adjust values of mi, m2, m3, L1, L2, and L3. You can also adjust the resolution of the grid to have more pendulums and make a more detailed map.

```
state_grid[:, :, 0] = T1           # X-axis of pixels maps to unique theta1 values
state_grid[:, :, 1] = T2           # Y-axis of pixels maps to unique theta2 values
state_grid[:, :, 2] = np.pi / 4    # Keep theta3 constant at 45 degrees for all --> You can change this as you please (again, in terms of pi for ease!)
state_grid[:, :, 3] = 0.0          # omega1 = 0
state_grid[:, :, 4] = 0.0          # omega2 = 0
state_grid[:, :, 5] = 0.0          # omega3 = 0
```
By the end of some kind of eternity, you'll have a beautiful phase map in front of you

# Interpreting the Phase Map


*The Dark Central Feature*: The dark blue and black region near the center represents an island of stability. These initial conditions result in regular, non-chaotic, or low-velocity periodic motion.

*The Bright Surrounding Regions*: The vibrant yellow and orange areas represent highly chaotic behavior. These initial angles cause the pendulum to experience rapid, unpredictable flipping and high peak angular velocities.

*The Fractal Boundaries*: The swirling, marbled patterns separating the dark and bright zones represent the complex, highly sensitive boundaries typical of chaotic dynamical systems, where a tiny change in initial angles completely alters the outcome.

(darker color, <2
) mean stable trajectories, while higher values (brighter color, 
>3) indicate extreme chaos.

Have fun exploring chaos theory!
