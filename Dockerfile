FROM python:3

COPY src /app
COPY poetry.lock /app
COPY pyproject.toml /app
WORKDIR /app
RUN pip3 install poetry
RUN poetry env use python3.9
RUN poetry install
ENV PORT=8000
ENV DB=postgresql+psycopg2://postgres:postgres@localhost/flask_db
ENV DEBUG=True
EXPOSE 5000
CMD poetry run python server.py
