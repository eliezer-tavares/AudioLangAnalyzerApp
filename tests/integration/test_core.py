import pytest
from core import AudioAnalyzer
from unittest.mock import patch

def test_full_analysis_flow():
    analyzer = AudioAnalyzer()
    with patch.object(analyzer.audio_processor, "validate_audio", return_value=5.0), \
         patch.object(analyzer.audio_processor, "convert_to_wav", return_value="temp.wav"), \
         patch.object(analyzer.stt_service, "transcribe", return_value=("Hello", "en")), \
         patch.object(analyzer.language_service, "detect_language", return_value={
             "code": "en", "name": "English", "regions": ["USA"], "confidence": 0.9
         }), \
         patch.object(analyzer.translation_service, "translate", return_value="Olá"), \
         patch.object(analyzer, "save_report") as mock_save:
        analyzer.analyze("test.mp3")
        assert analyzer.result["transcription"] == "Hello"
        assert analyzer.result["language"]["code"] == "en"
        assert analyzer.result["translation"] == "Olá"
