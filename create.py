from PIL import Image
from PIL import ImageDraw
import json
import math


def create(values):
    """Create graph."""
    im = Image.open("assets/template2.jpg")  # Some sort of background
    draw = ImageDraw.Draw(im)

    angle = 360. / len(values)

    origin = (im.size[0]/2, im.size[1]/2)

    points = []

    for i in list(range(len(values))):
        cur_angle = i * angle
        width = math.cos(math.radians(cur_angle)) * values[i] * 20
        height = math.sin(math.radians(cur_angle)) * values[i] * 20
        points.append((origin[0] - width, origin[1] - height))

    for i in list(range(len(points))):
        if i != (len(points) - 1):
            draw.line((points[i], points[i + 1]), fill=128, width=5)
        else:
            draw.line((points[i], points[0]), fill=128, width=5)

    del draw

    im.save("example.png")


if __name__ == "__main__":
    create([2, 8, 5, 3, 9, 10, 4, 1, 10, 5, 3, 9, 7, 4, 6, 5, 10, 9])
