import cv2
import numpy as np
import math
def first_task():
    # Tasks with lena.jpg image
    image = cv2.imread("lena.jpg")
    cv2.imshow("window1", image)

    cv2.imwrite("lena_new.jpg",image)

    image_copy = image.copy()
    cv2.imshow("window2", image_copy)

    lena_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imshow("window3", lena_gray)
    cv2.imwrite("lena_grey.jpg",lena_gray)

    (h, w) = image.shape[:2]

    res_img = cv2.resize(image, (int(h/2), int(w/2)), cv2.INTER_NEAREST)
    cv2.imshow("window4",res_img)

    (t,thresh) = cv2.threshold(lena_gray,127,255,cv2.THRESH_BINARY)
    cv2.imshow("window5",thresh)
    cv2.imwrite("lena_greyThresh.jpg",thresh)

    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(thresh, contours, -1, (0,255,0), 3)
    cv2.imshow("window6",thresh)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

    cv2.destroyAllWindows()
    # Tasks with apple.bpm image
    image = cv2.imread("apple.bmp")
    cv2.imshow("window7", image)

    apple_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imshow("window8", apple_gray)

    (t,thresh) = cv2.threshold(apple_gray,127,255,cv2.THRESH_BINARY)
    cv2.imshow("window9",thresh)

    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(thresh, contours, -1, (0,255,0), 3)
    cv2.imshow("window10",thresh)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

def second_task():
    image = cv2.imread("image0.jpg")
    cv2.imshow("Original", image)

    ksize = (5, 5)
    image_blurG = cv2.GaussianBlur(image, ksize, cv2.BORDER_DEFAULT) 
    

    image_gray = cv2.cvtColor(image_blurG, cv2.COLOR_BGR2GRAY)
 

    # Sobel
    grad_x = cv2.Sobel(image_gray, cv2.CV_16S, 1, 0, borderType=cv2.BORDER_DEFAULT)
    grad_y = cv2.Sobel(image_gray, cv2.CV_16S, 0, 1,  borderType=cv2.BORDER_DEFAULT)
    

    abs_grad_x = cv2.convertScaleAbs(grad_x)
    abs_grad_y = cv2.convertScaleAbs(grad_y)
    cv2.imshow("Grad_x", abs_grad_x)
    cv2.imshow("Grad_y",abs_grad_y)

    grad = cv2.addWeighted(abs_grad_x, 0.5, abs_grad_y, 0.5, 0)

    cv2.imshow("Sobel",grad)

    # Scharr
    grad_x = cv2.Scharr(image_gray, cv2.CV_16S, 1, 0, borderType=cv2.BORDER_DEFAULT)
    grad_y = cv2.Scharr(image_gray, cv2.CV_16S, 0, 1,  borderType=cv2.BORDER_DEFAULT)
    

    abs_grad_x = cv2.convertScaleAbs(grad_x)
    abs_grad_y = cv2.convertScaleAbs(grad_y)
    cv2.imshow("Grad_x", abs_grad_x)
    cv2.imshow("Grad_y",abs_grad_y)

    grad = cv2.addWeighted(abs_grad_x, 0.5, abs_grad_y, 0.5, 0)
    cv2.imshow("Scharr",grad)
    # Laplasian
    kernel_size = 3
    laplas = cv2.Laplacian(image_gray, cv2.CV_16S, kernel_size)
    laplas = cv2.convertScaleAbs(laplas)

    cv2.imshow("Laplasian",laplas)

    # Canny
    image_blur = cv2.blur(image, ksize) 
    image_gray = cv2.cvtColor(image_blur, cv2.COLOR_BGR2GRAY)
    canny = cv2.Canny(image_gray,50,150)
    cv2.imshow("Canny",canny)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def third_task():
    image = cv2.imread("image0.jpg")
    cv2.imshow("Original", image)
    # Hough
    canny = cv2.Canny(image,65,195)

    cdst = cv2.cvtColor(canny, cv2.COLOR_GRAY2BGR)
    cdstP = cdst.copy()
    canny = cv2.cvtColor(canny, cv2.COLOR_BAYER_BG2GRAY)

    lines = cv2.HoughLines(canny, 1, np.pi / 180, 150, None, 0, 0)
    for i in range(0, len(lines)):
            rho = lines[i][0][0]
            theta = lines[i][0][1]
            a = math.cos(theta)
            b = math.sin(theta)
            x0 = a * rho
            y0 = b * rho
            pt1 = (int(x0 + 1000*(-b)), int(y0 + 1000*(a)))
            pt2 = (int(x0 - 1000*(-b)), int(y0 - 1000*(a)))
            cv2.line(cdst, pt1, pt2, (0,0,255), 1, cv2.LINE_AA)

    linesP = cv2.HoughLinesP(canny, 1, np.pi / 180, 50, None, 50, 10)
    for i in range(0, len(linesP)):
            l = linesP[i][0]
            cv2.line(cdstP, (l[0], l[1]), (l[2], l[3]), (0,0,255), 1, cv2.LINE_AA)
    
    cv2.imshow("Standard Hough Line Transform", cdst)
    cv2.imshow("Probabilistic Line Transform", cdstP)
    cv2.waitKey(0)

def main():
     first_task()
     second_task()
     third_task()

if __name__ == "__main__":
    main()