from PIL import Image, ImageDraw, ImageFont
import os


def add_watermark(input_image_path, output_image_path, watermark_text):
    image = Image.open(input_image_path)

    draw = ImageDraw.Draw(image)

    font = ImageFont.truetype("arial.ttf", 36)

    text_width, text_height = draw.textsize(watermark_text, font)

    image_width, image_height = image.size
    margin = 10
    x = image_width - text_width - margin
    y = image_height - text_height - margin

    draw.text((x, y), watermark_text, font=font, fill=(255, 255, 255, 128))

    image.save(output_image_path)


input_folder = r"D:\Users\Анна\pythonProject11"
output_folder = r"D:\Users\Анна\pythonProject11\watermarked_images"

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

watermark_text = "Watermark"

for file_name in os.listdir(input_folder):
    if file_name.endswith(".jpg") or file_name.endswith(".png"):
        input_image_path = os.path.join(input_folder, file_name)
        output_image_path = os.path.join(output_folder, file_name)
        add_watermark(input_image_path, output_image_path, watermark_text)

print("Водяные знаки добавлены к изображениям.")