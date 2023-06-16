import cv2
import numpy as np
from matplotlib import pyplot as plt

def first_task():
    #Create images
    height = 400
    width = 800
    color = (255, 255, 255)
    pts = np.array([[0,0], [400, 0],[400, 400],
                    [0,400]],np.int32) 
    blank_image1 = np.zeros((height,width,3), np.uint8)
    blank_image1 = cv2.fillPoly(blank_image1, [pts], color)
    cv2.imshow("image1", blank_image1)

    pts = np.array([[240,200], [640, 200],[640, 250],
                    [240,250]],np.int32)
    blank_image2 = np.zeros((height,width,3), np.uint8)
    blank_image2 = cv2.fillPoly(blank_image2, [pts], color)
    cv2.imshow("image2", blank_image2)
    cv2.waitKey(0)

    # NOT
    cv2.imshow("not_image1", ~ blank_image1)
    # AND
    cv2.imshow("and_image", blank_image1 + blank_image2)
    # OR
    cv2.imshow("or_image",blank_image1*blank_image2)
    # XOR
    cv2.imshow("xor_image",blank_image1 ^ blank_image2)
    cv2.waitKey(0)



def second_task():

    image = cv2.imread("image2.jpg")
    cv2.imshow("image2", image)
    cv2.waitKey(0)
    # split
    split_img = cv2.split(image)
    # Displaying Blue channel image
    cv2.imshow("Model Blue Image", split_img[0])
    # Displaying Blue channel image
    cv2.imshow("Model Green Image", split_img[1])
    # Displaying Blue channel image
    cv2.imshow("Model Red Image", split_img[2])
    cv2.waitKey(0)

    # Построение всех гистограмм по всем нормализациям

    colors = ('b','g','r')
    norms = [cv2.NORM_MINMAX,cv2.NORM_INF,cv2.NORM_L1,cv2.NORM_L2]
    norms_title = {32:'NORM_MINMAX',1:'NORM_INF',2:'NORM_L1',4:'NORM_L2'}

    for j in norms:
        for i,color in enumerate(colors):
            plt.suptitle('Image Histogram '+ norms_title.get(j))
            ax1 = plt.subplot(211)
            ax2 = plt.subplot(212)

            hist = cv2.calcHist([image],[i],None,[256],[0,256])
            
            ax1.plot(hist,color = color)
            ax1.set_ylabel('Not normalized')

            cv2.normalize(hist, hist, alpha=1, beta=0, norm_type=j)

            ax2.plot(hist,color = color)
            ax2.set_ylabel('Normalized')
        plt.show()

    # normalize
    norm_image = cv2.normalize(image, image, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX)
    cv2.imshow("norm_image", norm_image)
    cv2.waitKey(0)

def third_task():
    image = cv2.imread("image3.jpg")
    cv2.imshow("image3", image)

    image_grey = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imshow("image_grey", image_grey)

    equ = cv2.equalizeHist(image_grey)
    cv2.imshow("image_grey_equalize", equ)

    orijinal_hist = cv2.calcHist([image],[0],None,[256],[0,256])
    grey_hist = cv2.calcHist([equ],[0],None,[256],[0,256])

    cv2.waitKey(0)
    
    plt.suptitle('Image Histogram ')
    ax1 = plt.subplot(211)
    ax2 = plt.subplot(212)

    
    ax1.plot(orijinal_hist)
    ax1.set_ylabel('Original')


    ax2.plot(grey_hist)
    ax2.set_ylabel('Normalized')
    plt.show()

def main():
    # first_task()
    second_task()
    third_task()

if __name__ == "__main__":
    main()