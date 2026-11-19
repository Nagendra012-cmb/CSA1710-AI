# Runnable object-detection workflow placeholder using sample detections
detections=[("person",0.96,(40,30,180,260)),("bicycle",0.88,(190,80,330,240))]
confidence_threshold=0.5
print("Detected objects (confidence >= 0.5):")
for label,confidence,box in detections:
    if confidence>=confidence_threshold:
        print(f"{label}: confidence={confidence:.2f}, bounding_box={box}")
print("To run a real pretrained detector, load a model such as YOLO with its weights.")
