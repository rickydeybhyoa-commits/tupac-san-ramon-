import streamlit as st
import json

# ==============================================================================
# CONFIGURACIÓN DE LA PÁGINA WEB INSTITUCIONAL
# ==============================================================================
st.set_page_config(
    page_title="SISTEMA INTERNO DE CONSULTA TUPA - SAN RAMÓN", 
    page_icon="🏛️", 
    layout="wide"
)

# Paleta de colores institucionales de San Ramón
COLOR_VERDE_OSCURO = "#1E5631"
COLOR_VERDE_ACENTO = "#4C9A2A"

# ==============================================================================
# BASE DE DATOS INTEGRADA (MUNICIPALIDAD DISTRITAL DE SAN RAMÓN)
# ==============================================================================
DATOS_TUPA = [
    {
        "id": "1",
        "numero": "1.0",
        "procedimiento": "INSCRIPCIÓN ORDINARIA DE NACIMIENTO DENTRO DE LOS 60 DÍAS",
        "sustento": "SUB GERENCIA DE REGISTRO CIVIL - PROCEDIMIENTOS ADMINISTRATIVOS",
        "requisitos": [
            "1.0 Certificado de Nacido Vivo expedido por Profesional Competente o constancia otorgada por persona autorizada por el Ministerio de Salud.",
            "2.0 Declaración Jurada de la Autoridad Política, Judicial o Administrativa en caso de no haber centro de salud.",
            "3.0 Presencia de los padres o de uno de ellos con DNI vigente."
        ],
        "derecho_tramite": "GRATUITO",
        "plazo": "Inmediato (Automático)",
        "inicio": "Sub Gerencia de Registro Civil",
        "autoridad": "Sub Gerente de Registro Civil",
        "reconsideracion": "Sub Gerente de Registro Civil",
        "apelacion": "Gerencia Municipal"
    },
{
        "id": "187",
        "numero": "169",
        "procedimiento": "ADMISIÓN DE OSB AL PROGRAMA DE COMPLEMENTACIÓN ALIMENTARIA MUNICIPAL PCAM",
        "sustento": "BASE LEGAL\n- Ley Nº 27767, Ley del Programa Nacional Complementario de Asistencia Alimentaria, pub 27.06.2002\n- D.S 002-2004-MINDES, Reglamento de la Ley Nº 27767, pub. 25.05.2004\n- Ley Nº 27972, Ley Orgánica de Municipalidades",
        "requisitos": [
            "1 Solicitud dirigido al Alcalde cumpliendo con los requisitos generales de presentación, peticionando la Admisión al PCAM",
            "2 Copia simple de la Resolución de Reconocimiento de la OSB emitido por la Municipalidad de San Ramón",
            "3 Copia simple del Padrón de Socias Activas (como mínimo de 15 socias)",
            "4 Copia simple del DNI vigente de las socias activas",
            "5 Copia simple del DNI vigente de los miembros del Consejo Directivo o Junta Directiva",
            "6 Croquis de ubicación del OSB",
            "7 Determinar el lugar donde la OSB recepcionará y atenderá el reparto de los productos pertenecientes al PCAM",
            "8 Libro de Actas",
            "9 Cuaderno de Almacén",
            "10 Cuaderno de gastos diarios y raciones",
            "--------------------------------------------------",
            "📌 NOTAS PARA EL CIUDADANO:",
            "- La Organización deberá contar con un local adecuado para la recepción, almacenamiento y distribución de los alimentos"
        ],
        "derecho_tramite": "GRATUITO",
        "plazo": "Evaluación Previa - 30 Días",
        "inicio": "Unidad de Trámite Documentario",
        "autoridad": "Gerente de Desarrollo Social y Humano",
        "reconsideracion": "Gerente de Desarrollo Social y Humano\nPlazo de Presentación: 15 Días hábiles.\nPlazo de Resolución: 30 Días hábiles.",
        "apelacion": "Gerente Municipal\nPlazo de Presentación: 15 Días hábiles.\nPlazo de Resolución: 30 Días hábiles."
    },
]

# --- ENCABEZADO INSTITUCIONAL ---
st.markdown(f"""
    <div style="background-color:{COLOR_VERDE_OSCURO}; padding:20px; border-radius:10px; text-align:center; margin-bottom:25px;">
        <h1 style="color:white; margin:0; font-size:28px;">🏛️ MUNICIPALIDAD DISTRITAL DE SAN RAMÓN</h1>
        <p style="color:#C5E1A5; margin:5px 0 0 0; font-style:italic; font-size:16px;">SISTEMA INTERNO DE CONSULTA TUPA</p>
    </div>
""", unsafe_allow_html=True)

# --- PANEL DE BÚSQUEDA ---
st.markdown(f"<h3 style='color:{COLOR_VERDE_OSCURO};'>🔍 Criterios de Búsqueda</h3>", unsafe_allow_html=True)

col_input, col_filtro = st.columns([3, 1])

with col_input:
    termino = st.text_input("Buscar término:", placeholder="Digite un número de ítem o palabra (ej. '169', 'nacimiento')...").strip()

with col_filtro:
    tipo_filtro = st.selectbox(
        "Filtrar por:",
        ["Todo", "Número de Item", "Nombre del Trámite", "Palabra Clave / Sustento"]
    )

