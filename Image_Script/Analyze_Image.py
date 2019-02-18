import cv2
import numpy as np
import xlsxwriter

test = True

#Iterate through file names you want to analyze
while test == True:
    print("Enter 0 to exit program")
    file_name = input("Enter filename you want to analyze: ")
    if file_name != '0':
        file_string = '../Images/' + file_name + '.jpg'
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
    else:
        break
