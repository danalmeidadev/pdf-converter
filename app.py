import streamlit as st
from streamlit_option_menu import option_menu

import menu_extrair

st.set_page_config(
    page_title="PDFTools",
    page_icon="📄",
    layout="wide"
)

_, col2, _ = st.columns(3)

with col2:
    st.title("PDFTools")
    st.markdown('''
    ### Escolha a opção desejada abaixo
    ''')

entradas_menu = {
    'Extrair página': 'file-earmark-pdf-fill',
    'Combinar PDFs': 'plus-square-fill',
    "Adicionar marca d'água": 'droplet-fill',
    'Imagens para PDF': 'file-earmark-richtext-fill',
    'Excel para PDF': 'file-earmark-spreadsheet-fill',
}

escolha = option_menu(
    "",
    orientation='horizontal',
    options=list(entradas_menu.keys()),
    icons=list(entradas_menu.values()),
    default_index=0
)
_, col2, _ = st.columns(3)
with col2:
    match escolha:
        case 'Extrair página':
            menu_extrair.exibir_menu_extrair(coluna=col2)
        case 'Combinar PDFs':
            st.write('Combinar PDFs')
        case "Adicionar marca d'água":
            st.write("Adicionar marca d'água")
        case 'Imagens para PDF':
            st.write('Imagens para PDF')
        case 'Excel para PDF':
            st.write('Excel para PDF')
        case _:
            st.write('Escolha uma opção')
