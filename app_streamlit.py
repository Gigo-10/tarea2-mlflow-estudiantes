import streamlit as st
import pandas as pd
import mlflow
import mlflow.sklearn

# =====================================================
# CONFIGURAR MLFLOW
# =====================================================

mlflow.set_tracking_uri("http://127.0.0.1:9090")

# =====================================================
# CARGAR MODELO
# =====================================================

modelo = mlflow.sklearn.load_model(
    "models:/Modelo_tarea2/1"
)

# =====================================================
# INTERFAZ
# =====================================================

st.title("Predicción de aprobación de estudiantes")

st.write(
    "Sistema de Machine Learning usando MLflow y Streamlit"
)

# =====================================================
# ENTRADAS
# =====================================================

carrera = st.selectbox(
    "Carrera",
    [
        "Computacion",
        "Derecho",
        "Economia",
        "Medicina",
        "Arquitectura",
        "Industrial"
    ]
)

modalidad = st.selectbox(
    "Modalidad",
    [
        "Presencial",
        "Virtual",
        "Hibrida"
    ]
)

beca = st.selectbox(
    "Beca",
    [
        "Si",
        "No"
    ]
)

edad = st.slider(
    "Edad",
    18,
    30,
    22
)

promedio = st.slider(
    "Promedio",
    0.0,
    10.0,
    7.0
)

asistencias = st.slider(
    "Asistencias",
    0,
    100,
    80
)

# =====================================================
# PREDICCIÓN
# =====================================================

if st.button("Predecir"):

    datos = pd.DataFrame([{

        "carrera": carrera,
        "modalidad": modalidad,
        "beca": beca,
        "edad": edad,
        "promedio": promedio,
        "asistencias": asistencias

    }])

    prediccion = modelo.predict(datos)[0]

    probabilidad = modelo.predict_proba(datos)[0][1]

    st.subheader("Resultado")

    if prediccion == 1:

        st.success(
            "El estudiante probablemente APRUEBA"
        )

    else:

        st.error(
            "El estudiante probablemente NO APRUEBA"
        )

    st.write(
        f"Probabilidad de aprobación: {probabilidad:.2%}"
    )

    st.write("Datos ingresados:")

    st.dataframe(datos)