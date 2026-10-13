from pathlib import Path
from pypdf import PdfReader
from docx import Document

ALLOWED_EXTENSIONS = {".pdf", ".docx", ".txt"}


def read_document(file_path):
    path = Path(file_path)

    if not path.is_file():
        return "Error: File not found."

    if path.suffix.lower() not in ALLOWED_EXTENSIONS:
        return "Error: Upload a PDF, DOCX, or TXT file."

    try:
        if path.suffix.lower() == ".pdf":
            reader = PdfReader(str(path))
            text = "\n".join(
                page.extract_text() or ""
                for page in reader.pages
            )

        elif path.suffix.lower() == ".docx":
            document = Document(str(path))
            text = "\n".join(
                paragraph.text
                for paragraph in document.paragraphs
            )

        else:
            text = path.read_text(encoding="utf-8")

        if not text.strip():
            return (
                "No readable text found. "
                "If this is a scanned PDF, OCR may be needed."
            )

        return text[:20000]

    except Exception as error:
        return f"Could not read the document: {error}"


if __name__ == "__main__":
    file_path = input("Enter the document's full path: ").strip()
    file_path = file_path.strip('"')

    result = read_document(file_path)
    print("\n--- DOCUMENT CONTENT ---\n")
    print(result)
