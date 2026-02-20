from pdfminer.high_level import extract_text

def extract_resume_text(pdf_path):
    """
    Extracts text from resume PDF
    """
    try:
        text = extract_text(pdf_path)

        # clean text
        text = text.replace('\n', ' ')
        text = text.replace('\t', ' ')
        text = " ".join(text.split())

        return text

    except Exception as e:
        print("Error reading resume:", e)
        return ""