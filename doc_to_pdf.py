from docx2pdf import convert
import os

# Example usage
input_word_file = "CV/Akhil_PS_CV.docx"
output_pdf_file = "CV/Akhil_PS_CV.pdf"

def convrt_or_not(input_file, output_file):
    if os.path.exists(output_file):
        if os.path.getmtime(input_file) > os.path.getmtime(output_file):
            return True
        else:
            return False
    else:
        return True

def convert_word_to_pdf(input_file, output_file):
    try:
        # Convert the Word file to PDF
        convert(input_file, output_file)
    except Exception as e:
        print(f"An error occurred: {e}")


if convrt_or_not(input_word_file, output_pdf_file) == True:
    print("Need update")
    convert_word_to_pdf(input_word_file, output_pdf_file)