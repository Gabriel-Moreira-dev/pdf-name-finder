from PyPDF2 import PdfReader, PdfWriter
import re
import os

f_path = r'file path'
size = len(os.listdir(f_path))

for root, dirs, files in os.walk(f_path):
    for f in files:
        old_path = os.path.join(root, f)
        writer = PdfWriter()

        reader = PdfReader(old_path)
        info = reader.pages[0]
        info = info.extract_text()

        name = re.findall(r'^[A-ZÀ-Ú]+.+[A-ZÀ-Ú]+$', info, re.M)[0]

        pdf_path = os.path.join(root, name)
        
        # Adding all the orginal pdf pages to the new one
        for p in range(reader.numPages):
            writer.add_page(reader.pages[p])
        
        # Saving with a new name
        with open(f'{pdf_path}.pdf', 'wb') as pdf:
            writer.write(pdf)
        
        # Remove old pdf
        os.remove(old_path)

       
new_size = len(os.listdir(f_path))

# Checking if it's the same n° of files
if size == new_size:
    print('Done')
else:
    raise IndexError