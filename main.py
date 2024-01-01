"""
main file
"""

from fastapi import (FastAPI,)
from url import (model,)

app = FastAPI(
    debug=True,version="1.0",
    title="Models API", openapi_url="/api.json",
)

@app.get("/")
def read_root() -> str:
    """ home page. """
    return "Welcome to the Model API!"

@app.get("/test/")
async def predict():
    """ API testing. """
    return 0

app.include_router(
    router=model.router,
    prefix="/models",
    # tags=["models"],
)
