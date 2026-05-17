# Proyecto MLflow - Predicción de aprobación de estudiantes

## Descripción

Proyecto de Machine Learning utilizando:

- MLflow
- Scikit-learn
- Streamlit

El sistema predice si un estudiante aprobará o no según:

- carrera
- modalidad
- beca
- edad
- promedio
- asistencias

## Dataset

El dataset fue generado artificialmente mediante Python y ya se encuentra incluido en:

```text
data/estudiantes.csv
```

## Tecnologías

- Python
- MLflow
- Streamlit
- Scikit-learn

## Ejecución

### 1. Ejecutar MLflow

```bash
mlflow server --backend-store-uri sqlite:///mlflow.db  --host 0.0.0.0 --port 9090    
```

### 2. Ejecutar notebook

Abrir:

```text
entrenamiento_mlflow.ipynb
```

### 3. Ejecutar Streamlit

```bash
streamlit run app_streamlit.py
```