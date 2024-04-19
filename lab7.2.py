from PIL import Image

image = Image.open("C:/Users/Вероника/Desktop/z1.jpeg")
width, height = image.size
small_image = image.resize((width // 3, height // 3))
small_image.save("small_" + "1.jpeg")
horizontal_mirror = image.transpose(Image.FLIP_LEFT_RIGHT)
horizontal_mirror.save("horizontal_mirror_" + "z1.jpeg")
vertical_mirror = image.transpose(Image.FLIP_TOP_BOTTOM)
vertical_mirror.save("vertical_mirror_" + "z1.jpeg")

print("Изображения сохранены!")
