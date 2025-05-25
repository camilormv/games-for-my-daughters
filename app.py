import streamlit as st
import random # Para barajar las preguntas

# --- Datos de las Preguntas ---
preguntas_ana = [
    {
        "pregunta": "¿Cómo se llama el personaje principal del libro?",
        "respuesta": "Ana",
        "opciones": ["Marilla", "Diana", "Rachel", "Ana"] # Para selección múltiple
    },
    {
        "pregunta": "¿Quién es la señora Rachel Lynde?",
        "respuesta": "Una mujer muy observadora y entrometida que vive en Avonlea y siempre está al tanto de todo lo que sucede en su comunidad.",
        "opciones": ["La tía de Ana", "La maestra de la escuela", "Una mujer muy observadora y entrometida", "La dueña de Tejas Verdes"]
    },
    {
        "pregunta": "¿Dónde vive la señora Rachel Lynde?",
        "respuesta": "Donde el camino real de Avonlea baja a un pequeño valle orlado de alisos y zarcillos.",
        "opciones": ["En la granja de los Cuthbert", "Donde el camino real de Avonlea baja a un pequeño valle", "En Charlottetown", "En el bosque"]
    },
    {
        "pregunta": "¿Cómo se describe el arroyo al pasar por la puerta de la señora Rachel Lynde?",
        "respuesta": "Como una pequeña corriente tranquila y bien educada, que pasa con 'el debido respeto por la decencia y el decoro'.",
        "opciones": ["Como un arroyo torrencial", "Como una pequeña corriente tranquila y bien educada", "Como un río caudaloso", "Como un estanque estancado"]
    },
    {
        "pregunta": "¿Por qué se dice que el arroyo era 'respetuoso' al pasar por la casa de la señora Lynde?",
        "respuesta": "Porque se daba cuenta de que la señora Rachel estaría sentada junto a su ventana, observando con ojo avizor a todo el que pasaba.",
        "opciones": ["Porque siempre había agua", "Porque era muy limpio", "Porque se daba cuenta de que la señora Rachel lo observaba", "Porque era muy profundo"]
    },
    {
        "pregunta": "¿Qué tipo de actividades comunitarias 'dirigía' o en cuáles participaba la señora Rachel Lynde?",
        "respuesta": "Dirigía el Círculo de Costura y ayudaba en la Escuela Dominical.",
        "opciones": ["El club de lectura", "El Círculo de Costura y la Escuela Dominical", "El comité del pueblo", "Las reuniones de vecinos"]
    },
    {
        "pregunta": "¿Qué característica principal se menciona de la señora Rachel Lynde en relación con los asuntos ajenos?",
        "respuesta": "Era capaz de vigilar al unísono los asuntos propios y los ajenos.",
        "opciones": ["Siempre estaba ocupada con sus propios asuntos", "Era capaz de vigilar al unísono los asuntos propios y los ajenos", "No le importaban los asuntos de los demás", "Era muy discreta"]
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
        "opciones": ["Tristeza y arrepentimiento", "Enojo y frustración", "Un alegre sentimiento y se siente feliz y en paz.", "Indiferencia"]
    },
    {
        "pregunta": "¿Qué tipo de felicidad espera Ana en su futuro?",
        "respuesta": "Una 'felicidad tranquila'",
        "opciones": ["Una felicidad extravagante", "Una vida de aventuras", "Una 'felicidad tranquila'", "Una vida llena de desafíos"]
    },
    {
        "pregunta": "¿Además de la felicidad tranquila, qué otros aspectos menciona Ana que serán suyos en el futuro?",
        "respuesta": "El gozo del trabajo sincero, la aspiración digna y la amistad.",
        "opciones": ["Riqueza y fama", "Viajes y nuevas experiencias", "El gozo del trabajo sincero, la aspiración digna y la amistad.", "Poder y control"]
    },
    {
        "pregunta": "¿Qué afirma Ana que nada podrá apartarla de su 'derecho'?",
        "respuesta": "Su derecho a la fantasía o del mundo ideal de sus sueños.",
        "opciones": ["Su derecho a la educación", "Su derecho a la libertad", "Su derecho a la fantasía o del mundo ideal de sus sueños.", "Su derecho a opinar"]
    },
    {
        "pregunta": "¿Qué frase final, aunque incompleta, se utiliza para describir la permanencia del espíritu soñador de Ana?",
        "respuesta": "Y siempre estaba...",
        "opciones": ["Y nunca se rindió.", "Y siempre fue feliz.", "Y siempre estaba...", "Y finalmente encontró la paz."]
    }
]

