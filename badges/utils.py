from PIL import Image, ImageDraw
import random
import rembg
import io

HAPPY_COLORS = [
    ['#DF7FD7', '#DF7FD7', '#591854'],
    ['#E3CAC8', '#DF8A82', '#5E3A37'],
    ['#E6845E', '#E05118', '#61230B'],
    ['#E0B050', '#E6CB97', '#614C23'],
    ['#9878AD', '#492661', '#C59BE0'],
    ['#787BAD', '#141961', '#9B9FE0'],
    ['#78A2AD', '#104F61', '#9BD1E0'],
    ['#78AD8A', '#0A6129', '#9BE0B3'],
    ['#AD8621', '#6B5621', '#E0AD2B'],
]

def select_random_color():
    return random.choice(HAPPY_COLORS)

def make_badge(image):
    '''
    This function resizes the uploaded image into size 512 X 512,
    fills the background inside the circle with a random color,
    crops the image, adds a circular mask,
    adds non-transparent pixels inside the circle,
    and finally stores the output image to disk.
    '''
    img = image.resize((512, 512))

    selected_colors = select_random_color()
    background_color = selected_colors[0]

    background = Image.new('RGB', img.size, color=background_color)

    background.paste(img, (0, 0), img)

    width, height = background.size
    x = (width - height) // 2
    img_cropped = background.crop((x, 0, x + height, height))

    mask = Image.new('L', img_cropped.size, 0)
    mask_draw = ImageDraw.Draw(mask)
    mask_draw.ellipse((0, 0, width, height), fill=255)

    img_cropped.putalpha(mask)

    output_filename = "resized_badge.png"
    output_path = f"badges/static/{output_filename}"
    img_cropped.save(output_path, format="PNG")

    return img_cropped, True


def remove_background_with_rembg(image_bytes):
    output_image_bytes = rembg.remove(image_bytes)
    output_image = Image.open(io.BytesIO(output_image_bytes))    
    return output_image
