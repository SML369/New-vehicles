import pandas as pd
import plotly.express as px
import streamlit as st

st.header('Gráficos de venta de vehiculos en US')
        
car_data = pd.read_csv('vehicles_us.csv') # leer los datos
hist_button = st.button('Construir histograma') # crear un botón
scatter_button = st.button('Construir gráfico de dispersión')

if scatter_button:
    st.write('Creación de un gráfico de dispersión para el conjunto de datos de anuncios de venta de coches')

    fig = px.scatter(car_data, x='odometer', y='price')

    st.plotly_chart(fig, use_container_width= True)
    
if hist_button: # al hacer clic en el botón
        
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')# escribir un mensaje
            
    # crear un histograma
    fig = px.histogram(car_data, x="odometer")
        
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

build_barchart = st.checkbox('Construir un gráfico de barras ')

if build_barchart: # si la casilla de verificación está seleccionada
    st.write('Construir un gráfico de barras para la columna modelo')

    fig = px.bar(car_data, x="model", y="price")

    st.plotly_chart(fig, use_container_width= True)