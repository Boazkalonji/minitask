ARG PYTHON_VERSION=3.10

FROM python:${PYTHON_VERSION}-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /mon-projet-minitask-packete



COPY requrement.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

VOLUME ["/mon-projet-minitask-packete/media"]

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "minitask.wsgi:application"]

