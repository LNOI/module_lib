from fastapi import FastAPI, File, UploadFile
from openai import OpenAI
from dotenv import load_dotenv
from lib.minio import upload_file

load_dotenv()

client = OpenAI()
app = FastAPI()


@app.post("/audio/")
async def create_upload_file(file: UploadFile = File(...)):
    with open("audio.mp3", "wb") as audio:
        audio.write(file.file.read())

    upload_file("audio.mp3", "195217711/audio.mp3")
    # with open("audio.mp3", "rb") as audio:
    #     transcription = client.audio.transcriptions.create(
    #         model="whisper-1", file=audio
    #     )
    return None
