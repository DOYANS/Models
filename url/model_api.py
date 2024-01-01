"""
models API
"""
from fastapi import APIRouter, UploadFile
from PIL import Image
from ml_model import vilt

router = APIRouter(prefix="/models",tags=["models"],)

@router.get("/")
async def home():
    """ prediction. """
    return 0

@router.post("/vilt")
def vilt_model(input_text: str, input_image: UploadFile) -> str:
    """ VILT prediction. """
    image_data = Image.open(input_image.file)
    results = vilt.model_pipeline(input_text, image_data)

    return results
