import pytesseract
from pytesseract import Output
import cv2

pytesseract.pytesseract.tesseract_cmd = r'C:\Users\trcar\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'
# change this dir to your install of tesseract

img = cv2.imread("test.jpg")
img_2 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_2[img_2 < 128] = 0
img_2[img_2 >= 128] = 255

#print(pytesseract.image_to_string(img_2, config=("--psm 6")))
#print(pytesseract.image_to_data(img_2, config=("--psm 11"))) # --psm num is for type of 'test'
#https://pyimagesearch.com/2021/11/15/tesseract-page-segmentation-modes-psms-explained-how-to-improve-your-ocr-accuracy/

t_data = pytesseract.image_to_data(img_2, config=("--psm 11"), output_type=Output.DICT)

CONFIDENCE = 20
num_matches = len(t_data["text"])

x,y,w,h = t_data['left'], t_data['top'],t_data['width'], t_data['height']


# based on confidence value
for i in range(num_matches):
    if t_data['conf'][i]> CONFIDENCE:
        cv2.rectangle(img,(x[i],y[i]), (x[i]+w[i],y[i]+h[i]), (0,0,255), 2)
        print(t_data['text'][i])



"""
#displays image 
cv2.imshow("text", img_2)
cv2.waitKey(0)
cv2.destroyAllWindows()
"""
