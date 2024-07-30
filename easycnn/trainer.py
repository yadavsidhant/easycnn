import pandas as pd
import tensorflow as tf
import os
from sklearn.model_selection import train_test_split

def load_data(metadata_path, image_dir):
    data = pd.read_csv(metadata_path)
    images = []
    labels = []
    
    for _, row in data.iterrows():
        image_path = os.path.join(image_dir, row['filename'])
        image = tf.keras.preprocessing.image.load_img(image_path, target_size=(224, 224))
        image = tf.keras.preprocessing.image.img_to_array(image)
        images.append(image)
        labels.append(row['label'])
    
    images = tf.convert_to_tensor(images)
    labels = tf.convert_to_tensor(labels)
    
    return train_test_split(images, labels, test_size=0.2, random_state=42)

def train_model(metadata_path, image_dir, model_name, epochs=10, batch_size=32):
    X_train, X_val, y_train, y_val = load_data(metadata_path, image_dir)
    
    model = get_model(model_name, input_shape=(224, 224, 3), num_classes=len(set(y_train.numpy())))
    model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
    
    history = model.fit(X_train, y_train, validation_data=(X_val, y_val), epochs=epochs, batch_size=batch_size)
    
    model.save('trained_model.h5')
    
    return history, model