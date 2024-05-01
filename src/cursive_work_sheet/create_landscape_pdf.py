from reportlab.lib.pagesizes import landscape, A4
from reportlab.pdfgen import canvas
from reportlab.lib.units import mm
from PIL import Image
from pathlib import Path
from cursive_work_sheet.create_line_image import SyntheticImageGenerator

num_rows = 10  # Adjust the number of rows as needed for landscape layout
margin = 10 * mm  # Margin around the table, might need adjustment for landscape

# Assuming SyntheticImageGenerator is defined elsewhere
synthetic_image_generator = SyntheticImageGenerator(
    image_width=1000,  # You might want to adjust this for landscape
    image_height=100,   # And this, depending on your desired row height
    font_size=26,
    spacing=12
)

def create_pdf_in_landscape(file_path, texts):
    filename = file_path.stem
    c = canvas.Canvas(str(file_path), pagesize=landscape(A4))  # Set to landscape mode
    width, height = landscape(A4)  # Get landscape dimensions
    width -= 2 * margin
    height -= 2 * margin

    c.translate(margin, margin)
    
    # Adjust column widths for landscape
    column_1_width = width * 0.9
    column_2_width = width * 0.1
    
    # You may want to adjust row heights for the landscape orientation
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
        
        if row < num_rows and row // 2 < len(texts):
            if row % 2 == 0:  # Even row index for images
                text = texts[row // 2]
                image_path = synthetic_image_generator.create_synthetic_data(text, row)
                with Image.open(image_path) as img:
                    img = img.resize((int(column_1_width), int(row_height)), Image.Resampling.LANCZOS)
                    img.save(image_path)
                c.drawImage(image_path, 0, y_position, width=column_1_width, height=row_height)
            else:  # Odd rows for drawing 'O'
                c.drawString(column_1_width + (column_2_width * 0.45), y_position + row_height / 3, 'O')
            if image_path.exists():
                image_path.unlink()  # Remove the image file after drawing it
    c.line(column_1_width, 0, column_1_width, height)
    c.drawRightString(300, 10, filename)  # Adjust position for landscape if necessary
    c.save()


if __name__ == "__main__":
    output_path = Path("./landscape.pdf")
    texts = ["༄༅༅། །ཞལ་གདམས་དང་གསུང་མགུར་སྣ་ཚོགས་ཀྱི་སྐོར་ཀུན་ཕན་བདུད་རྩིའི་སྤྲིན་ ཆེན་ཞེས་བྱ་བ་བཞུགས་སོ། །མཛད་པ་པོ། ཞེ་ཆེན་རྒྱལ་ཚབ་འགྱུར་མེད་པདྨ་","རྣམ་རྒྱལ།ཐོག་མའི་སྙན་སྒྲོན།༧ དེ་ཡང་ཀུན་མཁྱེན་མི་ཕམ་རིན་པོ་ཆེས་བསྟན་ བཅོས་བརྩམ་པ་བཀས་སྐུལ་ཞིང༌། གསུང་རྩོམ་རིགས་བསྟན་པའི་གཙིགས་སུ་ཆེ་","ཞེས་བྱ་བ་བཞུགས་སོ། །མཛད་པ་པོ། ཞེ་ཆེན་རྒྱལ་ཚབ་འགྱུར་མེད་པདྨ་རྣམ་རྒྱལ། ཐོག་མའི་སྙན་སྒྲོན།༧ དེ་ཡང་ཀུན་མཁྱེན་མི་ཕམ་རིན་པོ་ཆེས་བསྟན་བཅོས་","བརྩམ་པ་བཀས་སྐུལ་ཞིང༌། གསུང་རྩོམ་རིགས་བསྟན་པའི་གཙིགས་སུ་ཆེ་ཞེས་བྱ་བ་བཞུགས་སོ། །མཛད་པ་པོ། ཞེ་ཆེན་རྒྱལ་ཚབ་འགྱུར་མ"]
    create_pdf_in_landscape(output_path, texts)