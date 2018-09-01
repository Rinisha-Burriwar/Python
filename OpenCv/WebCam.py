import  cv2

capture = cv2.VideoCapture(0)

ret = True
while(ret):
    ret,frame = capture.read()
    cv2.imshow('captured image', frame)

    key = cv2.waitKey(27)
    if key == 27:
        cv2.destroyAllWindows()
        capture.release()
