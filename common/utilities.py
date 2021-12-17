import PIL
from PIL import Image
import os


def write_text(data: str, path_file: str):
    '''Create file and writes data to the file

    Args:
        data (str): data to write to the file
        path_file (str): complet path wiht file name
    '''
    with open(path_file, 'w') as file:
        file.write(data)


def create_background(image_path: str, rgb_color):
    '''Concatenate png image with a custom background image

    Args:
        image_path (str): path to the png image
        rgb_color (tuple): rgb color in tuple (1,1,1)

    Returns:
        cars: A car mileage
    '''
    image = Image.open(image_path).convert('RGBA')
    if type(rgb_color) == tuple:
        color = Image.new(mode="RGBA", size=image.size, color=rgb_color)
        color.save("color.png", format="png")
        background = Image.open("color.png").convert("RGBA")
    else:
        background = Image.open(rgb_color).convert("RGBA").resize(image.size)

    comp1 = Image.alpha_composite(background, image)

    rgb_im = comp1.convert('RGB')
    rgb_im.save(image_path, format="png")

    if type(rgb_color) == tuple:
        os.remove("color.png")


def flip_image(img_path: str, flip_method: str):
    '''Flips an image with a desired method

    Args:
        img_path (str): path of the image to flip
        flip_method (str): method to flip image

    '''
    im = Image.open(img_path)

    if flip_method == "right":
        out = im.transpose(PIL.Image.FLIP_LEFT_RIGHT)
    elif flip_method == "top":
        out = im.transpose(PIL.Image.FLIP_TOP_BOTTOM)
    out.save(img_path)
