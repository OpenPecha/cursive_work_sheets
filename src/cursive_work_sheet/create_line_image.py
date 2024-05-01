from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

IMAGE_PATH = './data/line_images/images'
font_path = './data/MonlamUniOuchan1.ttf'

class SyntheticImageGenerator:
    def __init__(self, image_width, image_height, font_size, spacing, font_type="Uchen") -> None:
        self.image_width = image_width
        self.image_height = image_height
        self.font_size = font_size
        self.font_type = font_type
        self.spacing = spacing

    def save_image(self, text, img_file_name):
        img = Image.new('RGB', (self.image_width,self.image_height), color = (255, 255, 255))
        d = ImageDraw.Draw(img)
        font = ImageFont.truetype(font_path, size=self.font_size, encoding='utf-16')
        text_color = (0,0,0)
        d.text((40,20), text, fill=text_color, spacing=self.spacing, font=font)
        img.save(img_file_name)

    def create_synthetic_data(self, line, line_number):
        img_path = Path(f"./data/line_images/lines/line_{line_number:06}.jpg")
        self.save_image(line, img_path)
        line_number += 1
        return img_path
        
    

