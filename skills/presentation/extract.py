import fitz  # PyMuPDF
import sys
import json

def extract_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    text = ""
    for page in doc:
        text += page.get_text() + "\n"
    return text

if __name__ == "__main__":
    text = extract_pdf(sys.argv[1])
    print(text)
