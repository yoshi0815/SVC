# -*- coding: utf-8 -*-

#read libraly
import cv2
import numpy as np
cap = cv2.VideoCapture(0)

while(1):
    _, frame = cap.read()

#画面サイズを小さくする
    if(_ > 0):
        frame = cv2.resize(frame, (640, 320))
        cv2.imshow("before", frame)
    #hsv変換
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    #hsv値域1
    hsv_min = np.array([0, 127, 0])
    hsv_max = np.array([10, 255, 255])
    mask1   = cv2.inRange(hsv, hsv_min, hsv_max)
    #hsv値域2
    hsv_min = np.array([170, 127, 0])
    hsv_max = np.array([180, 255, 255])
    mask2   = cv2.inRange(hsv, hsv_min, hsv_max)

    #赤色以外マスク処理
    res_red = cv2.bitwise_and(frame, frame, mask=mask1)
    res_red2 = cv2.bitwise_and(frame, frame, mask=mask2)
    sum_red = res_red + res_red2
    cv2.imshow('mask', sum_red)
    
    #輪郭取得
    gray = cv2.cvtColor(sum_red, cv2.COLOR_BGR2GRAY)
    cv2.imshow('gray', gray)
    ret, thresh = cv2.threshold(gray, 25, 255, cv2.THRESH_BINARY)
    cv2.imshow('thresh', thresh)
    img, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    #輪郭描画
    cv2.drawContours(frame, contours, -1, (0,255,0), 1)
    cv2.imshow('rinksku', frame)

    #一番大きい輪郭検出
    contours.sort(key=cv2.contourArea,reverse=True)

    cv2.drawContours(frame, contours, 0, (255,0,0), 3)
    cv2.imshow('rinksku_big', frame)

    if len(contours) > 0:
        cnt = contours[0]

        #最小外接円描く
        (x,y), radius = cv2.minEnclosingCircle(cnt)
        center        = (int(x), int(y))
        radius        = int(radius)
        cv2.circle(frame, center, radius, (0,255,0), 2)

    cv2.imshow('video', frame)

    k = cv2.waitKey(25)&0xFF
cv2.destroyALLWindows()
  
