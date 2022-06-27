from PIL import Image

# Задаю переменную прогресса
progress = 0

# Открытие изображениия
# image_name = input("Print image name: ")
image_name = "icon.jpg"
image = Image.open(image_name)

# Вывод параметров изображения
print("Image: ", image.format, image.size, image.mode)

# Работа с изображением
for i in range(0, image.size[0]):
    # Работаю с прогрессом
    progress += 1
    print("Porgress: ", (progress * 100) / image.size[1], "%")
    
    for j in range(0, image.size[1]):
        # Пиксели цвета (0, 0, 0) крашу в (1, 1, 1)
        if image.getpixel((i, j)) == (0, 0, 0):
            image.putpixel((i, j), (1, 1, 1))
        
        # Крашу линии
        if image.getpixel((i, j)) > (10, 10, 10) and image.getpixel((i, j)) < (90, 90, 90):
            image.putpixel((i, j), (0, 0, 0))

        # Пиксели цвета > (0, 0, 0) крашу в (255, 255, 255)
        if image.getpixel((i, j)) > (0, 0, 0):
            image.putpixel((i, j), (255, 255, 255))

# Сохранение и показ изображения
image.save("tests/image10.png")
image.show()