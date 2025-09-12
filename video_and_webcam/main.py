import cv2

cap = cv2.VideoCapture(0) #Opens webcam

frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
codec = cv2.VideoWriter_fourcc(*'XVID')
recorder = cv2.VideoWriter('output.avi', codec, 20, (frame_width, frame_height))  ##Save video to file

while True:
    ret, frame = cap.read()
    if not ret:
        break
    cv2.imshow("Video", frame)
    recorder.write(frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
recorder.release()
cv2.destroyAllWindows()