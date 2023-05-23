import cv2


def result(raw):
    return cv2.threshold(
        raw, 80, 150, cv2.THRESH_BINARY_INV)[1]
