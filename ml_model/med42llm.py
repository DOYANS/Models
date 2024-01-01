# """
# m42-health/med42-70b
# """
# import os
# from huggingface_hub import login
# from transformers import AutoTokenizer,AutoModelForCausalLM

# MODEL = "m42-health/med42-70b"
# TOKEN = os.getenv("READ_TOKEN_LOCAL")

# login(token=TOKEN)

# tokenizer = AutoTokenizer.from_pretrained(MODEL,device_map="auto")
# model = AutoModelForCausalLM.from_pretrained(MODEL,token=TOKEN)


# def model_pipeline(input_text: str) -> str:
#     """model output."""
#      # prepare inputs
#     prompt = input_text
#     prompt_template=f'''
#     <|system|>:
#     <|prompter|>:{prompt}
#     <|assistant|>:
#     '''
#     input_ids = tokenizer(prompt_template, return_tensors='pt').input_ids.cuda()

#     # forward pass
#     output = model.generate(inputs=input_ids, temperature=0.7,
#                             do_sample=True,eos_token_id=tokenizer.eos_token_id,
#                             pad_token_id=tokenizer.pad_token_id,
#                             max_new_tokens=512,
#                         )
#     result = tokenizer.decode(output[0])

#     return  result
