#https://realpython.com/creating-modifying-pdf/#extracting-text-from-a-pdf


from PyPDF2 import PdfFileReader, PdfFileWriter
from pathlib import Path
import os


ENCRYPTED_FILE_PATH = (Path().absolute()
                /"Pride.pdf")
FILE_OUT_PATH = (Path().absolute()/"pride.pdf")
OUTPUT_FILE_PATH = Path().absolute()/"Pride.txt"


def writing_txt(input_file_path, output_file_path):
    pdf_reader = PdfFileReader(str(input_file_path))
    with output_file_path.open("w") as output_file: 
        title = pdf_reader.documentInfo.title
        num_pages = pdf_reader.getNumPages()
        output_file.write(f"{title}\\ Number of pages: {num_pages}\\\n")

        for page in pdf_reader.pages:
            text = page.extractText()
            output_file.write(text)

OUTPUT_FILE_PATH = Path().absolute()/"Blank.pdf"
    

def writing_pdf(input_file_path, output_file_path):

    pdf_writer = PdfFileWriter()
    pdf_writer.addBlankPage(width=72, height=72)
    with open(output_file_path, "wb") as output_file:
        pdf_writer.write(output_file)
        

    


if __name__ == "__main__":

    writing_txt(FILE_OUT_PATH, OUTPUT_FILE_PATH)
    writing_pdf(FILE_OUT_PATH, OUTPUT_FILE_PATH)

    
  

    
    

