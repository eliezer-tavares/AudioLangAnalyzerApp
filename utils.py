import os
from typing import Optional

def format_duration(seconds: float) -> str:
    """Formata a duração em segundos para uma string legível."""
    return f"{seconds:.2f} segundos"

def cleanup_temp_file(file_path: Optional[str]) -> None:
    """Remove arquivo temporário, se existir."""
    if file_path and os.path.exists(file_path):
        try:
            os.unlink(file_path)
        except Exception as e:
            logging.warning(f"Não foi possível remover arquivo temporário {file_path}: {str(e)}")
