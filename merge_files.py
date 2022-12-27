from pypdf import PdfWriter
import os
from glob import glob

files = [f for f in os.listdir('.') if os.path.isfile(f)]
files = filter(lambda f: f.endswith(('.pdf', '.PDF')), files)

newFileName = input("New File Name: ")

merger = PdfWriter()

for pdf in files:
    merger.append(pdf)

merger.write(f"{newFileName}.pdf")
merger.close()