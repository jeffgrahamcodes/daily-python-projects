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
from PIL import Image, ImageDraw, ImageFont

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

# Create drawing object
draw = ImageDraw.Draw(img)

# Draw colored rectangle as background accent
# (top section with blue color)
draw.rectangle((0, 0 , 800, 150), fill = (41, 128, 185))

# Set up fonts
# (use default font with different sizes)
try:
    font_large = ImageFont.truetype("arial.ttf", 48)
    font_medium = ImageFont.truetype("arial.ttf", 40)
    font_small = ImageFont.truetype("arial.ttf", 36)
except:
    font_large = ImageFont.load_default(48)
    font_medium = ImageFont.load_default(40)
    font_small = ImageFont.load_default(36)


# Add name text (white text on blue background)
draw.text((50,20), name.upper(), fill="white",font = font_large)


# Add title text (white text on blue background)
draw.text((50,80), title, fill="white",font = font_medium)


# Add email text (dark text on white background)
draw.text((50,200), email, fill="black",font = font_small)


# Add phone text (dark text on white background)
draw.text((50,275), phone, fill="black",font = font_small)

# Create filename from name
filename = f"{name.replace(" ", "_").lower()}_business_card.png"

# Save the business card
img.save(filename)


# Print success message
print(f"Business card saved as: {filename}\n")
print("Card generated successfully!")
