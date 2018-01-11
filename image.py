import os
from PIL import Image
from resizeimage import resizeimage
from data import IMAGE_WIDTH, IMAGE_HEIGHT
from flask import Flask

app = Flask(__name__)

def resize_images():

    file_list = os.listdir(app.root_path + '/img/')

    # For each image set it equal to the height and width using behavior like background-size: cover
    for file in file_list:
        basewidth = IMAGE_WIDTH
        img = Image.open(app.root_path + '/img/' + file)
        wpercent = (basewidth / float(img.size[0]))
        hsize = int((float(img.size[1]) * float(wpercent)))
        img = img.resize((basewidth, hsize), Image.ANTIALIAS)
        img = resizeimage.resize('cover', img, [IMAGE_WIDTH, IMAGE_HEIGHT])
        try:
            os.makedirs(os.path.dirname(app.root_path + '/img/' + file), exist_ok=True)
            img.save(app.root_path + '/img/' + file, img.format)
        except:
            print('Could not save file')

        img.close()

    return
