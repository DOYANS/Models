"""
ClinicalBERT
1.2B words of diverse diseases.
EHRs from over 3 million patient records to fine tune the base language model.
"""
from transformers import AutoTokenizer, AutoModel

tokenizer = AutoTokenizer.from_pretrained("medicalai/ClinicalBERT")
model = AutoModel.from_pretrained("medicalai/ClinicalBERT")

inputs = tokenizer("Hello world!", return_tensors="pt")
outputs = model(**inputs)

print(outputs)
