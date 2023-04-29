    FROM python:3-alpine3.12
    WORKDIR /backend
    COPY ./backend /backend
    RUN pip install -r ./requirements.txt
    CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]