uvicorn main:app --reload --host 0.0.0.0 --port 8000
pip freeze > .\requirements.txt
set TF_ENABLE_ONEDNN_OPTS=0
