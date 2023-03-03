from PIL import Image, ImageFilter

# creating a image object
im1 = Image.open(r"C:\\Users\\yangs\\Desktop\\SECOND2\\val\\im2\\02208.png")

# applying the Gaussian Blur filter
im2 = im1.filter(ImageFilter.GaussianBlur(radius=2))

im2.show()