# Organizador de Arquivos em Python 🗂️

![Python](https://img.shields.io/badge/Python-3.6+-blue) 
![License](https://img.shields.io/badge/License-MIT-green)

Um script em Python para **organizar automaticamente arquivos em pastas por tipo**, facilitando a limpeza e organização de diretórios como Downloads, Documentos ou Desktop.

---

## Funcionalidades

- Move arquivos para subpastas de acordo com a extensão:
  - **Imagens**: `.jpg`, `.jpeg`, `.png`, `.gif`, `.bmp`
  - **Documentos**: `.pdf`, `.docx`, `.txt`, `.xlsx`
  - **Vídeos**: `.mp4`, `.avi`, `.mkv`
  - **Áudios**: `.mp3`, `.wav`, `.flac`
  - **Outros**: arquivos que não se encaixam em nenhuma categoria
- Cria automaticamente as pastas caso não existam.
- Evita sobrescrever arquivos existentes.
- Fácil de configurar e personalizar.

---

## Pré-requisitos

- Python 3.6 ou superior  
- Bibliotecas padrão do Python: `os` e `shutil` (já inclusas)

---

## Como usar

1. Clone este repositório:

```bash
git clone https://github.com/SEU_USUARIO/organizador-de-arquivos.git
cd organizador-de-arquivos
```
2. Abra o arquivo organizador.py e altere o caminho da pasta que deseja organizar:

```bash
pasta_origem = "/Users/SEU_USUARIO/Downloads"
```

3.Execute o script:

```bash
python3 organizador.py
```

Verifique sua pasta: os arquivos foram movidos para subpastas correspondentes, incluindo a pasta Outros para arquivos sem categoria definida.


