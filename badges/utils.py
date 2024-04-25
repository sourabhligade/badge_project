# badges/utils.py
from PIL import Image, ImageDraw
import numpy as np

def validate_badge(image):
    # Resize image to 512x512
    img = image.resize((512, 512))
    
    # Verify image size
    if img.size != (512, 512):
        return False, "Image size should be 512x512 pixels"
    
    # Convert image to RGBA mode
    img = img.convert("RGBA")
    pixels = np.array(img)
    
    # Verify non-transparent pixels within a circle
    width, height = img.size
    mask = Image.new("L", (width, height), 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0, width, height), fill=255)
    del draw
    non_transparent_pixels = np.sum((pixels[:, :, 3] > 0) & np.array(mask) == 255)
    total_pixels = np.sum(np.array(mask) == 255)
    if non_transparent_pixels != total_pixels:
        return False, "Non-transparent pixels should be within a circle"
    
    # Verify colors give a "happy" feeling
    # You can define your own criteria for what colors give a "happy" feeling
    
    return True, "Badge validation successful"
