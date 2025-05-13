# YOLO Object Detection Website

This project is a simple website for object detection using a YOLOv5 model with a FastAPI backend and a frontend for image upload and display of detection results.

## Setup

### Backend

1. Navigate to the backend directory:
   ```
   cd backend
   ```

2. Create a virtual environment (optional but recommended):
   ```
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Run the backend server:
   ```
   uvicorn main:app --host 0.0.0.0 --port 8000
   ```

### Frontend

1. Open the `frontend/index.html` file in a web browser (e.g., Chrome, Firefox).

2. Upload an image and click "Detect Objects" to see the detected objects with bounding boxes.

## Notes

- The backend uses a pre-trained YOLOv5s model from Ultralytics.
- The backend must be running for the frontend to communicate and get detection results.
- CORS is enabled on the backend to allow frontend requests.
- To train your own YOLO model, you will need to prepare a dataset and modify the backend accordingly.

## License

This project is provided as-is for demonstration purposes.
