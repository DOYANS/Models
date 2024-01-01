"""
main file
"""
from fastapi import (FastAPI,)
from url import (model_api,)

app = FastAPI(
    version="1.0",
    title="Models API", openapi_url="/api.json",
)
app.include_router(model_api.router)

@app.get("/")
def home() -> str:
    """ home page. """
    return "Welcome to the Model API!"
