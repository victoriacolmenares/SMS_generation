import json
import streamlit as st
from transformers import (
    AutoTokenizer,
    AutoModelForCausalLM,
    pipeline,
)

model_card = 'fine-tuned-sms-generation-model'
model = AutoModelForCausalLM.from_pretrained(model_card)
tokenizer = AutoTokenizer.from_pretrained(model_card)


def main():
    categories = read_json()
    container = st.container()
    if 'kpis' not in st.session_state:
        # Initialize KPIs
        st.session_state.kpis = {category: 0 for category, _ in categories.items()}

    with container:
        st.title("Generador de SMS promocionales")
        category = st.selectbox(
            "Sobre cuál tema quieres que generar el mensaje?",
            options=categories.keys(),
        )

        st.markdown("<br>", unsafe_allow_html=True)
        base_sms, add_new_template = st_base_sms_template(categories, category)

        st.markdown("<br>", unsafe_allow_html=True)
        number = st.number_input(
            "Cuántos SMS quieres generar?",
            min_value=1,
            max_value=3,
            value=1,
            step=1,
            format="%d",
        )

        st.markdown("<br>", unsafe_allow_html=True)
        st_create_button(base_sms, category, categories, number, add_new_template)

        st.markdown("<br>", unsafe_allow_html=True)
        st_sms_generated()

    return container


def read_json(path="categories.json"):
    with open(path, 'r') as file:
        categories = json.load(file)
    return categories


def write_json(data, path="categories.json"):
    with open(path, 'w') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)


def st_base_sms_template(categories, category):
    template_sms = ""
    st.subheader("Puedes seleccionar un mensaje predefinido o escribir uno nuevo")
    template_sms = st.selectbox(
        "Selecciona una plantilla",
        options=categories[category],
        index=None,
        placeholder="",
    )
    base_sms = st.text_area(
        label="Quiero que mi SMS comience por...",
        value=template_sms,
        height=20,
        max_chars=50,
    )
    add_new_template = st.checkbox("¿Quieres añadirlo a la lista de plantillas?")
    return base_sms, add_new_template


def st_create_button(base_sms, category, categories, number, add_new_template):
    if st.button("Crear", disabled=not base_sms):
        with st.spinner('Creando SMS...'):
            sms_generated = generate_sms_with_pipeline(base_sms, number)

        st.session_state.sms_generated = sms_generated

        # Update KPIs
        st.session_state.kpis[category] += 1

        # Add new template to the category if not exists in the category list
        if add_new_template and base_sms not in categories[category]:
            categories[category].append(base_sms)
            write_json(categories)
            st.rerun()


def st_sms_generated():
    if "sent" in st.session_state:
        st.success("Mensaje enviado con éxito!", icon="🎉")
        del st.session_state.sms_generated
        del st.session_state.sent
        return

    if "sms_generated" in st.session_state:
        st.subheader("Selecciona el mensaje que quieres enviar")
        for sms in st.session_state.sms_generated:
            # We only want the first 3 sentences
            clean_sms = sms["generated_text"].split('.', 3)[:3]
            clean_sms = '.'.join(clean_sms)
            if st.button(clean_sms, key=clean_sms):
                send_sms(clean_sms)


@st.experimental_dialog("Seguro que quieres enviar este mensaje")
def send_sms(sms):
    st.write(sms)
    if st.button("Enviar mensaje"):
        st.session_state.sent = True
        st.rerun()


def generate_sms_with_pipeline(text, top_k=1):
    generator_pipeline = pipeline(
        "text-generation",
        model=model,
        tokenizer=tokenizer,
    )
    return generator_pipeline(
        text,
        num_return_sequences=top_k,
        no_repeat_ngram_size=2,  # avoid repetitions
    )
