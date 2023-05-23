import cv2


def result(img):
    x = 0
    y = 0
    h = img.shape[0]
    w = img.shape[1]
    timg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    timg = cv2.GaussianBlur(timg, (5, 5), 7)
    timg = cv2.medianBlur(timg, 7, 5)
    timg = cv2.adaptiveThreshold(
        timg, 150, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 11, 2)
    canny = cv2.Canny(timg, 150, 200)
    contours, hierarchy = cv2.findContours(
        canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > 5000:
            peri = cv2.arcLength(cnt, True)
            vertices = cv2.approxPolyDP(cnt, peri*0.02, True)
            if len(vertices) == 4:
                x, y, w, h = cv2.boundingRect(vertices)
                break
    final_img = img[y:y+h, x:x+w]
    x = final_img.shape[0]//10*6
    y = final_img.shape[1]//3*2
    final_img = final_img[x:, y:]
    final_img = cv2.cvtColor(final_img, cv2.COLOR_RGB2GRAY)
    final_img = cv2.medianBlur(final_img, 1)
    all_pic = []
    all_pic.append(cv2.threshold(
        final_img, 100, 200, cv2.THRESH_BINARY_INV)[1])
    all_pic.append(cv2.threshold(
        final_img, 130, 200, cv2.THRESH_BINARY_INV)[1])
    all_pic.append(cv2.threshold(
        final_img, 80, 150, cv2.THRESH_BINARY_INV)[1])
    return all_pic
