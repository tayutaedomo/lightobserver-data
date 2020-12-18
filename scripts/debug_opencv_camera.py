#!/usr/bin/env python3
from datetime import datetime
import cv2


if __name__ == '__main__':
    cap = cv2.VideoCapture(0)

    #cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
    #cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)
    #cap.set(cv2.CAP_PROP_FPS, 5)

    ret, frame = cap.read()

    height, width, channels = frame.shape[:3]
    print('width:{},height:{}'.format(width, height))

    filename = 'opencv_camera_{0:%Y%m%d%H%M%S}.jpg'.format(datetime.now())
    cv2.imwrite(filename, frame)
    print('Output:', filename)

    cap.release()

