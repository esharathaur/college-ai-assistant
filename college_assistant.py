from document_reader import read_document
import sqlite3
from datetime import datetime

DB_NAME = "attendance.db"


def setup_database():
    with sqlite3.connect(DB_NAME) as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS attendance (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                student TEXT NOT NULL,
                subject TEXT NOT NULL,
                date TEXT NOT NULL,
                status TEXT NOT NULL,
                UNIQUE(student, subject, date)
            )
        """)


def calculate_attendance(attended, total):
    if total <= 0 or attended < 0 or attended > total:
        return "Invalid class counts."

    percentage = attended / total * 100
    return f"Attendance percentage: {percentage:.2f}%"


def mark_attendance(student, subject, date, status):
    try:
        datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        return "Invalid date. Use YYYY-MM-DD."

    status = status.strip().capitalize()
    if status not in ("Present", "Absent"):
        return "Status must be Present or Absent."

    try:
        with sqlite3.connect(DB_NAME) as conn:
            conn.execute("""
                INSERT INTO attendance
                (student, subject, date, status)
                VALUES (?, ?, ?, ?)
            """, (student, subject, date, status))
        return f"{student}: {status} for {subject} on {date}."
    except sqlite3.IntegrityError:
        return "Attendance already exists for this student, subject and date."


def run_assistant():
    setup_database()
    print("=== COLLEGE AI ASSISTANT ===")
    print("1. Calculate attendance percentage")
    print("2. Mark attendance")
    print("3. Read a PDF, DOCX, or TXT file")
    print("Type exit to close.")

    while True:
        choice = input("\nChoose 1 or 2 or 3: ").strip()

        if choice.lower() == "exit":
            break

        if choice == "1":
            try:
                attended = int(input("Classes attended: "))
                total = int(input("Total classes: "))
                print(calculate_attendance(attended, total))
            except ValueError:
                print("Enter valid whole numbers.")

        elif choice == "2":
            student = input("Student name or ID: ").strip()
            subject = input("Subject: ").strip()
            date = input("Date (YYYY-MM-DD): ").strip()
            status = input("Status (Present/Absent): ").strip()

            if not student or not subject:
                print("Student and subject are required.")
                continue

            print(mark_attendance(student, subject, date, status))
       
        elif choice == "3":
            file_path = input(
                "Enter the document's full path: "
            ).strip().strip('"')

            from document_reader import read_document
            result = read_document(file_path)

            print("\n--- DOCUMENT CONTENT ---\n")
            print(result)

        else:
            print("Please choose 1, 2, 3, or exit.")

          

if __name__ == "__main__":
    run_assistant()
