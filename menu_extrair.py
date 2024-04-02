from pathlib import Path
import tempfile


import streamlit as st
import pypdf


def exibir_menu_extrair(coluna):
    if coluna:
        st.markdown('''
        ### Extrair página PDF
        
        Escolha uma arquivo PDF para extrair uma página:
        
        ''')

        arquivo_pdf = st.file_uploader(
            label="Selecione o arquivo PDF...",
            type='pdf',
            accept_multiple_files=False,
        )
        if arquivo_pdf:
            botoes_desativados = False
        else:
            botoes_desativados = True

        numero_pagina = st.number_input('Página para extrair', min_value=1, disabled=botoes_desativados)
        clicou_processar = st.button(
            'Clique para processar o arquivo PDF',
            use_container_width=True,
            disabled=botoes_desativados
        )

        def extrair_pagina_pdf(arquivo_pdf, numero_pagina):
            leitor = pypdf.PdfReader(arquivo_pdf)
            pagina = leitor.pages[numero_pagina -1]
            escritor = pypdf.PdfWriter()
            escritor.add_page(pagina)

            with tempfile.TemporaryDirectory() as temp_dir:
                temp_pdf_file = Path(temp_dir) / 'temp.pdf'
                escritor.write(temp_pdf_file)

                with open(temp_pdf_file, 'rb') as file:
                    pdf_data = file.read()

            return  pdf_data

        if clicou_processar:
            dados_pdf = extrair_pagina_pdf(arquivo_pdf=arquivo_pdf, numero_pagina=numero_pagina)
            nome_arquivo = f'{Path(arquivo_pdf.name).stem}_pg{numero_pagina:03d}.pdf'
            st.download_button(
                'Clique para fazer download do arquivo PDF',
                type='primary',
                data=dados_pdf,
                file_name=nome_arquivo,
                mime='application/pdf',
                use_container_width=True
            )
