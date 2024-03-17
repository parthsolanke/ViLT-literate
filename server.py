from fastapi import FastAPI, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware
from PIL import Image
from io import BytesIO
from utils.pipeline import inference_pipeline

app = FastAPI()

# Allowing CORS
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Route for prediction
@app.post("/predict")
async def predict(image: UploadFile = File(...), query: str = Form(...)):
    try:
        # Open and process image
        image_bytes = await image.read()
        image_pil = Image.open(BytesIO(image_bytes))
        result = inference_pipeline(image=image_pil, question=query)
        return {"result": result}
    except Exception as e:
        return {"error": str(e)}

# Root route
@app.get("/")
def read_root():
    return {"Hello": "World"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
