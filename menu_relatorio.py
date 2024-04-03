import tempfile
from pathlib import Path
from utils import pegar_dados_pdf
from projeto_pdf_excel.gerar_relatorio import CONFIG, main as gerar_relatorio_pdf

import streamlit as st
import pypdf


def exibir_menu_relatorio(coluna):
    if coluna:
        st.markdown('''
        ### Gerar re;atório PDF
        
        Escolha um arquivo excel para gerar relatorio:
        
        ''')

        arquivo_excel = st.file_uploader(
            label="Selecione o arquivo excel...",
            type='xlsx',
            accept_multiple_files=False,
        )
        if arquivo_excel:
            botoes_desativados = False
        else:
            botoes_desativados = True

        col1, col2 = st.columns(2)
        with col1:
            seletor_ano = st.selectbox('Ano', range(2020, 2025), disabled=botoes_desativados)

        with col2:
            seletor_mes = st.selectbox('Mes', range(1, 13), disabled=botoes_desativados)

        clicou_processar = st.button(
            'Clique para processar o arquivo Excel',
            use_container_width=True,
            disabled=botoes_desativados
        )

        def pegar_dados_do_relatorio_pdf(arquivo_excel, seletor_ano, seletor_mes):
            mes_referencia = f'{seletor_ano}-{seletor_mes}'
            CONFIG['mes_referencia'] = mes_referencia
            with tempfile.TemporaryDirectory as tempdir:
                caminho_temp = Path(tempdir)
                CONFIG['pasta_dados'] = caminho_temp
                CONFIG['pasta_output'] = caminho_temp
                with open(caminho_temp / 'dados.xlsx', 'wb') as arquivo_excel_temp:
                    dados_excel = arquivo_excel.getvalue()
                    arquivo_excel_temp.write(dados_excel)

                gerar_relatorio_pdf(**CONFIG)
                nome_output = caminho_temp / f'Relatório Mensal - {mes_referencia}.pdf'
                with open(nome_output, 'rb') as relatorio_pdf:
                    dados_pdf = relatorio_pdf.read()
            return dados_pdf

        if clicou_processar:
            dados_excel = pegar_dados_do_relatorio_pdf(arquivo_excel, seletor_ano, seletor_mes)
            if dados_excel is None:
                st.warning(f'Excel não possui dados para ano {seletor_ano} e mês {seletor_mes}')
                return
            nome_arquivo = f'relatorio.pdf'
            st.download_button(
                'Clique para fazer download do arquivo PDF',
                type='primary',
                data=dados_excel,
                file_name=nome_arquivo,
                mime='application/pdf',
                use_container_width=True
            )
