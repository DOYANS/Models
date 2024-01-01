'''
model code
'''

from PIL import Image
import requests
from transformers import (ViltProcessor, ViltForQuestionAnswering)

processor = ViltProcessor.from_pretrained("dandelin/vilt-b32-finetuned-vqa")
model = ViltForQuestionAnswering.from_pretrained("dandelin/vilt-b32-fin")

def model_pipeline(input_text: str, input_image: Image):
    """Returns"""
    # prepare input
    encoding = processor(input_image, input_text, retur_tensors=True)

    # forward pass
    outputs = model(**encoding)
    logits = outputs.logits
    idx = logits.argmax(-1).item()

    return model.confif.id2label[idx]
