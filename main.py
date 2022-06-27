from PIL import Image

# Переменные смен цвета
pixel = (0, 0, 0)
pR = 0
pG = 0
pb = 0

# Открытие изображениия
# image_name = input("Print image name: ")
image_name = "icon.jpg"
image = Image.open(image_name)

# Запрашиваю параметры парогов смены цвета
pR = input("Parogue for R chnnale")

# Вывод параметров изображения
print("Image: ", image.format, image.size, image.mode)

# Работа с изображением
for i in range(0, image.size[0]):
    for j in range(0, image.size[1]):
        # Пиксели цвета (0, 0, 0) крашу в (1, 1, 1)
        if image.getpixel((i, j)) == (0, 0, 0):
            image.putpixel((i, j), (1, 1, 1))
        
        # Крашу линии
        if image.getpixel((i, j)) > (10, 10, 10):
            image.putpixel((i, j), (0, 0, 0))

        # Пиксели цвета > (0, 0, 0) крашу в (255, 255, 255)
        if image.getpixel((i, j)) > (0, 0, 0):
            image.putpixel((i, j), (255, 255, 255))

# Сохранение и показ изображения
image.save("tests/image10.png")
image.show()