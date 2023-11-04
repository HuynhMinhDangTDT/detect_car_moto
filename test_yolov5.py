import sys
import cv2
import torch


model = torch.hub.load('ultralytics/yolov5','yolov5s')
#model = torch.hub.load('ultralytics/yolov5','yolov5m')

model.conf = 0.3
#model.classes = [0]
#print(model.names)


camera = cv2.VideoCapture("2022_0121_090959_863.MOV")


while True:

  ret, img = camera.read()
  if not ret :
    while cv2.waitKey(100) == -1:
      pass
    break

  results = model(img)		#default=640
#  results = model(img, size=320)
#  results = model(img, size=480)


  for *bb, conf, cls in results.xyxy[0]:

      s   = model.names[int(cls)]+":"+'{:.1f}'.format(float(conf)*100)
      cc  = (255,255,0)
      cc2 = (128,0,0)

      cv2.rectangle(
          img,
          (int(bb[0]), int(bb[1])),
          (int(bb[2]), int(bb[3])),
          color=cc,
          thickness=2,
          )

      cv2.rectangle(img, (int(bb[0]), int(bb[1])-20), (int(bb[0])+len(s)*10, int(bb[1])), cc, -1)
      cv2.putText(img, s, (int(bb[0]), int(bb[1])-5), cv2.FONT_HERSHEY_PLAIN, 1, cc2, 1, cv2.LINE_AA)


  cv2.imshow('color',img)

  if cv2.waitKey(1) & 0xFF == ord('q'):
    break


camera.release()
cv2.destroyAllWindows()