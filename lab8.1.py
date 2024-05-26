from PIL import Image
img = Image.open("открытка.jpg")
area = (100, 100, 400, 400)
cropped_img = img.crop(area)
cropped_img.save("обрезанная_открытка.jpg")
