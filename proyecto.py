# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 08:35:22 2025

@author: usuario
"""

import pandas as pd
import matplotlib.pyplot as plt

datos = pd.read_csv("living.csv")

datos = datos.rename(columns={"Cost of living, 2017": "Costo_Vida", "Global rank": "Ranking"})

print(f"Número de filas: {datos.shape[0]}")
print(f"Número de columnas: {datos.shape[1]}")

costo_promedio = datos["Costo_Vida"].mean()
print(f"Costo de vida promedio: {costo_promedio:.2f}")

pais_mas_caro = datos.loc[datos["Costo_Vida"].idxmax(), "Countries"]
print(f"País con el costo de vida más alto: {pais_mas_caro}")

pais_mas_barato = datos.loc[datos["Costo_Vida"].idxmin(), "Countries"]
print(f"País con el costo de vida más bajo: {pais_mas_barato}")

peru = datos[datos["Countries"] == "Peru"]
if not peru.empty:
    costo_peru = peru["Costo_Vida"].values[0]
    ranking_peru = peru["Ranking"].values[0]
    print(f"Costo de vida en Perú: {costo_peru}")
    print(f"Ranking de Perú: {ranking_peru}")
else:
    print("No hay datos de Perú en el dataset.")

top_10_caros = datos.nlargest(10, "Costo_Vida")

plt.figure(figsize=(10, 5))
bars = plt.bar(top_10_caros["Countries"], top_10_caros["Costo_Vida"], color=plt.cm.Blues(range(10, 0, -1)))
plt.xlabel("Países")
plt.ylabel("Costo de Vida")
plt.title("Top 10 países con mayor costo de vida")
plt.xticks(rotation=45)

for i, bar in enumerate(bars):
    plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.1, top_10_caros["Countries"].iloc[i],
             ha='center', va='bottom', color="black", rotation=45)

plt.show()

top_10_baratos = datos.nsmallest(10, "Costo_Vida")

plt.figure(figsize=(10, 5))
bars = plt.bar(top_10_baratos["Countries"], top_10_baratos["Costo_Vida"], color=plt.cm.Greens(range(10, 0, -1)))
plt.xlabel("Países")
plt.ylabel("Costo de Vida")
plt.title("Top 10 países con menor costo de vida")
plt.xticks(rotation=45)

for i, bar in enumerate(bars):
    plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.1, top_10_baratos["Countries"].iloc[i],
             ha='center', va='bottom', color="black", rotation=45)

plt.show()

paises_america = ["Argentina", "Brazil", "Canada", "Chile", "Colombia", "Ecuador", 
                  "Mexico", "Peru", "United States", "Venezuela"]
datos_america = datos[datos["Countries"].isin(paises_america)]

plt.figure(figsize=(12, 5))
bars = plt.bar(datos_america["Countries"], datos_america["Costo_Vida"], color=plt.cm.RdBu(range(10, 0, -1)))
plt.xlabel("Países")
plt.ylabel("Costo de Vida")
plt.title("Costo de vida en países de América")
plt.xticks(rotation=45)

for i, bar in enumerate(bars):
    plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.1, datos_america["Countries"].iloc[i],
             ha='center', va='bottom', color="black", rotation=45)

plt.show()




