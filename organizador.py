import os
import shutil

# Caminho da pasta a ser organizada
pasta_origem = "/Users/amandananni/Documents/organizador de arquivos" 

# Categorias de arquivos
tipos_arquivos = {
    "Imagens": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Documentos": [".pdf", ".docx", ".txt", ".xlsx"],
    "Vídeos": [".mp4", ".avi", ".mkv"],
    "Áudios": [".mp3", ".wav", ".flac"]
}

# Organizar os arquivos
for arquivo in os.listdir(pasta_origem):
    caminho_completo = os.path.join(pasta_origem, arquivo)
    if os.path.isfile(caminho_completo):
        _, extensao = os.path.splitext(arquivo)
        for pasta, extensoes in tipos_arquivos.items():
            if extensao.lower() in extensoes:
                pasta_destino = os.path.join(pasta_origem, pasta)
                os.makedirs(pasta_destino, exist_ok=True)
                shutil.move(caminho_completo, os.path.join(pasta_destino, arquivo))
                print(f"{arquivo} → {pasta}")
                break 
