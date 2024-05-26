from PIL import Image, ImageDraw, ImageFont
card = Image.open("birthday_card2.jpg")
name = input("Кого Вы хотите поздравить? ")
draw = ImageDraw.Draw(card)
font = ImageFont.truetype("arial.ttf", 50)
text = name + ", поздравляю!"
text_color = (255, 0, 0)
text_width, text_height = draw.textsize(text, font)
image_width, image_height = card.size
text_position = (image_width - text_width - 50, image_height - text_height - 50)
draw.text(text_position, text, font=font, fill=text_color)
card.save("new_birthday_card.png")
