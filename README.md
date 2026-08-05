# Chaos

Hi! Welcome to the README for Chaos! Chaos theory is a branch of mathematics focusing on nonlinear systems that are highly sensitive to initial conditions, meaning small changes can lead to vastly different outcomes. For example, if you went and slapped Tom Holland on the face in Iceland, you could be the cause of a minion uprising against kangaroos in Australia. It's just like that, but with tiny bit more realistic constraints. You may know it as "the butterfly effect"! n-pendulums work based on a similar principle. While single pendulums move via simple harmonic motion governed and constrained by mathematical equations, double, triple, quadruple pendulums listen to chaos theory. They're completely random, and completely unpredictable! With my project, you can simulate a triple pendulum by messing around with the initial conditions (such as the initial angles etcetera), and then plot a 'phase map.' 

# The Phase Map
The Phase Map is a grid which attempts to find "islands of stability." The idea is, that even in a sea of chaos, there are small islands of stability that follow predictable patterns with extremely specific initial conditions. By drawing inspiration from Veritasium and other Youtubers, this phase grid runs on the concept of each pixel in the map representing a single pendulum, wher every neighboring pixel has an identical but slightly different pendulum based on intiial conditions (for example, 0.0001 degrees different from the one before).

# Prerequisites 
Ensure you have python installed along with libraries numpy, sympy, matplotlib, pillow, and streamlit

```
bash
pip install numpy scipy matplotlib pillow streamlit
```
# Installation of the Pendulum

Clone the repository:

```
bash
git clone https://github.com/ivanadua/Chaos.git
cd Chaos
```

# Run the app


```
bash
streamlit run app.py
```

# How to Use
1. Adjust the initial angles using the sliders.
2. Click **Run Simulation**.
3. Hold onto your hooplah while the simulation is generated.
4. The animation will appear once rendering is complete.

> **Note:** The simulation may take up to a minute to generate because it performs a high-resolution RK4 integration before rendering the animation.

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
Like before, you can adjust values of m1, m2, m3, L1, L2, and L3. You can also adjust the resolution of the grid to have more pendulums and make a more detailed map.

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
) mean stable trajectories, while higher values (brighter color, >3) indicate extreme chaos.

>Nonperiodic solutions are ordinarily unstable with respect to small modifications, so that slightly differing initial states can evolve into considerably different state - Edward Lorentz

Have fun exploring chaos theory!

## Project Structure

```
app.py                       # Streamlit interface
pendy.py                     # Runs the simulation and generates the animation
Triple_pendulum.py           # Symbolic Lagrangian derivation
pendulum_equations.py        # Stored equations of motion
requirements.txt             # Libraries needed!
```

## Technologies Used

- Python
- Streamlit
- NumPy
- Matplotlib
- SymPy

