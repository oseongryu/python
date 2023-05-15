import pytesseract
import cv2 
import matplotlib.pyplot as plt


path = './test.jpg'
image = cv2.imread(path)
rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
# use Tesseract to OCR the image 
pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
text = pytesseract.image_to_string(rgb_image, lang='kor+eng')
print(text)