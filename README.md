
# College AI Assistant

A Python-based college assistant project.

## Features
- Calculate attendance percentage
- Mark student attendance by subject and date
- Store attendance records using SQLite
- Read PDF, DOCX, and TXT documents
- Initial timetable text extraction

## Technologies
- Python
- SQLite
- OpenAI SDK (LLM integration planned)
- pypdf
- python-docx

## Setup

1. Install Python.
2. Open this folder in VS Code.
3. Create and activate a virtual environment.
4. Install dependencies:

   pip install -r requirements.txt

5. Create a `.env` file and add your API key when LLM integration is configured.
6. Run the application:

   python college_assistant.py

## Security
Do not upload API keys, `.env` files, or private student attendance records.
