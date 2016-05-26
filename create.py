from PIL import Image
from PIL import ImageDraw
import json


def create(values):
    """Create graph."""
    im = Image.open("assets/template.png")  # Some sort of background
    draw = ImageDraw.Draw(im)

    origin = (im.size[0]/2, im.size[1]/2)

    for value in list(range(len(values))):
        point = origin
        new_point = (origin[0] - values[value], origin[1])
        print (point)
        print (new_point)
        draw.line((point, new_point), fill="blue", width=10)
        break

    del draw

    im.save("example.jpg")


if __name__ == "__main__":
    create([4, 6, 2, 8, 5, 9, 1, 3, 7])
