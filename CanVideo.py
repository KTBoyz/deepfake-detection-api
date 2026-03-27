import cv2
import numpy

def canvideo(path):
    print("USING CANNY DENSITY")
    count_blur=0
    count_raw=0
    vid_path=cv2.VideoCapture(path)
    
    while vid_path.isOpened():
        ret, frame= vid_path.read()
        if not ret:
            print("Process Completed. Video Ended.")
            break
        h,w,_=frame.shape
        
        gray=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        blur=cv2.GaussianBlur(gray, (3,3), 0)

        roi_h, roi_w= int(h*0.5), int(w*0.3)
        start_y, start_x= int(h*0.25), int(w*0.35)

        frame_roi=frame[start_y:start_y+roi_h, start_x:start_x+roi_w]
        
        canny_raw=cv2.Canny(frame_roi, 100, 200)

        wp=numpy.sum(canny_raw==255)
        tp=canny_raw.size

        raw_density=(wp/tp)*100
        count_raw=count_raw + raw_density

        canny_blur=cv2.Canny(blur, 100, 200)

        wbp=numpy.sum(canny_blur==255)
        tbp=canny_blur.size

        blur_density=(wbp/tbp)*100
        count_blur=count_blur + blur_density

    frame_count= int(vid_path.get(cv2.CAP_PROP_FRAME_COUNT))
    avg_blur=count_blur/frame_count
    avg_raw=count_raw/frame_count
    delta=avg_raw-avg_blur

    print(f"Average Blur: {avg_blur:.2f}")
    print(f"Average Raw: {avg_raw:.2f}")
    print(f"Drop Rate: {delta:.2f}")

    if(avg_raw<0.50):
        print("QUALITY TOO LOW: VIDEO IS PRE BLURRED.")

    else:
        if(delta>=1.25):
            print("STATUS: AUTHENTIC REAL/ ORGANIC")
        elif(0.80<=delta<1.25):
            print("STATUS: INCONCLUSIVE. POSSIBLE HEAVY COMPRESSION OR A HIGH-QUALITY AI")
        elif(0.30<=delta<0.80):
            print("STAUS: SYNTHETIC. LACKS STOCHASTIC HIGH-FREQUENCY DATA")
        else:
            print("STATUS: DEEPFAKE. MATCHES 0.14 AI SIGNATURE")
        
    vid_path.release()
    cv2.destroyAllWindows()
    print("="*60)

def canny(path):
    print("USING CANNY EDGE DENSITY")
    image=cv2.imread(path)

    gray=cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray=cv2.equalizeHist(gray)

    blur=cv2.GaussianBlur(gray, (3,3), 0)

    #v=numpy.median(gray)
    #sigma=0.33

    #lower=int(max(0,(1.0-sigma)*v))
    #upper=int(min(255,(1.0+sigma)*v))

    canny_raw=cv2.Canny(image, 100, 200)

    wp=numpy.sum(canny_raw==255)
    tp=canny_raw.size

    raw_density=(wp/tp)*100
    print(f"Raw_ Texture Density: {raw_density:.2f}%")

    canny_blur=cv2.Canny(blur, 100, 200)

    wbp=numpy.sum(canny_blur==255)
    tbp=canny_blur.size

    blur_density=(wbp/tbp)*100
    print(f"Blur_Texture Density: {blur_density:.2f}%")

    drop_rate=(blur_density-raw_density)/raw_density
    print(f"Drop Rate: {drop_rate:.2f}")
    
    if(drop_rate>=0.70 and drop_rate<=1.0):
        print("AI IMAGE")

    else:
        print("REAL IMAGE")

    print("="*60)



    
