"""
ClinicalBERT
1.2B words of diverse diseases.
EHRs from over 3 million patient records to fine tune the base language model.
"""
from transformers import AutoTokenizer, AutoModel

tokenizer = AutoTokenizer.from_pretrained("medicalai/ClinicalBERT")
model = AutoModel.from_pretrained("medicalai/ClinicalBERT")


def model_pipeline(input_text: str) -> str:
    """model output."""
     # prepare inputs
    encoding = tokenizer(input_text, return_tensors="pt")

    # forward pass
    outputs = model(**encoding)
    result = outputs.last_hidden_state

    return  result
