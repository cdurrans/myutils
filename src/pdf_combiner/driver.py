
import argparse
import os
from PyPDF2 import PdfFileReader, PdfFileWriter

def combine_pdfs(paths, output):
    pdf_writer = PdfFileWriter()

    for path in paths:
        pdf_reader = PdfFileReader(path)
        for page in range(pdf_reader.getNumPages()):
            pdf_writer.addPage(pdf_reader.getPage(page))

    with open(output, 'wb') as out:
        pdf_writer.write(out)

if __name__ == "__main__":

    argparser = argparse.ArgumentParser()
    argparser.add_argument('path', nargs='+', help='Path to PDF files to combine')
    argparser.add_argument('-o', '--output', help='Output file name')
    args = argparser.parse_args()
    combine_pdfs(args['path'], args['output'])
