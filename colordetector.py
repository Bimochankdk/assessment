import cv2

def mouse_callback(event, x, y, flags, param):
    """Callback function to display BGR values on click"""
    global frame
    
    if event == cv2.EVENT_LBUTTONDOWN:
        # Get BGR values at clicked position
        b, g, r = frame[y, x]
        
        # Create overlay for text display
        overlay = frame.copy()
        cv2.rectangle(overlay, (0, 0), (250, 60), (0, 0, 0), -1)
        cv2.addWeighted(overlay, 0.7, frame, 0.3, 0, frame)
        
        # Display BGR values on the frame
        cv2.putText(frame, f"Position: ({x}, {y})", (10, 20), 
                   cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)
        cv2.putText(frame, f"B: {b}, G: {g}, R: {r}", (10, 40), 
                   cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)
        
        # Print to console
        print(f"Clicked at ({x}, {y}) - BGR: ({b}, {g}, {r})")

def main():
    global frame
    
    # Initialize webcam
    cap = cv2.VideoCapture(0)
    
    if not cap.isOpened():
        print("Error: Could not open webcam.")
        return
    
    # Create window and set mouse callback
    cv2.namedWindow("Webcam BGR Detector")
    cv2.setMouseCallback("Webcam BGR Detector", mouse_callback)
    
    print("Webcam BGR detector started.")
    print("Click anywhere on the image to see BGR values.")
    print("Press 'q' to quit.")
    
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error: Could not read frame.")
            break
        
        # Display the frame
        cv2.imshow("Webcam BGR Detector", frame)
        
        # Exit on 'q' key press
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    # Release resources
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()