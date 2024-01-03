from transformers import pipeline
from datasets import load_dataset
import soundfile as sf
import torch

tokenizer = T5Tokenizer.from_pretrained("sonoisa/t5-base-japanese")
model = T5ForConditionalGeneration.from_pretrained("sonoisa/t5-base-japanese")
print("load dataset")

with open("sample2.txt", "r", encoding="utf-8") as file:
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
