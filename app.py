# -*- coding: utf-8 -*-
"""
Evaluación 'Ana de las Tejas Verdes' – versión 3
"""

import streamlit as st
import random

# ------------------------------------------------------------------
# CAMBIA ESTA CADENA CUANDO MODIFIQUES EL BANCO DE PREGUNTAS
VERSION_APP = "v3_2024-05-25"
# ------------------------------------------------------------------

# ------------------------ 1. Banco de preguntas --------------------
preguntas_ana = [
    {
        "pregunta": "¿Cómo se llama el personaje principal del libro?",
        "respuesta": "Ana",
        "opciones": ["Marilla", "Diana", "Rachel", "Ana"]
    },
    {
        "pregunta": "¿Quién es la señora Rachel Lynde?",
        "respuesta": "Una mujer muy observadora y entrometida que vive en Avonlea.",
        "opciones": [
            "La tía de Ana",
            "La maestra de la escuela de Avonlea",
            "Una mujer muy observadora y entrometida que vive en Avonlea.",
            "La dueña de Tejas Verdes"
        ]
    },
    {
        "pregunta": "¿Dónde vive la señora Rachel Lynde?",
        "respuesta": "En su casa cerca del camino real de Avonlea.",
        "opciones": [
            "En la granja de los Cuthbert",
            "En Charlottetown",
            "En su casa cerca del camino real de Avonlea.",
            "En el bosque cerca del arroyo"
        ]
    },
    {
        "pregunta": "¿Cómo se describe el arroyo al pasar por la puerta de la señora Rachel Lynde?",
        "respuesta": "Como una pequeña corriente tranquila y bien educada.",
        "opciones": [
            "Como un arroyo torrencial e intrincado",
            "Como un río caudaloso y ruidoso",
            "Como una pequeña corriente tranquila y bien educada.",
            "Como un estanque estancado y oscuro"
        ]
    },
    {
        "pregunta": "¿Por qué se dice que el arroyo era 'respetuoso' al pasar por la casa de la señora Lynde?",
        "respuesta": "Porque la señora Rachel lo observaba atentamente.",
        "opciones": [
            "Porque era muy profundo y peligroso",
            "Porque la señora Rachel lo observaba atentamente.",
            "Porque siempre había suficiente agua",
            "Porque era muy limpio y claro"
        ]
    },
    {
        "pregunta": "¿Qué tipo de actividades comunitarias 'dirigía' o en cuáles participaba la señora Rachel Lynde?",
        "respuesta": "El Círculo de Costura y la Escuela Dominical.",
        "opciones": [
            "El club de lectura del pueblo",
            "El Círculo de Costura y la Escuela Dominical.",
            "Las reuniones del comité del pueblo",
            "Las actividades de la feria anual"
        ]
    },
    {
        "pregunta": "¿Qué característica principal se menciona de la señora Rachel Lynde en relación con los asuntos ajenos?",
        "respuesta": "Era capaz de vigilar al unísono los asuntos propios y los ajenos.",
        "opciones": [
            "Siempre estaba ocupada solo con sus propios asuntos",
            "Era capaz de vigilar al unísono los asuntos propios y los ajenos.",
            "No le importaban en absoluto los asuntos de los demás",
            "Era muy discreta y reservada con la vida de los demás"
        ]
    },
    {
        "pregunta": "¿Con quién se encuentra Ana en la colina de los Barry al final del libro?",
        "respuesta": "Gilbert Blythe",
        "opciones": ["Diana Barry", "Marilla Cuthbert", "Gilbert Blythe", "Matthew Cuthbert"]
    },
    {
        "pregunta": "¿Cuánto tiempo llevaban Ana y Gilbert sin hablarse antes de su reconciliación?",
        "respuesta": "Cinco años",
        "opciones": ["Un año", "Tres años", "Cinco años", "Diez años"]
    },
    {
        "pregunta": "¿Qué deciden Ana y Gilbert ser en el futuro, después de haber sido 'buenos enemigos'?",
        "respuesta": "Buenos amigos",
        "opciones": ["Novios", "Compañeros de estudio", "Buenos amigos", "Colegas de trabajo"]
    },
    {
        "pregunta": "¿Qué sensación tiene Ana al sentarse junto a su ventana después de la reconciliación?",
        "respuesta": "Un alegre sentimiento y se siente feliz y en paz.",
        "opciones": [
            "Tristeza y arrepentimiento",
            "Enojo y frustración",
            "Un alegre sentimiento y se siente feliz y en paz.",
            "Indiferencia y aburrimiento"
        ]
    },
    {
        "pregunta": "¿Qué tipo de felicidad espera Ana en su futuro?",
        "respuesta": "Una 'felicidad tranquila'.",
        "opciones": [
            "Una felicidad extravagante y ruidosa",
            "Una vida de aventuras y sorpresas constantes",
            "Una 'felicidad tranquila'.",
            "Una vida llena de desafíos y éxitos profesionales"
        ]
    },
    {
        "pregunta": "¿Además de la felicidad tranquila, qué otros aspectos menciona Ana que serán suyos en el futuro?",
        "respuesta": "El gozo del trabajo sincero, la aspiración digna y la amistad.",
        "opciones": [
            "Riqueza y fama",
            "Viajes y nuevas experiencias exóticas",
            "El gozo del trabajo sincero, la aspiración digna y la amistad.",
            "Poder y control sobre su destino"
        ]
    },
    {
        "pregunta": "¿Qué afirma Ana que nada podrá apartarla de su 'derecho'?",
        "respuesta": "Su derecho a la fantasía o del mundo ideal de sus sueños.",
        "opciones": [
            "Su derecho a la educación superior",
            "Su derecho a la libertad personal",
            "Su derecho a la fantasía o del mundo ideal de sus sueños.",
            "Su derecho a opinar y ser escuchada"
        ]
    },
    {
        "pregunta": "¿Qué frase final, aunque incompleta, se utiliza para describir la permanencia del espíritu soñador de Ana?",
        "respuesta": "Y siempre estaba...",
        "opciones": [
            "Y nunca se rindió.",
            "Y siempre fue feliz.",
            "Y siempre estaba...",
            "Y finalmente encontró la paz."
        ]
    }
]

