import cv2


def capture_image(dest_path):
    cap = cv2.VideoCapture(0)

    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 360)

    ret, frame = cap.read()

    cv2.imwrite(dest_path, frame)

    cap.release()



if __name__ == '__main__':
    capture_image('camera.jpg')

