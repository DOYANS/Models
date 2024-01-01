"""
stanford-crfm/BioMedLM
"""
from transformers import AutoTokenizer,AutoModelForCausalLM

MODEL = "stanford-crfm/BioMedLM"

tokenizer = AutoTokenizer.from_pretrained(MODEL,device_map="auto")
model = AutoModelForCausalLM.from_pretrained(MODEL)


def model_pipeline(input_text: str) -> str:
    """model output."""
    # prepare inputs
    inputs = tokenizer(input_text, return_tensors='pt')

    # forward pass
    outputs = model(**inputs, labels=inputs["input_ids"])
    # loss = outputs.loss
    # logits = outputs.logits

    result = outputs.last_hidden_state

    return  result
