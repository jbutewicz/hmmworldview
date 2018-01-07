import os
import numpy
from PIL import Image
from data import IMAGES_TO_STACK
from flask import Flask

app = Flask(__name__)

def stack_images():
    # Array of image arrays
    images = []

    file_list = os.listdir(app.root_path + '/img/')

    for file in file_list:
        # Add image array to list
        images.append(numpy.array(Image.open(app.root_path + '/img/' + file)))
        # Stop if number of stack limit met
        if len(images) >= IMAGES_TO_STACK:
            break

    # Find median image, convert values to uint8
    stack = numpy.uint8(numpy.median(images, 0))

    final = Image.fromarray(stack)

    # Save to final location as png and jpg
    final.save(app.root_path + '/static/img/stack.png', optimize=True)
    final.save(app.root_path + '/static/img/stack.jpg', optimize=True, quality=88)

    return
