from PIL import Image

# Открытие изображениия
# image_name = input("Print image name: ")
image_name = "icon.jpg"
image = Image.open(image_name)

# Вывод параметров изображения
print("Image: ", image.format, image.size, image.mode)

# Работа с изображением
for i in range(0, image.size[0]):
    for j in range(0, image.size[1]):
        if image.getpixel((i, j)) == (0, 0, 0):
            image.putpixel((i, j), (1, 1, 1))
        if image.getpixel((i,j)) > (0, 0, 0):
            image.putpixel((i, j), (255, 255, 255))

# Сохранение и показ изображения
image.save("tests/image8.png")
image.show()