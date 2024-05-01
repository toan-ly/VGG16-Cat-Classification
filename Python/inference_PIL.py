import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import glob


# Preprocess input image data
def preprocess_input_data(im):
    im = im.resize((224, 224))
    im = np.array(im).astype(np.float32)
    im -= mean_subtract_val 
    
    return im

# Predict label and confidence score for input image
def predict(model, im):
    # Preprocess the input image
    im = preprocess_input_data(im)
    
    # Make predictions
    predictions = model.predict(np.expand_dims(im, axis=0))
    label = np.argmax(predictions) # 0/1
    confidence = np.max(predictions) # 0-1
    return confidence, label 

# Display input image and prediction with confidence score
def display(im):
    # Make predictions
    confidence, label = predict(model, im)
    print('Predicted Label: ', label)
    print('Confidence Score: ', confidence)
    
    label_map = {0: 'Oggy', 1: 'Doraemon'}
    label = label_map[label]
   
    title = f'Predicted Label: {label}\nConfidence Score: {confidence:.2f}'
    
    plt.imshow(im)
    plt.axis('off')
    plt.title(title)
    plt.show()
 
# Mean subtraction values for RGB channels
mean_subtract_val = np.array([103.939, 116.779, 123.68])

# Load the trained model
MODEL_PATH = r"Model/2024-02-20-TF2.5.0-Net-CP080-8.560E-04-1.828E-01-1.000E+00-9.000E-01.h5"
model = tf.keras.models.load_model(MODEL_PATH)
    
# Load the input image
IMAGE_PATH = glob.glob(r"Data\Test\im23.*")[0]
im = Image.open(IMAGE_PATH).convert('RGB')

# Display input image and predictions with confidence scores
display(im)






