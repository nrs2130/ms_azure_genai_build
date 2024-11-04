import os
import glob
import PyPDF2

def pdf_to_text(pdf_path, output_txt):
    # Open the PDF file in read-binary mode
    with open(pdf_path, 'rb') as pdf_file:
        # Create a PdfReader object
        pdf_reader = PyPDF2.PdfReader(pdf_file)

        # Initialize an empty string to store the text
        text = ''

        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            text += page.extract_text() or ""  # Add text from each page

    # Write the extracted text to a text file
    with open(output_txt, 'w', encoding='utf-8') as txt_file:
        txt_file.write(text)

if __name__ == "__main__":
    # Path to the input folder with PDFs
    input_folder = r'G:\Shared drives\SURGO HEALTH\07 R&D\03 Methods\GenAI Experimentation\Organon Sandbox\01_Knowledge PDFs'
    
    # Path to the output folder for text files
    output_folder = r'C:\Users\NickStewart\Documents\Github\ms_azure_genai_build\text_outputs'

    # Ensure the output directory exists
    os.makedirs(output_folder, exist_ok=True)

    # Loop through all PDF files in the input folder
    for pdf_path in glob.glob(os.path.join(input_folder, '*.pdf')):
        # Get the base name of the PDF file (without directory and extension)
        base_name = os.path.splitext(os.path.basename(pdf_path))[0]
        
        # Define the path for the output text file
        output_txt = os.path.join(output_folder, f"{base_name}.txt")

        # Convert PDF to text
        pdf_to_text(pdf_path, output_txt)

        print(f"Converted {pdf_path} to {output_txt}")
    
    print("All PDFs have been successfully converted to text!")
