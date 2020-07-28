import cv2

cascade=cv2.CascadeClassifier("haarcascade_russian_plate_number.xml") 
# A Haar Cascade is basically a classifier which is used to detect particular objects from the source

minArea=200
color=(0,0,255)

#reading the values from web camera 
cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)
cap.set(10,150)
count=0
 
while True:
    success, img=cap.read()
    imgGray=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    numberPlates=cascade.detectMultiScale(imgGray, 1.1, 10)
    for (x,y,w,h) in numberPlates:
        area=w*h
        if area>minArea:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)
            cv2.putText(img,"Number-plate",(x,y-5),
                        cv2.FONT_HERSHEY_COMPLEX_SMALL,1,color,2)
            imgRoi=img[y:y+h,x:x+w]
            cv2.imshow("region of interest", imgRoi)
            
    cv2.imshow("Result", img)
 
    if cv2.waitKey(1) and 0xFF==ord('s'):
        cv2.imwrite("scanned/NoPlate_"+str(count)+".jpg",imgRoi) # there is a 'scanned' folder in which the outputs will be saved
        cv2.rectangle(img,(0,200),(640,300),(0,255,0),cv2.FILLED)
        cv2.putText(img,"Scan Saved",(150,265),cv2.FONT_HERSHEY_DUPLEX,
                    2,(0,0,255),2)
        cv2.imshow("Result",img)
        cv2.waitKey(500)
        count+=1