from pathlib import Path
import tempfile


def pegar_dados_pdf(escritor):
    with tempfile.TemporaryDirectory() as temp_dir:
        temp_pdf_file = Path(temp_dir) / 'temp.pdf'
        escritor.write(temp_pdf_file)

        with open(temp_pdf_file, 'rb') as file:
            pdf_data = file.read()

    return pdf_data
