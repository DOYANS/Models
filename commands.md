<!-- start local -->
- py -m venv venv
- .\venv\Scripts\activate

- python.exe -m pip install --upgrade pip
- python -m pip install fastapi uvicorn pytorch-transformers Pillow transformers
- python -m pip freeze > requirements.txt
- python -m uvicorn main:app --reload

- set TF_ENABLE_ONEDNN_OPTS=0
- docker compose up --build
