import cv2
import numpy

def lapvideo(vid_path):
    print("="*60)
    print("USING LAPLACIAN METHOD")
    sum=0
    video=cv2.VideoCapture(vid_path)

    if not video.isOpened():
        print("Error: Could Not Open The File.")
        return

    print(f"Analyzing Video Path: {vid_path}")

    while True:
        ret, frame=video.read()
        if not ret:
            print("Processing Complete. Video Ended.")
            break

        frame= cv2.resize(frame, (50,50))
        gray=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        score=numpy.var(cv2.Laplacian(gray, cv2.CV_64F))
        sum=sum+score
        if cv2.waitKey(25) & 0xFF==ord('q'):
            break

    count=int(video.get(cv2.CAP_PROP_FRAME_COUNT))
    avg=sum/count
    print(f"Total Frames: {count}")
    print(f"Score: {avg:.2f}")

    if(avg>=600):
        print("REAL/ ORGANIC VIDEO")
    else:
        print("AI/ SYNTHETIC")
    
    video.release()
    cv2.destroyAllWindows()
    print("="*60)


#Using Laplacian Baseline Energy
def laplacian(path):
    print("="*60)
    print("USING LAPLACIAN BASELINE ENERGY")
    image=cv2.imread(path)

    gray=cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray=cv2.equalizeHist(gray)

    h, w=gray.shape
    top_left=gray[0:60, 0:60]
    top_right=gray[h-50:h, w-50:w]

    base1=cv2.Laplacian(top_left, cv2.CV_64F).var()
    base2=cv2.Laplacian(top_right, cv2.CV_64F).var()

    center=gray[h//4:3*h//4, w//4:3*w//4]

    face_center=cv2.Laplacian(center, cv2.CV_64F).var()

    print(f"Face Enegy: {face_center:.2f}")
    print(f"Base1 Energy: {base1:.2f}")
    print(f"Base2 Energy: {base2:.2f}")

    if(face_center>(base1 *3) and face_center>(base2 *3)):
        print("AI IMAGE")
        print("Over-Sharpened")

    elif(face_center<(base1 / 3) and face_center<(base2 / 3)):
        print("AI IMAGE")
        print("Smoothed or Blurred")

    else:
        print("REAL IMAGE")

    print("="*60)    



