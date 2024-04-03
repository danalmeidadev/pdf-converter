import streamlit as st
from streamlit_option_menu import option_menu

import menu_combinar
import menu_extrair
import menu_imagens
import menu_marca_agua
import menu_relatorio

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
            menu_combinar.exibir_menu_combinar(coluna=col2)
        case "Adicionar marca d'água":
            menu_marca_agua.exibir_menu_marca_agua(coluna=col2)
        case 'Imagens para PDF':
            menu_imagens.exibir_menu_imagens(coluna=col2)
        case 'Excel para PDF':
            menu_relatorio.exibir_menu_relatorio(coluna=col2)
        case _:
            st.write('Escolha uma opção')
