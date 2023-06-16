import cv2
import numpy as np

def first_task():
    cap = cv2.VideoCapture('Jalinga_360.mp4')
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter('output.mp4', fourcc, 30.0,(640,  360))

    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_alt2.xml")
    count = 0
    while cap.isOpened():
        ret, frame = cap.read()
        # if frame is read correctly ret is True
        if not ret:
            print("Can't receive frame (stream end?). Exiting ...")
            break
        faces = face_cascade.detectMultiScale(frame)
        for (x,y,w,h) in faces:
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
        cv2.imshow('frame', frame)
        out.write(frame)
        count = count + 1
        if cv2.waitKey(1) == ord('q'):
            break
    cap.release()
    print(count)

    cv2.destroyAllWindows()

def second_task():
    image = cv2.imread("lena.jpg")
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_alt2.xml")
    faces = face_cascade.detectMultiScale(image)
    for (x,y,w,h) in faces:
        center = (x + w//2, y + h//2)
        cv2.ellipse(image, center, (w//2, h//2), 0, 0, 360, (255, 0, 255), 4)
        cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,0),2)
    cv2.imshow("detect",image)
    cv2.waitKey(0)
def main():
    first_task()
    second_task()
if __name__ == "__main__":
    main()