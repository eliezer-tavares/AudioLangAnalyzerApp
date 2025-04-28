from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from typing import Dict
import logging

logger = logging.getLogger(__name__)

def create_report(data: Dict, output_path: str) -> None:
    """Cria um relatório PDF com os resultados da análise."""
    doc = SimpleDocTemplate(output_path, pagesize=A4)
    styles = getSampleStyleSheet()
    story = []

    story.append(Paragraph("Relatório de Análise de Áudio", styles["Title"]))
    story.append(Spacer(1, 12))

    # Informações do arquivo
    story.append(Paragraph("Informações do Arquivo", styles["Heading2"]))
    story.append(Paragraph(f"Caminho: {data['file_path']}", styles["Normal"]))
    story.append(Paragraph(f"Duração: {data['duration']:.2f} segundos", styles["Normal"]))
    story.append(Spacer(1, 12))

    # Sumário da análise
    story.append(Paragraph("Sumário da Análise", styles["Heading2"]))
    story.append(Paragraph("Status: Sucesso", styles["Normal"]))
    story.append(Spacer(1, 12))

    # Transcrição
    story.append(Paragraph("Transcrição Original", styles["Heading2"]))
    story.append(Paragraph(data["transcription"] or "N/A", styles["Normal"]))
    story.append(Spacer(1, 12))

    # Detalhes do idioma
    story.append(Paragraph("Detalhes do Idioma", styles["Heading2"]))
    lang = data["language"]
    story.append(Paragraph(f"Idioma Detectado: {lang['name']} ({lang['code']})", styles["Normal"]))
    story.append(Paragraph(f"Regiões: {', '.join(lang['regions']) or 'N/A'}", styles["Normal"]))
    story.append(Paragraph(f"Nível de Fluência Estimado: {data['fluency']}", styles["Normal"]))
    story.append(Spacer(1, 12))

    # Tradução
    story.append(Paragraph("Tradução para Português", styles["Heading2"]))
    story.append(Paragraph(data["translation"] or "N/A", styles["Normal"]))

    doc.build(story)
    logger.info(f"Relatório gerado em: {output_path}")
