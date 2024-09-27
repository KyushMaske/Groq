import os
from dotenv import load_dotenv
from PyPDF2 import PdfReader
from groq import Groq
from tkinter import Tk
from tkinter.filedialog import askopenfilename


load_dotenv()

api_key = os.getenv("GROQ_API_KEY")


client = Groq(api_key=api_key)


def extract_text_from_pdf(pdf_file_path):
    try:
        reader = PdfReader(pdf_file_path)
        text = ""
        for page in reader.pages:
            text += page.extract_text()
        return text
    except Exception as e:
        return f"Error extracting text from PDF: {str(e)}"


def generate_cover_letter(cv_text, job_position, company_name):
    try:
        prompt = (
            f"Based on the following CV, please write a personalized cover letter for the position of {job_position} "
            f"at {company_name}. The cover letter should be professional, concise,polite and relevant to the role.\n\n"
            f"CV:\n{cv_text}"
        )

        # Create a request to generate the cover letter
        messages = [
            {
                "role": "system",
                "content": "You are an AI that generates personalized professional cover letters.",
            },
            {"role": "user", "content": prompt},
        ]

        response = client.chat.completions.create(
            messages=messages,
            model="llama3-8b-8192",
            temperature=0.7,
            max_tokens=1024,
            top_p=1,
            stop=None,
        )

        cover_letter = response.choices[0].message.content
        return cover_letter
    except Exception as e:
        return f"Error generating cover letter: {str(e)}"


def save_cover_letter_as_text(cover_letter, job_position, company_name):

    file_name = f"{job_position}_Cover_Letter_for_{company_name}.txt"
    try:
        with open(file_name, "w") as file:
            file.write(cover_letter)
        print(f"\nCover letter successfully saved as {file_name}")
    except Exception as e:
        print(f"Error saving cover letter as text: {str(e)}")


def main():
    root = Tk()
    root.withdraw()

    pdf_path = askopenfilename(
        filetypes=[("PDF files", "*.pdf")], title="Select your CV in PDF format"
    )

    if not pdf_path:
        print("No file selected. Exiting.")
        return

    cv_text = extract_text_from_pdf(pdf_path)
    if "Error" in cv_text:
        print(cv_text)
        return

    print("\nExtracted CV Text:\n", cv_text[:1000], "...")

    job_position = input(
        "\nEnter the job position you're applying for (e.g., Software Engineer): "
    )
    company_name = input("Enter the company name: ")

    cover_letter = generate_cover_letter(cv_text, job_position, company_name)

    if "Error" not in cover_letter:
        print("\nGenerated Cover Letter:\n")
        print(cover_letter)

        save_cover_letter_as_text(cover_letter, job_position, company_name)
    else:
        print(cover_letter)


if __name__ == "__main__":
    main()
