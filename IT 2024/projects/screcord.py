import numpy as np
import cv2
import pyautogui

filename = "ScreenRec.avi"
codec = cv2.VideoWriter_fourcc(*"XVID")
fps = 60.0
res = (1920, 1080)
output = cv2.VideoWriter(filename, codec, fps, res)
cv2.namedWindow("Live", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Live", 480, 270)

while True:

    img = pyautogui.screenshot()
    frame = np.array(img)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    output.write(frame)
    cv2.imshow("Live", frame)

    if cv2.waitKey(1) == ord("q"):
        break

output.release()
cv2.destroyAllWindows()



