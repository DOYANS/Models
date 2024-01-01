"""
models API
"""
from fastapi import APIRouter, UploadFile
from PIL import Image
from ml_model import (biomedllm,vilt,clinicalbert,)

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

@router.post("/clinical_bert")
def clinical_bert_model(input_text: str) -> str:
    """ clinical BERT prediction. """
    results = clinicalbert.model_pipeline(input_text)

    return results

@router.post("/biomedllm")
def medllm_model(input_text: str) -> str:
    """ Bio Med LLM prediction. """
    results = biomedllm.model_pipeline(input_text)

    return results
