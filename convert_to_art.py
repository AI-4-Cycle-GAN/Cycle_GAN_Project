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

def generate_art_from_image(image):
    global ART_GENERATOR
    image = preprocess_image(image)
    art = ART_GENERATOR.predict(image)
    art = tf.squeeze(art, axis = 0)
    art = (art + 1) / 2.0
    art = tf.image.resize(art, DISPLAY_SIZE)
    image = tf.image.resize(image, DISPLAY_SIZE)
    return image.numpy(), art.numpy()


load_model()