# -*- coding: utf-8 -*-
import sys
import cv2
import numpy as np
import math

def detect_fingers(image_path):
    image = cv2.imread(image_path)
    if image is None:
        print("no hay iamgen!!!")
        return
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (35, 35), 0)
    _, thresh = cv2.threshold(blur, 60, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    contours, _ = cv2.findContours(thresh.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    if len(contours) > 0:
        cnt = max(contours, key=cv2.contourArea)
        hull = cv2.convexHull(cnt, returnPoints=False)
        if hull is not None and len(hull) > 3 and len(cnt) >= 5:
            defects = cv2.convexityDefects(cnt, hull)
            if defects is not None:
                finger_count = 0
                for i in range(defects.shape[0]):
                    s, e, f, d = defects[i, 0]
                    start = tuple(cnt[s][0])
                    end = tuple(cnt[e][0])
                    far = tuple(cnt[f][0])
                    a = math.dist(end, start)
                    b = math.dist(far, start)
                    c = math.dist(end, far)
                    if b != 0 and c != 0:
                        angle = math.acos((b**2 + c**2 - a**2) / (2 * b * c))
                        if angle <= math.pi / 2:
                            finger_count += 1
                print(finger_count + 1)
                return
    print("error1")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("error")
    else:
        detect_fingers(sys.argv[1])
