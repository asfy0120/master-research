"""Synthesizes speech from the input string of text or ssml.

Note: ssml must be well-formed according to:
    https://www.w3.org/TR/speech-synthesis/
"""
#日本語or英語判定
import re
import csv
import time
import datetime
import os
p = re.compile('[a-zA-Zａ-ｚＡ-Ｚ0123456789]+')

from google.cloud import texttospeech

#学習用メモのパス
path = os.getcwd()+'\\'
bupath= os.getcwd()+'\\'+'backup'+'\\'

#datetime 20XX-XX-XX XX:XX:XX.XX
dt_now = datetime.datetime.now()

#バックアップファイル名　TTS_sumple_buckup"UNIXTIME".csv
bu="TTS_sumple_backup"+str(int(dt_now.timestamp()))+".csv"

#読み上げる文字列の選択
with open(path+"TTS_sumple.csv",encoding="utf-8_sig") as readFile:
    reader = csv.reader(readFile)
    l = list(reader)
    #print(l)
    #l = [row for row in reader]

    #csvファイルの先頭の行を対象に
    #メモの日付dtを取得
    dt=datetime.datetime(int(l[0][2]),int(l[0][3]),int(l[0][4]))
    l[0]=[l[0][0],l[0][1],int(dt_now.year),int(dt_now.month),int(dt_now.day)]

    #1日以上たってればprint
    if(abs(dt_now.timestamp()-dt.timestamp()) > 86400):
        with open(bupath+bu, 'w',encoding="utf-8_sig") as writeFile:
            writer = csv.writer(writeFile, lineterminator="\n")
            with open(path+"TTS_sumple.csv",encoding="utf-8_sig") as readFile:
                reader = csv.reader(readFile)
                lines=list(reader)
            writer.writerows(lines)
            readFile.close()
            writeFile.close()
        print(l[0][0])
        with open(path+"TTS_sumple.csv", 'w',encoding="utf-8_sig") as writeFile:
            writer = csv.writer(writeFile, lineterminator="\n")
            writer.writerows(l)
            writeFile.close()

    #デバッグ用
    print("debug用：")
    print("現在時刻とメモ記入時刻との差:"+str(abs(dt_now.timestamp()-dt.timestamp())) )
    print("メモ行数:"+str(len(l)))
    word=l[0][0]
    print("音声化文字列:"+word)


readFile.close()


# Instantiates a client
client = texttospeech.TextToSpeechClient()

# Set the text input to be synthesized
synthesis_input = texttospeech.SynthesisInput(text=word)

# Build the voice request, select the language code ("en-US") and the ssml
if p.fullmatch(word):
    voice = texttospeech.VoiceSelectionParams(
        language_code="en-US-Standard-H", ssml_gender=texttospeech.SsmlVoiceGender.NEUTRAL
    )
else:
    voice = texttospeech.VoiceSelectionParams(
        language_code="ja-JP-Wavenet-B", ssml_gender=texttospeech.SsmlVoiceGender.NEUTRAL
    )

# Select the type of audio file you want returned
audio_config = texttospeech.AudioConfig(
    audio_encoding=texttospeech.AudioEncoding.LINEAR16
)

# Perform the text-to-speech request on the text input with the selected
# voice parameters and audio file type
response = client.synthesize_speech(
    input=synthesis_input, voice=voice, audio_config=audio_config
)

# The response's audio_content is binary.
with open("output.wav", "wb") as out:
    # Write the response to the output file.
    out.write(response.audio_content)
    print('Audio content written to file "output.wav"')
