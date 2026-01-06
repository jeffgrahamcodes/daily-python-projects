"""
THE APP:
Business card generator that takes user information and creates
a professional business card image using Pillow.

WHAT TO FIGURE OUT:
- How do you create a blank image with Pillow?
- How do you draw shapes like rectangles?
- How do you add text to images?
- How do you use different fonts and sizes?
- How do you position text at specific coordinates?

START HERE:
First, create a blank white image and save it.
Then add a colored rectangle as a background accent.
Finally, add all the text elements with different sizes.

KEY CONCEPT:
Image.new() creates a new blank image.
ImageDraw.Draw() creates a drawing context for adding shapes/text.
draw.rectangle() draws filled rectangles with coordinates.
draw.text() adds text at (x, y) coordinates.
ImageFont sets font style and size for text.
"""

#---------------------------------------------
# THE CODE SKELETON

# Import necessary libraries
# (PIL for image creation and text rendering)
from PIL import Image, ImageDraw

# Print header
print("Business Card Generator")
print("=======================\n")

# Get user information
print("Enter your information:")
name = input("Name: ")
title = input("Title: ")
email = input("Email: ")
phone = input("phone: ")


# Print processing message
print("\nGenerating business card...")

# Create a new image with white background
# (800x400 pixels, RGB mode, white color)
img = Image.new("RGB", (800, 400), color="white")
img.save("business_card.png")

# Create drawing object
draw = ImageDraw.Draw(img)

# Draw colored rectangle as background accent
# (top section with blue color)
draw.rectangle((0, 0 , 800, 400 // 3),
               fill = "blue",
               outline = "blue",
               width = 1)

# Set up fonts
# (use default font with different sizes)




# Add name text (white text on blue background)


# Add title text (white text on blue background)


# Add email text (dark text on white background)


# Add phone text (dark text on white background)


# Create filename from name


# Save the business card
img.save("business_card.png")


# Print success message