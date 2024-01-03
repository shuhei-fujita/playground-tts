from pathlib import Path
from openai import OpenAI
from dotenv import load_dotenv
import os


def load_text(file_path):
    with file_path.open("r", encoding="utf-8") as file:
        return file.read()


def generate_speech(client, text, model_name="tts-1", voice="nova"):
    response = client.audio.speech.create(model=model_name, voice=voice, input=text)
    return response


# 環境変数のロード
load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=openai_api_key)
text_file_path = Path(__file__).parent / "sample-text-jp.txt"
speech_file_path = Path(__file__).parent / "speech.mp3"
speech_file_path = Path(__file__).parent / "speech.wav"
print("loaded envrinment variables")

# テキストファイルの読み込み
text = load_text(text_file_path)
print("loaded text file")

# 音声の生成
speech = generate_speech(client, text)
speech.stream_to_file(speech_file_path)
print("generated speech")
