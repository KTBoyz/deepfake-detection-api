import cv2
import numpy

def sobvideo(path):
    print("USING SOBEL INTENSITY GRADIENT")
    vid_cap=cv2.VideoCapture(path)
    if not vid_cap:
        print("Error. Video Path Not Found.")
        return
    
    print(f"Analyzing Video Path: {path}")

    while vid_cap.isOpened():
        ret, frame= vid_cap.read()

        if not ret:
            print("Process Completed. Video Ended.")
            break

        frame=cv2.resize(frame, (640,640))
        gray=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        sobel_x=cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
        sobel_y=cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)

        magnitude=numpy.sqrt(sobel_x**2 + sobel_y**2)
        score=numpy.mean(magnitude)

    print(f"Score: {score:.2f}")

    threshold=10
    if(score>=threshold):
        print("STATUS: REAL/ ORGANIC.")

    else:
        print("STATUS: AI/ SYNTHETIC")    
    
    vid_cap.release()
    cv2.destroyAllWindows()
    print("="*60)


def sobel(path):
    print("USING SOBEL ENERGY RATIO")
    image=cv2.imread(path)

    gray=cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray=cv2.equalizeHist(gray)
    
    sobel_x=cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
    sobel_y=cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)

    abs_x=cv2.convertScaleAbs(sobel_x)
    abs_y=cv2.convertScaleAbs(sobel_y)

    energy_x=numpy.sum(abs_x)
    energy_y=numpy.sum(abs_y)

    ratio=energy_x/energy_y
    print(f"Energy Ratio:{ratio:.2f}")

    if(ratio>0.90):
        print("AI IMAGE")

    else:
        print("REAL IMAGE")

    print("="*60)
        
    

        