# ---------  Verificación automática de coherencia ----------
for p in preguntas_ana:
    assert p["respuesta"] in p["opciones"], f"Incongruencia en: {p['pregunta']}"

# --------------------- 2. Reset de sesión -------------------
if st.session_state.get("version") != VERSION_APP:
    st.session_state.clear()
    st.session_state.version = VERSION_APP  # graba la versión actual

# --------------------- 3. Inicialización --------------------
if "pregunta_actual_idx" not in st.session_state:
    st.session_state.pregunta_actual_idx = 0
    st.session_state.puntuacion = 0
    st.session_state.evaluacion_terminada = False
    st.session_state.preguntas_mezcladas = random.sample(preguntas_ana, len(preguntas_ana))
    st.session_state.respuestas_correctas_dadas = []
    st.session_state.respuestas_incorrectas_dadas = []

# --------------------- 4. Funciones -------------------------
def siguiente_pregunta():
    if st.session_state.pregunta_actual_idx < len(st.session_state.preguntas_mezcladas) - 1:
        st.session_state.pregunta_actual_idx += 1
    else:
        st.session_state.evaluacion_terminada = True

def verificar_respuesta(opcion_elegida, respuesta_correcta, pregunta_texto):
    if opcion_elegida == respuesta_correcta:
        st.session_state.puntuacion += 1
        st.success("¡Correcto!")
        st.session_state.respuestas_correctas_dadas.append(pregunta_texto)
    else:
        st.error(f"Incorrecto. La respuesta correcta era: **{respuesta_correcta}**")
        st.session_state.respuestas_incorrectas_dadas.append(
            f"{pregunta_texto} (Tu respuesta: {opcion_elegida}, Correcta: {respuesta_correcta})"
        )
    siguiente_pregunta()
    st.rerun()

def reiniciar_evaluacion():
    st.session_state.clear()
    st.session_state.version = VERSION_APP
    st.rerun()

# --------------------- 5. Interfaz --------------------------
st.set_page_config(page_title="Evaluación Ana de las Tejas Verdes", page_icon="📚")

st.title("📚 Evaluación de 'Ana de las Tejas Verdes'")
st.markdown("Pon a prueba tu conocimiento sobre el inicio y el final del libro.")
st.markdown("---")

if not st.session_state.evaluacion_terminada:
    pregunta_actual = st.session_state.preguntas_mezcladas[st.session_state.pregunta_actual_idx]
    st.subheader(f"Pregunta {st.session_state.pregunta_actual_idx + 1} de {len(st.session_state.preguntas_mezcladas)}")
    st.write(f"**{pregunta_actual['pregunta']}**")

    opciones_barajadas = random.sample(pregunta_actual["opciones"], len(pregunta_actual["opciones"]))
    for opcion in opciones_barajadas:
        if st.button(opcion, key=f"{st.session_state.pregunta_actual_idx}_{opcion}"):
            verificar_respuesta(opcion, pregunta_actual["respuesta"], pregunta_actual["pregunta"])
else:
    total = len(st.session_state.preguntas_mezcladas)
    st.success("¡Evaluación terminada!")
    st.subheader(f"Puntuación final: {st.session_state.puntuacion} / {total}")

    porcentaje = (st.session_state.puntuacion / total)
    st.progress(porcentaje)

    if porcentaje == 1.0:
        st.balloons()
        st.write("¡Felicidades! ¡Dominas el libro por completo! 🎉")
    elif porcentaje >= 0.7:
        st.write("¡Muy bien! Tienes un excelente conocimiento del libro. 👍")
    else:
        st.write("Sigue leyendo y repasando. ¡Puedes hacerlo mejor! 💪")

    st.markdown("---")
    st.subheader("Resumen de respuestas")

    if st.session_state.respuestas_correctas_dadas:
        st.markdown("**Correctas:**")
        for r in st.session_state.respuestas_correctas_dadas:
            st.write(f"• {r}")
    else:
        st.info("No hubo respuestas correctas.")

    if st.session_state.respuestas_incorrectas_dadas:
        st.markdown("**Incorrectas:**")
        for r in st.session_state.respuestas_incorrectas_dadas:
            st.write(f"• {r}")
    else:
        st.info("¡Todas tus respuestas fueron correctas!")

    st.markdown("---")
    if st.button("Reiniciar evaluación"):
        reiniciar_evaluacion()

# --------------------- 6. Sidebar ---------------------------
st.sidebar.markdown("---")
st.sidebar.info("Esta evaluación se basa en el primer capítulo y en un fragmento del final del libro 'Ana de las Tejas Verdes'.")