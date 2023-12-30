"""
main file
"""

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    """ home page. """
    return "Welcome to the Medical Model API!"

@app.get("/ClinicalBERT/{input_data}")
async def predict(input_data: str):
    """ prediction with ClinicalBERT. """
    prediction = "Your prediction: " + input_data
    return {"prediction": prediction}
