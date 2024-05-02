import cv2
from PIL import Image

from util import get_limits


colors = {
    "yellow": [0, 255, 255],
    "red": [0, 0, 255],
    "blue": [255, 0, 0],
    "green": [0, 255, 0]
}

PIXEL_TO_CM = 0.1  

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    hsvImage = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    for color_name, color_bgr in colors.items():
        lowerLimit, upperLimit = get_limits(color=color_bgr)

        mask = cv2.inRange(hsvImage, lowerLimit, upperLimit)

        mask_ = Image.fromarray(mask)

        bbox = mask_.getbbox()

        if bbox is not None:
            x1, y1, x2, y2 = bbox
            frame = cv2.rectangle(frame, (x1, y1), (x2, y2), color_bgr, 5)
            cv2.putText(frame, color_name, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, color_bgr, 2)

            
            box_width_pixels = x2 - x1
            box_height_pixels = y2 - y1

            
            size_cm = max(box_width_pixels, box_height_pixels) * PIXEL_TO_CM

           
            cv2.putText(frame, f'Size: {size_cm:.2f} cm', (x1, y1 - 30), cv2.FONT_HERSHEY_SIMPLEX, 0.9, color_bgr, 2)

    cv2.imshow('frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
