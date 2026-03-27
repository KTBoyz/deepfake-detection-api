from fastapi import FastAPI, Query
from fastapi.responses import PlainTextResponse
import CanVideo
import LapVideo
import SobVideo
from Pipeline import choice
import io, sys

app = FastAPI()

# Helper to capture print output
def capture_output(func, *args, **kwargs):
    buffer = io.StringIO()
    sys_stdout = sys.stdout
    sys.stdout = buffer
    try:
        func(*args, **kwargs)
    finally:
        sys.stdout = sys_stdout
    return buffer.getvalue()

@app.get("/canny_image", response_class=PlainTextResponse)
def run_canny_image(path: str = Query(..., description="Full path to the image file")):
    return capture_output(CanVideo.canny, path)

@app.get("/canny_video", response_class=PlainTextResponse)
def run_canny_video(path: str = Query(..., description="Full path to the video file")):
    return capture_output(CanVideo.canvideo, path)

@app.get("/laplacian_image", response_class=PlainTextResponse)
def run_laplacian_image(path: str = Query(..., description="Full path to the image file")):
    return capture_output(LapVideo.laplacian, path)

@app.get("/laplacian_video", response_class=PlainTextResponse)
def run_laplacian_video(path: str = Query(..., description="Full path to the video file")):
    return capture_output(LapVideo.lapvideo, path)

@app.get("/sobel_image", response_class=PlainTextResponse)
def run_sobel_image(path: str = Query(..., description="Full path to the image file")):
    return capture_output(SobVideo.sobel, path)

@app.get("/sobel_video", response_class=PlainTextResponse)
def run_sobel_video(path: str = Query(..., description="Full path to the video file")):
    return capture_output(SobVideo.sobvideo, path)
