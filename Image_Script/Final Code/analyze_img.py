import cv2
import numpy as np
import xlsxwriter

def analyze_img(file):
    file_name = file
    file_string = '../Images/' + file_name + '.png'
    #Reading in Image from Directory
    img = cv2.imread(file_string,0)
    img = cv2.transpose(img)

    #Determine img dimensions and store as matrix
    width,height = img.shape
    intensity = np.empty([width,height])

    #Initialize excel sheet
    excel__string = file_name + '.xlsx'
    workbook = xlsxwriter.Workbook(excel__string)
    worksheet =  workbook.add_worksheet()

    #Iterate through pixels and store intensity and write information to excel sheet
    for i in range(0,width):
        for j in range(0,height):
            intensity[i,j] = img[i,j]
            worksheet.write(i,j,intensity[i,j]) 

    print(intensity)
    workbook.close()