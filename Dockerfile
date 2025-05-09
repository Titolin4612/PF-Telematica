FROM ubuntu:22.04

LABEL maintainer="Santiago Hernandez Morantes <santiago@example.com>"
LABEL version="1.0"
LABEL description="Servicio Telemático Profesional con Flask y Docker para CAZ"

RUN apt update && \
    apt install -y --no-install-recommends python3.10 python3-pip && \
    rm -rf /var/lib/apt/lists/*

RUN pip3 install --no-cache-dir flask

WORKDIR /app

# Copia solo la carpeta app/ (que contiene todo lo necesario)
COPY app/ .

EXPOSE 80

CMD ["python3.10", "main.py"]

