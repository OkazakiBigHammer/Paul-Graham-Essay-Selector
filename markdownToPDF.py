import markdown
import pdfkit
import os
from PyPDF2 import PdfMerger

# List of selected essay titles
selected_essays = [
    "How to Do Great Work", 
    "Putting Ideas into Words", 
    "Is There Such a Thing as Good Taste?",
    "How People Get Rich Now",
    "Charisma / Power",
    "Life is Short",
    "How to Get Startup Ideas",
    "The Acceleration of Addictiveness",
    "Why Twitter is a Big Deal",
    "How to Do Philosophy"     
    ]  

processed_essays = ["_".join(title.split(" ")).lower() for title in selected_essays]
print(processed_essays)

def markdown_to_pdf(markdown_file_path, pdf_file_path):
    # Read the markdown file
    with open(markdown_file_path, 'r', encoding='utf-8') as f:
        markdown_text = f.read()

    # Convert markdown to HTML
    html_text = markdown.markdown(markdown_text)

    # Convert HTML to PDF
    config = pdfkit.configuration(wkhtmltopdf='C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe')
    pdfkit.from_string(html_text, pdf_file_path, configuration=config)

# PDF merger
merger = PdfMerger()

# Convert selected markdown files in the directory
for file in os.listdir("./essays"):
    if file.endswith(".md"):
        # Extract the title from the file name
        title = os.path.splitext(file)[0][4:]  # adjust this based on your file naming convention        
        if title in processed_essays:
            print("selected: ",title)
            markdown_file_path = os.path.join("./essays", file)
            pdf_file_path = os.path.join("./essays", file.replace('.md', '.pdf'))
            markdown_to_pdf(markdown_file_path, pdf_file_path)
            
            # Merge the PDFs
            merger.append(pdf_file_path)

# Output the merged PDFs to a new file
merger.write("./essays/selected_essays.pdf")
merger.close()
