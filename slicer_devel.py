import pathlib
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from PIL import Image
from skimage import color, io
import scipy.ndimage as ndimage
import scipy.signal as signal
from scipy.ndimage.interpolation import zoom
from gcode_file_creator import GCodeFile
from command import DrawLine, Vec2, DisEngageTool


def load_image(path):
    img = Image.open(path).convert("RGBA")
    background = Image.new("RGBA",img.size,(255,255,255))
    composite = Image.alpha_composite(background, img).convert("RGB")
    composite.show()
    return composite

def scale_img(img):
    img.thumbnail((16 * 10 * 2, 16 * 10 * 2), Image.ANTIALIAS)
    return img


def img_to_numpy(img):
    
    w, h = img.size
    img = np.asarray(img)

    img = img.reshape((h, w, 3))

    return img


def treshold_image(img):
    # TODO: Filter on std deviations
    # WARN: The top 10 is completly empty
    h, w, _ = img.shape
    print("treshold:", h, w)
    img = color.rgb2gray(img)
    standard_dev = np.std(img.ravel())
    tresholds = [i * standard_dev / 4 for i in range(10)]
    tresholded_images = np.empty((10, h, w, 1))
    for i, t in enumerate(tresholds):
        tresholded = np.array(
            list(map(lambda x: 1
                     if x < t else 0, img.ravel()))).reshape(h, w, 1)
        tresholded_images[i] = tresholded
    return tresholded_images


def horizontal_filter(tresholded_images):
    # plt.imsave("test.png", tresholded_images[0])
    filtered_images_horizontal = np.empty_like(tresholded_images)
    for i, img in enumerate(tresholded_images):
        filtered_images_horizontal[i] = ndimage.generic_filter(img,
                                                               sum,
                                                               mode="reflect",
                                                               footprint=[
                                                                   [[0], [1],
                                                                    [0]],
                                                                   [[0], [1],
                                                                    [0]],
                                                                   [[0], [1],
                                                                    [0]],
                                                               ])

    filtered_images_staged = np.empty_like(tresholded_images)
    last = filtered_images_horizontal[0]
    for i, img in enumerate(filtered_images_horizontal):
        filtered_images_staged[i] = np.array(
            list(map(lambda x: x if x > 0 else 0,
                     (img - last).ravel()))).reshape(img.shape)
        last = img
        plt.imshow(img)
        plt.savefig(f"out/{i}.png")

    return filtered_images_staged


def generate_gcode(image_stages, gcode_path):

    min_x_move = 1 / 2  # in mm
    min_y_move = 1 / 2  # in mm

    bed_size_x = 20 * 10  # in mm
    bed_size_y = 20 * 10  # in mm

    assert len(image_stages) > 0

    h, w, _ = image_stages[0].shape

    assert h * min_y_move < bed_size_y, "Cannot draw with this many pixels in y"
    assert w * min_x_move < bed_size_x, "Cannot draw with this many pixels in x"

    gfile = GCodeFile(gcode_path)
    gfile.start_up()

    offset_x = 36     
    offset_y = 21     

    fig, ax = plt.subplots()
    plt.xlim(0, 200)
    plt.ylim(0, 200)

    for image in image_stages:
        working_image = image

        for y, row in enumerate(working_image):
            y = h - y
            y = offset_y + y * min_y_move
            start = None
            for x, pixel in enumerate(row):
                # x = w - x
                x = offset_x + x * min_x_move
                if pixel > 1 and start is None:
                    start = Vec2(x=x, y=y)

                if pixel < 1 and start is not None:
                    gfile.push_command(DrawLine(start, Vec2(x=x, y=y)))
                    rect = patches.Rectangle((start.x, start.y),
                                             x - start.x,
                                             y - start.y + 1,
                                             linewidth=1,
                                             edgecolor='r',
                                             facecolor='r')
                    ax.add_patch(rect)
                    start = None

                if x == len(row) - 1 and start is not None:
                    gfile.push_command(DrawLine(start, Vec2(x=x, y=y)))
                    rect = patches.Rectangle((start.x, start.y),
                                             x - start.x,
                                             y - start.y + 0.1,
                                             linewidth=0.1,
                                             edgecolor='r',
                                             facecolor='r')
                    ax.add_patch(rect)
                    start = None

    gfile.shut_down()
    gfile.save_file()
    fname = "converted.png"
    plt.savefig(fname)
    return fname

import os
from pathlib import Path
def convert_img(path, gcode_path):
    if not os.path.isdir("out"):  
        os.mkdir("out")
    
    img = load_image(path)
    img = scale_img(img)
    img = img_to_numpy(img)
    img = treshold_image(img)
    img = horizontal_filter(img)
    return generate_gcode(img, gcode_path)
