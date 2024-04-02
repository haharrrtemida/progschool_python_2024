with open("original.png", "rb") as image_file:
    image = image_file.read()

with open("copy.png", "wb") as image_file:
    image_file.write(image)