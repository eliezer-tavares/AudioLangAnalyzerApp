from pydub import AudioSegment
import tempfile
import os
from typing import Optional
import logging

logger = logging.getLogger(__name__)

class AudioProcessor:
    """Gerencia o carregamento e pré-processamento de arquivos de áudio."""
    def validate_audio(self, file_path: str) -> float:
        """Valida o arquivo de áudio e retorna sua duração."""
        if not file_path.endswith(".mp3"):
            raise ValueError("Arquivo deve ser MP3")
        if not os.path.exists(file_path):
            raise FileNotFoundError("Arquivo não encontrado")
        
        audio = AudioSegment.from_mp3(file_path)
        return len(audio) / 1000.0  # Duração em segundos

    def convert_to_wav(self, file_path: str) -> str:
        """Converte MP3 para WAV temporário."""
        audio = AudioSegment.from_mp3(file_path)
        temp_file = tempfile.NamedTemporaryFile(suffix=".wav", delete=False)
        audio.export(temp_file.name, format="wav")
        return temp_file.name
