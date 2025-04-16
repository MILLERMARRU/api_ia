python -m venv venv

venv\Scripts\activate

pip install fastapi pymysql uvicorn


.\ngrok config add-authtoken TU_TOKEN_AQUI
uvicorn main:app --host 127.0.0.1 --port 8000

.\ngrok http 8000

uvicorn app.main:app --reload


