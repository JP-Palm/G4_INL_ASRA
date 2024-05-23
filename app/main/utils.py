from PIL import Image
from torchvision import models, transforms
import torch
import os
import io

# Load the trained cat/dog/unknown model with ResNet18 architecture
model = models.resnet18(weights=models.ResNet18_Weights.IMAGENET1K_V1)
num_ftrs = model.fc.in_features
model.fc = torch.nn.Linear(num_ftrs, 3)  # Tre klasser: cat, dog, unknown

# Load the state dictionary from the file
model_path = 'cat_dog_unknown_best_model.pth'
model.load_state_dict(torch.load(model_path, map_location=torch.device('cpu')))
model.eval()

# Define the transforms
test_transforms = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
])

def transform_image(image_bytes):
    image = Image.open(io.BytesIO(image_bytes)).convert('RGB')
    return test_transforms(image).unsqueeze(0)

def get_prediction(image_bytes, confidence_threshold=0.945):
    tensor = transform_image(image_bytes=image_bytes)
    
    with torch.no_grad():
        outputs = model(tensor)
        probabilities = torch.nn.functional.softmax(outputs, dim=1)
        confidence, predicted = torch.max(probabilities, 1)
        confidence = confidence.item()
        predicted_class = predicted.item()
        
        class_names = ['cat', 'dog', 'unknown']
        
        if confidence >= confidence_threshold:
            return class_names[predicted_class], confidence
        else:
            return 'unknown', confidence
        
def save_image(image_bytes, folder, filename):
    image = Image.open(io.BytesIO(image_bytes)).convert('RGB')
    if not os.path.exists(folder):
        os.makedirs(folder)
    image.save(os.path.join(folder, filename))