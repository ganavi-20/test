import numpy as np
import cv2
import pyautogui
from PIL import ImageGrab
import time
fourcc = cv2.VideoWriter_fourcc(*'XVID')
fps = 20.0
screen_size = pyautogui.size()
out = cv2.VideoWriter('screen_recording.avi', fourcc, fps, screen_size)

print("Screen recording started...")
start_time = time.time()
duration = 10

while True:
    
    img = ImageGrab.grab(bbox=(0, 0, screen_size[0], screen_size[1]))
    img_np = np.array(img)
    
    frame = cv2.cvtColor(img_np, cv2.COLOR_RGB2BGR)
    out.write(frame)

    if time.time() - start_time > duration:
        break

out.release()
cv2.destroyAllWindows()

print("Screen recording saved as 'screen_recording.avi'")
