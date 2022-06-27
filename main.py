from PIL import Image

image_name = input("Print image name: ")
# image_name = "icon.jpg"

image = Image.open(image_name)
# image = Image.new("RGBA", [640, 480], color = "black")
print("Image: ", image.format, image.size, image.mode)

for i in range(0, image.size[0]):
    for j in range(0, image.size[1]):
        if image.getpixel((i, j)) > (0, 0, 0) and image.getpixel((i, j)) < (100, 100, 100):
            image.putpixel((i, j), (255, 255, 255))

image.save("tests/image6.png")
image.show()