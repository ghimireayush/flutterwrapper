from PIL import Image, ImageDraw, ImageFont

# Create a 1024x1024 image with blue background
img = Image.new('RGB', (1024, 1024), color='#2196F3')
draw = ImageDraw.Draw(img)

# Try to use a monospace font, fallback to default
try:
    font = ImageFont.truetype("consola.ttf", 400)
except:
    try:
        font = ImageFont.truetype("C:/Windows/Fonts/consola.ttf", 400)
    except:
        font = ImageFont.load_default()

# Draw the </> text in white
text = "</>"
bbox = draw.textbbox((0, 0), text, font=font)
text_width = bbox[2] - bbox[0]
text_height = bbox[3] - bbox[1]
x = (1024 - text_width) // 2
y = (1024 - text_height) // 2 - 50

draw.text((x, y), text, fill='white', font=font)

# Save the image
img.save('assets/icon.png')
print("Icon created successfully!")
