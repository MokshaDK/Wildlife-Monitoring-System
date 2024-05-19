from ultralytics import YOLO
from PIL import Image as PILImage
from IPython.display import display, Image
import os
import csv

def predict(directory_path):
    model = YOLO('/home/vaibhav/Desktop/temp/bird/weights/best.pt')
    num_annotated_boxes_total = 0

    for filename in os.listdir(directory_path):
        if filename.endswith(".jpg") or filename.endswith(".jpeg") or filename.endswith(".png"):
            image_path = os.path.join(directory_path, filename)
            results = model.predict(source=image_path, conf=0.7)
            num_annotated_boxes = 0

            for result in results:
                img_bytes = result.save()
                display(Image(filename=img_bytes))
                num_annotated_boxes += len(result.boxes.xyxy)

            num_annotated_boxes_total += num_annotated_boxes
            print("Total number of annotated boxes for", filename, ":", num_annotated_boxes)

    data =[{'Bird' : num_annotated_boxes_total}]
    path = '/home/vaibhav/Desktop/temp/X_OUTPUT/outx.csv'
    with open(path, 'w', newline='') as csvfile:
        fieldnames = ['Bird']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        # Write the header
        writer.writeheader()

        # Write the data
        for row in data:
            writer.writerow(row)

    print("Total number of annotated boxes for all images:", num_annotated_boxes_total)


if __name__ == '__main__':
    predict('/home/vaibhav/Desktop/temp/User_Input')