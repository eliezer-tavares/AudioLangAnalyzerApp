import pytest
from audio_processor import AudioProcessor
from unittest.mock import patch, MagicMock

def test_validate_audio_valid():
    processor = AudioProcessor()
    with patch("pydub.AudioSegment.from_mp3") as mock_audio:
        mock_audio.return_value = MagicMock(len=lambda: 5000)  # 5 segundos
        duration = processor.validate_audio("test.mp3")
        assert duration == 5.0

def test_validate_audio_invalid_extension():
    processor = AudioProcessor()
    with pytest.raises(ValueError, match="Arquivo deve ser MP3"):
        processor.validate_audio("test.wav")

def test_validate_audio_not_found():
    processor = AudioProcessor()
    with pytest.raises(FileNotFoundError, match="Arquivo não encontrado"):
        processor.validate_audio("nonexistent.mp3")
