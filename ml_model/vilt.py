'''
model code
'''
from PIL import Image
from transformers import (ViltProcessor, ViltForQuestionAnswering)

processor = ViltProcessor.from_pretrained("dandelin/vilt-b32-finetuned-vqa")
model = ViltForQuestionAnswering.from_pretrained("dandelin/vilt-b32-finetuned-vqa")

def model_pipeline(input_text: str, input_image: Image) -> str:
    """Returns"""
     # prepare inputs
    encoding = processor(input_image, input_text, return_tensors="pt")

    # forward pass
    outputs = model(**encoding)
    logits = outputs.logits
    idx = logits.argmax(-1).item()

    result = model.config.id2label[idx]

    return  result
