import cv2

def open_camera():
  
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Unable to open camera.")
        return


    while True:
       
        ret, frame = cap.read()

      
        if not ret:
            print("Error: Failed to capture frame.")
            break
        
        cv2.imshow('Camera', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

open_camera()
