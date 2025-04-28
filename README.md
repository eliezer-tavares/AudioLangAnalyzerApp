# AudioLangAnalyzerApp

Aplicação desktop para análise de áudio, transcrição, detecção de idioma e geração de relatórios, em desenvolvimento por um programador deficiente visual total com foco em acessibilidade.

## Pré-requisitos
- Python 3.9+
- FFmpeg instalado (necessário para pydub)

## Instalação
1. Clone o repositóri em https://github.com/eliezer-tavares/AudioLangAnalyzerApp.git
2. Crie um ambiente virtual: `python -m venv venv`
3. Ative o ambiente: `venv\Scripts\activate` (Windows) ou `source venv/bin/activate` (Linux/Mac)
4. Instale as dependências: `pip install -r requirements.txt`
5. Instale o FFmpeg:
   - Windows: Baixe em https://ffmpeg.org/download.html
   - Linux: `sudo apt-get install ffmpeg`
   - Mac: `brew install ffmpeg`

## Uso
1. Execute: `python main.py`
2. Selecione um arquivo MP3
3. Clique em "Analisar Áudio"
4. Após a análise, clique em "Salvar Relatório PDF"

Contato do desenvolvedor:

Eliezer Tavares de Oliveira

Linkedin: www.eliezertavaresdeoliveira.com

E-mail: eliezertavaresdeoliveira@gmail.com
