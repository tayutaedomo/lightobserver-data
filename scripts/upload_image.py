#!/usr/bin/env python3
import os
import sys

ROOT_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
ROOT_PATH = os.path.abspath(ROOT_PATH)
sys.path.append(os.path.abspath(ROOT_PATH))

from applib.camera import write_capture_image
from applib.uploader import CaptureImageUploader


if __name__ == '__main__':
    file_path = os.path.join(ROOT_PATH, 'tmp', 'camera.jpg')
    write_capture_image(file_path)
    print('File:', file_path)

    uploader = CaptureImageUploader()
    gcs_path = uploader.upload()
    print('GCS:', gcs_path)

