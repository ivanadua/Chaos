import streamlit as st
import subprocess
import sys
import os

st.title("Triple Pendulum Simulator")

theta1 = st.slider("Theta 1 (rad)", -3.14, 3.14, 3.14)
theta2 = st.slider("Theta 2 (rad)", -3.14, 3.14, 0.52)
theta3 = st.slider("Theta 3 (rad)", -3.14, 3.14, 1.57)

if st.button("Run Simulation"):
    with st.spinner("Running simulation... Hold on to your hooplah."):
        subprocess.run([
            sys.executable,
            "pendy.py",
            str(theta1),
            str(theta2),
            str(theta3)
        ])

    st.success("Simulation completeeee")

    if os.path.exists("pendulum.gif"):
        st.image("pendulum.gif")
