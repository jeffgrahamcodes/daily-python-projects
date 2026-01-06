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
phone = input("Phone: ")

# Print processing message
print("\nGenerating business card...\n")

# Create a new image with white background
# (800x400 pixels, RGB mode, white color)
card = Image.new('RGB', (800, 400), color=(255, 255, 255))

# Create drawing object
draw = ImageDraw.Draw(card)

# Draw colored rectangle as background accent
# (top section with blue color)
draw.rectangle([(0, 0), (800, 150)], fill=(41, 128, 185))

# Set up fonts
# (use default font with different sizes)
try:
    font_large = ImageFont.truetype("arial.ttf", 100)
    font_medium = ImageFont.truetype("arial.ttf", 56)
    font_small = ImageFont.truetype("arial.ttf", 50)
except:
    font_large = ImageFont.load_default()
    font_medium = ImageFont.load_default()
    font_small = ImageFont.load_default()

# Add name text (white text on blue background)
draw.text((50, 40), name.upper(), fill=(255, 255, 255), font=font_large)

# Add title text (white text on blue background)
draw.text((50, 100), title, fill=(255, 255, 255), font=font_medium)

# Add email text (dark text on white background)
draw.text((50, 200), email, fill=(0, 0, 0), font=font_small)

# Add phone text (dark text on white background)
draw.text((50, 250), phone, fill=(0, 0, 0), font=font_small)

# Create filename from name
filename = f"business_card_{name.lower().replace(' ', '_')}.png"

# Save the business card
card.save(filename)

# Print success message
print(f"Business card saved as: {filename}\n")
print("Card generated successfully!")