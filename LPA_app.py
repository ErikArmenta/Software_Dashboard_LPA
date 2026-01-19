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
    <style>
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
