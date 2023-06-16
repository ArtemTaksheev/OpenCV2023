import cv2
import numpy as np

def first_task():
    image = cv2.imread("image0.jpg")
    cv2.imshow("Original", image)
    kernel = np.array([-0.1, 0.2, -0.1,
                 0.2, 3.0,  0.2,
                -0.1, 0.2, -0.1])
    # using filter
    img_filt = cv2.filter2D(src=image, ddepth=-1, kernel=kernel)
    cv2.imshow("filtered",img_filt)
    cv2.waitKey(0)

def second_task():
    image = cv2.imread("image0.jpg")
    cv2.imshow("Original", image)
    ksize = (5, 5)
    # using blur
    image_blur = cv2.blur(image, ksize) 
    cv2.imshow("Blur", image_blur)

    image_box = cv2.boxFilter(src=image, ddepth=-1, ksize=ksize) 
    cv2.imshow("Box filter", image_box)
    image_blurG = cv2.GaussianBlur(image, ksize, cv2.BORDER_DEFAULT) 
    cv2.imshow("GausanBlur", image_blurG)
    image_blurM = cv2.medianBlur(image, 15) 
    cv2.imshow("MedianBlur", image_blurM)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def third_task():
    image = cv2.imread("lena.jpg")
    cv2.imshow("Original", image)
    #   rotation
    (h, w) = image.shape[:2]
    center = (int(w / 2), int(h / 2))
    rotation_matrix = cv2.getRotationMatrix2D(center, -45, 0.6)
    rotated = cv2.warpAffine(image, rotation_matrix, (w, h))
    cv2.imshow("Rotated",rotated)

    res_img = cv2.resize(image, (int(h/2), int(w)), cv2.INTER_NEAREST)
    cv2.imshow("Resized",res_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
def forth_task():
    image = cv2.imread("image1.jpg")
    cv2.imshow("Original", image)
    
    kernel = np.ones((3, 3), 'uint8')
    erode_img = cv2.erode(image, kernel, iterations=1)
    cv2.imshow('Eroded Image', erode_img)

    dilate_img = cv2.dilate(image, kernel, iterations=1)
    cv2.imshow('Dilated Image', dilate_img)

    erode_plus_delate = cv2.dilate(erode_img, kernel, iterations=1)
    cv2.imshow('Erode + Dilated Image', erode_plus_delate)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    cv2.imshow("Original", image)
    opening = cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel, iterations=1)
    cv2.imshow('Opening', opening)
    closing = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel, iterations=1)
    cv2.imshow('Closing', closing)
    gradient = cv2.morphologyEx(image, cv2.MORPH_GRADIENT, kernel, iterations=1)
    cv2.imshow('Gradient', gradient)
    hat = cv2.morphologyEx(image, cv2.MORPH_BLACKHAT, kernel, iterations=1)
    cv2.imshow('BlackHat', hat)
    cylinder = cv2.morphologyEx(image, cv2.MORPH_TOPHAT, kernel, iterations=1)
    cv2.imshow('Cylinder', cylinder)
    cv2.waitKey(0)

def main():
    first_task()
    second_task()
    third_task()
    forth_task()

if __name__ == "__main__":
    main()