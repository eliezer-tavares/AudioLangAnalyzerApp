import speech_recognition as sr
from typing import Tuple, Optional
import logging

logger = logging.getLogger(__name__)

class STTService:
    """Gerencia a transcrição de áudio usando Whisper."""
    def __init__(self):
        self.recognizer = sr.Recognizer()

    def transcribe(self, wav_path: str) -> Tuple[str, Optional[str]]:
        """Transcreve o áudio e tenta detectar o idioma."""
        with sr.AudioFile(wav_path) as source:
            audio = self.recognizer.record(source)
            try:
                # Usar Whisper local
                result = self.recognizer.recognize_whisper(audio, model="base", language=None)
                # Whisper não retorna idioma confiável diretamente, usamos None como fallback
                return result, None
            except sr.UnknownValueError:
                raise ValueError("Não foi possível entender o áudio")
            except sr.RequestError as e:
                raise RuntimeError(f"Erro no serviço de transcrição: {str(e)}")
