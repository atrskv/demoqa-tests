from PyPDF2 import PdfReader

def test_pdf_number_of_pages():
    reader = PdfReader('docs-pytest-org-en-latest.pdf')
    number_of_pages = len(reader.pages)  # сколько страниц?
    print(number_of_pages)
    assert number_of_pages == 444, 'не 444'

def test_pdf_read():
    reader = PdfReader('docs-pytest-org-en-latest.pdf')
    page_0 = reader.pages[0]
    text = page_0.extractText()
    assert 'Release 0.1' in text
    print(text)