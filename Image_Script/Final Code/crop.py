import cv2
import numpy as np


def crop_img(file_name):
    file_string = file_name
    img = cv2.imread(file_string,0)
    img = cv2.transpose(img)

    left_x = 0
    left_y = 0
    right_x = 0
    right_y = 0
    bot_x = 0
    bot_y = 0

    #Determine img dimensions and store as matrix
    width,height = img.shape
    intensity = np.empty([width,height])
    #Iterate through pixels and store intensity and write information to excel sheet
    for i in range(10,width-10):
        for j in range(10,height-10):
            if img[i,j] > 10 and img[i,j] < 50:
                #Right Corner
                if img[i+10,j] > 50 and img[i,j-10] > 50 and img[i,j+10] > 50 and j != height-1:
                    right_x = i
                    right_y = j

                #Left Corner
                elif img[i-10,j] > 50 and img[i,j-10] > 50 and img[i,j+10] > 50 and j != height-1:
                    left_x = i
                    left_y = j

                #Bottom Corner
                elif img[i-10,j] > 50 and img[i+10,j] > 50 and img[i,j-10] < 50 and img[i,j+10] < 50 and j != height-1:
                    bot_x = i
                    bot_y = j
    '''
    print("left dimensions:")
    print(left_x)
    print(left_y)
    print("right dimensions:")
    print(right_x)
    print(right_y)
    print("bottom dimensions:")
    print(bot_x)
    print(bot_y)
    '''
    crop_img = img[left_x-30:right_x+30,left_y-30:bot_y+50]
    cv2.imshow("cropped", crop_img)
    cv2.waitKey(0)




