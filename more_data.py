import os
import random
import cv2
from ultralytics import YOLO
import cv2

model = YOLO("runs/detect/train2/weights/best.pt")
images_folder = 'DATA_FULL'
output_folder = "SAVED_IMAGE"
if not os.path.exists(output_folder): os.makedirs(output_folder)
all_images = [os.path.join(images_folder, filename) for filename in os.listdir(images_folder)]
selected_images = random.sample(all_images, 1000)
for filename in selected_images:
    image = cv2.imread(filename)
    path = os.path.join(output_folder, os.path.basename(filename))
    results = model(source = filename, conf = 0.5, save_txt = True, save =  True)
    cv2.imwrite(path, image)

