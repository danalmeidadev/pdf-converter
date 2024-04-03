from pathlib import Path
from utils import pegar_dados_pdf

import streamlit as st
import pypdf


def exibir_menu_marca_agua(coluna):
    if coluna:
        st.markdown('''
        ### Adicionar marca d'agua
        
        Selecione um arquivo PDF e uma marca d'agua nos seletores abaixo:
        
        ''')

        arquivo_pdf = st.file_uploader(
            label="Selecione o arquivo PDF...",
            type='pdf',
            accept_multiple_files=False,
        )
        arquivio_marca = st.file_uploader(
            label="Selecione o arquivo contendo a marca d'agua...",
            type='pdf',
            accept_multiple_files=False,
        )
        if arquivo_pdf and arquivio_marca:
            botoes_desativados = False
        else:
            botoes_desativados = True

        clicou_processar = st.button(
            'Clique para processar o arquivo PDF',
            use_container_width=True,
            disabled=botoes_desativados
        )

        def adicionar_marca_dagua(arquivo_pdf, arquivo_marca):
            pagina_marca = pypdf.PdfWriter(arquivo_marca).pages(0)
            escritor = pypdf.PdfWriter(clone_from=arquivo_pdf)
            for pagina in escritor.pages:
                escala_x = pagina.mediabox.width / pagina_marca.mediabox.width
                escala_y = pagina.mediabox.height / pagina_marca.mediabox.height
                transforme = pypdf.Transformation(escala_x, escala_y)
                pagina.merge_transformed_page(pagina_marca, transforme, over=False)

            dados_pdf = pegar_dados_pdf(escritor)
            return dados_pdf

        if clicou_processar:
            dados_pdf = adicionar_marca_dagua(arquivo_pdf=arquivo_pdf, arquivio_marca=arquivio_marca)

            nome_arquivo = f'{Path(arquivo_pdf.name).stem}_marca.pdf'
            st.download_button(
                'Clique para fazer download do arquivo PDF',
                type='primary',
                data=dados_pdf,
                file_name=nome_arquivo,
                mime='application/pdf',
                use_container_width=True
            )
