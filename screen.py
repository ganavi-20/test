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

