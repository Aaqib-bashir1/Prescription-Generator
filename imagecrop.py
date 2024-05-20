from PIL import Image

# Open the image file
img = Image.open('images.jpeg')

# Get the dimensions of the image
width, height = img.size

# Define the points for cropping (left, upper, right, lower)

left = 0
upper = height-(height*79/100)
right = width
lower = (height-(height*5.5/100))

# Crop the image
img_cropped = img.crop((left, upper, right, lower))

# Save the cropped image
img_cropped.save('body.png')