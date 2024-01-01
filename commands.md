uvicorn main:app --reload --host 0.0.0.0 --port 8001
pip freeze > .\requirements.txt
set TF_ENABLE_ONEDNN_OPTS=0
docker compose up --build