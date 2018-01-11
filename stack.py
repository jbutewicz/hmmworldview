import os
import numpy
from PIL import Image
from data import IMAGES_TO_STACK, MIN_IMAGE_SIZE
from flask import Flask

app = Flask(__name__)

def stack_images():
    # Array of image arrays
    images = []

    file_list = os.listdir(app.root_path + '/img/')

    # Delete files that are not of a certain size
    for file in file_list:
        if os.path.getsize(app.root_path + '/img/' + file) < MIN_IMAGE_SIZE * 1024:
            os.remove(app.root_path + '/img/' + file)

    file_list = os.listdir(app.root_path + '/img/')

    for file in file_list:
        # Add image array to list
        images.append(numpy.array(Image.open(app.root_path + '/img/' + file).convert('RGB')))
        # Stop if number of stack limit met
        if len(images) >= IMAGES_TO_STACK:
            break

    # Find median image, convert values to uint8
    stack = numpy.uint8(numpy.median(images, 0))

    final = Image.fromarray(stack)

    # Save to final location as png and jpg
    os.makedirs(os.path.dirname(app.root_path + '/static/img/stack.png'), exist_ok=True)
    final.save(app.root_path + '/static/img/stack.png', optimize=True)
    final.save(app.root_path + '/static/img/stack-100.jpg', optimize=True, quality=100)
    final.save(app.root_path + '/static/img/stack.jpg', optimize=True, quality=88)

    return
