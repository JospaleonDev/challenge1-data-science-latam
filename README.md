# Challenge Data Science — Alura Store (Latam)

Este repo reproduce la estructura del proyecto del challenge **Alura Store** (ONE/Alura Latam), con un cuaderno base `AluraStoreLatam.ipynb` y una carpeta `data/` para cargar los CSV provistos en el reto original.

## 🚀 Qué incluye
- `notebooks/AluraStoreLatam.ipynb`: guía paso a paso para EDA, limpieza, métricas y visualizaciones.
- `data/raw/`: coloca aquí los CSV originales del challenge.
- `data/processed/`: salida de datos limpios/transformados.
- `src/`: utilidades reutilizables (carga de datos, validaciones, gráficos).
- `reports/figures/`: imágenes exportadas.
- `requirements.txt`: dependencias mínimas.

## ▶️ Cómo usar
1. Crea un entorno (opcional) y instala dependencias:
   ```bash
   pip install -r requirements.txt
   ```
2. Copia los archivos CSV oficiales del challenge a `data/raw/` (respeta los nombres originales).
3. Abre el cuaderno:
   ```bash
   jupyter notebook notebooks/AluraStoreLatam.ipynb
   ```
4. Ejecuta las celdas en orden. Ajusta los nombres de archivo si difieren.

## 📁 Archivos esperados
Según el reto oficial, tendrás una carpeta con bases de datos (CSV). Colócalas **tal cual** en `data/raw/`.
Si los nombres difieren, actualiza la sección **Carga de datos** del notebook.

## ✅ Objetivos sugeridos
- EDA (calidad de datos, nulos, outliers, duplicados, consistencia de claves).
- KPIs de negocio (ingresos, ticket promedio, recurrencia, top categorías).
- Visualizaciones (series, barras, boxplots, cohortes simples).
- Segmentación y/o recomendación básica (opcional).
- Informe ejecutivo con insights y next steps.

---

> Nota: este scaffold no incluye los datos por licencias del challenge. Usa los datos del repositorio oficial.