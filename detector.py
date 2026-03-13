from fastapi import FastAPI, UploadFile, File
import uvicorn
import random

# 1. Initialize the app
app = FastAPI()

# 2. The "Home" page (The Get request)
@app.get("/")
def home():
    return {"status": "Server is running!", "message": "Welcome to the Deepfake Detection API"}

# 3. The "Detection" page (The Post request)
@app.post("/detect")
async def detect_deepfake(file: UploadFile = File(...)):
    # This simulates an AI model's logic for your hackathon demo
    confidence_score = round(random.uniform(0.7, 0.99), 2)
    is_fake = random.choice([True, False])
    
    return {
        "filename": file.filename,
        "content_type": file.content_type,
        "is_deepfake": is_fake,
        "confidence": confidence_score,
        "message": "Analysis complete"
    }

# 4. The "Start" logic
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)