import tensorflow as tf

def predict_image(model_path, image_path):
    model = tf.keras.models.load_model(model_path)
    
    image = tf.keras.preprocessing.image.load_img(image_path, target_size=(224, 224))
    image = tf.keras.preprocessing.image.img_to_array(image)
    image = tf.expand_dims(image, axis=0)
    
    predictions = model.predict(image)
    predicted_class = tf.argmax(predictions[0])
    
    return predicted_class.numpy()