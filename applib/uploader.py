import os
import sys
from datetime import datetime

ROOT_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
ROOT_PATH = os.path.abspath(ROOT_PATH)
sys.path.append(os.path.abspath(ROOT_PATH))

import applib.gcs


class CaptureImageUploader:
    def __init__(self):
        self.image_name = 'camera.jpg'
        self.local_path = os.path.join(ROOT_PATH, 'tmp', self.image_name)
        self.gcs_dir = 'camera'

    def upload(self):
        if not os.path.exists(self.local_path):
            raise FileNotFoundError()

        gcs_file_name = '{0:%Y%m%d%H%M}.jpg'.format(datetime.now())
        gcs_path = self.gcs_dir + '/' + gcs_file_name

        applib.gcs.upload(gcs_path, self.local_path)

        return gcs_path



if __name__ == '__main__':
    uploader = CaptureImageUploader()
    uploader.upload()

