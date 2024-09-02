import fitz

def read_pdf(file_path):
    text = ""
    try:
        pdf_document = fitz.open(file_path)
        for page_num in range(len(pdf_document)):
            page = pdf_document.load_page(page_num)
            text += page.get_text()
        pdf_document.close()
    except FileNotFoundError:
        print(f"Erro: O arquivo '{file_path}' não foi encontrado.")
    except Exception as e:
        print(f"Erro ao ler o arquivo '{file_path}': {e}")
    
    return text

def process_text(text):
    words = ''.join(char.lower() if char.isalnum() or char.isspace() 
                    else ' ' for char in text).split()
    return words

def analyze_text(text):
    unique_words = len(set(text))
    total_words = len(text)
    return unique_words, total_words

biblia = read_pdf('biblia.pdf')
pdf_process = process_text(biblia)
b_unique, b_total = analyze_text(pdf_process)

print(f"Número de palavras distintas: {b_unique}")
print(f"Número de total de palavras: {b_total}")