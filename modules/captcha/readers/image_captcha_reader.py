from .captcha_reader import CaptchaReader
import tensorflow as tf
import numpy as np
from PIL import Image
from io import BytesIO
from modules.visual.image import readImage
from modules.web.html import HTMLElement

class ImageCaptchaReader(CaptchaReader):
    def __init__(self, model_path, vocabulary,target_width,target_height):
        super().__init__(model_path=model_path)
        self.vocabulary = vocabulary
        self.target_width = target_width
        self.target_height = target_height
    
    def decode(self, output):
        debatched = np.squeeze(output)
        print(np.argmax(debatched,axis=-1))
        char_list = [self.vocabulary[i] for i in np.argmax(debatched,axis=-1)]
        decoded = ''.join(char_list)
        return decoded

    def readJPG(self,filepath):
        input_captcha = tf.expand_dims(readImage(filepath),axis=0)
        output = self.model.predict(input_captcha)
        decoded_captcha =  self.translateOutput(output)

        return decoded_captcha
    
    def read(self, input:HTMLElement):
        png_bytes = input.WebElement().screenshot_as_png
        image = Image.open(BytesIO(png_bytes))
        image_rgb = image.convert('RGB')
        buffer = BytesIO()
        image_rgb.save(buffer,format='JPEG')
        
        img = tf.io.decode_jpeg(buffer.getvalue(), channels=1)
        img = tf.image.convert_image_dtype(img, tf.float32)
        img = tf.image.resize(img, [40, 200])
        img = tf.expand_dims(tf.transpose(img, perm=[1, 0, 2]),axis=0)

        output = self.model.predict(img)
        decoded = self.decode(output)

        return decoded
