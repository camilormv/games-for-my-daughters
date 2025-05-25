# -*- coding: utf-8 -*-
"""
Evaluación ‘Ana de las Tejas Verdes’ – versión corta
"""

import streamlit as st
import random

# ---- 1. Banco de preguntas (≤ 5 palabras) ----
preguntas_ana = [
    {
        "pregunta": "¿Cómo se llama la protagonista?",
        "respuesta": "Ana",
        "opciones": ["Marilla", "Diana", "Rachel", "Ana"]
    },
    {
        "pregunta": "¿Quién es Rachel Lynde?",
        "respuesta": "Vecina entrometida Avonlea",
        "opciones": [
            "Tía de Ana",
            "Maestra de Avonlea",
            "Vecina entrometida Avonlea",
            "Dueña Tejas Verdes"
        ]
    },
    {
        "pregunta": "¿Dónde vive Rachel Lynde?",
        "respuesta": "Junto al camino real",
        "opciones": [
            "Granja Cuthbert",
            "Charlottetown",
            "Junto al camino real",
            "Bosque del arroyo"
        ]
    },
    {
        "pregunta": "¿Cómo es el arroyo allí?",
        "respuesta": "Tranquilo y educado",
        "opciones": [
            "Torrencial intrincado",
            "Ruidoso caudaloso",
            "Tranquilo y educado",
            "Estanque oscuro"
        ]
    },
    {
        "pregunta": "¿Por qué el arroyo es respetuoso?",
        "respuesta": "Rachel lo vigila",
        "opciones": [
            "Muy profundo",
            "Rachel lo vigila",
            "Mucha agua",
            "Muy limpio"
        ]
    },
    {
        "pregunta": "¿Qué dirige Rachel Lynde?",
        "respuesta": "Círculo y dominical",
        "opciones": [
            "Club lectura",
            "Círculo y dominical",
            "Comité pueblo",
            "Feria anual"
        ]
    },
    {
        "pregunta": "Rasgo de Rachel con chismes:",
        "respuesta": "Vigila propios y ajenos",
        "opciones": [
            "Solo propios",
            "Vigila propios y ajenos",
            "No le importan",
            "Muy discreta"
        ]
    },
    {
        "pregunta": "¿Con quién se encuentra Ana?",
        "respuesta": "Gilbert Blythe",
        "opciones": [
            "Diana Barry",
            "Marilla Cuthbert",
            "Gilbert Blythe",
            "Matthew Cuthbert"
        ]
    },
    {
        "pregunta": "¿Cuánto sin hablarse?",
        "respuesta": "Cinco años",
        "opciones": ["Un año", "Tres años", "Cinco años", "Diez años"]
    },
    {
        "pregunta": "¿Qué deciden ser luego?",
        "respuesta": "Buenos amigos",
        "opciones": [
            "Novios",
            "Compañeros estudio",
            "Buenos amigos",
            "Colegas trabajo"
        ]
    },
    {
        "pregunta": "Sentir de Ana tras paz:",
        "respuesta": "Feliz y en paz",
        "opciones": [
            "Triste arrepentida",
            "Enojada frustrada",
            "Feliz y en paz",
            "Indiferente aburrida"
        ]
    },
    {
        "pregunta": "Felicidad que desea Ana:",
        "respuesta": "Felicidad tranquila",
        "opciones": [
            "Extravagante ruidosa",
            "Aventuras constantes",
            "Felicidad tranquila",
            "Éxitos profesionales"
        ]
    },
    {
        "pregunta": "Además desea también:",
        "respuesta": "Trabajo sincero amistad",
        "opciones": [
            "Riqueza fama",
            "Viajes exóticos",
            "Trabajo sincero amistad",
            "Poder control"
        ]
    },
    {
        "pregunta": "Derecho irrenunciable Ana:",
        "respuesta": "Derecho a fantasía",
        "opciones": [
            "Derecho estudiar",
            "Derecho personal",
            "Derecho a fantasía",
            "Derecho opinar"
        ]
    },
    {
        "pregunta": "Frase final incompleta:",
        "respuesta": "Y siempre estaba...",
        "opciones": [
            "Y nunca cedió.",
            "Y siempre feliz.",
            "Y siempre estaba...",
            "Y halló paz."
        ]
    }
]

# Comprobación rápida
limite = 5
for p in preguntas_ana:
    assert p["respuesta"] in p["opciones"]
    assert len(p["respuesta"].split()) <= limite
    for op in p["opciones"]:
        assert len(op.split()) <= limite

# ---- 2. Gestión de sesión con versión ----
VERSION_APP = "v2_corto"

if st.session_state.get("version") != VERSION_APP:
    # limpiar completamente la sesión
    for k in list(st.session_state.keys()):
        del st.session_state[k]
    st.session_state.version = VERSION_APP

if "idx" not in st.session_state:
    st.session_state.idx = 0
    st.session_state.score = 0
    st.session_state.done = False
    st.session_state.pool = random.sample(preguntas_ana, len(preguntas_ana))
    st.session_state.ok = []
    st.session_state.fail = []

# ---- 3. UI ----
st.set_page_config(page_title="Ana – Quiz", page_icon="📚", initial_sidebar_state="collapsed")
st.title("📚 Quiz de 'Ana de las Tejas Verdes'")
st.write("Responde cada pregunta. ¡Éxitos!")
st.markdown("---")

# ---- 4. Funciones ----
def avanzar():
    if st.session_state.idx < len(st.session_state.pool) - 1:
        st.session_state.idx += 1
    else:
        st.session_state.done = True

def responder(elegida, correcta, texto):
    if elegida == correcta:
        st.session_state.score += 1
        st.success("¡Correcto!")
        st.session_state.ok.append(texto)
    else:
        st.error(f"Incorrecto. Era: {correcta}")
        st.session_state.fail.append(f"{texto} (Elegiste: {elegida})")
    avanzar()
    st.rerun()

def reiniciar():
    for k in ["idx", "score", "done", "pool", "ok", "fail"]:
        del st.session_state[k]
    st.rerun()

# ---- 5. Flujo principal ----
if not st.session_state.done:
    q = st.session_state.pool[st.session_state.idx]
    st.subheader(f"Pregunta {st.session_state.idx + 1}/{len(st.session_state.pool)}")
    st.write(f"**{q['pregunta']}**")
    for op in random.sample(q["opciones"], len(q["opciones"])):
        if st.button(op, key=f"{st.session_state.idx}_{op}"):
            responder(op, q["respuesta"], q["pregunta"])
else:
    total = len(st.session_state.pool)
    st.success("¡Terminaste!")
    st.write(f"Puntuación: **{st.session_state.score}/{total}**")
    st.progress(st.session_state.score / total)

    st.markdown("#### Correctas")
    for r in st.session_state.ok or ["(ninguna)"]:
        st.write("•", r)
    st.markdown("#### Incorrectas")
    for r in st.session_state.fail or ["(ninguna)"]:
        st.write("•", r)

    if st.button("Reiniciar"):
        reiniciar()

st.sidebar.info("Contenido: capítulo 1 y final del libro.")