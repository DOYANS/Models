<!-- start local -->
py -m venv env
.\env\Scripts\activate
python.exe -m pip install --upgrade pip
python -m pip install fastapi uvicorn pytorch-transformers Pillow transformers
python -m pip freeze > requirements.txt
python -m uvicorn main:app --reload
