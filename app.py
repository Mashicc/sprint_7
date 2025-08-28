import streamlit as st
import pandas as pd
import plotly.express as px

car_data = pd.read_csv('vehicles_us.csv')

st.header('Exploracion de los datos de autos en USA')

build_histogram = st.button('Construir Histograma')
build_scatter = st.button('Construir Grafico de Dispersion')

if build_histogram:
    st.write('Crear histograma')
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

if build_scatter:
    st.write('Crear grafico de dispersion')
    fig = px.scatter(car_data, x="model_year", y="price")
    st.plotly_chart(fig, use_container_width=True)
