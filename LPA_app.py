# -*- coding: utf-8 -*-
"""
Created on Wed Dec 17 09:13:36 2025
@author: acer
"""

import streamlit as st
import pandas as pd
import altair as alt
import requests
from io import StringIO
import urllib3
from datetime import datetime
import json

# Deshabilitar advertencias de SSL
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# 1. CONFIGURACIÓN DE LA PÁGINA
st.set_page_config(page_title="Analisis LPA Dashboard", page_icon="📊", layout="wide")

# 2. ESTILO DARK PREMIUM
st.markdown("""
    <style># app.py
import streamlit as st
from supabase import create_client, Client
from datetime import datetime
import uuid
import pandas as pd
import altair as alt
import json
import base64
import time

# ------------------------------------------------------------
# Configuración desde secrets.toml
# ------------------------------------------------------------
SUPABASE_URL = st.secrets["SUPABASE_URL"]
SUPABASE_KEY = st.secrets["SUPABASE_KEY"]
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

# ------------------------------------------------------------
# Estilos personalizados (colores del logo)
# ------------------------------------------------------------
def aplicar_estilos():
    st.markdown("""
    <style>
    /* Fuente moderna */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');

    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }

    /* Fondo principal oscuro */
    .stApp {
        background: #0a0c10 !important;
    }

    /* Fondo de bloques y contenedores */
    .stMarkdown, .stTextInput, .stSelectbox, .stTextArea, .stDateInput {
        background: transparent !important;
    }

    /* Botones principales */
    .stButton > button {
        background-color: #1e3a8a !important;
        color: white !important;
        border: none !important;
        border-radius: 8px !important;
        padding: 0.5rem 1rem !important;
        font-weight: 600 !important;
        transition: all 0.3s ease !important;
    }
    .stButton > button:hover {
        background-color: #3b82f6 !important;
        box-shadow: 0 4px 12px rgba(59,130,246,0.3) !important;
        transform: translateY(-1px);
    }

    /* Sidebar oscuro */
    [data-testid="stSidebar"] {
        background-color: #0f172a !important;
        border-right: 1px solid #1e293b !important;
    }
    [data-testid="stSidebar"] * {
        color: #e2e8f0 !important;
    }
    [data-testid="stSidebar"] .stSelectbox label,
    [data-testid="stSidebar"] .stMultiSelect label {
        color: #94a3b8 !important;
    }

    /* Métricas (KPIs) en modo oscuro */
    [data-testid="stMetric"] {
        background-color: #1e293b !important;
        border-radius: 16px !important;
        padding: 1rem !important;
        box-shadow: 0 4px 6px -1px rgba(0,0,0,0.3) !important;
        border: 1px solid #334155 !important;
    }
    [data-testid="stMetric"] label {
        color: #60a5fa !important;
        font-weight: 600 !important;
    }
    [data-testid="stMetric"] .stMetricValue {
        color: #f1f5f9 !important;
        font-size: 2rem !important;
        font-weight: 700 !important;
    }

    /* Expanders en modo oscuro */
    .streamlit-expanderHeader {
        background-color: #1e293b !important;
        border-radius: 12px !important;
        border: 1px solid #334155 !important;
        font-weight: 600 !important;
        color: #60a5fa !important;
    }
    .streamlit-expanderContent {
        background-color: #0f172a !important;
        border-radius: 12px !important;
        padding: 1rem !important;
        border: 1px solid #334155 !important;
        border-top: none !important;
        color: #e2e8f0 !important;
    }

    /* Inputs, selects, textarea en oscuro */
    .stTextInput input, .stTextArea textarea, .stSelectbox div[data-baseweb="select"] > div,
    .stDateInput input {
        background-color: #1e293b !important;
        color: #f1f5f9 !important;
        border: 1px solid #334155 !important;
        border-radius: 8px !important;
    }
    .stTextInput label, .stTextArea label, .stSelectbox label, .stDateInput label {
        color: #94a3b8 !important;
    }

    /* Radio buttons y checkboxes en oscuro */
    .stRadio label, .stCheckbox label {
        color: #e2e8f0 !important;
    }
    .stRadio div[role="radiogroup"] {
        background-color: transparent !important;
    }

    /* Títulos y texto general */
    h1, h2, h3, h4, h5, h6, .stMarkdown h1, .stMarkdown h2, .stMarkdown h3 {
        color: #60a5fa !important;
    }
    p, li, .stMarkdown {
        color: #cbd5e1 !important;
    }

    /* Tarjeta de login oscura */
    .login-card {
        background-color: #1e293b !important;
        border-radius: 24px;
        padding: 2rem;
        box-shadow: 0 20px 35px -10px rgba(0,0,0,0.5);
        text-align: center;
        max-width: 450px;
        margin: 0 auto;
        border: 1px solid #334155;
    }
    .login-title {
        font-size: 1.8rem;
        font-weight: 700;
        color: #60a5fa !important;
        margin-bottom: 0.5rem;
    }
    .login-subtitle {
        color: #94a3b8 !important;
        margin-bottom: 2rem;
        font-size: 0.9rem;
    }
    .login-footer {
        margin-top: 2rem;
        font-size: 0.75rem;
        color: #64748b !important;
        text-align: center;
    }

    /* Tablas en modo oscuro */
    .dataframe {
        border-radius: 12px !important;
        overflow: hidden !important;
        border: 1px solid #334155 !important;
        background-color: #0f172a;
    }
    .dataframe th {
        background-color: #1e3a8a !important;
        color: white !important;
        font-weight: 600 !important;
    }
    .dataframe td {
        background-color: #1e293b !important;
        color: #e2e8f0 !important;
    }
    .dataframe tr:hover td {
        background-color: #334155 !important;
    }

    /* Tooltips Vega (hovers) en oscuro */
    #vg-tooltip-element {
        background-color: #0f172a !important;
        color: #f1f5f9 !important;
        border-radius: 8px !important;
        border: 1px solid #3b82f6 !important;
        font-family: 'Inter', sans-serif !important;
    }

    /* Mensajes de éxito, error, info, warning en modo oscuro */
    .stAlert {
        background-color: #1e293b !important;
        border-left: 4px solid #3b82f6 !important;
    }
    .stAlert p {
        color: #e2e8f0 !important;
    }
    .stSuccess {
        background-color: #0f3d28 !important;
    }
    .stError {
        background-color: #4a0b0b !important;
    }
    .stWarning {
        background-color: #4a3b0b !important;
    }
    .stInfo {
        background-color: #0f2e4a !important;
    }
    </style>
    """, unsafe_allow_html=True)

# ------------------------------------------------------------
# Autenticación y sesión
# ------------------------------------------------------------
def init_session():
    if "authenticated" not in st.session_state:
        st.session_state.authenticated = False
        st.session_state.user = None
        st.session_state.rol = None

def login(email, password):
    try:
        resp = supabase.auth.sign_in_with_password({"email": email, "password": password})
        user = resp.user
        profile = supabase.from_("profiles").select("rol").eq("id", user.id).execute()
        rol = profile.data[0]["rol"] if profile.data else "inspector"
        st.session_state.authenticated = True
        st.session_state.user = user
        st.session_state.rol = rol
        return True
    except Exception as e:
        st.error(f"❌ {e}")
        return False

def signup(email, password):
    try:
        resp = supabase.auth.sign_up({"email": email, "password": password})
        if resp.user:
            st.success("✅ Registro exitoso. Ahora inicia sesión.")
            return True
        return False
    except Exception as e:
        st.error(f"❌ {e}")
        return False

def logout():
    supabase.auth.sign_out()
    st.session_state.clear()
    init_session()
    st.rerun()

# ------------------------------------------------------------
# Subida de imágenes a Storage
# ------------------------------------------------------------
def upload_image(file, folder="evidencias"):
    if file is None:
        return None
    ext = file.name.split(".")[-1]
    file_name = f"{uuid.uuid4()}.{ext}"
    file_path = f"{folder}/{file_name}"
    try:
        supabase.storage.from_("evidencias_lpa").upload(file_path, file.getvalue())
        return supabase.storage.from_("evidencias_lpa").get_public_url(file_path)
    except Exception as e:
        st.warning(f"Error subiendo imagen: {e}")
        return None

def upload_multiple_images(files_dict):
    urls = {}
    for key, file in files_dict.items():
        if file:
            urls[key] = upload_image(file, folder="lpa_evidencias")
        else:
            urls[key] = None
    return urls

def get_base64_logo():
    try:
        with open("EA_2.png", "rb") as f:
            return base64.b64encode(f.read()).decode()
    except:
        return None

# ------------------------------------------------------------
# Formulario Nivel 1 (C1 a C8, una subpregunta cada uno)
# ------------------------------------------------------------
def form_nivel_1():
    st.title("📋 Auditoría LPA - Nivel 1")
    with st.form(key="form_nivel_1"):
        # Datos generales
        col1, col2 = st.columns(2)
        with col1:
            fecha = st.date_input("Fecha", datetime.today())
            turno = st.selectbox("Selecciona el turno", ["Matutino", "Vespertino", "Nocturno"])
            area = st.text_input("Área / Célula")
        with col2:
            maquina = st.text_input("Máquina")
            operacion = st.text_input("Operación")
            supervisor = st.text_input("Nombre del Supervisor")
            ingeniero = st.text_input("Nombre del Ingeniero")
            num_parte = st.text_input("Número de Parte o Modelo")

        resp = {}
        fotos = {}

        # C1 - Alerta
        with st.expander("🔔 C1 - Acciones recomendadas en la alerta"):
            resp["c1_1"] = st.radio(
                "C1_1 ¿Se están siguiendo las acciones recomendadas en la alerta?",
                ["Cumple", "No Cumple", "N/A"], key="c1_1"
            )
            resp["obs_c1"] = st.text_area("Observaciones C1")
            resp["sol_c1"] = st.text_area("Solución propuesta C1")
            col_f1, col_f2 = st.columns(2)
            with col_f1:
                fotos["c1_antes"] = st.file_uploader("Foto ANTES C1", type=["jpg","png"], key="foto_c1_antes")
            with col_f2:
                fotos["c1_despues"] = st.file_uploader("Foto DESPUÉS C1", type=["jpg","png"], key="foto_c1_despues")

        # C2 - Poka Yokes
        with st.expander("⚙️ C2 - Poka Yokes o dispositivos secuenciales"):
            resp["c2_1"] = st.radio(
                "C2_1 ¿Los Poka yokes o dispositivos secuenciales están funcionando?",
                ["Cumple", "No Cumple", "N/A"], key="c2_1"
            )
            resp["obs_c2"] = st.text_area("Observaciones C2")
            resp["sol_c2"] = st.text_area("Solución propuesta C2")
            col_f1, col_f2 = st.columns(2)
            with col_f1:
                fotos["c2_antes"] = st.file_uploader("Foto ANTES C2", type=["jpg","png"], key="foto_c2_antes")
            with col_f2:
                fotos["c2_despues"] = st.file_uploader("Foto DESPUÉS C2", type=["jpg","png"], key="foto_c2_despues")

        # C3 - Instrucciones de trabajo
        with st.expander("📄 C3 - Instrucciones de trabajo o QPS"):
            resp["c3_1"] = st.radio(
                "C3_1 ¿Se encuentran las instrucciones de trabajo o QPS en la estación?",
                ["Cumple", "No Cumple", "N/A"], key="c3_1"
            )
            resp["obs_c3"] = st.text_area("Observaciones C3")
            resp["sol_c3"] = st.text_area("Solución propuesta C3")
            col_f1, col_f2 = st.columns(2)
            with col_f1:
                fotos["c3_antes"] = st.file_uploader("Foto ANTES C3", type=["jpg","png"], key="foto_c3_antes")
            with col_f2:
                fotos["c3_despues"] = st.file_uploader("Foto DESPUÉS C3", type=["jpg","png"], key="foto_c3_despues")

        # C4 - Plan de Control
        with st.expander("📑 C4 - Plan de Control"):
            resp["c4_1"] = st.radio(
                "C4_1 ¿Se encuentra el plan de control en su área?",
                ["Cumple", "No Cumple", "N/A"], key="c4_1"
            )
            resp["obs_c4"] = st.text_area("Observaciones C4")
            resp["sol_c4"] = st.text_area("Solución propuesta C4")
            col_f1, col_f2 = st.columns(2)
            with col_f1:
                fotos["c4_antes"] = st.file_uploader("Foto ANTES C4", type=["jpg","png"], key="foto_c4_antes")
            with col_f2:
                fotos["c4_despues"] = st.file_uploader("Foto DESPUÉS C4", type=["jpg","png"], key="foto_c4_despues")

        # C5 - Gráficos de control
        with st.expander("📈 C5 - Gráficos de control"):
            resp["c5_1"] = st.radio(
                "C5_1 ¿Se está llevando el gráfico requerido de control (Software, XR, Tendencia, etc.)? / ¿Se encuentra dentro de control?",
                ["Cumple", "No Cumple", "N/A"], key="c5_1"
            )
            resp["obs_c5"] = st.text_area("Observaciones C5")
            resp["sol_c5"] = st.text_area("Solución propuesta C5")
            col_f1, col_f2 = st.columns(2)
            with col_f1:
                fotos["c5_antes"] = st.file_uploader("Foto ANTES C5", type=["jpg","png"], key="foto_c5_antes")
            with col_f2:
                fotos["c5_despues"] = st.file_uploader("Foto DESPUÉS C5", type=["jpg","png"], key="foto_c5_despues")

        # C6 - Entrenamiento y certificación
        with st.expander("🎓 C6 - Entrenamiento y certificación"):
            resp["c6_1"] = st.radio(
                "C6_1 ¿La persona en la operación se encuentra certificada y está documentado en la matriz de entrenamiento?",
                ["Cumple", "No Cumple", "N/A"], key="c6_1"
            )
            resp["obs_c6"] = st.text_area("Observaciones C6")
            resp["sol_c6"] = st.text_area("Solución propuesta C6")
            col_f1, col_f2 = st.columns(2)
            with col_f1:
                fotos["c6_antes"] = st.file_uploader("Foto ANTES C6", type=["jpg","png"], key="foto_c6_antes")
            with col_f2:
                fotos["c6_despues"] = st.file_uploader("Foto DESPUÉS C6", type=["jpg","png"], key="foto_c6_despues")

        # C7 - Materiales
        with st.expander("📦 C7 - Materiales de entrada/salida y no conformes"):
            resp["c7_1"] = st.radio(
                "C7_1 ¿Están los materiales de Entrada / salida y no conformantes identificados?",
                ["Cumple", "No Cumple", "N/A"], key="c7_1"
            )
            resp["obs_c7"] = st.text_area("Observaciones C7")
            resp["sol_c7"] = st.text_area("Solución propuesta C7")
            col_f1, col_f2 = st.columns(2)
            with col_f1:
                fotos["c7_antes"] = st.file_uploader("Foto ANTES C7", type=["jpg","png"], key="foto_c7_antes")
            with col_f2:
                fotos["c7_despues"] = st.file_uploader("Foto DESPUÉS C7", type=["jpg","png"], key="foto_c7_despues")

        # C8 - Calibración
        with st.expander("🔧 C8 - Calibración de instrumentos"):
            resp["c8_1"] = st.radio(
                "C8_1 ¿La fecha de calibración aún está vigente?",
                ["Cumple", "No Cumple", "N/A"], key="c8_1"
            )
            resp["obs_c8"] = st.text_area("Observaciones C8")
            resp["sol_c8"] = st.text_area("Solución propuesta C8")
            col_f1, col_f2 = st.columns(2)
            with col_f1:
                fotos["c8_antes"] = st.file_uploader("Foto ANTES C8", type=["jpg","png"], key="foto_c8_antes")
            with col_f2:
                fotos["c8_despues"] = st.file_uploader("Foto DESPUÉS C8", type=["jpg","png"], key="foto_c8_despues")

        # Información adicional (IDs y trazabilidad)
        with st.expander("📎 Información adicional (IDs y trazabilidad)"):
            info_alerta = st.text_input("Info Alerta C1")
            id_dispositivo = st.text_input("ID Dispositivo y Función C2")
            id_qps = st.text_input("ID QPS C3")
            id_nomina = st.text_input("ID Nómina y Porcentaje Avance C6")
            id_control = st.text_input("ID Control")

        submitted = st.form_submit_button("✅ Enviar Auditoría Nivel 1")
        if submitted:
            urls = upload_multiple_images(fotos)
            data = {
                "nombre_auditor": st.session_state.user.email,
                "fecha": str(fecha),
                "turno": turno,
                "nombre_supervisor": supervisor,
                "nombre_ingeniero": ingeniero,
                "num_parte_modelo": num_parte,
                "area_celula": area,
                "maquina": maquina,
                "operacion": operacion,
                "c1_1_sigue_acciones": resp["c1_1"],
                "resultado_c1": resp["c1_1"],
                "obs_c1": resp["obs_c1"],
                "sol_c1": resp["sol_c1"],
                "foto_antes_c1": urls.get("c1_antes"),
                "foto_despues_c1": urls.get("c1_despues"),
                "c2_1_poka_yokes_funcionando": resp["c2_1"],
                "resultado_c2": resp["c2_1"],
                "obs_c2": resp["obs_c2"],
                "sol_c2": resp["sol_c2"],
                "foto_antes_c2": urls.get("c2_antes"),
                "foto_despues_c2": urls.get("c2_despues"),
                "c3_1_instrucciones_trabajo": resp["c3_1"],
                "resultado_c3": resp["c3_1"],
                "obs_c3": resp["obs_c3"],
                "sol_c3": resp["sol_c3"],
                "foto_antes_c3": urls.get("c3_antes"),
                "foto_despues_c3": urls.get("c3_despues"),
                "c4_1_plan_control": resp["c4_1"],
                "resultado_c4": resp["c4_1"],
                "obs_c4": resp["obs_c4"],
                "sol_c4": resp["sol_c4"],
                "foto_antes_c4": urls.get("c4_antes"),
                "foto_despues_c4": urls.get("c4_despues"),
                "c5_1_grafico_control": resp["c5_1"],
                "resultado_c5": resp["c5_1"],
                "obs_c5": resp["obs_c5"],
                "sol_c5": resp["sol_c5"],
                "foto_antes_c5": urls.get("c5_antes"),
                "foto_despues_c5": urls.get("c5_despues"),
                "c6_1_certificado": resp["c6_1"],
                "resultado_c6": resp["c6_1"],
                "obs_c6": resp["obs_c6"],
                "sol_c6": resp["sol_c6"],
                "foto_antes_c6": urls.get("c6_antes"),
                "foto_despues_c6": urls.get("c6_despues"),
                "c7_1_materiales_identificados": resp["c7_1"],
                "resultado_c7": resp["c7_1"],
                "obs_c7": resp["obs_c7"],
                "sol_c7": resp["sol_c7"],
                "foto_antes_c7": urls.get("c7_antes"),
                "foto_despues_c7": urls.get("c7_despues"),
                "c8_1_calibracion_vigente": resp["c8_1"],
                "resultado_c8": resp["c8_1"],
                "obs_c8": resp["obs_c8"],
                "sol_c8": resp["sol_c8"],
                "foto_antes_c8": urls.get("c8_antes"),
                "foto_despues_c8": urls.get("c8_despues"),
                # Campos adicionales de trazabilidad (igual que en el CSV)
                "info_alerta_c1": info_alerta,
                "id_dispositivo_funcion_c2": id_dispositivo,
                "id_qps_c3": id_qps,
                "id_nomina_porcentaje_c6": id_nomina,
                "id_control": id_control,
                "user_id": st.session_state.user.id,
            }
            try:
                supabase.from_("lpa_nivel_1").insert(data).execute()
                st.success("✅ Auditoría Nivel 1 guardada exitosamente.")
                st.balloons()
                st.rerun()
            except Exception as e:
                st.error(f"Error al guardar: {e}")

# ------------------------------------------------------------
# Formulario Nivel 2 (completo, con todas las subpreguntas hasta C12)
# ------------------------------------------------------------
def form_nivel_2():
    st.title("📋 Auditoría LPA - Nivel 2")
    with st.form(key="form_nivel_2"):
        # Datos generales
        col1, col2 = st.columns(2)
        with col1:
            fecha = st.date_input("Fecha", datetime.today())
            turno = st.selectbox("Turno", ["Matutino", "Vespertino", "Nocturno"])
            area = st.text_input("Área / Célula")
        with col2:
            maquina = st.text_input("Máquina o Célula")
            operacion = st.text_input("Operación")
            supervisor = st.text_input("Nombre del Supervisor")
            ingeniero = st.text_input("Nombre del Ingeniero")
            num_parte = st.text_input("Número de Parte")

        resp = {}   # almacena todas las respuestas
        fotos = {}  # almacena los file uploaders

        # ================= SECCIÓN C1 =================
        with st.expander("🔔 C1 - Alertas publicadas"):
            resp["c1_1"] = st.radio("C1_1 - Operador conoce las alertas publicadas",
                                    ["Cumple","No Cumple","N/A"], key="c1_1")
            resp["c1_2"] = st.radio("C1_2 - Se siguen las acciones recomendadas",
                                    ["Cumple","No Cumple","N/A"], key="c1_2")
            resp["c1_3"] = st.radio("C1_3 - La alerta está vigente",
                                    ["Cumple","No Cumple","N/A"], key="c1_3")
            resp["obs_c1"] = st.text_area("Observaciones C1")
            resp["sol_c1"] = st.text_area("Solución propuesta C1")
            col_f1, col_f2 = st.columns(2)
            with col_f1:
                fotos["c1_antes"] = st.file_uploader("Foto ANTES C1", type=["jpg","png"], key="foto_c1_antes")
            with col_f2:
                fotos["c1_despues"] = st.file_uploader("Foto DESPUÉS C1", type=["jpg","png"], key="foto_c1_despues")

        # ================= SECCIÓN C2 =================
        with st.expander("⚙️ C2 - Poka Yokes"):
            resp["c2_1"] = st.radio("C2_1 - ¿Poka Yoke funcionando?",
                                    ["Cumple","No Cumple","N/A"], key="c2_1")
            resp["c2_2"] = st.radio("C2_2 - ¿Cuenta con pieza rabbit?",
                                    ["Cumple","No Cumple","N/A"], key="c2_2")
            resp["c2_3"] = st.radio("C2_3 - ¿Operador sigue plan de reacción?",
                                    ["Cumple","No Cumple","N/A"], key="c2_3")
            resp["c2_4"] = st.radio("C2_4 - ¿Los Poka Yokes están identificados?",
                                    ["Cumple","No Cumple","N/A"], key="c2_4")
            resp["c2_5"] = st.radio("C2_5 - ¿Controlados en Plan de Control?",
                                    ["Cumple","No Cumple","N/A"], key="c2_5")
            resp["c2_6"] = st.radio("C2_6 - ¿Parámetros definidos?",
                                    ["Cumple","No Cumple","N/A"], key="c2_6")
            resp["obs_c2"] = st.text_area("Observaciones C2")
            resp["sol_c2"] = st.text_area("Solución propuesta C2")
            col_f1, col_f2 = st.columns(2)
            with col_f1:
                fotos["c2_antes"] = st.file_uploader("Foto ANTES C2", type=["jpg","png"], key="foto_c2_antes")
            with col_f2:
                fotos["c2_despues"] = st.file_uploader("Foto DESPUÉS C2", type=["jpg","png"], key="foto_c2_despues")

        # ================= SECCIÓN C3 =================
        with st.expander("📄 C3 - Instrucciones de trabajo / QPS"):
            resp["c3_1"] = st.radio("C3_1 - ¿Instrucción en la estación?",
                                    ["Cumple","No Cumple","N/A"], key="c3_1")
            resp["c3_2"] = st.radio("C3_2 - ¿Encabezados correctos?",
                                    ["Cumple","No Cumple","N/A"], key="c3_2")
            resp["c3_3"] = st.radio("C3_3 - ¿Opera según instrucción?",
                                    ["Cumple","No Cumple","N/A"], key="c3_3")
            resp["c3_4"] = st.radio("C3_4 - ¿Ayudas visuales en operación?",
                                    ["Cumple","No Cumple","N/A"], key="c3_4")
            resp["c3_5"] = st.radio("C3_5 - ¿Interpreta ayudas visuales?",
                                    ["Cumple","No Cumple","N/A"], key="c3_5")
            resp["c3_6"] = st.radio("C3_6 - ¿Llena reportes en forma y tiempo?",
                                    ["Cumple","No Cumple","N/A"], key="c3_6")
            resp["c3_7"] = st.radio("C3_7 - ¿Característica especial en QPS = Plan de Control?",
                                    ["Cumple","No Cumple","N/A"], key="c3_7")
            resp["obs_c3"] = st.text_area("Observaciones C3")
            resp["sol_c3"] = st.text_area("Solución propuesta C3")
            col_f1, col_f2 = st.columns(2)
            with col_f1:
                fotos["c3_antes"] = st.file_uploader("Foto ANTES C3", type=["jpg","png"], key="foto_c3_antes")
            with col_f2:
                fotos["c3_despues"] = st.file_uploader("Foto DESPUÉS C3", type=["jpg","png"], key="foto_c3_despues")

        # ================= SECCIÓN C4 =================
        with st.expander("📑 C4 - Plan de Control"):
            resp["c4_1"] = st.radio("C4_1 - ¿Supervisor tiene plan de control?",
                                    ["Cumple","No Cumple","N/A"], key="c4_1")
            resp["c4_2"] = st.radio("C4_2 - ¿Plan más actual?",
                                    ["Cumple","No Cumple","N/A"], key="c4_2")
            resp["c4_3"] = st.radio("C4_3 - ¿Sello copia controlada legible?",
                                    ["Cumple","No Cumple","N/A"], key="c4_3")
            resp["obs_c4"] = st.text_area("Observaciones C4")
            resp["sol_c4"] = st.text_area("Solución propuesta C4")
            col_f1, col_f2 = st.columns(2)
            with col_f1:
                fotos["c4_antes"] = st.file_uploader("Foto ANTES C4", type=["jpg","png"], key="foto_c4_antes")
            with col_f2:
                fotos["c4_despues"] = st.file_uploader("Foto DESPUÉS C4", type=["jpg","png"], key="foto_c4_despues")

        # ================= SECCIÓN C5 =================
        with st.expander("📈 C5 - Gráficos de control"):
            resp["c5_1"] = st.radio("C5_1 - ¿Gráfico requerido?",
                                    ["Cumple","No Cumple","N/A"], key="c5_1")
            resp["c5_2"] = st.radio("C5_2 - ¿Dentro de especificaciones?",
                                    ["Cumple","No Cumple","N/A"], key="c5_2")
            resp["c5_3"] = st.radio("C5_3 - ¿Dentro de control?",
                                    ["Cumple","No Cumple","N/A"], key="c5_3")
            resp["c5_4"] = st.radio("C5_4 - ¿Seguimiento plan reacción?",
                                    ["Cumple","No Cumple","N/A"], key="c5_4")
            resp["c5_5"] = st.radio("C5_5 - ¿Característica dentro de especificación?",
                                    ["Cumple","No Cumple","N/A"], key="c5_5")
            resp["obs_c5"] = st.text_area("Observaciones C5")
            resp["sol_c5"] = st.text_area("Solución propuesta C5")
            col_f1, col_f2 = st.columns(2)
            with col_f1:
                fotos["c5_antes"] = st.file_uploader("Foto ANTES C5", type=["jpg","png"], key="foto_c5_antes")
            with col_f2:
                fotos["c5_despues"] = st.file_uploader("Foto DESPUÉS C5", type=["jpg","png"], key="foto_c5_despues")

        # ================= SECCIÓN C6 =================
        with st.expander("🎓 C6 - Entrenamiento"):
            resp["c6_1"] = st.radio("C6_1 - ¿Operador entrenado?",
                                    ["Cumple","No Cumple","N/A"], key="c6_1")
            resp["c6_2"] = st.radio("C6_2 - ¿Autónomo alcanza 50% certificación?",
                                    ["Cumple","No Cumple","N/A"], key="c6_2")
            resp["c6_3"] = st.radio("C6_3 - ¿Nombre en matriz de versatilidad?",
                                    ["Cumple","No Cumple","N/A"], key="c6_3")
            resp["c6_4"] = st.radio("C6_4 - ¿En entrenamiento no opera CS?",
                                    ["Cumple","No Cumple","N/A"], key="c6_4")
            resp["c6_5"] = st.radio("C6_5 - ¿Gafete identificación?",
                                    ["Cumple","No Cumple","N/A"], key="c6_5")
            resp["obs_c6"] = st.text_area("Observaciones C6")
            resp["sol_c6"] = st.text_area("Solución propuesta C6")
            col_f1, col_f2 = st.columns(2)
            with col_f1:
                fotos["c6_antes"] = st.file_uploader("Foto ANTES C6", type=["jpg","png"], key="foto_c6_antes")
            with col_f2:
                fotos["c6_despues"] = st.file_uploader("Foto DESPUÉS C6", type=["jpg","png"], key="foto_c6_despues")

        # ================= SECCIÓN C7 =================
        with st.expander("📦 C7 - Materiales"):
            resp["c7_1"] = st.radio("C7_1 - ¿Materiales entrada/salida identificados?",
                                    ["Cumple","No Cumple","N/A"], key="c7_1")
            resp["c7_2"] = st.radio("C7_2 - ¿Materiales correctamente identificados?",
                                    ["Cumple","No Cumple","N/A"], key="c7_2")
            resp["c7_3"] = st.radio("C7_3 - ¿Operación identificada?",
                                    ["Cumple","No Cumple","N/A"], key="c7_3")
            resp["c7_4"] = st.radio("C7_4 - ¿No conformes con etiqueta amarilla?",
                                    ["Cumple","No Cumple","N/A"], key="c7_4")
            resp["c7_5"] = st.radio("C7_5 - ¿Bins con material productivo (evitar daños)?",
                                    ["Cumple","No Cumple","N/A"], key="c7_5")
            resp["c7_6"] = st.radio("C7_6 - ¿Trazabilidad en reproceso?",
                                    ["Cumple","No Cumple","N/A"], key="c7_6")
            resp["obs_c7"] = st.text_area("Observaciones C7")
            resp["sol_c7"] = st.text_area("Solución propuesta C7")
            col_f1, col_f2 = st.columns(2)
            with col_f1:
                fotos["c7_antes"] = st.file_uploader("Foto ANTES C7", type=["jpg","png"], key="foto_c7_antes")
            with col_f2:
                fotos["c7_despues"] = st.file_uploader("Foto DESPUÉS C7", type=["jpg","png"], key="foto_c7_despues")

        # ================= SECCIÓN C8 =================
        with st.expander("🔧 C8 - Calibración"):
            resp["c8_1"] = st.radio("C8_1 - ¿Identificados con número de control?",
                                    ["Cumple","No Cumple","N/A"], key="c8_1")
            resp["c8_2"] = st.radio("C8_2 - ¿Fecha calibración vigente?",
                                    ["Cumple","No Cumple","N/A"], key="c8_2")
            resp["c8_3"] = st.radio("C8_3 - ¿Usando los gages?",
                                    ["Cumple","No Cumple","N/A"], key="c8_3")
            resp["c8_4"] = st.radio("C8_4 - ¿Dañado?",
                                    ["Cumple","No Cumple","N/A"], key="c8_4")
            resp["obs_c8"] = st.text_area("Observaciones C8")
            resp["sol_c8"] = st.text_area("Solución propuesta C8")
            col_f1, col_f2 = st.columns(2)
            with col_f1:
                fotos["c8_antes"] = st.file_uploader("Foto ANTES C8", type=["jpg","png"], key="foto_c8_antes")
            with col_f2:
                fotos["c8_despues"] = st.file_uploader("Foto DESPUÉS C8", type=["jpg","png"], key="foto_c8_despues")

        # ================= SECCIÓN C9 =================
        with st.expander("🧹 C9 - 5S"):
            resp["c9_1"] = st.radio("C9_1 - ¿Área limpia?",
                                    ["Cumple","No Cumple","N/A"], key="c9_1")
            resp["c9_2"] = st.radio("C9_2 - ¿Área organizada?",
                                    ["Cumple","No Cumple","N/A"], key="c9_2")
            resp["c9_3"] = st.radio("C9_3 - ¿Área estandarizada?",
                                    ["Cumple","No Cumple","N/A"], key="c9_3")
            resp["c9_4"] = st.radio("C9_4 - ¿Logos correctos de la empresa?",
                                    ["Cumple","No Cumple","N/A"], key="c9_4")
            resp["c9_5"] = st.radio("C9_5 - ¿Herramientas apropiadas y usadas?",
                                    ["Cumple","No Cumple","N/A"], key="c9_5")
            resp["obs_c9"] = st.text_area("Observaciones C9")
            resp["sol_c9"] = st.text_area("Solución propuesta C9")
            col_f1, col_f2 = st.columns(2)
            with col_f1:
                fotos["c9_antes"] = st.file_uploader("Foto ANTES C9", type=["jpg","png"], key="foto_c9_antes")
            with col_f2:
                fotos["c9_despues"] = st.file_uploader("Foto DESPUÉS C9", type=["jpg","png"], key="foto_c9_despues")

        # ================= SECCIÓN C10 =================
        with st.expander("🚛 C10 - Dock Audit"):
            resp["c10_1"] = st.radio("C10_1 - ¿No libera producto sin IP completadas y aprobadas?",
                                    ["Cumple","No Cumple","N/A"], key="c10_1")
            resp["c10_2"] = st.text_input("C10_2 - # de TR de acuerdo a Plan de Control")
            resp["obs_c10"] = st.text_area("Observaciones C10")
            resp["sol_c10"] = st.text_area("Solución propuesta C10")
            col_f1, col_f2 = st.columns(2)
            with col_f1:
                fotos["c10_antes"] = st.file_uploader("Foto ANTES C10", type=["jpg","png"], key="foto_c10_antes")
            with col_f2:
                fotos["c10_despues"] = st.file_uploader("Foto DESPUÉS C10", type=["jpg","png"], key="foto_c10_despues")

        # ================= SECCIÓN C11 =================
        with st.expander("💡 C11 - Mejora continua"):
            resp["c11_1"] = st.radio("C11_1 - ¿Identifica hallazgos de mejora continua?",
                                    ["Cumple","No Cumple","N/A"], key="c11_1")
            resp["c11_2"] = st.radio("C11_2 - ¿Revisión llenado correcto de pizarrones?",
                                    ["Cumple","No Cumple","N/A"], key="c11_2")
            resp["obs_c11"] = st.text_area("Observaciones C11")
            resp["sol_c11"] = st.text_area("Solución propuesta C11")
            col_f1, col_f2 = st.columns(2)
            with col_f1:
                fotos["c11_antes"] = st.file_uploader("Foto ANTES C11", type=["jpg","png"], key="foto_c11_antes")
            with col_f2:
                fotos["c11_despues"] = st.file_uploader("Foto DESPUÉS C11", type=["jpg","png"], key="foto_c11_despues")

        # ================= SECCIÓN C12 =================
        with st.expander("🔗 C12 - Link entre documentos y trazabilidad"):
            resp["c12_1"] = st.radio("C12_1 - ¿Diagrama Flujo, PFMEA, PC, QPS, ayudas, checklists, matriz Poka Yokes linkeados?",
                                    ["Cumple","No Cumple","N/A"], key="c12_1")
            resp["c12_2"] = st.radio("C12_2 - ¿Trazabilidad de producto correcta?",
                                    ["Cumple","No Cumple","N/A"], key="c12_2")
            resp["obs_c12"] = st.text_area("Observaciones C12")
            resp["sol_c12"] = st.text_area("Solución propuesta C12")
            col_f1, col_f2 = st.columns(2)
            with col_f1:
                fotos["c12_antes"] = st.file_uploader("Foto ANTES C12", type=["jpg","png"], key="foto_c12_antes")
            with col_f2:
                fotos["c12_despues"] = st.file_uploader("Foto DESPUÉS C12", type=["jpg","png"], key="foto_c12_despues")

        # ================= CAMPOS EXTRA DE TRAZABILIDAD =================
        with st.expander("📎 Trazabilidad adicional (IDs, lotes, fechas)"):
            info_alerta = st.text_input("Info Alerta C1")
            id_poka = st.text_input("ID Poka Yoke Vigente C2")
            id_instrumento = st.text_input("ID Instrumento Control C2")
            valores_resultados = st.text_input("Valores y Resultados Obtenidos C2")
            id_ayudas = st.text_input("ID Ayudas Visuales C3")
            espec_y_resultado = st.text_input("Especificación y Resultado Parte Auditada C5")
            id_control = st.text_input("ID Control C8")
            fecha_vencimiento = st.date_input("Fecha Vencimiento C8", value=None)
            escribir_ids = st.text_input("Escribir los identificados C11")
            lote_serie = st.text_input("ID Lote / Número de Serie C12")

        # ------------------------------------------------------------
        # Botón de envío
        # ------------------------------------------------------------
        submitted = st.form_submit_button("✅ Enviar Auditoría Nivel 2")
        if submitted:
            # Subir todas las fotos
            urls = upload_multiple_images(fotos)

            # Función auxiliar para calcular resultado global de una sección
            def resultado_seccion(*args):
                if any(v == "No Cumple" for v in args if v in ["Cumple","No Cumple","N/A"]):
                    return "No Cumple"
                return "Cumple"

            data = {
                "nombre_auditor": st.session_state.user.email,
                "turno": turno, "fecha": str(fecha),
                "operacion": operacion, "maquina_celula": maquina,
                "area_celula": area, "num_parte": num_parte,
                "nombre_supervisor": supervisor, "nombre_ingeniero": ingeniero,
                # C1
                "c1_1_conoce_alerta": resp["c1_1"], "c1_2_sigue_acciones": resp["c1_2"],
                "c1_3_alerta_vigente": resp["c1_3"],
                "resultado_c1": resultado_seccion(resp["c1_1"], resp["c1_2"], resp["c1_3"]),
                "obs_c1": resp["obs_c1"], "sol_c1": resp["sol_c1"],
                "foto_antes_c1": urls.get("c1_antes"), "foto_despues_c1": urls.get("c1_despues"),
                # C2
                "c2_1_poka_yoke_funcionando": resp["c2_1"], "c2_2_pieza_rabbit": resp["c2_2"],
                "c2_3_sigue_plan_reaccion": resp["c2_3"], "c2_4_dispositivos_identificados": resp["c2_4"],
                "c2_5_controlados_plan_control": resp["c2_5"], "c2_6_parametros_definidos": resp["c2_6"],
                "resultado_c2": resultado_seccion(resp["c2_1"], resp["c2_2"], resp["c2_3"], resp["c2_4"], resp["c2_5"], resp["c2_6"]),
                "obs_c2": resp["obs_c2"], "sol_c2": resp["sol_c2"],
                "foto_antes_c2": urls.get("c2_antes"), "foto_despues_c2": urls.get("c2_despues"),
                # C3
                "c3_1_instruccion_trabajo": resp["c3_1"], "c3_2_encabezados_correctos": resp["c3_2"],
                "c3_3_opera_segun_instruccion": resp["c3_3"], "c3_4_ayudas_visuales": resp["c3_4"],
                "c3_5_interpreta_ayudas": resp["c3_5"], "c3_6_llena_reportes": resp["c3_6"],
                "c3_7_caracteristica_especial": resp["c3_7"],
                "resultado_c3": resultado_seccion(resp["c3_1"], resp["c3_2"], resp["c3_3"], resp["c3_4"], resp["c3_5"], resp["c3_6"], resp["c3_7"]),
                "obs_c3": resp["obs_c3"], "sol_c3": resp["sol_c3"],
                "foto_antes_c3": urls.get("c3_antes"), "foto_despues_c3": urls.get("c3_despues"),
                # C4
                "c4_1_supervisor_tiene_plan": resp["c4_1"], "c4_2_plan_actualizado": resp["c4_2"],
                "c4_3_sello_legible": resp["c4_3"],
                "resultado_c4": resultado_seccion(resp["c4_1"], resp["c4_2"], resp["c4_3"]),
                "obs_c4": resp["obs_c4"], "sol_c4": resp["sol_c4"],
                "foto_antes_c4": urls.get("c4_antes"), "foto_despues_c4": urls.get("c4_despues"),
                # C5
                "c5_1_llenando_grafico": resp["c5_1"], "c5_2_dentro_especificaciones": resp["c5_2"],
                "c5_3_dentro_control": resp["c5_3"], "c5_4_seguimiento_plan_reaccion": resp["c5_4"],
                "c5_5_caracteristica_espec_control": resp["c5_5"],
                "resultado_c5": resultado_seccion(resp["c5_1"], resp["c5_2"], resp["c5_3"], resp["c5_4"], resp["c5_5"]),
                "obs_c5": resp["obs_c5"], "sol_c5": resp["sol_c5"],
                "foto_antes_c5": urls.get("c5_antes"), "foto_despues_c5": urls.get("c5_despues"),
                # C6
                "c6_1_operador_entrenado": resp["c6_1"], "c6_2_autonomo_50_porciento": resp["c6_2"],
                "c6_3_nombre_en_matriz": resp["c6_3"], "c6_4_no_operacion_significante": resp["c6_4"],
                "c6_5_gafete_identificacion": resp["c6_5"],
                "resultado_c6": resultado_seccion(resp["c6_1"], resp["c6_2"], resp["c6_3"], resp["c6_4"], resp["c6_5"]),
                "obs_c6": resp["obs_c6"], "sol_c6": resp["sol_c6"],
                "foto_antes_c6": urls.get("c6_antes"), "foto_despues_c6": urls.get("c6_despues"),
                # C7
                "c7_1_materiales_identificados": resp["c7_1"], "c7_2_materiales_correctos": resp["c7_2"],
                "c7_3_operacion_identificada": resp["c7_3"], "c7_4_no_conformes_etiqueta": resp["c7_4"],
                "c7_5_bins_con_material_productivo": resp["c7_5"], "c7_6_trazabilidad_reproceso": resp["c7_6"],
                "resultado_c7": resultado_seccion(resp["c7_1"], resp["c7_2"], resp["c7_3"], resp["c7_4"], resp["c7_5"], resp["c7_6"]),
                "obs_c7": resp["obs_c7"], "sol_c7": resp["sol_c7"],
                "foto_antes_c7": urls.get("c7_antes"), "foto_despues_c7": urls.get("c7_despues"),
                # C8
                "c8_1_identificados_numero": resp["c8_1"], "c8_2_fecha_calibracion_vigente": resp["c8_2"],
                "c8_3_usando_gages": resp["c8_3"], "c8_4_danado": resp["c8_4"],
                "resultado_c8": resultado_seccion(resp["c8_1"], resp["c8_2"], resp["c8_3"], resp["c8_4"]),
                "obs_c8": resp["obs_c8"], "sol_c8": resp["sol_c8"],
                "foto_antes_c8": urls.get("c8_antes"), "foto_despues_c8": urls.get("c8_despues"),
                # C9
                "c9_1_area_limpia": resp["c9_1"], "c9_2_area_organizada": resp["c9_2"],
                "c9_3_area_estandarizada": resp["c9_3"], "c9_4_logos_correctos": resp["c9_4"],
                "c9_5_herramientas_apropiadas": resp["c9_5"],
                "resultado_c9": resultado_seccion(resp["c9_1"], resp["c9_2"], resp["c9_3"], resp["c9_4"], resp["c9_5"]),
                "obs_c9": resp["obs_c9"], "sol_c9": resp["sol_c9"],
                "foto_antes_c9": urls.get("c9_antes"), "foto_despues_c9": urls.get("c9_despues"),
                # C10
                "c10_1_no_liberar_sin_ip": resp["c10_1"], "c10_2_numero_tr": resp["c10_2"],
                "resultado_c10": resultado_seccion(resp["c10_1"]),
                "obs_c10": resp["obs_c10"], "sol_c10": resp["sol_c10"],
                "foto_antes_c10": urls.get("c10_antes"), "foto_despues_c10": urls.get("c10_despues"),
                # C11
                "c11_1_hallazgos_mejora": resp["c11_1"], "c11_2_pizarrones_comunicacion": resp["c11_2"],
                "resultado_c11": resultado_seccion(resp["c11_1"], resp["c11_2"]),
                "obs_c11": resp["obs_c11"], "sol_c11": resp["sol_c11"],
                "foto_antes_c11": urls.get("c11_antes"), "foto_despues_c11": urls.get("c11_despues"),
                # C12
                "c12_1_documentos_linkeados": resp["c12_1"], "c12_2_trazabilidad_producto": resp["c12_2"],
                "resultado_c12": resultado_seccion(resp["c12_1"], resp["c12_2"]),
                "obs_c12": resp["obs_c12"], "sol_c12": resp["sol_c12"],
                "foto_antes_c12": urls.get("c12_antes"), "foto_despues_c12": urls.get("c12_despues"),
                # Campos extra
                "info_alerta_c1": info_alerta, "id_poka_yoke_vigente_c2": id_poka,
                "id_instrumento_control_c2": id_instrumento, "valores_y_resultados_c2": valores_resultados,
                "id_ayudas_visuales_c3": id_ayudas, "espec_y_resultado_parte_c5": espec_y_resultado,
                "id_control_c8": id_control, "fecha_vencimiento_c8": str(fecha_vencimiento) if fecha_vencimiento else None,
                "escribir_identificados_c11": escribir_ids, "id_lote_numero_serie_c12": lote_serie,
                "user_id": st.session_state.user.id,
            }
            try:
                supabase.from_("lpa_nivel_2").insert(data).execute()
                st.success("✅ Auditoría Nivel 2 guardada exitosamente.")
                st.balloons()
                st.rerun()
            except Exception as e:
                st.error(f"Error al guardar: {e}")

# ------------------------------------------------------------
# Dashboard y gráficos
# ------------------------------------------------------------
def load_dashboard_data(nivel):
    if nivel == 1:
        data = supabase.from_("lpa_nivel_1").select("*").execute()
    else:
        data = supabase.from_("lpa_nivel_2").select("*").execute()
    df = pd.DataFrame(data.data)
    if df.empty:
        return None, None
    res_cols = [c for c in df.columns if c.startswith("resultado_c")]
    id_vars = [c for c in ["fecha", "nombre_auditor", "area_celula", "maquina", "maquina_celula", "turno"] if c in df.columns]
    extra = [c for c in df.columns if any(x in c for x in ["info_", "id_", "fecha_vencimiento", "valores_", "espec_"])]
    id_vars += extra
    melted = df.melt(id_vars=id_vars, value_vars=res_cols, var_name="cat_raw", value_name="estatus")
    melted["Categoría"] = melted["cat_raw"].str.extract(r"resultado_(C\d+)")
    melted["Estatus"] = melted["estatus"].astype(str).str.lower().apply(
        lambda x: "Cumple" if "cumple" in x and "no" not in x else "No Cumple"
    )
    return melted, df

def dashboard_global():
    st.title("📊 Dashboard Global de Cumplimiento LPA")
    nivel = st.radio("Selecciona nivel:", ["1er Nivel", "2do Nivel"], horizontal=True)
    nivel_num = 1 if nivel == "1er Nivel" else 2
    df_melted, df_raw = load_dashboard_data(nivel_num)
    if df_melted is None or df_melted.empty:
        st.warning("No hay datos aún para este nivel.")
        return

    # Filtros
    col_maq = "maquina" if "maquina" in df_melted.columns else "maquina_celula"
    f_aud = st.sidebar.multiselect("Auditor", df_melted["nombre_auditor"].unique())
    f_area = st.sidebar.multiselect("Área", df_melted["area_celula"].unique())
    f_maq = st.sidebar.multiselect("Máquina", df_melted[col_maq].unique())

    filtered = df_melted.copy()
    if f_aud: filtered = filtered[filtered["nombre_auditor"].isin(f_aud)]
    if f_area: filtered = filtered[filtered["area_celula"].isin(f_area)]
    if f_maq: filtered = filtered[filtered[col_maq].isin(f_maq)]

    cumplimiento = (filtered["Estatus"] == "Cumple").mean() * 100 if len(filtered) > 0 else 0
    col1, col2, col3 = st.columns(3)
    col1.metric("Cumplimiento Global", f"{cumplimiento:.1f}%")
    col2.metric("Auditorías", len(df_raw))
    col3.metric("Puntos Evaluados", len(filtered))

    # Gráfico 1: Cumplimiento por categoría
    bar = alt.Chart(filtered).mark_bar(size=40, cornerRadiusTopLeft=2, cornerRadiusTopRight=2).encode(
        x=alt.X('Categoría:N', sort=alt.EncodingSortField(field="Categoría", op="count", order='ascending')),
        y=alt.Y('count():Q', title='Cantidad'),
        color=alt.Color('Estatus:N', scale=alt.Scale(domain=['Cumple', 'No Cumple'], range=['#22c55e', '#ef4444'])),
        tooltip=['Categoría', 'Estatus', 'nombre_auditor']
    ).properties(height=450).interactive()
    st.altair_chart(bar, use_container_width=True)

    # Gráfico 2: Tendencia (convertir fecha a string para evitar error JSON)
    st.subheader("📈 Tendencia de Cumplimiento")
    filtered["fecha_dt"] = pd.to_datetime(filtered["fecha"])
    # Convertir la fecha a string para el gráfico (evita problemas de serialización en reporte)
    filtered["fecha_str"] = filtered["fecha_dt"].dt.strftime("%Y-%m-%d")
    trend = filtered.groupby("fecha_str")["Estatus"].apply(lambda x: (x == "Cumple").mean() * 100).reset_index()
    trend.columns = ["Fecha", "Cumplimiento"]
    line = alt.Chart(trend).mark_line(point=True, color='#3b82f6').encode(
        x=alt.X('Fecha:T', title='Fecha', axis=alt.Axis(format="%Y-%m-%d")),
        y=alt.Y('Cumplimiento:Q', title='% Cumplimiento', scale=alt.Scale(domain=[0, 105])),
        tooltip=['Fecha', 'Cumplimiento']
    ).properties(height=300).interactive()
    st.altair_chart(line, use_container_width=True)

    # Gráfico 3: Pareto de máquinas con hallazgos
    st.subheader("⚠️ Top Máquinas con Hallazgos")
    fallas = filtered[filtered["Estatus"] == "No Cumple"]
    if not fallas.empty:
        pareto_data = fallas[col_maq].value_counts().reset_index()
        pareto_data.columns = ["Máquina", "Conteo"]
        pareto_chart = alt.Chart(pareto_data).mark_bar(color='#ef4444').encode(
            x=alt.X('Conteo:Q', title='Fallas'),
            y=alt.Y('Máquina:N', sort='-x', title='Máquina'),
            tooltip=['Máquina', 'Conteo']
        ).properties(height=300).interactive()
        st.altair_chart(pareto_chart, use_container_width=True)
    else:
        pareto_chart = None
        st.success("✅ Sin hallazgos críticos.")

    # Botón de descarga de reporte HTML
    if st.button("📥 Descargar Reporte Gerencial (HTML)"):
        generar_reporte_html(filtered, df_raw, cumplimiento, nivel, bar, line, pareto_chart)

def generar_reporte_html(df_filtered, df_raw, cumplimiento, nivel, chart1, chart2, chart3):
    """Genera el reporte HTML con gráficos incrustados y logo"""
    # Convertir gráficos a JSON de forma segura
    chart1_json = chart1.to_json()
    chart2_json = chart2.to_json()
    chart3_json = chart3.to_json() if chart3 else "{}"

    # Tabla de hallazgos
    fallas = df_filtered[df_filtered["Estatus"] == "No Cumple"]
    cols_tabla = ["fecha", "nombre_auditor", "area_celula", "Categoría", "Estatus"]
    if "maquina" in df_filtered.columns:
        cols_tabla.append("maquina")
    elif "maquina_celula" in df_filtered.columns:
        cols_tabla.append("maquina_celula")
    extra = [c for c in df_filtered.columns if c.startswith(("info_", "id_", "fecha_vencimiento", "valores_", "espec_"))]
    cols_tabla = [c for c in cols_tabla if c in df_filtered.columns] + extra
    tabla_html = fallas[cols_tabla].to_html(classes='table table-dark table-striped text-center', index=False, justify='center')

    # Incrustar logo en base64
    logo_base64 = get_base64_logo()
    logo_img = f'<img src="data:image/png;base64,{logo_base64}" width="80" style="display:block; margin:0 auto;">' if logo_base64 else ""

    html_content = f"""
    <html>
    <head>
        <script src="https://cdn.jsdelivr.net/npm/vega@5"></script>
        <script src="https://cdn.jsdelivr.net/npm/vega-lite@5"></script>
        <script src="https://cdn.jsdelivr.net/npm/vega-embed@6"></script>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
        <style>
            body {{ background-color: #0e1117; color: white; font-family: 'Inter', sans-serif; padding: 30px; }}
            .card {{ background-color: #1c212d; border: 1px solid #3b82f6; border-radius: 15px; padding: 25px; margin-bottom: 25px; text-align: center; width: 100%; }}
            .kpi-card {{ border-left: 5px solid #3b82f6; }}
            .kpi-value {{ font-size: 2.5rem; font-weight: bold; color: #3b82f6; }}
            .kpi-label {{ font-size: 1rem; color: #94a3b8; text-transform: uppercase; }}
            h1, h2 {{ color: #3b82f6; text-align: center; font-weight: bold; margin-bottom: 20px; }}
            .table-responsive {{ border-radius: 10px; overflow: hidden; }}
            .table {{ color: white; margin: 0 auto; width: 100% !important; font-size: 0.9rem; }}
            .table th {{ background-color: #3b82f6 !important; color: white !important; text-align: center !important; }}
            .chart-frame {{ width: 100%; min-height: 450px; }}
            #vg-tooltip-element {{ background-color: #1c212d !important; color: #ffffff !important; border: 1px solid #3b82f6 !important; }}
            .footer-logo {{ margin-top: 30px; text-align: center; color: #3b82f6; }}
        </style>
    </head>
    <body>
        <div class="container-fluid">
            {logo_img}
            <h1>🚀 Reporte Gerencial LPA</h1>
            <p style="text-align: center; color: #94a3b8;">Nivel: {nivel} | Generado: {datetime.now().strftime('%d/%m/%Y %H:%M')}</p>
            <div class="row mb-4">
                <div class="col-md-4"><div class="card kpi-card"><div class="kpi-label">Cumplimiento</div><div class="kpi-value">{cumplimiento:.1f}%</div></div></div>
                <div class="col-md-4"><div class="card kpi-card"><div class="kpi-label">Auditorías</div><div class="kpi-value">{len(df_raw)}</div></div></div>
                <div class="col-md-4"><div class="card kpi-card"><div class="kpi-label">Evaluaciones</div><div class="kpi-value">{len(df_filtered)}</div></div></div>
            </div>
            <div class="card"><h2>📊 Cumplimiento por Categoría</h2><div id="vis1" class="chart-frame"></div></div>
            <div class="card"><h2>📈 Tendencia de Cumplimiento</h2><div id="vis2" class="chart-frame"></div></div>
            <div class="card"><h2>⚠️ Top Máquinas con Hallazgos</h2><div id="vis3" class="chart-frame"></div></div>
            <div class="card"><h2>🔍 Detalle de Hallazgos y Trazabilidad</h2><div class="table-responsive">{tabla_html}</div></div>
            <div class="footer-logo">
                {logo_img if logo_base64 else "Sistema LPA"}
                <p>Desarrollado por Master Engineer Erik Armenta</p>
            </div>
        </div>
        <script>
            const opt = {{ actions: {{export: true, source: false, compiled: false, editor: false}}, theme: 'dark', width: 'container' }};
            vegaEmbed('#vis1', {chart1_json}, opt);
            vegaEmbed('#vis2', {chart2_json}, opt);
            vegaEmbed('#vis3', {chart3_json}, opt);
        </script>
    </body>
    </html>
    """
    st.download_button("📥 Descargar HTML", data=html_content, file_name=f"reporte_lpa_{nivel}_{datetime.now().strftime('%Y%m%d_%H%M')}.html", mime="text/html")

# ------------------------------------------------------------
# Administración de usuarios (CRUD básico)
# ------------------------------------------------------------
def admin_usuarios():
    st.subheader("👥 Gestión de Usuarios - CRUD")

    # ------------------ CREAR NUEVO USUARIO ------------------
    with st.expander("➕ Crear nuevo usuario"):
        with st.form("nuevo_usuario"):
            new_email = st.text_input("Email")
            new_password = st.text_input("Contraseña", type="password")
            new_role = st.selectbox("Rol inicial", ["inspector", "submitter", "admin"])
            submitted_new = st.form_submit_button("Crear usuario")
            if submitted_new and new_email and new_password:
                # Llamar a la función signup (registra en auth.users y crea perfil automáticamente)
                try:
                    resp = supabase.auth.sign_up({"email": new_email, "password": new_password})
                    if resp.user:
                        # Esperar un momento a que el trigger cree el perfil
                        time.sleep(1)
                        # Actualizar el rol al seleccionado (por defecto 'inspector')
                        supabase.from_("profiles").update({"rol": new_role}).eq("id", resp.user.id).execute()
                        st.success(f"✅ Usuario {new_email} creado con rol {new_role}.")
                        st.rerun()
                    else:
                        st.error("Error al crear usuario.")
                except Exception as e:
                    st.error(f"Error: {e}")

    # ------------------ LISTAR Y GESTIONAR USUARIOS ------------------
    perfiles = supabase.from_("profiles").select("*").execute()
    if not perfiles.data:
        st.info("No hay usuarios en la tabla profiles.")
        return

    df_users = pd.DataFrame(perfiles.data)
    # Mostrar tabla completa
    st.dataframe(df_users[["email", "rol"]], use_container_width=True)

    # Seleccionar usuario para acciones
    user_email = st.selectbox("Selecciona usuario", df_users["email"])
    current_rol = df_users[df_users["email"] == user_email]["rol"].values[0]

    col1, col2 = st.columns(2)
    with col1:
        new_role = st.selectbox("Nuevo rol", ["admin", "inspector", "submitter"], index=["admin","inspector","submitter"].index(current_rol))
        if st.button("Actualizar rol"):
            supabase.from_("profiles").update({"rol": new_role}).eq("email", user_email).execute()
            st.success(f"Rol actualizado para {user_email} a {new_role}")
            st.rerun()

    with col2:
        if st.button("🗑️ Eliminar perfil (solo tabla profiles)"):
            supabase.from_("profiles").delete().eq("email", user_email).execute()
            st.warning(f"Perfil de {user_email} eliminado. El usuario aún puede iniciar sesión, pero no tendrá rol asociado.")
            st.rerun()

    # Nota sobre eliminación completa
    st.info("💡 Nota: Para eliminar completamente un usuario (incluyendo `auth.users`) se necesita la clave `service_role` de Supabase. Si la tienes, puedo ayudarte a integrarla.")

# ------------------------------------------------------------
# Interfaz principal
# ------------------------------------------------------------
def main():
    init_session()
    st.set_page_config(page_title="LPA Auditorías", page_icon="🔍", layout="wide")
    aplicar_estilos()   # Aplicar estilos personalizados

    if not st.session_state.authenticated:
        # Centrar el contenido del login
        col_center1, col_center2, col_center3 = st.columns([1, 2, 1])
        with col_center2:
            # Tarjeta de login
            st.markdown('<div class="login-card">', unsafe_allow_html=True)
            try:
                st.image("EA_2.png", width=100)
            except:
                pass
            st.markdown('<div class="login-title">LPA Auditorias</div>', unsafe_allow_html=True)
            st.markdown('<div class="login-subtitle">Sistema de Auditorías de Procesos</div>', unsafe_allow_html=True)

            opcion = st.radio("", ["Iniciar sesión", "Registrarse"], label_visibility="collapsed")
            email = st.text_input("Usuario", placeholder="correo@ejemplo.com")
            pwd = st.text_input("Contraseña", type="password", placeholder="••••••••")

            if opcion == "Iniciar sesión":
                if st.button("Ingresar", use_container_width=True):
                    if login(email, pwd):
                        st.rerun()
            else:
                if st.button("Crear cuenta", use_container_width=True):
                    if signup(email, pwd):
                        st.info("Ahora inicia sesión con tu nueva cuenta.")

            st.markdown('<div class="login-footer">Engineered by Erik Armenta, M.Eng. | Operational Excellence through Technology</div>', unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)
        return

    # Sidebar para usuarios autenticados
    try:
        st.sidebar.image("EA_2.png", width=100)
    except:
        pass
    st.sidebar.title("📋 Sistema LPA")
    st.sidebar.write(f"👤 **{st.session_state.user.email}**")
    st.sidebar.write(f"🎭 Rol: **{st.session_state.rol}**")
    if st.sidebar.button("Cerrar sesión"):
        logout()

    st.sidebar.divider()
    menu = []
    if st.session_state.rol in ["inspector", "submitter", "admin"]:
        menu.append("📝 Nueva Auditoría Nivel 1")
        menu.append("📝 Nueva Auditoría Nivel 2")
    if st.session_state.rol == "admin":
        menu.append("👑 Administración de Usuarios")
        menu.append("📊 Dashboard Global")

    choice = st.sidebar.radio("Ir a:", menu)

    if choice == "📝 Nueva Auditoría Nivel 1":
        form_nivel_1()
    elif choice == "📝 Nueva Auditoría Nivel 2":
        form_nivel_2()
    elif choice == "👑 Administración de Usuarios":
        admin_usuarios()
    elif choice == "📊 Dashboard Global":
        dashboard_global()

if __name__ == "__main__":
    main()
    .stApp { background-color: #0e1117; }
    div[data-testid="stMetric"] {
        background-color: #1c212d; border: 1px solid #3b82f6;
        padding: 20px; border-radius: 15px; text-align: center;
    }
    h1, h2, h3 { color: #3b82f6; font-family: 'Inter', sans-serif; }
    .stDownloadButton button {
        width: 100%;
        background-color: #1c212d;
        color: #3b82f6;
        border: 1px solid #3b82f6;
        border-radius: 10px;
    }
    .stDownloadButton button:hover {
        background-color: #3b82f6;
        color: white;
    }
    </style>
    """, unsafe_allow_html=True)

# --- ENLACES CSV TRANSFORMADOS ---
URL_1ER_NIVEL = "https://docs.google.com/spreadsheets/d/1V_DhqlKEgH13v9SLDfmPJBwXe9pwX_modSxeg7b52gQ/export?format=csv&gid=12953958"
URL_2DO_NIVEL = "https://docs.google.com/spreadsheets/d/13YqXoVENbDHNXM6Eq4ZlOOsvRXNO5gnY82gu1hUKa7k/export?format=csv&gid=1005755816"

@st.cache_data(ttl=60)
def load_data(url):
    try:
        response = requests.get(url, verify=False, timeout=10)
        if response.status_code == 200:
            df = pd.read_csv(StringIO(response.text))
            df.columns = df.columns.str.strip().str.replace('\n', ' ')
            if 'Marca temporal' in df.columns:
                df['Marca temporal'] = pd.to_datetime(df['Marca temporal'])
            return df
        return None
    except: return None

# 4. LÓGICA DE PROCESAMIENTO ACTUALIZADA PARA TRAZABILIDAD IATF
def get_melted_data(df):
    res_cols = [col for col in df.columns if 'Res' in col and '_C' in col]

    # Identificar columnas de información técnica adicional
    extra_info_cols = [c for c in df.columns if any(pref in c for pref in
                      ['Info_', 'ID_', 'Valores_', 'Espec_', 'Fecha_', 'Escribir', 'Valor_'])]

    col_auditor = next((c for c in df.columns if 'Auditor' in c), "Auditor")
    col_maquina = next((c for c in df.columns if any(x in c for x in ['Maquina', 'Célula', 'Celula'])), "Maquina")
    col_operacion = next((c for c in df.columns if 'Operación' in c or 'Operacion' in c), "Operacion")
    col_area = next((c for c in df.columns if 'Área' in c or 'Area' in c), "Area")
    col_turno = next((c for c in df.columns if 'Turno' in c), "Turno")
    col_supervisor = next((c for c in df.columns if 'Supervisor' in c), "Supervisor")
    col_ingeniero = next((c for c in df.columns if 'Ingeniero' in c), "Ingeniero")

    cols_dict = {
        'auditor': col_auditor, 'maquina': col_maquina, 'operacion': col_operacion,
        'area': col_area, 'turno': col_turno, 'supervisor': col_supervisor, 'ingeniero': col_ingeniero,
        'extra_info': extra_info_cols
    }

    meta_cols = [col_auditor, col_maquina, col_operacion, col_area, col_turno, col_supervisor, col_ingeniero, 'Marca temporal'] + extra_info_cols
    existing_meta = [c for c in meta_cols if c in df.columns]

    if not res_cols: return None, cols_dict

    df_melted = df.melt(id_vars=existing_meta, value_vars=res_cols,
                        var_name='Categoria_Raw', value_name='Estatus_Original')

    df_melted['Categoría'] = df_melted['Categoria_Raw'].str.extract(r'_(C\d+)')
    df_melted['Estatus'] = df_melted['Estatus_Original'].astype(str).str.lower().apply(
        lambda x: 'Cumple' if 'cumple' in x and 'no' not in x else 'No Cumple'
    )

    return df_melted, cols_dict

# 5. UI NAVEGACIÓN
try:
    st.sidebar.image("EA_2.png", width=100)
except:
    pass
st.sidebar.title("📊 Control LPA Pro")

if st.sidebar.button("🔄 Sincronizar Datos"):
    st.cache_data.clear()
    st.rerun()

page = st.sidebar.radio("Nivel:", ["LPA 1er Nivel", "LPA 2do Nivel"])
current_url = URL_1ER_NIVEL if page == "LPA 1er Nivel" else URL_2DO_NIVEL
df_raw = load_data(current_url)

if df_raw is not None and not df_raw.empty:
    df_melted, cols_nombres = get_melted_data(df_raw)

    st.title(f"🚀 {page}")

    # --- FILTROS ---
    st.sidebar.divider()
    st.sidebar.subheader("Filtros Maestros")
    f_auditor = st.sidebar.multiselect("Auditor:", sorted(df_raw[cols_nombres['auditor']].unique()))
    f_area = st.sidebar.multiselect("Área:", sorted(df_raw[cols_nombres['area']].unique())) if cols_nombres['area'] in df_raw.columns else []
    f_maquina = st.sidebar.multiselect("Máquina/Célula:", sorted(df_raw[cols_nombres['maquina']].unique())) if cols_nombres['maquina'] in df_raw.columns else []

    df_filtered = df_melted.copy()
    if f_auditor: df_filtered = df_filtered[df_filtered[cols_nombres['auditor']].isin(f_auditor)]
    if f_area: df_filtered = df_filtered[df_filtered[cols_nombres['area']].isin(f_area)]
    if f_maquina: df_filtered = df_filtered[df_filtered[cols_nombres['maquina']].isin(f_maquina)]

    # --- MÉTRICAS ---
    cumplimiento = (df_filtered['Estatus'] == 'Cumple').mean() * 100 if len(df_filtered) > 0 else 0
    c1, c2, c3 = st.columns(3)
    c1.metric("Cumplimiento Global", f"{cumplimiento:.1f}%")
    c2.metric("Auditorías Registradas", len(df_raw))
    c3.metric("Puntos Evaluados", len(df_filtered))

    # --- GRÁFICO 1: CUMPLIMIENTO ---
    st.subheader("Análisis de Cumplimiento por Categoría")
    tooltips_list = [
        alt.Tooltip('Categoría:N', title='Tópico'),
        alt.Tooltip('Marca temporal:T', title='Fecha', format='%d/%m/%Y'),
        alt.Tooltip(f"{cols_nombres['auditor']}:N", title='Auditor'),
        alt.Tooltip('Estatus:N', title='Resultado')
    ]
    for info_col in cols_nombres['extra_info']:
        tooltips_list.append(alt.Tooltip(f"{info_col}:N", title=info_col))

    bar_chart = alt.Chart(df_filtered).mark_bar(size=40, cornerRadiusTopLeft=2, cornerRadiusTopRight=2).encode(
        x=alt.X('Categoría:N', sort=alt.EncodingSortField(field="Categoría", op="count", order='ascending')),
        y=alt.Y('count():Q', title='Cantidad'),
        color=alt.Color('Estatus:N', scale=alt.Scale(domain=['Cumple', 'No Cumple'], range=['#22c55e', '#ef4444'])),
        tooltip=tooltips_list
    ).properties(height=450).interactive()
    st.altair_chart(bar_chart, use_container_width=True)

    # --- GRÁFICA 2: TENDENCIA ---
    st.subheader("📈 Tendencia de Cumplimiento")
    df_trend = df_filtered.copy()
    df_trend['Fecha_Label'] = df_trend['Marca temporal'].dt.strftime('%Y-%m-%d')
    trend_data = df_trend.groupby('Fecha_Label')['Estatus'].apply(lambda x: (x == 'Cumple').mean() * 100).reset_index()
    line_chart = alt.Chart(trend_data).mark_line(point=True, color='#3b82f6').encode(
        x=alt.X('Fecha_Label:T', title='Fecha'),
        y=alt.Y('Estatus:Q', title='% Cumplimiento', scale=alt.Scale(domain=[0, 105])),
        tooltip=[alt.Tooltip('Fecha_Label:T', title='Fecha'), alt.Tooltip('Estatus:Q', format='.1f', title='% Cumplimiento')]
    ).properties(height=300).interactive()
    st.altair_chart(line_chart, use_container_width=True)

    # --- GRÁFICA 3: PARETO ---
    st.subheader("⚠️ Top Máquinas con Hallazgos")
    df_fallas = df_filtered[df_filtered['Estatus'] == 'No Cumple']
    df_pareto = df_fallas[cols_nombres['maquina']].value_counts().reset_index()
    df_pareto.columns = ['Máquina', 'Conteo']
    pareto_chart = alt.Chart(df_pareto).mark_bar(color='#ef4444').encode(
        x=alt.X('Conteo:Q', title='Fallas'),
        y=alt.Y('Máquina:N', sort='-x', title='Máquina'),
        tooltip=['Máquina', 'Conteo']
    ).properties(height=300).interactive()
    st.altair_chart(pareto_chart, use_container_width=True)

    # --- REPORTE HTML (CON CORRECCIÓN DE COLOR EN HOVER) ---
    chart1_json = bar_chart.properties(width='container').to_json()
    chart2_json = line_chart.properties(width='container').to_json()
    chart3_json = pareto_chart.properties(width='container').to_json()

    cols_tabla_imp = ['Marca temporal', cols_nombres['auditor'], cols_nombres['maquina'], 'Categoría'] + cols_nombres['extra_info']
    cols_tabla = [c for c in cols_tabla_imp if c in df_fallas.columns]
    tabla_html = df_fallas[cols_tabla].to_html(classes='table table-dark table-striped text-center', index=False, justify='center')

    reporte_html = f"""
    <html>
    <head>
        <script src="https://cdn.jsdelivr.net/npm/vega@5"></script>
        <script src="https://cdn.jsdelivr.net/npm/vega-lite@5"></script>
        <script src="https://cdn.jsdelivr.net/npm/vega-embed@6"></script>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
        <style>
            body {{ background-color: #0e1117; color: white; font-family: 'Inter', sans-serif; padding: 30px; }}
            .card {{ background-color: #1c212d; border: 1px solid #3b82f6; border-radius: 15px; padding: 25px; margin-bottom: 25px; text-align: center; width: 100%; }}
            .kpi-card {{ border-left: 5px solid #3b82f6; }}
            .kpi-value {{ font-size: 2.5rem; font-weight: bold; color: #3b82f6; }}
            .kpi-label {{ font-size: 1rem; color: #94a3b8; text-transform: uppercase; }}
            h1, h2 {{ color: #3b82f6; text-align: center; font-weight: bold; margin-bottom: 20px; }}
            .table-responsive {{ border-radius: 10px; overflow: hidden; }}
            .table {{ color: white; margin: 0 auto; width: 100% !important; font-size: 0.9rem; }}
            .table th {{ background-color: #3b82f6 !important; color: white !important; text-align: center !important; }}
            .chart-frame {{ width: 100%; min-height: 450px; }}

            /* CORRECCIÓN DE TOOLTIP (HOVER) */
            #vg-tooltip-element {{
                background-color: #1c212d !important;
                color: #ffffff !important;
                border: 1px solid #3b82f6 !important;
                font-family: sans-serif !important;
                font-size: 12px !important;
            }}
            #vg-tooltip-element table tr td.key {{ color: #94a3b8 !important; font-weight: bold !important; }}
            #vg-tooltip-element table tr td.value {{ color: #ffffff !important; }}
        </style>
    </head>
    <body>
        <div class="container-fluid">
            <h1>🚀 Reporte Gerencial LPA</h1>
            <p style="text-align: center; color: #94a3b8;">Nivel: {page} | Developed by Master Engineer Erik Armenta | {datetime.now().strftime('%d/%m/%Y %H:%M')}</p>

            <div class="row mb-4">
                <div class="col-md-4"><div class="card kpi-card"><div class="kpi-label">Cumplimiento</div><div class="kpi-value">{cumplimiento:.1f}%</div></div></div>
                <div class="col-md-4"><div class="card kpi-card"><div class="kpi-label">Auditorías</div><div class="kpi-value">{len(df_raw)}</div></div></div>
                <div class="col-md-4"><div class="card kpi-card"><div class="kpi-label">Evaluaciones</div><div class="kpi-value">{len(df_filtered)}</div></div></div>
            </div>

            <div class="card"><h2>📊 Cumplimiento por Categoría</h2><div id="vis1" class="chart-frame"></div></div>
            <div class="card"><h2>📈 Tendencia de Cumplimiento</h2><div id="vis2" class="chart-frame"></div></div>
            <div class="card"><h2>⚠️ Top Máquinas con Hallazgos</h2><div id="vis3" class="chart-frame"></div></div>

            <div class="card">
                <h2>🔍 Detalle de Hallazgos y Trazabilidad (IDs)</h2>
                <div class="table-responsive">{tabla_html}</div>
            </div>

            <footer style="text-align: center; margin-top: 50px;">
                <p style="color: #3b82f6; font-weight: bold; font-size: 1.2rem;">Developed by Master Engineer Erik Armenta</p>
            </footer>
        </div>
        <script>
            const opt = {{ actions: {{export: true, source: false, compiled: false, editor: false}}, theme: 'dark', width: 'container' }};
            vegaEmbed('#vis1', {chart1_json}, opt);
            vegaEmbed('#vis2', {chart2_json}, opt);
            vegaEmbed('#vis3', {chart3_json}, opt);
        </script>
    </body>
    </html>
    """

    st.sidebar.divider()
    st.sidebar.download_button(
        label="📥 Descargar Reporte Gerencial",
        data=reporte_html,
        file_name=f"Reporte_LPA_{page}.html",
        mime="text/html"
    )

    with st.expander("🔍 Ver Hallazgos Críticos y Trazabilidad"):
        if not df_fallas.empty:
            st.dataframe(df_fallas[cols_tabla].style.set_properties(**{'text-align': 'center'}), use_container_width=True)
        else:
            st.success("✅ Sin hallazgos críticos.")

else:
    st.info("🔥 Dashboard listo. Esperando registros de Google Forms...")

st.sidebar.caption('LPA Dashboard v1.2 | Developed by Master Engineer Erik Armenta')
