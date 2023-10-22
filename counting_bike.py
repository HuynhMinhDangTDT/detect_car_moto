# import cv2

# camera=cv2.VideoCapture('bikes.mp4')

# while(True):
    
#     ret,img=camera.read()
#     cv2.imshow('LIVE',img)
    
#     key=cv2.waitKey(1)
    
#     if key==27:
#         break    

# cv2.destroyAllWindows()
# camera.release()

# import cv2

# bikes_classifier=cv2.CascadeClassifier('Cascades/Vehicle and pedestrain detection/two_wheeler.xml')

# camera=cv2.VideoCapture('bikes.mp4')

# while(True):

#     ret,img=camera.read()
    
#     blur=cv2.blur(img,(3,3))
#     gray=cv2.cvtColor(blur,cv2.COLOR_BGR2GRAY)
    
#     bikes=bikes_classifier.detectMultiScale(gray)
    
#     for (x,y,w,h) in bikes:

#         cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
#         cv2.putText(img,'Bike',(x,y-10),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,255,0),2)
        
#     cv2.imshow('LIVE',img)
#     key=cv2.waitKey(1)
    
#     if key==27:
#         break

# cv2.destroyAllWindows()
# camera.release()

import cv2

bikes_classifier=cv2.CascadeClassifier('Cascades/Vehicle and pedestrain detection/two_wheeler.xml')

camera=cv2.VideoCapture('bikes.mp4')

count=0

while(True):

    ret,img=camera.read()
    
    height,width=img.shape[0:2]
    
    img[0:70,0:width]=[0,0,255]
    cv2.putText(img,'MOTOR BIKE COUNT:',(10,50),cv2.FONT_HERSHEY_SIMPLEX,1.5,(255,255,255),2)
    
    cv2.line(img,(0,height-200),(width,height-200),(0,255,255),2)
    
    blur=cv2.blur(img,(3,3))
    gray=cv2.cvtColor(blur,cv2.COLOR_BGR2GRAY)
    cv2.imshow('gray',gray)
    
    bikes=bikes_classifier.detectMultiScale(gray)
    for (x,y,w,h) in bikes:
        
        bikeCy=int(y+h/2)
        linCy=height-200
        
        if(bikeCy<linCy+6 and bikeCy>linCy-6):
            
            count=count+1
            cv2.line(img,(0,height-200),(width,height-200),(0,0,255),5)
        
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
        cv2.putText(img,'Bike',(x,y-10),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,255,0),2)
        cv2.putText(img,str(count),(500,50),cv2.FONT_HERSHEY_SIMPLEX,1.5,(255,255,255),2)
        
    cv2.imshow('LIVE',img)
    key=cv2.waitKey(1)
    
    if key==27:
        break

cv2.destroyAllWindows()
camera.release()