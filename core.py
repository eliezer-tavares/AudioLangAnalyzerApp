from audio_processor import AudioProcessor
from stt_service import STTService
from language_service import LanguageService
from translation_service import TranslationService
from report_generator import create_report
from wx.lib.pubsub import pub
import logging
from typing import Dict, Optional

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

class AudioAnalyzer:
    """Orquestra a análise de áudio e geração de relatório."""
    def __init__(self):
        self.audio_processor = AudioProcessor()
        self.stt_service = STTService()
        self.language_service = LanguageService()
        self.translation_service = TranslationService()
        self.result = None

    def analyze(self, file_path: str) -> None:
        """Executa o fluxo completo de análise em uma thread separada."""
        try:
            pub.sendMessage("status_update", message="Validando arquivo de áudio...")
            duration = self.audio_processor.validate_audio(file_path)
            if duration < 4.0:
                pub.sendMessage("status_update", message="Erro: Áudio deve ter pelo menos 4 segundos.")
                pub.sendMessage("analysis_error")
                return

            pub.sendMessage("status_update", message="Convertendo áudio para WAV...")
            wav_path = self.audio_processor.convert_to_wav(file_path)

            pub.sendMessage("status_update", message="Transcrevendo áudio...")
            transcription, detected_lang = self.stt_service.transcribe(wav_path)

            pub.sendMessage("status_update", message="Confirmando idioma...")
            language_info = self.language_service.detect_language(transcription, detected_lang)

            fluency = self.estimate_fluency(transcription)
            translation = None
            if language_info["code"] != "pt":
                pub.sendMessage("status_update", message="Traduzindo para Português...")
                translation = self.translation_service.translate(transcription, "pt")

            self.result = {
                "file_path": file_path,
                "duration": duration,
                "transcription": transcription,
                "language": language_info,
                "fluency": fluency,
                "translation": translation
            }
            pub.sendMessage("status_update", message="Análise concluída com sucesso.")
            pub.sendMessage("analysis_complete")

        except Exception as e:
            logger.error(f"Erro na análise: {str(e)}")
            pub.sendMessage("status_update", message=f"Erro: {str(e)}")
            pub.sendMessage("analysis_error")

    def estimate_fluency(self, transcription: str) -> str:
        """Estima o nível de fluência com base na transcrição."""
        words = transcription.split()
        sentences = transcription.split(".") if "." in transcription else [transcription]
        avg_words_per_sentence = len(words) / max(1, len(sentences))
        unique_words = len(set(words)) / max(1, len(words))

        if avg_words_per_sentence < 10 or unique_words < 0.3:
            return "Básico"
        elif avg_words_per_sentence < 20 or unique_words < 0.5:
            return "Intermediário"
        return "Avançado"

    def save_report(self, output_path: str) -> None:
        """Salva o relatório em PDF."""
        if self.result:
            create_report(self.result, output_path)
        else:
            raise ValueError("Nenhum resultado disponível para gerar relatório.")
