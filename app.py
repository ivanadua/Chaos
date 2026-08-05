import streamlit as st
import subprocess
import sys
from pathlib import Path

st.set_page_config(page_title="Triple Pendulum Simulator")

st.title("Triple Pendulum Simulator")
st.write("Adjust the initial angles and click **Run Simulation**.")

theta1 = st.slider("Theta 1 (rad)", -3.14, 3.14, 3.14)
theta2 = st.slider("Theta 2 (rad)", -3.14, 3.14, 0.52)
theta3 = st.slider("Theta 3 (rad)", -3.14, 3.14, 1.57)

gif_path = Path(__file__).parent / "pendulum.gif"

if st.button("Run Simulation"):

    with st.spinner("Running simulation..."):
        result = subprocess.run(
    [
        sys.executable,
        "pendy.py",
        str(theta1),
        str(theta2),
        str(theta3)
    ],
    capture_output=True,
    text=True
)

st.text(result.stdout)
st.text(result.stderr)

    st.success("Simulation complete!")

    if gif_path.exists():
        st.image(str(gif_path))
    else:
        st.error(f"Couldn't find {gif_path}")
