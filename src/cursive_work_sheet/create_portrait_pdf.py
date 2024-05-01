from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.units import mm
from PIL import Image
import os
from cursive_work_sheet.create_line_image import SyntheticImageGenerator

num_rows = 14  # Number of rows in the table, ensuring exactly 15 rows are generated
margin = 10 * mm  # Margin around the table in mm

synthetic_image_generator = SyntheticImageGenerator(
    image_width=1000,
    image_height=90,
    font_size=32,
    spacing=12
)

def create_pdf_in_portrait(file_path, texts):
    filename = file_path.stem
    c = canvas.Canvas(str(file_path), pagesize=A4)
    width, height = A4
    width -= 2 * margin
    height -= 2 * margin

    c.translate(margin, margin)
    
    column_1_width = width * 0.9
    column_2_width = width * 0.1
    
    # Calculate row heights based on the total number of rows to fit within the specified height
    even_row_height = 39  # Height for even rows
    odd_row_height = 58  # Height for odd rows
    
    c.setLineWidth(2)  # Make lines thicker
    
    c.rect(0, 0, width, height, stroke=True, fill=False)
    
    y_position = height
    for row in range(num_rows):
        if row % 2 == 0:
            row_height = even_row_height
        else:
            row_height = odd_row_height
        
        y_position -= row_height

        c.setLineWidth(2) 
        
        c.line(0, y_position, width, y_position)
        
        # Ensure that images are added only within the actual count of rows specified by num_rows
        if row < num_rows and row // 2 < len(texts):
            if row % 2 == 0:  # Condition to check for even row index for images
                text = texts[row // 2]
                image_path = synthetic_image_generator.create_synthetic_data(text, row)
                with Image.open(image_path) as img:
                    img = img.resize((int(column_1_width), int(row_height)), Image.Resampling.LANCZOS)
                    img.save(image_path)
                c.drawImage(image_path, 0, y_position, width=column_1_width, height=row_height)
            else:  # Condition for odd rows to draw 'O'
                c.drawString(column_1_width + (column_2_width * 0.45), y_position + row_height / 3, 'O')
            # delete the line image after using it
            if image_path.exists():
                image_path.unlink()

    c.line(column_1_width, 0, column_1_width, height)
    c.drawRightString(300, 10, filename)
    c.save()
    
