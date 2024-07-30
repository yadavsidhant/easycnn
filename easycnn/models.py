import tensorflow as tf
from tensorflow.keras.applications import (
    VGG16, VGG19, ResNet50, ResNet101, ResNet152, InceptionV3, InceptionResNetV2,
    MobileNet, MobileNetV2, DenseNet121, DenseNet169, DenseNet201, NASNetMobile,
    NASNetLarge, EfficientNetB0, EfficientNetB1, EfficientNetB2, EfficientNetB3,
    EfficientNetB4, EfficientNetB5, EfficientNetB6, EfficientNetB7
)

MODEL_ARCHITECTURES = {
    'VGG16': VGG16,
    'VGG19': VGG19,
    'ResNet50': ResNet50,
    'ResNet101': ResNet101,
    'ResNet152': ResNet152,
    'InceptionV3': InceptionV3,
    'InceptionResNetV2': InceptionResNetV2,
    'MobileNet': MobileNet,
    'MobileNetV2': MobileNetV2,
    'DenseNet121': DenseNet121,
    'DenseNet169': DenseNet169,
    'DenseNet201': DenseNet201,
    'NASNetMobile': NASNetMobile,
    'NASNetLarge': NASNetLarge,
    'EfficientNetB0': EfficientNetB0,
    'EfficientNetB1': EfficientNetB1,
    'EfficientNetB2': EfficientNetB2,
    'EfficientNetB3': EfficientNetB3,
    'EfficientNetB4': EfficientNetB4,
    'EfficientNetB5': EfficientNetB5,
    'EfficientNetB6': EfficientNetB6,
    'EfficientNetB7': EfficientNetB7
}

def get_model(name, input_shape, num_classes):
    if name not in MODEL_ARCHITECTURES:
        raise ValueError(f"Model {name} is not supported.")
    
    base_model = MODEL_ARCHITECTURES[name](weights='imagenet', include_top=False, input_shape=input_shape)
    model = tf.keras.Sequential([
        base_model,
        tf.keras.layers.GlobalAveragePooling2D(),
        tf.keras.layers.Dense(1024, activation='relu'),
        tf.keras.layers.Dense(num_classes, activation='softmax')
    ])
    
    return model