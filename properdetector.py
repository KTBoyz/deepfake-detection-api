from fastapi import FastAPI, UploadFile, File
import cv2
import numpy as np
import io
from PIL import Image
import uvicorn

app = FastAPI()

def analyze_face_sharpness(image_bytes):
    # Convert bytes to OpenCV format
    nparr = np.frombuffer(image_bytes, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    
    # 1. Convert to Grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # 2. Detect Faces (using built-in Haar Cascade)
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    
    if len(faces) == 0:
        return "No Face Detected", 0.0

    # 3. Lapalcian Variance (Sharpness Check)
    # Deepfakes often have 'smoothing' artifacts around the eyes/mouth
    for (x, y, w, h) in faces:
        face_roi = gray[y:y+h, x:x+w]
        laplacian_var = cv2.Laplacian(face_roi, cv2.CV_64F).var()
        
        # High variance (>100) usually means a sharp, real photo.
        # Low variance (<50) can indicate AI smoothing or blur.
        if laplacian_var < 60:
            return "Likely Deepfake (AI Smoothing Detected)", round(1 - (laplacian_var/100), 2)
        else:
            return "Likely Real (Natural Textures Found)", round(laplacian_var/500, 2)

    return "Inconclusive", 0.5

@app.post("/detect")
async def detect(file: UploadFile = File(...)):
    contents = await file.read()
    
    # Run our new OpenCV logic
    result_text, confidence = analyze_face_sharpness(contents)
    
    return {
        "filename": file.filename,
        "analysis": result_text,
        "score": min(confidence, 0.99), # Cap it at 99%
        "details": "Pixel frequency and texture analysis complete."
    }

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)