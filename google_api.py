import os
import fitz  # PyMuPDF para ler PDFs
from docx import Document  # Para ler arquivos Word (.docx)
import google.generativeai as genai  # Biblioteca oficial do Gemini


# ====== CONFIGURE SUA API KEY AQUI ======
genai.configure(api_key="")  # Substitua pela sua API key do Gemini

# ====== Função para ler PDF ======
def ler_pdf(path):
    texto = ""
    with fitz.open(path) as doc:
        for pagina in doc:
            texto += pagina.get_text()
    return texto

# ====== Função para ler Word (.docx) ======
def ler_docx(path):
    texto = ""
    doc = Document(path)
    for par in doc.paragraphs:
        texto += par.text + "\n"
    return texto

# ====== Função para ler todos os arquivos da pasta ======
def ler_arquivos_da_pasta(pasta):
    conteudo = ""
    for arquivo in os.listdir(pasta):
        caminho = os.path.join(pasta, arquivo)
        if arquivo.endswith(".pdf"):
            conteudo += ler_pdf(caminho) + "\n"
        elif arquivo.endswith(".docx"):
            conteudo += ler_docx(caminho) + "\n"
    return conteudo

# ====== Função para perguntar ao Gemini ======
def perguntar_ao_gemini(texto_base, pergunta_usuario):
    model = genai.GenerativeModel('models/gemini-1.5-flash-001')
    resposta = model.generate_content([texto_base, pergunta_usuario])
    return resposta.text

# ====== DEFINA O CAMINHO DA SUA PASTA AQUI ======
pasta = "C:/Users/Braga/Desktop/teste"  # Ex: "C:/Users/bruno/Documentos/relatorios"

# ====== Lê os arquivos e junta tudo ======
conteudo_total = ler_arquivos_da_pasta(pasta)

# ====== Defina sua pergunta ======
pergunta = "qual o dono da elevato?"

# ====== Faz a pergunta ao Gemini ======
resposta = perguntar_ao_gemini(conteudo_total, pergunta)

# ====== Mostra a resposta ======
print("\n📘 RESPOSTA DO GEMINI:\n")
print(resposta)
