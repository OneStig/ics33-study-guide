import os
import subprocess
from PyPDF2 import PdfMerger

def find_notebooks(directory):
    notebooks = [os.path.join(dp, f) for dp, dn, filenames in os.walk(directory) for f in filenames if f.endswith('.ipynb')]
    notebooks.sort()
    return notebooks

def convert_to_pdf(notebook, output_dir):
    output_path = os.path.join(output_dir, os.path.basename(notebook).replace('.ipynb', '.pdf'))
    subprocess.run(['jupyter-nbconvert', '--to', 'pdf', notebook, '--output-dir', output_dir], check=True)
    return output_path

def merge_pdfs(pdf_files, output_pdf):
    merger = PdfMerger()
    for pdf in pdf_files:
        merger.append(pdf)
    merger.write(output_pdf)
    merger.close()

directory = '.'
output_dir = 'pdfs'
os.makedirs(output_dir, exist_ok=True)

notebooks = find_notebooks(directory)
pdf_files = [convert_to_pdf(nb, output_dir) for nb in notebooks]

final_pdf = 'ics33_study_guide.pdf'
merge_pdfs(pdf_files, final_pdf)
print(f"Compiled PDF saved as {final_pdf}")

