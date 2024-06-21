import streamlit as st
from generate_sms import main as generate_sms
from kpis import main as kpis


def main():
    st.set_page_config(
        page_title="Generador de SMS promocionales",
        page_icon="📩",
    )

    tabs = ["📲 Generar SMS", "📈 KPIs"]
    tab1_content, tab2_content = st.tabs(tabs)

    with tab1_content:
        generate_sms()

    with tab2_content:
        kpis()


if __name__ == "__main__":
    main()
