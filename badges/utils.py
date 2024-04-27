from PIL import Image, ImageDraw
import numpy as np

def validate_badge(image):
    # Resize image to 512x512
    print("Image dimensions:", image.size)

    img = image.resize((512, 512))

    # Print the dimensions of the image
    print("Image dimensions:", img.size)
    
    # Verify image size
    # if img.size != (512, 512):
    #     return False, "Image size should be 512x512 pixels"
    
    # Convert image to RGBA mode
    # img = img.convert("RGBA")
    # pixels = np.array(img)
    
    # Verify colors give a "happy" feeling
    # You can define your own criteria for what colors give a "happy" feeling
    
    return img, True
