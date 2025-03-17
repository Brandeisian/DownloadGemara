from bs4 import BeautifulSoup
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
import html

def reformat_html(html_content):
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(html_content, "html.parser")
    
    # Extract text from HTML, converting tags to suitable format
    for br in soup.find_all("br"):
        br.replace_with("\n")
    for strong in soup.find_all("strong"):
        strong.insert_before("<b>")
        strong.insert_after("</b>")
    for em in soup.find_all("em"):
        em.insert_before("<i>")
        em.insert_after("</i>")
    
    return html.unescape(str(soup))

def parse_text_to_elements(text):
    elements = []
    styles = getSampleStyleSheet()
    lines = text.split('\n')
    
    for line in lines:
        if line.startswith('---') and line.endswith('---'):
            # Tractate title
            title = line.strip('---').strip()
            elements.append(Paragraph(f'<b>{title}</b>', styles['Title']))
            elements.append(Spacer(1, 12))
        else:
            # Regular paragraph
            elements.append(Paragraph(line, styles['BodyText']))
            elements.append(Spacer(1, 12))
    
    return elements

def create_pdf(elements, output_filename):
    doc = SimpleDocTemplate(output_filename, pagesize=letter)
    doc.build(elements)

def main():
    input_filename = "/workspaces/DownloadGemara/master_text_file.txt"
    output_filename = "/workspaces/DownloadGemara/reformatted_master_text_file.pdf"
    
    try:
        with open(input_filename, 'r', encoding='utf-8') as file:
            html_content = file.read()
        
        reformatted_content = reformat_html(html_content)
        elements = parse_text_to_elements(reformatted_content)
        create_pdf(elements, output_filename)
        
        print(f"Reformatted text has been exported to {output_filename}")
    
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()