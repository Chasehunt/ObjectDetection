from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from io import BytesIO
from PIL import Image
import torch

app = FastAPI()

# Allow CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load YOLOv5 model from Ultralytics hub (pretrained)
model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)

@app.post("/detect")
async def detect_objects(file: UploadFile = File(...)):
    try:
        image_bytes = await file.read()
        img = Image.open(BytesIO(image_bytes)).convert("RGB")
        results = model(img)
        detections = results.pandas().xyxy[0].to_dict(orient="records")
        return JSONResponse(content={"detections": detections})
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
