import cv2
import os

##---------------------------------------------------------------------------------------------
def make_video(images, outvid=None, fps=5, size=None, is_color=True, format="XVID"):
    """
    Create a video from a list of images.
    @param      outvid      output video
    @param      images      list of images to use in the video
    @param      fps         frame per second
    @param      size        size of each frame
    @param      is_color    color
    @param      format      
    """
    # fourcc = VideoWriter_fourcc(*format)
    # For opencv2 and opencv3:
    if int(cv2.__version__[0]) > 2:
        fourcc = cv2.VideoWriter_fourcc(*format)
    else:
        fourcc = cv2.cv.CV_FOURCC(*format)
    vid = None
    for img in images:
        if vid is None:
            if size is None:
                size = img.shape[1], img.shape[0]
            vid = cv2.VideoWriter(outvid, fourcc, float(fps), size, is_color)
        if size[0] != img.shape[1] and size[1] != img.shape[0]:
            img = cv2.resize(img, size)
        vid.write(img)
    vid.release() 

##------------------------------------------------------------------------------------------------



first_frame = None
video=cv2.VideoCapture("video.mp4")
images = []
imagesT = []

while True:
    check, frame = video.read()
    if frame is None:
        break
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    gray=cv2.GaussianBlur(gray,(21,21),0)

    if first_frame is None:
        first_frame=gray
        continue

    delta_frame=cv2.absdiff(first_frame,gray)
    thresh_frame=cv2.threshold(delta_frame, 70, 255, cv2.THRESH_BINARY)[1]
    thresh_frame=cv2.dilate(thresh_frame, None, iterations=2)

    cnts = cv2.findContours(thresh_frame, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    # cnts is tuple
    for contour in cnts[0]:
        if cv2.contourArea(contour) < 10000:
            continue

        (x, y, w, h)=cv2.boundingRect(contour)
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0,255,0), 3)

    images.append(frame)
    imagesT.append(thresh_frame)
    cv2.imshow("Gray Frame",gray)
    cv2.imshow("Delta Frame",delta_frame)
    cv2.imshow("Threshold Frame",thresh_frame)
    cv2.imshow("Color Frame",frame)

    key=cv2.waitKey(30)


make_video(images, outvid='Color_Frame.avi', fps=50, size=None, is_color=True, format="XVID")
make_video(imagesT, outvid='Threshold.avi', fps=50, size=None, is_color=False, format="XVID")
video.release()
cv2.destroyAllWindows()
