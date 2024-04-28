from PIL import Image, ImageDraw
import numpy as np

def make_badge(image):
    '''
    This fuction resizes the uploaded image into size 512 X 512
    crops the image and adds circular mask and
    adds nontransparent pixels inside the circle and finally stores the output image to disk
    '''
    img = image.resize((512, 512))

    width, height = img.size
    x = (width - height) // 2
    img_cropped = img.crop((x, 0, x + height, height))

    mask = Image.new('L', img_cropped.size, 0)
    mask_draw = ImageDraw.Draw(mask)
    mask_draw.ellipse((0, 0, width, height), fill=255)

    img_cropped.putalpha(mask)

    output_filename = "resized_badge.png"
    output_path = f"badges/static/{output_filename}"
    img_cropped.save(output_path, format="PNG")

    return img_cropped, True
