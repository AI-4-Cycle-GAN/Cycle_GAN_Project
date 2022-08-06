from config import *
import tensorflow as tf
import os

ART_GENERATOR = None

def load_model():
    global ART_GENERATOR
    model_path = os.path.abspath(MODEL_DIR)
    ART_GENERATOR = tf.keras.models.load_model(model_path)

def preprocess_image(image):
    image = tf.image.convert_image_dtype(image, tf.float32)
    image = tf.image.resize(image, RESIZE_DIM)
    image = tf.expand_dims(image, axis = 0)
    image = 2 * image - 1
    return image

def postprocess_image(image):
    image = tf.image.resize(image, DISPLAY_SIZE)
    image = tf.squeeze(image, axis = 0)
    image = (image + 1) / 2.0
    return image.numpy()

def generate_art_from_image(image):
    global ART_GENERATOR
    image = preprocess_image(image)
    art = ART_GENERATOR.predict(image)
    art = postprocess_image(art)
    image = postprocess_image(image)
    return image, art


load_model()