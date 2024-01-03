# microsoftによりチューニングされたT5モデルを使用して英語の音声合成を行う
# https://huggingface.co/microsoft/speecht5_tts

from transformers import pipeline
from datasets import load_dataset
import soundfile as sf
import torch

synthesiser = pipeline("text-to-speech", "microsoft/speecht5_tts")
embeddings_dataset = load_dataset("Matthijs/cmu-arctic-xvectors", split="validation")
speaker_embedding = torch.tensor(embeddings_dataset[7306]["xvector"]).unsqueeze(0)
print("load dataset")

with open("sample-en.txt", "r", encoding="utf-8") as file:
    text = file.read()
    print("file read")

speech = synthesiser(
    text,
    forward_params={"speaker_embeddings": speaker_embedding},
)
print("initializing synthesiser")

# 音声をファイルに保存
# sf.write("speech.wav", speech["audio"], samplerate=speech["sampling_rate"])
sf.write("speech.mp3", speech["audio"], samplerate=speech["sampling_rate"])
print("complete")
