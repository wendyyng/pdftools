from PyPDF2 import PdfWriter, PdfReader

file_name = input("Name of the file: ")
file = open(f'{file_name}.pdf', 'rb')
readpdf = PdfReader(file)
totalpages = len(readpdf.pages)
print(f"There are {totalpages} pages in total.")

pages = []
pages = [int(item) for item in input("Page numbers to delete: ").split()]

for i in range(0, len(pages)):
    pages[i] = pages[i] - 1

# print(pages)

infile = PdfReader(f'{file_name}.pdf', 'rb')
output = PdfWriter()

for i in range(totalpages):
    if(i not in pages):
        p = infile.pages[i]
        output.add_page(p)

with open(f'{file_name}_new.pdf', 'wb') as f:
    output.write(f)

print("Completed.")