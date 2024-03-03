import numpy as np
import cv2
import matplotlib.pyplot as plt

correct_answers = [4,8,6,8,8,4,6,6,6,13]
MAE = 0 

def calculate_brightness(image):
        brightness = np.mean(image)
        return brightness

def is_dark(image, threshold=100):
    avg_brightness = np.mean(image)
    return avg_brightness < threshold

def lighten_image(image, factor=2.9):
    return cv2.convertScaleAbs(image, alpha=factor, beta=0)

def erode_dilate(img):
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3,3)) #Kernel was set to these dimensions because it couldn't be larger (otherwise 2 squirtles would be seen as one)
    img = cv2.erode(img, kernel, iterations=2)

    for j in range(13):
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (2,3)) 
        img = cv2.erode(img, kernel, iterations=1)

        kernel = cv2.getStructuringElement(cv2.MORPH_CROSS, (3,3)) 
        img = cv2.dilate(img, kernel, iterations=1)
    return img

def count_contours(contours):
    count = 0
    max_contour_area = max(contours, key=cv2.contourArea) #The max contour area (image edge)
    for contour in contours:
        area = cv2.contourArea(contour)
        if area > 160 and not np.array_equal(contour, max_contour_area):  #Excluding the largest contour (image edge)
            filtered_contours.append(contour)
            count += 1
    return count

#Doing iterations for every image
for i in range(10):
    file_path = f'pictures/picture_{i + 1}.jpg'
    image = cv2.imread(file_path)
    img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) #Converting image to gray

    if (is_dark(calculate_brightness(img_gray))): #Lightening up all the images which are dark
        img_gray = lighten_image(img_gray)

    image_squirtle_dots = cv2.adaptiveThreshold(img_gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 3, 53) #Using Gaussian threshold. I set the numbers in this way so that most of the unwanted dots are removed.
    #plt.imshow(image_ada_bin, 'gray')

    img_contours = erode_dilate(image_squirtle_dots) #We are merging the dots into squartles by eroding and dilating
    #plt.imshow(img_contours, 'gray')

    contours, _ = cv2.findContours(img_contours, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE) #Finding contours

    img = image.copy()
    filtered_contours = []

    count = count_contours(contours)
            
    print('picture_' + str(i+1) + '.jpg-' + str(correct_answers[i]) + '-' + str(count))
    MAE += np.abs(count - correct_answers[i])
    cv2.drawContours(img, filtered_contours, -1, (255, 0, 0), 2)
    
    plt.imshow(img)
    plt.show()
print("MAE: ", MAE/10)