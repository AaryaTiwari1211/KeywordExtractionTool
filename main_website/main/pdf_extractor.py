import io
from django.conf import settings
import PyPDF2 

def extract_text_from_pdf(file):
    with file.open('rb') as f:
        reader = PyPDF2.PdfReader(f)
        text = ''
        for page in reader.pages:
            text += page.extract_text()
        return text
