FROM python:3

COPY src /app
COPY poetry.lock /app
COPY pyproject.toml /app
WORKDIR /app
RUN pip3 install poetry
RUN poetry env use python3.9
RUN poetry install
ENV PORT=8000
ENV DB=localhost
ENV DEBUG=True
EXPOSE 5000
CMD poetry run python app.py
