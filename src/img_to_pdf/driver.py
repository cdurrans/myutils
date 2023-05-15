

import img2pdf
import argparse

def convert_images_to_pdf(image_paths, output_path):
    with open(output_path, "wb") as f:
        f.write(img2pdf.convert([i for i in image_paths if i.endswith(".jpg") or i.endswith(".png") or i.endswith(".jpeg")]))



if __name__ == "__main__":
    # Example usage:
    argparser = argparse.ArgumentParser()
    argparser.add_argument('path', nargs='+', help='Path to PDF files to combine')
    argparser.add_argument('-o', '--output', help='Output file name')
    args = argparser.parse_args()
    convert_images_to_pdf(args['path'], args['output'])


