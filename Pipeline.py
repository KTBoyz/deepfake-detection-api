import CanVideo
import LapVideo
import SobVideo

#LapVideo.lapvideo(path)

#CanVideo.canvideo(path)

#SobVideo.sobvideo(path)

def choice():
    print("Enter 1 for image detection.\n")
    print("Enter 2 for video detection.\n")
    choice=int(input("Enter Choice: "))
    if(choice==1):
        path=input("Enter image path: ")

        LapVideo.laplacian(path)

        SobVideo.sobel(path)

        CanVideo.canny(path)

    else:
        vid=input("Enter Video Path: ")
    
        LapVideo.lapvideo(vid)

        SobVideo.sobvideo(vid)

        CanVideo.canvideo(vid)

