import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(0)

def imgdetect():
    img = cv2.imread('test.jpg')

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

    cv2.imwrite('img.jpg', img) 
def viddetect():
    
    while True:
    
        _, img = cap.read()
  
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
   
        faces = face_cascade.detectMultiScale(gray, 1.5, 5)
    
        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 3)
    
        cv2.imshow('img', img)
  
        if cv2.waitKey(1) & 0xff == ord('q'):
            break

# to face detect from a pic
imgdetect()

# to face detect from webcam
viddetect()

cap.release()

