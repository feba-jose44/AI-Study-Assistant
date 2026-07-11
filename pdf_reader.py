from PyPDF2 import PdfReader

def read_pdf(uploaded_file):
    """
    Reads a PDF and returns all the extracted text.
    """

    reader = PdfReader(uploaded_file)

    all_text = ""

    for page in reader.pages:
        text = page.extract_text()

        if text:
            all_text += text + "\n"

    return all_text