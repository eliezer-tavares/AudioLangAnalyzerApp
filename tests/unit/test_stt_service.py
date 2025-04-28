import pytest
from stt_service import STTService
from unittest.mock import patch, MagicMock

def test_transcribe_success():
    service = STTService()
    with patch("speech_recognition.Recognizer.recognize_whisper") as mock_whisper:
        mock_whisper.return_value = "Hello world"
        transcription, lang = service.transcribe("test.wav")
        assert transcription == "Hello world"
        assert lang is None

def test_transcribe_unknown_value():
    service = STTService()
    with patch("speech_recognition.Recognizer.recognize_whisper") as mock_whisper:
        mock_whisper.side_effect = sr.UnknownValueError()
        with pytest.raises(ValueError, match="Não foi possível entender o áudio"):
            service.transcribe("test.wav")
