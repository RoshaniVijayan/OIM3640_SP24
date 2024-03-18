import matplotlib.pyplot as plt
import numpy as np
import streamlit as st

st.write("## [Streamlit Homepage](https://streamlit.io/gallery)")

x = 1e6
x

st.sidebar.header("Parameters")
x = int(st.sidebar.text_input("Number of iterations: "))
norms = np.random.randn(x)
fig, axes = plt.subplots(figsize=(4,2))
axes.hist(norms, bins=50, edgecolor='w')
st.pyplot(fig)


button = st.button("Click me to get hacked!")

if button:
    st.header("Hello!")
