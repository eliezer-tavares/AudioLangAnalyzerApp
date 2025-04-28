from deep_translator import GoogleTranslator
from typing import Optional
import logging

logger = logging.getLogger(__name__)

class TranslationService:
    """Gerencia a tradução de textos."""
    def translate(self, text: str, target_lang: str) -> Optional[str]:
        """Traduz o texto para o idioma alvo."""
        try:
            translator = GoogleTranslator(source="auto", target=target_lang)
            return translator.translate(text)
        except Exception as e:
            logger.error(f"Erro na tradução: {str(e)}")
            return None
