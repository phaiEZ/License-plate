import cv2
import numpy
import matplotlib.pyplot as ply
import pytesseract  
from PIL import Image, ImageGrab

def convertImage(image):
    gray = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
    blur = cv2.GaussianBlur(gray,(5,5),0)
    canny = cv2.Canny(gray,100,200)
    return canny
while True :
    cap = cv2.VideoCapture(0)
    while (True) :
        ret,frame = cap.read()
        cv2.imshow("frame",frame)
        if (cv2.waitKey(1) & 0xFF == ord("a")) :
            cv2.imwrite('123.jpg',frame)
            break
        if (cv2.waitKey(1) & 0xFF == ord("o")) :
            break

    img = cv2.imread("123.jpg")
    processed_img = convertImage(img)
    contour_img = processed_img.copy()
    original_img = img.copy()

    contours, heirachy = cv2.findContours(contour_img,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
    contours = sorted(contours, key=cv2.contourArea, reverse=True)[:10]

    for contour in contours :
        p = cv2.arcLength(contour,True)
        approx = cv2.approxPolyDP(contour,0.02*p,True)
        
        if len(approx) == 4:
            x,y,w,h = cv2.boundingRect(contour)
            license_img = original_img[y:y+h,x:x+w]
            cv2.drawContours(img, [contour],-1,(0,255,255),3)

    cv2.imshow("license Detected :",license_img)
    cv2.imshow("test",img)
    cv2.imwrite('F:\code\chatbot/456.jpg',license_img)
    if __name__ == "__main__":
        img = Image.open("456.jpg")
        x = pytesseract.image_to_string(img,lang ='tha')
        print(x)
    cv2.waitKey(0)