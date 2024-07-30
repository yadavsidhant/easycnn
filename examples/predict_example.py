from easycnn import predict_image

model_path = 'trained_model.h5'
image_path = 'path/to/your/image.jpg'

predicted_class = predict_image(model_path, image_path)
print(f"The predicted class is: {predicted_class}")