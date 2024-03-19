from ultralytics import YOLO

# Load a model
model = YOLO('yolov8n.pt')

# Train the model
results = model.train(data='NEW_DATA/data.yaml', epochs=25, imgsz=320)