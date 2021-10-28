import numpy as np
from PIL import ImageGrab
import cv2
import time
from directkeys import *
from laneFinding import *
import ctypes

def screen_record(): 
    last_time = time.time()
    while(True):
        # 800x600 windowed mode
        printscreen =  np.array(ImageGrab.grab(bbox=(0,40,800,640)))
        # print('loop took {} seconds'.format(time.time()-last_time))
        last_time = time.time()
        new_screen, original, m1, m2 = image_process(printscreen)
        # cv2.imshow('window', new_screen)
        cv2.imshow('window',cv2.cvtColor(original, cv2.COLOR_BGR2RGB))

        # if m1 < 0 and m2 < 0:
        #     right()
        # elif m1 > 0 and m2 > 0:
        #     left()
        # else:
        #     straight()

        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break

# def draw_lines(img, lines):
#     for coords in lines:
#         coords = coords[0]
#         cv2.line(img, (coords[0], coords[1]), (coords[2], coords[3]), [255,255,255], 2)

def image_process(image):
    original=image
    processed_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # Detecting edges
    processed_image = cv2.Canny(processed_image, threshold1 = 125, threshold2 = 200)
    processed_image = cv2.GaussianBlur(processed_image, (5,5), 0)

    # Setting vertices for polygon
    vertices = np.array([[0,350],[300,310], [500,310], [800,350] , [800,480], [0,480]])
    processed_image = makingMask(processed_image, [vertices])

    # processed_image, rho = 1, theta = np.pi/180, threshold = 180, minLineLenth = 20, maxLineGap = 15
    lines = cv2.HoughLinesP(processed_image, 1, np.pi/180, 180, 20, 15)
    m1 = 0
    m2 = 0
    # draw_lines(processed_image, lines)

    try:
        l1, l2, m1, m2 = draw_lanes(original,lines)
        cv2.line(original, (l1[0], l1[1]), (l1[2], l1[3]), [0,255,0], 30)
        cv2.line(original, (l2[0], l2[1]), (l2[2], l2[3]), [0,255,0], 30)
    except Exception as e:
        print(str(e))
        pass
    try:
        for coords in lines:
            coords = coords[0]
            try:
                cv2.line(processed_image, (coords[0], coords[1], coords[2], coords[3]), [255,0,0], 3)
            except Exception as e:
                print(str(e))

    except Exception as e:
        pass
    return processed_image, original, m1, m2

def makingMask(img, vertices):
    mask = np.zeros_like(img)
    cv2.fillPoly(mask, vertices, 255)
    masked = cv2.bitwise_and(img, mask)
    return masked

def main():
    # test()
    screen_record()
    

main()