# EasyCNN

EasyCNN is a Python library that simplifies the creation, training, and usage of custom Convolutional Neural Networks (CNNs) for image processing. It allows users to input their own datasets and metadata files, select from a variety of popular CNN architectures, and visualize training results, all with minimal code.

## Features

- **Easy Model Selection**: Choose from over 20 popular CNN architectures.
- **Custom Training**: Train your models using your own datasets and metadata.
- **Visualization**: Visualize training and validation accuracy and loss.
- **Predictions**: Make predictions on new images using your trained model.
- **Automated Publishing**: Publish your models with GitHub Actions and PyPI.

## Installation

Install EasyCNN using pip:

```sh
pip install easycnn
```

# Usage
## Training a Model
To train a model using your own dataset and metadata:
```py
from easycnn import train_model, visualize_training

metadata_path = 'path/to/your/metadata.csv'
image_dir = 'path/to/your/images'
model_name = 'ResNet50'
epochs = 10
batch_size = 32

history, model = train_model(metadata_path, image_dir, model_name, epochs, batch_size)
visualize_training(history)
print("Model saved as 'trained_model.h5'")
```
## Making Predictions
To make predictions on new images using your trained model:
```py
from easycnn import predict_image

model_path = 'trained_model.h5'
image_path = 'path/to/your/image.jpg'

predicted_class = predict_image(model_path, image_path)
print(f"The predicted class is: {predicted_class}")
```
# Supported Model Architectures
EasyCNN supports 22 of the following CNN architectures:
- VGG16
- VGG19
- ResNet50
- ResNet101
- ResNet152
- InceptionV3
- InceptionResNetV2
- MobileNet
- MobileNetV2
- DenseNet121
- DenseNet169
- DenseNet201
- NASNetMobile
- NASNetLarge
- EfficientNetB0
- EfficientNetB1
- EfficientNetB2
- EfficientNetB3
- EfficientNetB4
- EfficientNetB5
- EfficientNetB6
- EfficientNetB7

# Contributing
Contributions are welcome! Please open an issue or submit a pull request on GitHub.

# License
This project is licensed under the MIT License. See the [LICENSE](https://github.com/yadavsidhant/easycnn?tab=MIT-1-ov-file) file for details.

# Contact
For any inquiries, please contact Sidhant Yadav at supersidhant10@gmail.com
