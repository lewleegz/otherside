import streamlit as st

st.title("Otherside")
st.subheader("Enter your coordinates")

st.session_state.latitud = st.text_input("Enter your latitude:")
st.session_state.longitud = st.text_input("Enter your longitude:")

if st.session_state.latitud and st.session_state.longitud:
    try:
        latitud = float(st.session_state.latitud)
        longitud = float(st.session_state.longitud)
        latitud = latitud * -1
        longitud = 180 - longitud
        st.write("Your opposite coordinates are:", latitud, longitud)
    except ValueError:
        st.error("Please enter valid shit.")
else:
    st.write("Please enter your coordinates.")