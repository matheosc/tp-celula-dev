
# scripts/analisis_ventas.py
# Autor: Paco (P2) - Desarrollador Técnico
# Descripción: Analiza ventas simuladas y genera indicadores clave

import pandas as pd
import matplotlib.pyplot as plt

# Cargamos el dataset desde la carpeta /datos
df = pd.read_csv("datos/ventas.csv", parse_dates=["fecha"])

# --- INDICADORES ---
# Total de ventas en el período
total_ventas = df["total"].sum()
print(f"Ventas totales: ${total_ventas:,.2f}")

# Producto más vendido por cantidad
mas_vendido = df.groupby("producto")["cantidad"].sum().idxmax()
print(f"Producto más vendido: {mas_vendido}")

# Ventas por mes (agrupamos por mes para ver tendencia temporal)
df["mes"] = df["fecha"].dt.to_period("M")
ventas_mes = df.groupby("mes")["total"].sum()
print(ventas_mes)

# --- GRÁFICO ---
fig, ax = plt.subplots(figsize=(10, 5))
ventas_mes.plot(kind="bar", ax=ax, color="steelblue")
ax.set_title("Evolución de Ventas por Mes")
ax.set_xlabel("Mes")
ax.set_ylabel("Total ($)")
plt.tight_layout()
plt.savefig("resultados/ventas_por_mes.png")
print("Gráfico guardado en resultados/")
