from docx2pdf import convert
import os

def needs_conversion(input_file, output_file):
    """Check if the Word file needs to be converted to PDF."""
    return not os.path.exists(output_file) or os.path.getmtime(input_file) > os.path.getmtime(output_file)

def convert_word_to_pdf(input_file, output_file):
    """Convert a Word document to a PDF."""
    try:
        convert(input_file, output_file)
        print("Conversion successful.")
    except Exception as e:
        print(f"Error during conversion: {e}")

# File paths
input_word_file = "CV/Akhil_PS_CV.docx"
output_pdf_file = "CV/Akhil_PS_CV.pdf"

# Perform conversion if needed
if needs_conversion(input_word_file, output_pdf_file):
    print("Updating PDF...")
    convert_word_to_pdf(input_word_file, output_pdf_file)
