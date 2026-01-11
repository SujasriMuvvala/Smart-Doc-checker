# Smart Doc Checker

Smart Doc Checker is a Python-based tool that analyzes resume PDFs to check
basic ATS and formatting compliance.

## Features
- Checks whether PDF text is selectable (ATS-friendly)
- Counts number of pages
- Detects common resume sections like Skills, Projects, and Education

## Tech Stack
- Python
- PyPDF2
- File Handling

## How to Run
1. Install dependencies:
   pip install PyPDF2
2. Place a resume PDF as `sample_resume.pdf`
3. Run:
   python smart_doc_checker.py

## Output
The tool prints a compliance report directly in the terminal.
