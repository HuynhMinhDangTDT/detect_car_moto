import torch
from matplotlib import pyplot as plt
import numpy as np
import cv2
from PIL import ImageGrab
import time


# model = torch.hub.load('D:\\vehicle_detection\\yolov5\\runs\\train\\exp15\\weights', 'best') 
# model = torch.hub.load('ultralytics/yolov5', 'custom', path='runs/train/exp15/weights/best.pt', force_reload=True)
model = torch.hub.load('D:\\vehicle_detection\\yolov5', 'custom', path='runs/train/exp15/weights/best.pt', source='local', force_reload=True)


# class_id_name=model.names[0] = 'xe may'

# print(model.names[0])
# print(model.names[1])
# print(model.names[2])
# print(model.names[3])

CLASSES = ["xe may", "xe hoi", "xe bus", "xe tai"]

cap = cv2.VideoCapture('D:\\vehicle_detection\\highway.mp4')


size = 416
count=0
counter_xe_may=0
counter_xe_hoi=0
counter_xe_tai=0
counter_xe_bus=0

color=(0,0,255)

cy1=100
offset=5

fps_start_time = time.time()
fps=0




while cap.isOpened():
    ret, frame = cap.read()
    
    # fps_start_time = time.time()
    
    count += 1
    if count % 4 != 0:
        continue
    
    fps_end_time = time.time()
    fps_diff_time = fps_end_time - fps_start_time
    fps = 1 / fps_diff_time
    fps_start_time = fps_end_time
    fps_text="FPS: {:.2f}ms".format(fps)
    frame = cv2.resize(frame,(600,500))
    # cv2.line(frame, (79,cy1),(599,cy1), (0,0,255), 2)
    
    results = model(frame)
    # a= results.pandas().xyxy[0].sort_values('xmin')  # sorted left-right
    # print(results.pandas().xyxy[0])
    for index,row in results.pandas().xyxy[0].iterrows():
        # print(row)
        x1 = int(row['xmin'])
        y1 = int(row['ymin'])
        x2 = int(row['xmax'])
        y2 = int(row['ymax'])
        id = (row['class'])
        acuracy = (row['confidence'])
        # print(id)
        # if acuracy*100 > 60:
        cv2.rectangle(frame, (x1,y1), (x2,y2), (0,0,255),2)
        rectx1,recty1 =((x1+x2)/2,(y1+y2)/2)
        rectcenter = int(rectx1),int(recty1)
        cx = rectcenter[0]
        cy = rectcenter[1]
        cv2.circle(frame, (cx,cy), 3, (0,255,0), -1)
        
        cv2.putText(frame,CLASSES[id],(x1,y1),cv2.FONT_HERSHEY_PLAIN,2,(0,255,0),2)
        
        if cy<(cy1+offset) and cy>(cy1-offset):
            if id == 0:
                counter_xe_may+=1
            elif id == 1:
                counter_xe_hoi+=1
            elif id == 2:
                counter_xe_bus+=1
            elif id == 3:
                counter_xe_tai+=1
            cv2.line(frame, (1,cy1),(599,cy1), (0,255,255), 2)
            # print(counter)
            
        cv2.putText(frame,"So luong xe may: "+str(counter_xe_may),(250,300),cv2.FONT_HERSHEY_PLAIN,2,(0,255,0),2)
        cv2.putText(frame,"So luong xe hoi: "+str(counter_xe_hoi),(250,350),cv2.FONT_HERSHEY_PLAIN,2,(0,255,0),2)
        cv2.putText(frame,"So luong xe tai: "+str(counter_xe_tai),(250,400),cv2.FONT_HERSHEY_PLAIN,2,(0,255,0),2)
        cv2.putText(frame,"So luong xe bus: "+str(counter_xe_bus),(250,450),cv2.FONT_HERSHEY_PLAIN,2,(0,255,0),2)
        cv2.putText(frame, fps_text, (5, 30), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 0), 1)

        
    cv2.imshow("result",frame)
    # results.print()
    # results.show()
    # print(np.squeeze(results.render()))
    # print('\n',results.xyxy[0])
    # cv2.imshow('YOLO', np.squeeze(results.render()))
    # print(count)
    
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()


