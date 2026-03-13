from fastapi import FastAPI, UploadFile, File
from PIL import Image
import io
import uvicorn

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Deepfake Detector is Active"}

@app.post("/detect")
async def detect(file: UploadFile = File(...)):
    # 1. Read the file into Pillow
    contents = await file.read()
    image = Image.open(io.BytesIO(contents))
    
    # 2. Logic: Look for "Metadata" (Digital Fingerprints)
    # Most AI images (DALL-E, Midjourney) don't have EXIF data.
    # Real photos from phones usually do.
    has_metadata = True if image.getexif() else False
    
    # 3. Logic: Look for "AI Resolution"
    # Many AI generators output perfect squares (1024x1024).
    is_square = image.width == image.height
    
    # Simple Demo Logic
    if not has_metadata and is_square:
        result = "Likely AI Generated"
        confidence = 0.92
    elif not has_metadata:
        result = "Suspicious (No Camera Data)"
        confidence = 0.65
    else:
        result = "Likely Real (Camera Data Found)"
        confidence = 0.88

    return {
        "filename": file.filename,
        "format": image.format,
        "size": f"{image.width}x{image.height}",
        "analysis": result,
        "confidence": confidence
    }

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)