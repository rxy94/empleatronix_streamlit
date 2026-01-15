import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("EMPLEATRONIX")
st.write("Todos los datos sobre los empleados en una aplicación.")

# Cargamos los datos del csv y los mostramos en un dataframe
df = pd.read_csv("datasets/employees.csv")
st.dataframe(df)

st.divider()

# Mostramos los datos en un gráfico de barras
with st.container(horizontal=True, gap="large"):
    color = st.color_picker("Elige un color para las barras", "#ab29df")
    nombre_on = st.toggle("Mostrar el nombre")
    sueldo_on = st.toggle("Mostrar el sueldo en la barra")

fig, ax = plt.subplots()
ax.barh(df["full name"], df["salary"], color=color)
ax.margins(x=0.2)
ax.set_xlim(0, 4500)
ax.set_xticks(range(0, 4501, 500))
ax.tick_params(axis='x', rotation=90) 

if not nombre_on:
    ax.set_yticks([])

if sueldo_on:
    for indice, valor in enumerate(df["salary"]):
        ax.text(valor + 50, indice, str(df["salary"][indice]) + "€", va='center')

st.pyplot(fig)

st.write("© Ruyi Xia Ye - CPIFP Alan Turing")
