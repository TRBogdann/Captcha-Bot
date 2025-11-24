from PIL import Image
import numpy as np
import tensorflow as tf

def readAsJpg(image_path,save = False):
    image = Image.open(image_path)
    image_rgb = image.convert('RGB')
    if save:
        image_rgb.save(image_path.split('.')[0]+'.jpg')

def readImage(image_path,IMG_HEIGHT, IMG_WIDTH):
    img = tf.io.read_file(image_path)
    img = tf.io.decode_jpeg(img, channels=1)
    img = tf.image.convert_image_dtype(img, tf.float32)
    img = tf.image.resize(img, [IMG_HEIGHT, IMG_WIDTH])
    img = tf.transpose(img, perm=[1, 0, 2])
    return img