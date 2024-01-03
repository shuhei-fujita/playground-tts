from pathlib import Path
from openai import OpenAI
from dotenv import load_dotenv
import os
from pydub import AudioSegment


def load_text(file_path):
    with file_path.open("r", encoding="utf-8") as file:
        return file.read()


def generate_speech(client, text, model_name="tts-1", voice="nova"):
    response = client.audio.speech.create(model=model_name, voice=voice, input=text)
    return response


def process_speech(client, text, voice):
    speech = generate_speech(client, text, voice=voice)
    temp_path = Path(__file__).parent / f"speach_{voice}.mp3"
    speech.stream_to_file(temp_path)
    return AudioSegment.from_mp3(temp_path)


# 環境変数のロード
load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=openai_api_key)

# テキストファイルの読み込み
text_file_path = Path(__file__).parent / "sample-text-jp.txt"
text = load_text(text_file_path)

combined_sounds = AudioSegment.empty()
for line in text.split("\n"):
    if "Aさん:" in line:
        combined_sounds += process_speech(
            client, line.replace("Aさん:", "").strip(), "nova"
        )
    elif "Bさん:" in line:
        combined_sounds += process_speech(
            client, line.replace("Bさん:", "").strip(), "alloy"
        )

# 結合した音声をMP3ファイルとして保存
speech_file_path = Path(__file__).parent / "speech_combined.mp3"
combined_sounds.export(speech_file_path, format="mp3")
