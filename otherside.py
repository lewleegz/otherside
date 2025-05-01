import streamlit as st
from streamlit_geolocation import streamlit_geolocation

st.title("Otherside")
st.write("This app will show you the other side of the world based on your location.")
st.write("Click the button below to get your antipode.")

location2 = streamlit_geolocation()
location =str(location2)

location = location.replace("{", "").replace("}", "").replace("'", "")
parts = location.split(",")
st.session_state.latitud = float(parts[0].split(":")[1].strip())
st.session_state.longitud = float(parts[1].split(":")[1].strip())

if st.session_state.latitud and st.session_state.longitud:
    try:
        latitud = float(st.session_state.latitud)
        longitud = float(st.session_state.longitud)
        latitud = latitud * -1
        longitud = (longitud + 180) if longitud < 0 else (longitud - 180)
        st.write("Your otherside are:", latitud, longitud)
        st.link_button("Go to maps", f"https://www.google.com/maps/search/?api=1&query={latitud},{longitud}")
    except ValueError:
        st.error("Location not found")
