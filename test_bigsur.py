import streamlit as st
import sys

st.title("✅ macOS Big Sur Test Successful!")
st.write(f"Python version: {sys.version}")
st.write("Your Big Sur environment is ready!")

# Simple test
if st.button("Click me!"):
    st.balloons()
    st.success("Big Sur is working perfectly! 🎉")
