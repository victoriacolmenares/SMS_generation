import streamlit as st


def main():
    container = st.container()
    with container:
        if "kpis" in st.session_state:
            kpis = st.session_state.kpis
            categories = list(kpis.keys())
            num_cols = len(kpis)
            columns = st.columns(num_cols)
            for i, categoria in enumerate(categories):
                col = columns[i % num_cols]
                with col:
                    st.metric(label=categoria, value=kpis[categoria])
        else:
            st.write("No se han enviado SMS...")

    return container