# --- MOTOR DE BÚSQUEDA ---
coincidencias = []

if termino:
    for item in DATOS_TUPA:
        match_numero = termino.lower() in item["numero"].lower()
        match_nombre = termino.lower() in item["procedimiento"].lower()
        match_sustento = termino.lower() in item["sustento"].lower() or any(termino.lower() in req.lower() for req in item["requisitos"])
        
        if tipo_filtro == "Número de Item" and match_numero:
            coincidencias.append(item)
        elif tipo_filtro == "Nombre del Trámite" and match_nombre:
            coincidencias.append(item)
        elif tipo_filtro == "Palabra Clave / Sustento" and match_sustento:
            coincidencias.append(item)
        elif tipo_filtro == "Todo" and (match_numero or match_nombre or match_sustento):
            coincidencias.append(item)

# --- PANEL DE RESULTADOS (FICHA TÉCNICA) ---
st.markdown("---")

if not termino:
    st.info("💡 **SISTEMA TUPA ACTIVO:** Escriba un término o palabra descriptiva en la barra superior para desplegar la ficha estructurada institucional.")
else:
    total_resultados = len(coincidencias)
    
    if total_resultados == 0:
        st.error(f"❌ No se encontraron procedimientos vinculados al término: '{termino}'")
    else:
        st.markdown(f"<span style='color:{COLOR_VERDE_ACENTO}; font-weight:bold;'>TOTAL COINCIDENCIAS ENCONTRADAS: {total_resultados}</span>", unsafe_allow_html=True)
        
        # Control de navegación web (Paginador numérico integrado de una sola línea)
        if total_resultados > 1:
            indice_actual = st.number_input("Ir a la coincidencia número:", min_value=1, max_value=total_resultados, step=1, value=1) - 1
        else:
            indice_actual = 0
            
        proc = coincidencias[indice_actual]
        
        # Desplegar la ficha en la página web de forma ordenada
        st.markdown(f"## 📋 Ficha del Procedimiento (Coincidencia {indice_actual + 1} de {total_resultados})")
        
        st.markdown(f"**N.º ITEM:** `{proc['numero']}`")
        st.markdown(f"### **PROCEDIMIENTO:**\n{proc['procedimiento']}")
        st.markdown(f"**BASE LEGAL / SUSTENTO:**\n{proc['sustento']}")
        
        # Dividir la información técnica en dos columnas limpias
        col_a, col_b = st.columns(2)
        with col_a:
            st.markdown(f"🔹 **DERECHO DE TRÁMITE:** {proc['derecho_tramite']}")
            st.markdown(f"🔹 **PLAZO PARA RESOLVER:** {proc['plazo']}")
            st.markdown(f"🔹 **INICIO DEL PROCEDIMIENTO:** {proc['inicio']}")
        with col_b:
            st.markdown(f"🔹 **AUTORIDAD COMPETENTE:** {proc['autoridad']}")
            st.markdown(f"🔹 **RECURSO DE RECONSIDERACIÓN:**\n{proc['reconsideracion']}")
            st.markdown(f"🔹 **RECURSO DE APELACIÓN:**\n{proc['apelacion']}")
            
        st.markdown("### **REQUISITOS ESTRUCTURADOS:**")
        for req in proc["requisitos"]:
            st.markdown(f"  * {req}")
            
        # ==============================================================================
        # GENERACIÓN DE LA HOJA LIMPIA E INSTITUCIONAL PARA IMPRIMIR/GUARDAR
        # ==============================================================================
        hoja_limpia = "======================================================================\n"
        hoja_limpia += "               MUNICIPALIDAD DISTRITAL DE SAN RAMÓN                   \n"
        hoja_limpia += "             TEXTO ÚNICO DE PROCEDIMIENTOS ADMINISTRATIVOS            \n"
        hoja_limpia += "======================================================================\n\n"
        hoja_limpia += f"N.º ITEM: {proc['numero']}\n\n"
        hoja_limpia += f"PROCEDIMIENTO:\n{proc['procedimiento']}\n\n"
        hoja_limpia += f"BASE LEGAL / SUSTENTO:\n{proc['sustento']}\n\n"
        hoja_limpia += f"DERECHO DE TRÁMITE: {proc['derecho_tramite']}\n"
        hoja_limpia += f"PLAZO PARA RESOLVER: {proc['plazo']}\n"
        hoja_limpia += f"INICIO DEL PROCEDIMIENTO: {proc['inicio']}\n"
        hoja_limpia += f"AUTORIDAD COMPETENTE: {proc['autoridad']}\n"
        hoja_limpia += f"RECURSO DE RECONSIDERACIÓN:\n{proc['reconsideracion']}\n\n"
        hoja_limpia += f"RECURSO DE APELACIÓN:\n{proc['apelacion']}\n\n"
        hoja_limpia += "REQUISITOS ESTRUCTURADOS:\n"
        for req in proc["requisitos"]:
            hoja_limpia += f"  - {req}\n"
        hoja_limpia += "\n======================================================================\n"
        
        st.write("---")
        
        # Botón nativo de descarga web: descarga la ficha formal limpia
        st.download_button(
            label="💾 Guardar / Exportar Ficha Limpia Oficial",
            data=hoja_limpia,
            file_name=f"Ficha_TUPA_Item_{proc['numero']}.txt",
            mime="text/plain"
        )