# -*- coding: utf-8 -*-
"""
Evaluación de 'Ana de las Tejas Verdes'
"""

import streamlit as st
import random

# -------------------------------------------------
# 1. Banco de preguntas (≤ 5 palabras por opción)
# -------------------------------------------------
preguntas_ana = [
    {
        "pregunta": "¿Cómo se llama el personaje principal del libro?",
        "respuesta": "Ana",
        "opciones": ["Marilla", "Diana", "Rachel", "Ana"]
    },
    {
        "pregunta": "¿Quién es la señora Rachel Lynde?",
        "respuesta": "Vecina entrometida de Avonlea",
        "opciones": [
            "Tía de Ana",
            "Maestra de Avonlea",
            "Vecina entrometida de Avonlea",
            "Dueña de Tejas Verdes"
        ]
    },
    {
        "pregunta": "¿Dónde vive la señora Rachel Lynde?",
        "respuesta": "Cerca del camino real",
        "opciones": [
            "Granja Cuthbert",
            "Charlottetown",
            "Cerca del camino real",
            "Bosque junto al arroyo"
        ]
    },
    {
        "pregunta": "¿Cómo se describe el arroyo al pasar por la puerta de la señora Rachel Lynde?",
        "respuesta": "Corriente tranquila y educada",
        "opciones": [
            "Arroyo torrencial intrincado",
            "Río caudaloso ruidoso",
            "Corriente tranquila y educada",
            "Estanque estancado oscuro"
        ]
    },
    {
        "pregunta": "¿Por qué el arroyo era 'respetuoso' al pasar junto a la casa?",
        "respuesta": "Rachel lo observaba siempre",
        "opciones": [
            "Muy profundo peligroso",
            "Rachel lo observaba siempre",
            "Había mucha agua",
            "Muy limpio claro"
        ]
    },
    {
        "pregunta": "¿Qué labores comunitarias dirigía Rachel Lynde?",
        "respuesta": "Círculo y escuela dominical",
        "opciones": [
            "Club de lectura",
            "Círculo y escuela dominical",
            "Comité del pueblo",
            "Feria anual"
        ]
    },
    {
        "pregunta": "¿Qué rasgo muestra Rachel sobre asuntos ajenos?",
        "respuesta": "Vigila propios y ajenos",
        "opciones": [
            "Solo sus asuntos",
            "Vigila propios y ajenos",
            "No le importan otros",
            "Muy discreta"
        ]
    },
    {
        "pregunta": "¿Con quién se encuentra Ana al final?",
        "respuesta": "Gilbert Blythe",
        "opciones": ["Diana Barry", "Marilla Cuthbert", "Gilbert Blythe", "Matthew Cuthbert"]
    },
    {
        "pregunta": "¿Cuánto tiempo llevaban sin hablar?",
        "respuesta": "Cinco años",
        "opciones": ["Un año", "Tres años", "Cinco años", "Diez años"]
    },
    {
        "pregunta": "¿Qué deciden ser Ana y Gilbert?",
        "respuesta": "Buenos amigos",
        "opciones": ["Novios", "Compañeros de estudio", "Buenos amigos", "Colegas de trabajo"]
    },
    {
        "pregunta": "¿Cómo se siente Ana tras reconciliarse?",
        "respuesta": "Feliz y en paz",
        "opciones": [
            "Triste y arrepentida",
            "Enojada y frustrada",
            "Feliz y en paz",
            "Indiferente y aburrida"
        ]
    },
    {
        "pregunta": "¿Qué clase de felicidad espera Ana?",
        "respuesta": "Felicidad tranquila",
        "opciones": [
            "Extravagante ruidosa",
            "Aventuras constantes",
            "Felicidad tranquila",
            "Éxitos profesionales"
        ]
    },
    {
        "pregunta": "¿Qué más ansía Ana para su futuro?",
        "respuesta": "Trabajo sincero y amistad",
        "opciones": [
            "Riqueza y fama",
            "Viajes exóticos",
            "Trabajo sincero y amistad",
            "Poder y control"
        ]
    },
    {
        "pregunta": "¿De qué derecho no renuncia Ana?",
        "respuesta": "Derecho a la fantasía",
        "opciones": [
            "Derecho a estudiar",
            "Derecho personal",
            "Derecho a la fantasía",
            "Derecho a opinar"
        ]
    },
    {
        "pregunta": "¿Qué frase incompleta cierra el pasaje?",
        "respuesta": "Y siempre estaba...",
        "opciones": [
            "Y nunca cedió.",
            "Y siempre feliz.",
            "Y siempre estaba...",
            "Y halló paz."
        ]
    }
]