# --- Configuración de la Sesión ---
if 'pregunta_actual_idx' not in st.session_state:
    st.session_state.pregunta_actual_idx = 0
    st.session_state.puntuacion = 0
    st.session_state.evaluacion_terminada = False
    st.session_state.preguntas_mezcladas = random.sample(preguntas_ana, len(preguntas_ana)) # Mezcla las preguntas
    st.session_state.respuestas_correctas_dadas = [] # Para almacenar las respuestas correctas del usuario
    st.session_state.respuestas_incorrectas_dadas = [] # Para almacenar las respuestas incorrectas del usuario

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
        st.session_state.respuestas_incorrectas_dadas.append(f"{pregunta_texto} (Tu respuesta: {opcion_elegida}, Correcta: {respuesta_correcta})")

    # Después de verificar, avanzamos a la siguiente pregunta
    siguiente_pregunta()
    st.experimental_rerun() # Fuerza una nueva ejecución para mostrar la siguiente pregunta

def reiniciar_evaluacion():
    st.session_state.pregunta_actual_idx = 0
    st.session_state.puntuacion = 0
    st.session_state.evaluacion_terminada = False
    st.session_state.preguntas_mezcladas = random.sample(preguntas_ana, len(preguntas_ana)) # Vuelve a mezclar
    st.session_state.respuestas_correctas_dadas = []
    st.session_state.respuestas_incorrectas_dadas = []
    st.experimental_rerun()

# --- Interfaz de Usuario con Streamlit ---
st.set_page_config(page_title="Evaluación Ana de las Tejas Verdes", page_icon="📚")

st.title("📚 Evaluación de 'Ana de las Tejas Verdes'")
st.markdown("Pon a prueba tu conocimiento sobre el inicio y final del libro.")
st.markdown("---")

if not st.session_state.evaluacion_terminada:
    pregunta_actual_data = st.session_state.preguntas_mezcladas[st.session_state.pregunta_actual_idx]

    st.subheader(f"Pregunta {st.session_state.pregunta_actual_idx + 1} de {len(st.session_state.preguntas_mezcladas)}")
    st.write(f"**{pregunta_actual_data['pregunta']}**")

    # Shuffle options for multiple choice
    opciones_mezcladas = random.sample(pregunta_actual_data['opciones'], len(pregunta_actual_data['opciones']))

    for opcion in opciones_mezcladas:
        if st.button(opcion, key=f"opcion_{opcion}_{st.session_state.pregunta_actual_idx}"):
            verificar_respuesta(opcion, pregunta_actual_data['respuesta'], pregunta_actual_data['pregunta'])

else:
    st.success("¡Evaluación terminada!")
    st.subheader(f"Tu puntuación final es: {st.session_state.puntuacion} de {len(st.session_state.preguntas_mezcladas)}")

    porcentaje = (st.session_state.puntuacion / len(st.session_state.preguntas_mezcladas)) * 100
    st.progress(porcentaje / 100) # Barra de progreso

    if porcentaje == 100:
        st.balloons()
        st.write("¡Felicidades! ¡Dominas el libro por completo! 🎉")
    elif porcentaje >= 70:
        st.write("¡Muy bien! Tienes un excelente conocimiento del libro. 👍")
    else:
        st.write("Sigue leyendo y repasando. ¡Puedes hacerlo mejor! 💪")

    st.markdown("---")
    st.subheader("Resumen de Respuestas:")
    if st.session_state.respuestas_correctas_dadas:
        st.markdown("**Respuestas Correctas:**")
        for r in st.session_state.respuestas_correctas_dadas:
            st.markdown(f"- {r}")
    else:
        st.info("No hubo respuestas correctas.")

    if st.session_state.respuestas_incorrectas_dadas:
        st.markdown("**Respuestas Incorrectas:**")
        for r in st.session_state.respuestas_incorrectas_dadas:
            st.markdown(f"- {r}")
    else:
        st.info("No hubo respuestas incorrectas.")

    st.markdown("---")
    if st.button("Reiniciar Evaluación"):
        reiniciar_evaluacion()

st.sidebar.markdown("---")
st.sidebar.info("Esta evaluación se basa en el primer capítulo y un fragmento del final del libro 'Ana de las Tejas Verdes'.")