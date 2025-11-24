from __future__ import annotations
from abc import ABC, abstractmethod
import tensorflow as tf
from modules.web.html import HTMLElement

class CaptchaReader(ABC):
    def __init__(self, model_path):
        self.model = tf.keras.models.load_model(model_path)

    @abstractmethod
    def read(self,captchaElement: HTMLElement):
        pass