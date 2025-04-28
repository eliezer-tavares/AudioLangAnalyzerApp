# AudioLangAnalyzerApp

[![Licença MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

**Análise Inteligente de Áudio com Foco Total em Acessibilidade**

## Visão Geral

O **AudioLangAnalyzerApp** é uma aplicação desktop desenvolvida em Python com wxPython, projetada para analisar arquivos de áudio (MP3). A ferramenta realiza as seguintes tarefas:

*   **Validação e Pré-processamento:** Verifica a validade do arquivo e o converte para um formato adequado.
*   **Transcrição:** Converte a fala do áudio em texto usando o modelo Whisper.
*   **Detecção de Idioma:** Identifica o idioma principal falado no áudio.
*   **Estimativa de Fluência:** Fornece uma estimativa (Básico, Intermediário, Avançado) da fluência do falante.
*   **Tradução:** Traduz a transcrição para o Português (caso o idioma original não seja PT-BR).
*   **Geração de Relatório:** Salva um relatório completo da análise em formato PDF.

## Motivação e Acessibilidade: Um Projeto Pessoal

Eu sou Eliezer Tavares de Oliveira, estudante do sexto semestre de Engenharia de Computação na Univesp e desenvolvedor deficiente visual total. Criei o **AudioLangAnalyzerApp** com um duplo propósito:

*   **Minimizar Barreiras de Comunicação:** Facilitar a compreensão de conteúdos em áudio recebidos em idiomas estrangeiros, tornando a informação mais acessível a todos.
*   **Software Acessível por Design:** Desenvolver uma aplicação que seja **completamente utilizável por pessoas com deficiência visual** que dependem de leitores de tela (como NVDA ou JAWS). A acessibilidade não é um recurso adicional, mas um pilar fundamental desde a concepção, utilizando as APIs de acessibilidade do wxPython (`wx.Accessible`) e realizando testes contínuos com leitores de tela.

Este projeto também serve como uma demonstração prática das minhas habilidades em desenvolvimento de software, arquitetura de aplicação, integração de APIs e meu compromisso com a criação de tecnologia inclusiva.

## Tecnologias Utilizadas

*   **Linguagem:** Python 3.9+
*   **Interface Gráfica:** wxPython (com foco em acessibilidade)
*   **Processamento de Áudio:** pydub (requer FFmpeg)
*   **Transcrição (STT):** SpeechRecognition com OpenAI Whisper (modelo local 'base')
*   **Detecção de Idioma:** langdetect, langid, pycountry
*   **Tradução:** deep-translator (usando Google Translate API)
*   **Geração de PDF:** reportlab
*   **Testes:** pytest, pytest-mock, pytest-cov
*   **Comunicação entre Threads:** wx.lib.pubsub

## Pré-requisitos

*   Python 3.9 ou superior
*   **FFmpeg:** Essencial para o `pydub` manipular arquivos de áudio.
    *   **Windows:** Baixe o executável em [ffmpeg.org](https://ffmpeg.org/download.html) e adicione-o ao PATH do sistema.
    *   **Linux (Debian/Ubuntu):** `sudo apt update && sudo apt install ffmpeg`
    *   **macOS (usando Homebrew):** `brew install ffmpeg`

## Instalação

1.  **Clone o Repositório:**
    ```bash
    git clone https://github.com/eliezer-tavares/AudioLangAnalyzerApp.git
    cd AudioLangAnalyzerApp
    ```

2.  **Crie e Ative um Ambiente Virtual:**
    ```bash
    # Windows
    python -m venv venv
    venv\Scripts\activate

    # Linux / macOS
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Instale as Dependências:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Verifique a Instalação do FFmpeg:**
    Execute `ffmpeg -version` no seu terminal. Se o comando não for encontrado, certifique-se de que ele está instalado e no PATH do seu sistema.

## Uso

1.  **Execute a Aplicação:**
    ```bash
    python main.py
    ```
2.  **Selecione o Arquivo:** Clique no botão "Selecionar Arquivo MP3" (totalmente acessível via teclado e leitor de tela) e escolha um arquivo `.mp3` com pelo menos 4 segundos de duração.
3.  **Inicie a Análise:** Clique no botão "Analisar Áudio". O status da análise será exibido na área de texto e anunciado pelo leitor de tela (se ativo). Uma barra de progresso indicará atividade.
4.  **Salve o Relatório:** Após a conclusão bem-sucedida da análise, o botão "Salvar Relatório PDF" será habilitado. Clique nele para salvar o PDF com os resultados detalhados.

## Executando os Testes

Para garantir a qualidade e a robustez do código, testes unitários e de integração foram desenvolvidos usando `pytest`.

1.  Certifique-se de que as dependências de teste estão instaladas (elas já estão no `requirements.txt`).
2.  Execute os testes e veja a cobertura de código:
    ```bash
    pytest --cov=. tests/
    ```

## Licença

Este projeto é distribuído sob a **Licença MIT**. Veja o arquivo [LICENSE](LICENSE) para mais detalhes. Sinta-se à vontade para usar, modificar e distribuir o código, mantendo o aviso de copyright.

## Oportunidades e Contato

Este projeto é um reflexo da minha paixão por programação e resolução de problemas, e uma vitrine das minhas capacidades técnicas. Estou ativamente **buscando oportunidades de estágio ou emprego na área de desenvolvimento de software**, onde possa aplicar e expandir meus conhecimentos, contribuindo para equipes e projetos inovadores.

Se você se interessou pelo meu trabalho ou acredita que minhas habilidades podem agregar valor à sua empresa, por favor, entre em contato:

*   **Nome:** Eliezer Tavares de Oliveira
*   **LinkedIn:** [https://www.linkedin.com/in/eliezer-tavares-de-oliveira-625a6b40/](https://www.linkedin.com/in/eliezer-tavares-de-oliveira-625a6b40/)
*   **E-mail:** [eliezertavaresdeoliveira@gmail.com](mailto:eliezertavaresdeoliveira@gmail.com)
*   **GitHub:** [github.com/eliezer-tavares](https://github.com/eliezer-tavares)
