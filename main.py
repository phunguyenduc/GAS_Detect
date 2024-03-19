import os
from ultralytics import YOLO

# Load a model
# model = YOLO("runs/detect/train2/weights/best.pt")
model = YOLO("runs/detect/train4/weights/best.pt")

# Train the model
dir = "DATA_FULL"
# if not os.path.exists(dir): os.makedirs(dir)

for filename in os.listdir(dir):
    file_path = os.path.join(dir, filename)
    results = model(source = file_path, save = True)