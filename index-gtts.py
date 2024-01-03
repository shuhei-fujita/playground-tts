# Google Text to Speech

from gtts import gTTS

# tts = gTTS("ここにテキストを入力", lang="ja")
with open("sample2.txt", "r", encoding="utf-8") as file:
    text = file.read()
    print("file opened")

tts = gTTS(text=text, lang="ja")
print("tts created")
tts.save("output.mp3")
print("complete")
