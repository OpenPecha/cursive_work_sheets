from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.units import mm
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics

# Register the Tibetan font
font_name = "MonlamUniOuchan1"  # Replace with your font's name
pdfmetrics.registerFont(TTFont(font_name, './data/MonlamUniOuchan1.ttf'))

def create_pdf_with_tibetan_text_in_rows(filename, texts, num_rows, margin):
    c = canvas.Canvas(filename, pagesize=A4)
    width, height = A4  # A4 dimensions in points
    
    # Adjust the width and height for the margins
    width -= 2 * margin
    height -= 2 * margin
    
    # Start the drawing from the margin
    c.translate(margin, margin)
    
    # Define the widths of the columns and the uniform height of each row
    column_1_width = width * 0.9  # 90% of the width for column 1
    column_2_width = width * 0.1  # 10% of the width for column 2
    row_height = height / num_rows  # Uniform height for each row
    
    # Set font for Tibetan text entries
    c.setFont(font_name, 12)
    
    # Draw the border for the table
    c.rect(0, 0, width, height, stroke=True, fill=False)
    
    # Draw the table rows, columns, and add Tibetan text
    for row in range(num_rows):
        # Calculate the y_position for the text
        y_position = height - (row * row_height) - (row_height * 0.7)
        
        # Draw the horizontal lines for each row
        c.line(0, height - row * row_height, width, height - row * row_height)
        
        # Insert text in the odd rows
        if row % 2 == 0 and row // 2 < len(texts):  # Checking for odd row index and text availability
            text = texts[row // 2]
            c.drawString(column_1_width * 0.05, y_position, text)
        
        # Insert 'O' in the even rows in column 2 with font size 15
        if row % 2 == 1:
            c.setFont(font_name, 15)
            c.drawString(column_1_width + (column_2_width * 0.4), y_position, 'O')
            c.setFont(font_name, 12)  # Reset the font size to 12 for the next row
    
    # Draw the vertical line for the first column
    c.line(column_1_width, 0, column_1_width, height)
    
    # Save the PDF
    c.save()

def create_pdf(texts):
    # Replace with your actual texts
    num_rows = 20  # Number of rows in the table
    margin = 15 * mm  # Margin around the table in mm
    output_filename = "./table_with_tibetan_texts.pdf"
    create_pdf_with_tibetan_text_in_rows(output_filename, texts, num_rows, margin)  # Change to your desired output path
