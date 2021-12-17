from PIL import Image
import os


def create_background(image_path: str, rgb_color):
    image = Image.open(image_path).convert('RGBA')

    color = Image.new(mode="RGBA", size=image.size, color=rgb_color)
    color.save("color.png", format="png")

    background = Image.open("color.png").convert("RGBA")
    comp1 = Image.alpha_composite(background, image)

    rgb_im = comp1.convert('RGB')
    rgb_im.save(image_path, format="png")
    os.remove("color.png")
