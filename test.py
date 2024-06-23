import cv2
import numpy as np

def main():
    # Load the pre-trained MobileNet SSD model
    model_weights = "MobileNetSSD_deploy.caffemodel"
    model_config = "MobileNetSSD_deploy.prototxt"
    
    net = cv2.dnn.readNetFromCaffe(model_config, model_weights)

    if net is None:
        print("Error: Could not load model.")
        return

    # Open a video capture object (0 for webcam, or specify video file path)
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Could not open camera.")
        return

    while True:
        # Read a frame from the camera
        ret, frame = cap.read()

        if not ret:
            print("Error: Failed to capture frame.")
            break

        # Resize frame to width 300 for faster processing
        frame_resized = cv2.resize(frame, (300, 300))

        # Pre-process the frame for the model
        blob = cv2.dnn.blobFromImage(frame_resized, 0.007843, (300, 300), 127.5)

        # Set the input to the model
        net.setInput(blob)

        # Perform inference and get detections
        detections = net.forward()

        # Process detections
        for i in range(detections.shape[2]):
            confidence = detections[0, 0, i, 2]
            
            if confidence > 0.5:  # Filter detections by confidence threshold
                class_id = int(detections[0, 0, i, 1])
                class_name = class_names[class_id]
                print(f"Detected {class_name} with confidence {confidence:.2f}")

                # Draw bounding box around the detected object
                box = detections[0, 0, i, 3:7] * np.array([frame.shape[1], frame.shape[0], frame.shape[1], frame.shape[0]])
                (startX, startY, endX, endY) = box.astype(int)

                cv2.rectangle(frame, (startX, startY), (endX, endY), (0, 255, 0), 2)
                cv2.putText(frame, f"{class_name} {confidence:.2f}", (startX, startY - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

        # Display the frame
        cv2.imshow('Object Detection', frame)

        # Exit loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release resources
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    # List of class names (from the model's class labels)
    class_names = ["background", "aeroplane", "bicycle", "bird", "boat",
                   "bottle", "bus", "car", "cat", "chair", "cow", "diningtable",
                   "dog", "horse", "motorbike", "person", "pottedplant", "sheep",
                   "sofa", "train", "tvmonitor"]

    main()
