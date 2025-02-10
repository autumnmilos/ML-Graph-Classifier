import fitz
import os
import argparse
 
def extract_images_from_pdf(pdf_path, output_folder):
    doc = fitz.open(pdf_path)
    for i, page in enumerate(doc):
        for img_index, img in enumerate(page.get_images(full=True)):
            xref = img[0]
            base_image = doc.extract_image(xref)
            image_bytes = base_image["image"]
            ext = base_image["ext"]
            image_filename = f"{output_folder}/page_{i+1}_img_{img_index+1}.{ext}"
            with open(image_filename, "wb") as f:
                f.write(image_bytes)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--pdf_folder", required=True)
    parser.add_argument("--output_folder", required=True)
    args = parser.parse_args()
    
    os.makedirs(args.output_folder, exist_ok=True)
    for pdf_file in os.listdir(args.pdf_folder):
        if pdf_file.endswith(".pdf"):
            extract_images_from_pdf(os.path.join(args.pdf_folder, pdf_file), args.output_folder)

if __name__ == "__main__":
    main()
