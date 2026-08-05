import sympy as sp 
import inspect

t=sp.symbols('t')
theta1=sp.Function('theta1')(t)
theta2=sp.Function('theta2')(t)
theta3=sp.Function('theta3')(t)
L1, L2, L3 = sp.symbols('L1 L2 L3')
m1, m2, m3 = sp.symbols('m1 m2 m3')
x1= L1*sp.sin(theta1)
y1= -L1*sp.cos(theta1)
x2= x1 + L2*sp.sin(theta2)
y2= y1 - L2*sp.cos(theta2)
x3= x2 + L3*sp.sin(theta3)
y3= y2 - L3*sp.cos(theta3)
T1,T2,T3 = sp.symbols('T1 T2 T3')
V1,V2,V3 = sp.symbols('V1 V2 V3')

x1dd= sp.diff(x1,t,2)
x2dd= sp.diff(x2,t,2)
x3dd= sp.diff(x3,t,2)
y1dd= sp.diff(y1,t,2)
y2dd= sp.diff(y2,t,2)
y3dd= sp.diff(y3,t,2)
vx1=sp.diff(x1,t)
vy1=sp.diff(y1,t)
vx2=sp.diff(x2,t)
vy2=sp.diff(y2,t)
vx3=sp.diff(x3,t)
vy3=sp.diff(y3,t)
T = (sp.Rational(1,2)*m1*(vx1**2 + vy1**2)
    + sp.Rational(1,2)*m2*(vx2**2 + vy2**2)
    + sp.Rational(1,2)*m3*(vx3**2 + vy3**2))
g = sp.symbols('g')

V = m1*g*y1 + m2*g*y2 + m3*g*y3 
Lagrangian = T - V
print("Getting Lagrangian!!!")
Lagrangian = sp.simplify(Lagrangian)
print(Lagrangian)

print("YEEHAW, we got the Lagrangian!")
#Euler-Lagrange equations:

Euler1= sp.diff(sp.diff(Lagrangian, sp.diff(theta1,t)), t) - sp.diff(Lagrangian, theta1)
Euler2= sp.diff(sp.diff(Lagrangian, sp.diff(theta2,t)), t) - sp.diff(Lagrangian, theta2)
Euler3= sp.diff(sp.diff(Lagrangian, sp.diff(theta3,t)), t) - sp.diff(Lagrangian, theta3)
theta1dd=sp.diff(theta1,t,2)
theta2dd=sp.diff(theta2,t,2)
theta3dd=sp.diff(theta3,t,2)
derivs=[theta1dd, theta2dd, theta3dd]
solution=sp.solve((Euler1, Euler2, Euler3), derivs, dict=True)
alpha1 = solution[0][derivs[0]]
alpha2 = solution[0][derivs[1]]
alpha3 = solution[0][derivs[2]]


print("alpha1=", alpha1)
print("******************************************************************************************")
print("alpha2=", alpha2)
print("******************************************************************************************")
print("alpha3=", alpha3)

accel_func = sp.lambdify(
    (theta1, theta2, theta3, sp.diff(theta1,t), sp.diff(theta2,t), sp.diff(theta3,t), L1, L2, L3, m1, m2, m3, g),
    (solution[0][theta1dd], solution[0][theta2dd], solution[0][theta3dd]),
    "numpy")

print("Writing equationssssss...")
with open("pendulum_equations.py", "w") as f:
    f.write("import numpy as np\n")
    
    f.write("from numpy import sin, cos\n\n") 
    f.write(inspect.getsource(accel_func))

print("Successfully saved math script to 'pendulum_equations.py'! Go for it gurl")
