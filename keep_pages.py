from PyPDF2 import PdfWriter, PdfReader

file_name = input("Name of the file: ")

pages = []
# pages = int(input("Page numbers to keep: "))
pages = [int(item) for item in input("Page numbers to keep: ").split()]

for i in range(0, len(pages)):
    pages[i] = pages[i] - 1
# print(pages)
print(pages)
# for i in range(0, pages):
#     ele = int(input())
#     pages_to_keep.append(ele)

# if the input is not-integer, just print the list
# except:
#     print(my_list)

infile = PdfReader(f'{file_name}.pdf', 'rb')
output = PdfWriter()

for i in pages:
    p = infile.pages[i]
    output.add_page(p)

with open(f'{file_name}_new.pdf', 'wb') as f:
    output.write(f)

print("Completed.")
