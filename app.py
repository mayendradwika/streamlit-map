import streamlit as st
import folium
from streamlit_folium import st_folium

st.set_page_config(page_title= "Peta Interaktif", layout="wide")
st.title("🗺️ Peta Interaktif dengan Streamlit + Folium")

st.markdown("""
Masukkan koordinat (latitude & longitude) untuk melihat lokasi di peta.\
Kamu juga bisa menambahkan marker ke lokasi tersebut.
""")

lat = st.number_input("Latitude (Lintang)", value=-6.2, format="%.6f")
lon = st.number_input("Longitude (Bujur)", value=106.816666, format="%.6f")
zoom = st.slider("Zoom Level", min_value=1, max_value=18, value=12)
add_marker = st.checkbox("Tambahkan marker ke lokasi ini", value=True)

m = folium.Map(location=[lat,lon], zoom_start=zoom)

if add_marker:
    folium.Marker([lat,lon], tooltip="Lokasi Marker", popup=f"Lat:{lat}, lon:{lon}").add_to(m)


st_folium(m,width=700, height=500)