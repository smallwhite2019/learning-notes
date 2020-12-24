
#文件播放视频，并把它转换成灰度视频显示出来
'''
视频在保存不成功的时候，考虑下原视频的帧率，高度和宽度

'''
import numpy as np 
import cv2

import time
time_now = time.localtime()
TIME = time.strftime("%Y-%m-%d_%H:%M", time_now )
logs = './logs/' + TIME

cap = cv2.VideoCapture('./data/wecharm.mp4')
fourcc = cv2.VideoWriter_fourcc(*'XVID')
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))     
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))    
#fps = int(cv2.GetCaptureProperty(cap,CV_CAP_PROP_FPS))
fps = cap.get(cv2.CAP_PROP_FPS)
out = cv2.VideoWriter( 'logs' + '/output3.avi', fourcc, fps, (width, height))
while(True):
    ret, frame = cap.read()   # capture frame-by-frame
    if ret == True:
        frame = cv2.flip(frame, 0)
        out.write(frame)
        cv2.imshow('frame', frame)  #display the resulting frame
        if cv2.waitKey(1)&0xFF == ord('q'):
            break
    else:
        break
cap.release()
out.release()
cv2.destroyAllWindows()


'''

#从文件播放视频
import numpy as np 
import cv2
cap = cv2.VedioCapture(0)
#define the codec and create VideoWriter object
fourcc = cv2.VedioWriter_fourcc(*'XNID')
out  = cv2.VedioWriter('teaching.mp4', fourcc, 20.0, (640,480))
while(cap.isOpended()):
    ret, frame = cap.read()
    if ret == True:
        frame = cv2.flip(frame, 0)
        out.write(frame)
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
cap.release()
out.release()
cv2.destroyAllWindows()



cap.read
'''