import numpy as np
import streamlit as st
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

shells = {
    'Natica': {'r': 1.7, 'a': 2.6, 'b': 2.0, 'c': 1.0, 'd': 1.25, 'e': 2.0, 'f': 0.18, 'h': 6.0, 'u1': -20},
    'Ammonite': {'r': 1.2, 'f': 0.35, 'a': 0.09, 'b': 0.22, 'c': 1.9, 'd': 0.2, 'e': 0.13, 'h': 1.1, 'u1': 19},
    'Buccinum': {'r': 5.2, 'a': 1.1, 'b': 1.75, 'c': 1.0, 'd': 1.5, 'e': 5.0, 'f': 0.08, 'h': 7.0, 'u1': -60},
    'Nautilus': {'r': 4.4, 'a': 1.0, 'b': 0.6, 'c': 1.0, 'd': 1.0, 'e': 0.0, 'f': 0.18, 'h': 4.0, 'u1': -20},
    'Bellerophina': {'r': 2.6, 'a': 0.85, 'b': 1.2, 'c': 1.0, 'd': 0.75, 'e': 0.0, 'f': 0.06, 'h': 3.0, 'u1': -10},
    'Lyria': {'r': 1.7, 'a': 6.0, 'b': 2.1, 'c': 6.5, 'd': 1.25, 'e': 2.0, 'f': 1.0, 'h': 6.0, 'u1': -4},
    'Asteroceras': {'r': 1.4, 'a': 1.25, 'b': 1.25, 'c': 1.0, 'd': 3.5, 'e': 0.0, 'f': 0.12,'h': 4.0, 'u1': -40},
}

# Title and Description
st.markdown('<h1 style="font-size: 30px;">Modeling Shell Geometry Using Parametric Equations</h1>', unsafe_allow_html=True)
st.write("""
This application allows you to visualize various types of shells using parametric equations.
Choose a shell type from the dropdown to see the corresponding shell with its unique properties.
Adjust the sliders to experiment with different parameter values and generate a custom 3D shell shape.
""")

st.sidebar.markdown("**Select Shell Type**")
st.sidebar.markdown("*Choose a type of shell to visualize. The selected shell will set default parameters that are the characteristic of that shell.*")

# Dropdown for selecting shell type
selected_shell = st.sidebar.selectbox('', list(shells.keys()))


params = shells[selected_shell]

r = st.sidebar.slider("Radius (r)", 0.5, 2.0, params['r'])
a = st.sidebar.slider("Amplitude along X (a)", 0.01, 5.0, params['a'])
b = st.sidebar.slider("Amplitude along Z (b)", 0.1, 5.0, params['b'])
c = st.sidebar.slider("Angular frequency along spiral (c)", 1.0, 5.0, params['c'])
d = st.sidebar.slider("Radial offset (d)", 0.1, 5.0, params['d'])
e = st.sidebar.slider("Shape modifier (e)", 0.0, 10.0, params['e'])
f = st.sidebar.slider("Exponential growth factor (f)", 0.1, 1.0, params['f'])
h = st.sidebar.slider("Height offset (h)", 0.5, 10.0, float(params['h']))
u1 = st.sidebar.slider("Starting Angle (u1)", -60, 60, params['u1'])

def spiral_shell(*args):
    u = np.linspace(u1, -1.2, 200)  # Angle parameter
    v = np.linspace(-np.pi, np.pi, 200)  # Vertical parameter
    u, v = np.meshgrid(u, v)

    # X, Y, Z coordinates using the parametric equations
    x = r * np.exp(f * u) * (d + a * np.cos(v)) * np.cos(c * u)
    y = r * np.exp(f * u) * (d + a * np.cos(v)) * np.sin(c * u)
    z = r * np.exp(f * u) * (-1.4 * e + b * np.sin(v)) + h

    return x, y, z



if __name__ == "__main__":
    
    x, y, z = spiral_shell(r, f, a, b, c, d, e, h, u1)

    #Plot
    fig = plt.figure(figsize=(20, 10))
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(x, y, z, cmap="bone", edgecolor='black')

    ax.set_title(f"{selected_shell}")

    st.pyplot(fig)
