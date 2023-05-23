import cv2


def result(raw):
    return cv2.threshold(
        raw, 100, 200, cv2.THRESH_BINARY_INV)[1]
