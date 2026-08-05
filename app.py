import streamlit as st
import subprocess
import sys
import os
import time

st.set_page_config(page_title="Triple Pendulum Simulator", layout="centered")

st.title("Triple Pendulum Simulator")
st.write("Adjust the initial angles and click **Run Simulation**.")

theta1 = st.slider("Theta 1 (rad)", -3.14, 3.14, 3.14)
theta2 = st.slider("Theta 2 (rad)", -3.14, 3.14, 0.52)
theta3 = st.slider("Theta 3 (rad)", -3.14, 3.14, 1.57)

if st.button("Run Simulation"):

    with st.spinner("Running simulation... This may take a minute."):
        subprocess.run([
            sys.executable,
            "pendy.py",
            str(theta1),
            str(theta2),
            str(theta3)
        ])

    st.success("Simulation complete!")

    # Give the GIF a moment to finish writing
    time.sleep(1)

    if os.path.exists("pendulum.gif"):
        with open("pendulum.gif", "rb") as file:
            gif = file.read()

        st.image(gif)
    else:
        st.error("pendulum.gif was not found.")
