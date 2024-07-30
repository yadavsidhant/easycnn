from easycnn import train_model, visualize_training

metadata_path = 'path/to/your/metadata.csv'
image_dir = 'path/to/your/images'
model_name = 'ResNet50'
epochs = 10
batch_size = 32

history, model = train_model(metadata_path, image_dir, model_name, epochs, batch_size)
visualize_training(history)
print("Model saved as 'trained_model.h5'")