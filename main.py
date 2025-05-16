from fastapi import FastAPI, UploadFile, File
from fastapi.responses import FileResponse
import uuid
import os
import subprocess

app = FastAPI()

@app.post("/convert")
async def convert(file: UploadFile = File(...)):
    input_filename = f"/tmp/{uuid.uuid4()}.m4v"
    output_filename = input_filename.replace(".m4v", ".mp4")

    with open(input_filename, "wb") as f:
        f.write(await file.read())

    try:
        subprocess.run(["ffmpeg", "-i", input_filename, "-c", "copy", output_filename], check=True)
        return FileResponse(output_filename, filename="converted.mp4")
    except subprocess.CalledProcessError:
        return {"error": "Conversion failed"}
    finally:
        if os.path.exists(input_filename):
            os.remove(input_filename)
from fastapi.staticfiles import StaticFiles

app.mount("/", StaticFiles(directory="static", html=True), name="static")