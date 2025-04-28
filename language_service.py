from langdetect import detect_langs
import langid
import pycountry
from typing import Dict, Optional
import logging

logger = logging.getLogger(__name__)

class LanguageService:
    """Gerencia detecção de idioma e informações geográficas."""
    def detect_language(self, transcription: str, whisper_lang: Optional[str] = None) -> Dict:
        """Detecta o idioma da transcrição."""
        if not transcription.strip():
            return {"code": None, "name": "Indeterminado", "regions": [], "confidence": 0.0}

        # Priorizar idioma do Whisper, se disponível
        if whisper_lang:
            return self.get_language_info(whisper_lang, 0.95)

        # Usar langdetect como principal
        try:
            langs = detect_langs(transcription)
            primary_lang = langs[0]
            code = primary_lang.lang
            confidence = primary_lang.prob
        except:
            code = None
            confidence = 0.0

        # Confirmar com langid
        if code:
            langid_code, langid_conf = langid.classify(transcription)
            if langid_code != code and langid_conf > confidence:
                code = langid_code
                confidence = langid_conf

        return self.get_language_info(code, confidence)

    def get_language_info(self, code: Optional[str], confidence: float) -> Dict:
        """Obtém informações detalhadas do idioma."""
        if not code:
            return {"code": None, "name": "Indeterminado", "regions": [], "confidence": confidence}

        try:
            lang = pycountry.languages.get(alpha_2=code)
            name = lang.name if lang else code
            regions = []
            # Mapeamento simplificado para regiões
            region_map = {
                "en": ["Reino Unido", "Estados Unidos"],
                "es": ["Espanha", "América Latina"],
                "pt": ["Portugal", "Brasil"],
            }
            regions = region_map.get(code, [])
            return {
                "code": code,
                "name": name,
                "regions": regions,
                "confidence": confidence
            }
      except:
            return {"code": code, "name": code, "regions": [], "confidence": confidence}
