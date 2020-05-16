from PIL import Image, ImageFilter

img = Image.open('./Pokedex/pikachu.jpg')
# filtered_img = img.filter(ImageFilter.SMOOTH)
filtered_img = img.convert('L')
# crooked = filtered_img.rotate(90)
# resize = filtered_img.resize((300, 300))
box = (100, 100, 400, 400)
region = filtered_img.crop(box)
region.save('grey.jpg', 'png')
# filtered_img.show()
# print(dir(img))
