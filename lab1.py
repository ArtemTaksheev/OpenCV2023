import cv2
import numpy as np
import random


def first_task():
    height = 400
    width = 400
    blank_image = np.zeros((height,width,3), np.uint8)
    cv2.imshow("blank_image", blank_image)
    cv2.waitKey(0)

    #drawing a line
    start_point = (15, 20)
    end_point = (70, 50)
    # Green color in BGR
    color = (0, 255, 0)
    # Line thickness of 9 px
    thickness = 2
    blank_image = cv2.line(blank_image, start_point, end_point, color, thickness)
    cv2.imshow("blank_image", blank_image)
    cv2.waitKey(0)

    #drawing circle
    center = (200, 200)
    radius = 32
    blank_image = cv2.circle(blank_image, center, radius, color, thickness)
    cv2.imshow("blank_image", blank_image)
    cv2.waitKey(0)

    #draw elipce
    center_coordinates = (200, 200)
    axesLength = (100, 160)
    angle = 45  
    startAngle = 0
    endAngle = 360
    blank_image = cv2.ellipse(blank_image, center_coordinates, axesLength,
            angle, startAngle, endAngle, color, thickness)
    cv2.imshow("blank_image", blank_image)
    cv2.waitKey(0)
   

    #draw rectangle
    first_point = (15, 20)
    second_point = (70, 50)
    blank_image = cv2.rectangle(blank_image, first_point, second_point, color, thickness)
    cv2.imshow("blank_image", blank_image)
    cv2.waitKey(0)

def second_task():
    height = 400
    width = 400
    image = np.zeros((height,width,3), np.uint8)
    pts = np.array([[75,325], [100, 325],[142, 175],
                     [75, 175],[75, 50], [75, 50],
                     [120,50], [120,100],[165,100],
                     [165,50],[210,50],[210,100],
                     [255,100],[255,50],[300,50],
                     [300,175],[232,175],[275,325],
                     [300,325],[300,350],[75,350]],np.int32)
    #pts = pts.reshape((-1, 1, 2))
    isClosed = False
    # Blue color in BGR
    color = (255, 0, 0)

    thickness = 2

    image = cv2.polylines(image, [pts], isClosed, color, thickness)
    cv2.imshow("image", image)
    cv2.waitKey(0)

    isClosed = True
    
    image = cv2.polylines(image, [pts], isClosed, color, thickness)
    cv2.imshow("image1", image)
    cv2.waitKey(0)

    image = cv2.fillPoly(image, [pts], color)
    cv2.imshow("image2", image)
    cv2.waitKey(0)

def third_task():
    height = 400
    width = 400
    text = np.zeros((height,width,3), np.uint8)
    # font
    font = [cv2.FONT_HERSHEY_SIMPLEX, cv2.FONT_HERSHEY_PLAIN, cv2.FONT_HERSHEY_DUPLEX]
    org = [50, 50]
    for i in range(6):
        fontScale = random.randint(1,2)
        color = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
        thickness = random.randint(1,5)
        fon = random.choice(font)
        text = cv2.putText(text, 'Hello World!', org, fon, fontScale, color, thickness, cv2.LINE_8)
        cv2.imshow("Text", text)
        cv2.waitKey(0)
        org[1] = org[1] + 50

    

def main():
    first_task()
    second_task()
    third_task()

if __name__ == "__main__":
    main()