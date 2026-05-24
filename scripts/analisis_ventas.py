
# scripts/analisis_ventas.py
# Autor: Paco (P2) - Desarrollador Técnico
# Descripción: Análisis de ventas reales de una pequeña empresa
# Dataset: ventas.csv - 150 registros, enero a mayo 2026

import pandas as pd
import matplotlib.pyplot as plt
import os

# Creamos la carpeta de resultados si no existe
os.makedirs("resultados", exist_ok=True)

# ---------------------------------------------
# CARGA DE DATOS
# Usamos ruta relativa para garantizar
# reproducibilidad en cualquier entorno
# ---------------------------------------------
df = pd.read_csv("datos/ventas.csv", parse_dates=["Fecha"])

# ---------------------------------------------
# INDICADOR 1: Ventas totales del período
# Suma del campo Total para tener el ingreso
# acumulado en todo el período analizado
# ---------------------------------------------
total_ventas = df["Total"].sum()
print(f"Ventas totales del período: ${total_ventas:,.2f}")

# ---------------------------------------------
# INDICADOR 2: Producto más vendido
# Agrupamos por Producto y sumamos Cantidad
# para identificar el de mayor volumen
# ---------------------------------------------
ventas_por_producto = df.groupby("Producto")["Cantidad"].sum().sort_values(ascending=False)
mas_vendido = ventas_por_producto.idxmax()
print(f"Producto más vendido: {mas_vendido} ({ventas_por_producto[mas_vendido]} unidades)")

# ---------------------------------------------
# INDICADOR 3: Ventas totales por mes
# Extraemos el período mensual de la fecha
# para analizar la tendencia temporal
# ---------------------------------------------
df["Mes"] = df["Fecha"].dt.to_period("M")
ventas_por_mes = df.groupby("Mes")["Total"].sum()
print("Ventas por mes:")
print(ventas_por_mes)

# ---------------------------------------------
# INDICADOR 4: Ventas por categoría
# Permite identificar qué rubro genera
# más ingresos en el período
# ---------------------------------------------
ventas_por_categoria = df.groupby("Categoria")["Total"].sum().sort_values(ascending=False)
print("Ventas por categoría:")
print(ventas_por_categoria)

# ---------------------------------------------
# INDICADOR 5: Ventas por región
# Útil para detectar zonas de mayor demanda
# ---------------------------------------------
ventas_por_region = df.groupby("Region")["Total"].sum().sort_values(ascending=False)
print("Ventas por región:")
print(ventas_por_region)

# ---------------------------------------------
# GRÁFICO 1: Evolución de ventas por mes
# Gráfico de barras para visualizar tendencia
# temporal de los ingresos totales
# ---------------------------------------------
fig, ax = plt.subplots(figsize=(10, 5))
ventas_por_mes.plot(kind="bar", ax=ax, color="steelblue", edgecolor="white")
ax.set_title("Evolución de Ventas Mensuales - 2026", fontsize=14)
ax.set_xlabel("Mes")
ax.set_ylabel("Total ($)")
ax.tick_params(axis="x", rotation=45)
plt.tight_layout()
plt.savefig("resultados/ventas_por_mes.png")
plt.close()
print("Gráfico 1 guardado: resultados/ventas_por_mes.png")

# ---------------------------------------------
# GRÁFICO 2: Ventas por categoría
# Gráfico de torta para visualizar la
# participación de cada rubro en el total
# ---------------------------------------------
fig, ax = plt.subplots(figsize=(7, 7))
ventas_por_categoria.plot(kind="pie", ax=ax, autopct="%1.1f%%", startangle=90)
ax.set_title("Participación por Categoría en Ventas Totales", fontsize=14)
ax.set_ylabel("")
plt.tight_layout()
plt.savefig("resultados/ventas_por_categoria.png")
plt.close()
print("Gráfico 2 guardado: resultados/ventas_por_categoria.png")

# ---------------------------------------------
# GRÁFICO 3: Ventas por región
# Comparativo de rendimiento entre regiones
# ---------------------------------------------
fig, ax = plt.subplots(figsize=(8, 5))
ventas_por_region.plot(kind="bar", ax=ax, color=["#2ecc71","#3498db","#e74c3c"], edgecolor="white")
ax.set_title("Ventas Totales por Región - 2026", fontsize=14)
ax.set_xlabel("Región")
ax.set_ylabel("Total ($)")
ax.tick_params(axis="x", rotation=0)
plt.tight_layout()
plt.savefig("resultados/ventas_por_region.png")
plt.close()
print("Gráfico 3 guardado: resultados/ventas_por_region.png")

# ---------------------------------------------
# EXPORTAR RESUMEN
# Guardamos un CSV con los indicadores
# principales para referencia futura
# ---------------------------------------------
resumen = pd.DataFrame({
    "Indicador": [
        "Ventas totales del período",
        "Producto más vendido",
        "Categoría líder",
        "Región líder"
    ],
    "Valor": [
        f"${total_ventas:,.2f}",
        mas_vendido,
        ventas_por_categoria.idxmax(),
        ventas_por_region.idxmax()
    ]
})
resumen.to_csv("resultados/resumen_indicadores.csv", index=False)
print("Resumen exportado: resultados/resumen_indicadores.csv")
