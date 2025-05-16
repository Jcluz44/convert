FROM python:3.11-slim

# Installer ffmpeg
RUN apt update && apt install -y ffmpeg

# Définir le répertoire de travail
WORKDIR /app

# Copier les fichiers
COPY . /app

# Installer les dépendances Python
RUN pip install --no-cache-dir -r requirements.txt

# Exposer le port utilisé par uvicorn
EXPOSE 10000

# Commande de démarrage
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "10000"]