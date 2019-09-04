
import cv2
import numpy as np

slection = 2
#%%
if slection == 0:
    
    img = cv2.imread("rgb.png", 1)
    # 0 : black and white
    # 1 : RGB
    # -1 : RGB with alpha (transparancy)
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # BGR to GRAY transformation
    print(img.shape)
    for i in range(3):
        cv2.imshow("M",img[:,:,i])
        cv2.waitKey(0)
    # the resize function does a pooling (down-sampling)
#%%
elif slection ==1:
    img = cv2.imread("galaxy.jpg", 1)
    img = cv2.resize(img, (500,500))


    cv2.imwrite("Resized.jpg", new_img)
    cv2.imshow("Galaxy", new_img)
    cv2.waitKey(0) # if number -> ms wait

    for i in range(1,10):
        cv2.imshow("Non",cv2.resize(img, (i*100,i*100)))
        cv2.waitKey(0)
#%%
elif slection==2 :
    img = cv2.imread("rgb.png", 0)
    color_img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
    print(color_img.shape)
    for i in range(3):
        cv2.imshow("N%d"%i, color_img[:,:,i])
        cv2.waitKey(5000)