# Comprobaciones de coherencia (se pueden quitar en producción)
def _contar_palabras(txt): return len(txt.split())
for p in preguntas_ana:
    assert p["respuesta"] in p["opciones"], f"Respuesta fuera de opciones: {p['pregunta']}"
    assert _contar_palabras(p["respuesta"]) <= 5, f"Respuesta muy larga: {p['respuesta']}"
    for op in p["opciones"]:
        assert _contar_palabras(op) <= 5, f"Opción muy larga: {op}"

# -------------------------------------------------
# 2. Configuración básica de Streamlit
# -------------------------------------------------
st.set_page_config(page_title="Evaluación Ana de las Tejas Verdes",
                   page_icon="📚",
                   initial_sidebar_state="collapsed")

st.title("📚 Evaluación de 'Ana de las Tejas Verdes'")
st.write("Pon a prueba tu conocimiento sobre el inicio y el final del libro.")
st.markdown("---")

# -------------------------------------------------
# 3. Estado de sesión
# -------------------------------------------------
if "idx" not in st.session_state:
    st.session_state.idx = 0
    st.session_state.puntuacion = 0
    st.session_state.terminado = False
    st.session_state.pool = random.sample(preguntas_ana, len(preguntas_ana))
    st.session_state.ok = []
    st.session_state.fail = []

# -------------------------------------------------
# 4. Funciones auxiliares
# -------------------------------------------------
def avanzar():
    if st.session_state.idx < len(st.session_state.pool) - 1:
        st.session_state.idx += 1
    else:
        st.session_state.terminado = True

def responder(opcion, correcta, texto):
    if opcion == correcta:
        st.session_state.puntuacion += 1
        st.success("¡Correcto!")
        st.session_state.ok.append(texto)
    else:
        st.error(f"Incorrecto. Era: {correcta}")
        st.session_state.fail.append(f"{texto} (Elegiste: {opcion})")
    avanzar()
    st.rerun()

def reiniciar():
    st.session_state.idx = 0
    st.session_state.puntuacion = 0
    st.session_state.terminado = False
    st.session_state.pool = random.sample(preguntas_ana, len(preguntas_ana))
    st.session_state.ok = []
    st.session_state.fail = []
    st.rerun()

# -------------------------------------------------
# 5. Lógica principal
# -------------------------------------------------
if not st.session_state.terminado:
    q = st.session_state.pool[st.session_state.idx]
    st.subheader(f"Pregunta {st.session_state.idx + 1} de {len(st.session_state.pool)}")
    st.write(f"**{q['pregunta']}**")
    for op in random.sample(q["opciones"], len(q["opciones"])):
        if st.button(op, key=f"{st.session_state.idx}_{op}"):
            responder(op, q["respuesta"], q["pregunta"])
else:
    total = len(st.session_state.pool)
    st.success("¡Evaluación terminada!")
    st.markdown(f"### Puntuación: **{st.session_state.puntuacion} / {total}**")
    st.progress(st.session_state.puntuacion / total)

    if st.session_state.puntuacion == total:
        st.balloons()
        st.write("¡Perfecto! Dominas el libro.")
    elif st.session_state.puntuacion / total >= 0.7:
        st.write("¡Muy bien! Conoces bastante el libro.")
    else:
        st.write("Sigue leyendo y practicando.")

    st.markdown("---")
    st.subheader("Respuestas correctas")
    for r in st.session_state.ok or ["(ninguna)"]:
        st.write(f"• {r}")
    st.subheader("Respuestas incorrectas")
    for r in st.session_state.fail or ["(ninguna)"]:
        st.write(f"• {r}")

    st.markdown("---")
    if st.button("Reiniciar evaluación"):
        reiniciar()

# -------------------------------------------------
# 6. Barra lateral
# -------------------------------------------------
st.sidebar.info(
    "Esta evaluación se basa en el primer capítulo y en un fragmento del final "
    "del libro 'Ana de las Tejas Verdes'."
)