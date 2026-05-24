# TP - Gestión Colaborativa con Git, GitHub y Jira

## Integrantes
- Hugo (P1): Líder y Organizador
- Paco (P2): Desarrollador Técnico  
- Luis (P3): Revisor y QA

## Escenario elegido
**Escenario B – Análisis de Ventas de una Pequeña Empresa**

## Dataset utilizado
Archivo: `datos/ventas.csv`  
Registros: 150 transacciones de ventas (enero - mayo 2026)  
Columnas: ID_Venta, Fecha, Producto, Categoria, Cantidad, Precio_Unitario, Total, Region  
Fuente: Dataset propio generado para el trabajo práctico  

## Resultados generados
- `resultados/ventas_por_mes.png` — Evolución mensual de ventas
- `resultados/ventas_por_categoria.png` — Participación por categoría
- `resultados/ventas_por_region.png` — Comparativo por región
- `resultados/resumen_indicadores.csv` — Tabla de indicadores clave

## Cómo ejecutar
1. Clonar el repositorio
2. Abrir Google Colab y montar el entorno
3. Ejecutar: `python scripts/analisis_ventas.py`

## Resultados
Los gráficos generados se guardan en la carpeta `/resultados`.
