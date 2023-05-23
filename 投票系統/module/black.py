import cv2


def result(raw):
    return cv2.threshold(raw, 130, 200, cv2.THRESH_BINARY_INV)[1]
