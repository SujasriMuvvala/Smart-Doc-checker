import PyPDF2

def check_resume(pdf_path):
    report = {}
    
    try:
        with open(pdf_path, "rb") as file:
            reader = PyPDF2.PdfReader(file)
            report["Total Pages"] = len(reader.pages)

            full_text = ""
            for page in reader.pages:
                text = page.extract_text()
                if text:
                    full_text += text.lower()

            if full_text.strip():
                report["Text Selectable"] = "Yes (ATS Friendly)"
            else:
                report["Text Selectable"] = "No (Image-based PDF)"

            sections = ["skills", "projects", "education", "experience"]
            found_sections = []

            for section in sections:
                if section in full_text:
                    found_sections.append(section.capitalize())

            report["Detected Sections"] = found_sections if found_sections else "None"

    except Exception as e:
        report["Error"] = str(e)

    return report


if __name__ == "__main__":
    pdf_file = "sample_resume.pdf"   # change if needed
    result = check_resume(pdf_file)

    print("\nSMART DOC CHECKER REPORT")
    print("-" * 30)
    for key, value in result.items():
        print(f"{key}: {value}")
