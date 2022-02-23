# import requests
# import speech_recognition as sr
# from converter import Converter
# import subprocess
# import os

# url = 'https://cdn.fbsbx.com/v/t59.3654-21/273435150_630569734868930_5045159025695793697_n.mp4/audioclip-1644285883000-2810.mp4?_nc_cat=104&ccb=1-5&_nc_sid=7272a8&_nc_ohc=YMt5zfXNsrAAX91XOm9&_nc_ht=cdn.fbsbx.com&oh=03_AVI4Pdo8xhUyNTTuEa8_lD5cRP3E05AvK9zF3Jy_r4AX_g&oe=6203A2A6'
# r = requests.get(url)
# ffmpegPath = r"D:\HieuCali\File of Hieu\Project\DSA Company\Project\ChatBox_RASA\dsa_demo_sell_materia\draft\ffmpeg-64-gpl\bin\ffmpeg.exe"
# ffprobePath = r"D:\HieuCali\File of Hieu\Project\DSA Company\Project\ChatBox_RASA\dsa_demo_sell_materia\draft\ffmpeg-64-gpl\bin\ffprobe.exe"
# c = Converter(ffmpegPath, ffprobePath)

# with open("test.mp4", "wb") as handle:
#     for data in r.iter_content():
#         handle.write(data)
# cmdline = ['avconv',
#            '-i',
#            'test.mp4',
#            '-vn',
#            '-f',
#            'wav',
#            'test.wav']
# subprocess.call(cmdline)

# ra = sr.Recognizer()
# with sr.AudioFile('test.wav') as source:
#     audio = ra.record(source)

# command = ra.recognize_google(audio)
# print (command)

# os.remove("test.mp4")
# os.remove("test.wav")
# %%
import requests
import speech_recognition as sr
import moviepy.editor as mp
url = 'https://cdn.fbsbx.com/v/t59.3654-21/273435150_630569734868930_5045159025695793697_n.mp4/audioclip-1644285883000-2810.mp4?_nc_cat=104&ccb=1-5&_nc_sid=7272a8&_nc_ohc=YMt5zfXNsrAAX91XOm9&_nc_ht=cdn.fbsbx.com&oh=03_AVI4Pdo8xhUyNTTuEa8_lD5cRP3E05AvK9zF3Jy_r4AX_g&oe=6203A2A6'
r = requests.get(url)
with open("test.wav", "wb") as handle:
    for data in r.iter_content():
        handle.write(data)
# import soundfile
# data, samplerate = soundfile.read('test.wav')
# soundfile.write('new.wav', data, samplerate, subtype='PCM_16')
# audio = "new.wav"
# with sr.AudioFile(audio) as source:
#     audio = r.record(source)
# text= r.recognize_google(audio)
# print(text)
r = sr.Recognizer()
with sr.AudioFile('test.wav') as source:
    audio = r.record(source)
command = r.recognize_google(audio)
print(command)

# %%
import subprocess
import os
import requests
import speech_recognition as sr

url = 'https://cdn.fbsbx.com/v/t59.3654-21/273435150_630569734868930_5045159025695793697_n.mp4/audioclip-1644285883000-2810.mp4?_nc_cat=104&ccb=1-5&_nc_sid=7272a8&_nc_ohc=YMt5zfXNsrAAX91XOm9&_nc_ht=cdn.fbsbx.com&oh=03_AVI4Pdo8xhUyNTTuEa8_lD5cRP3E05AvK9zF3Jy_r4AX_g&oe=6203A2A6'
r = requests.get(url)
with open("test.wav", "wb") as handle:
    for data in r.iter_content():
        handle.write(data)

cmdline = ['avconv',
           '-i',
           'test.mp4',
           '-vn',
           '-f',
           'wav',
           'test.wav']
subprocess.call(cmdline)

r = sr.Recognizer()
with sr.AudioFile('test.wav') as source:
    audio = r.record(source)

command = r.recognize_google(audio)
print(command)

os.remove("test.mp4")
os.remove("test.wav")


# %%
# importing libraries 
import speech_recognition as sr
import requests

url = 'https://cdn.fbsbx.com/v/t59.3654-21/273435150_630569734868930_5045159025695793697_n.mp4/audioclip-1644285883000-2810.mp4?_nc_cat=104&ccb=1-5&_nc_sid=7272a8&_nc_ohc=YMt5zfXNsrAAX91XOm9&_nc_ht=cdn.fbsbx.com&oh=03_AVI4Pdo8xhUyNTTuEa8_lD5cRP3E05AvK9zF3Jy_r4AX_g&oe=6203A2A6'
r = requests.get(url)
with open("test.wav", "wb") as handle:
    for data in r.iter_content():
        handle.write(data)


filename = "test.wav"
# initialize the recognizer
r = sr.Recognizer()
# open the file
with sr.AudioFile(filename) as source:
    # listen for the data (load audio to memory)
    audio_data = r.record(source)
    # recognize (convert from speech to text)
    text = r.recognize_google(audio_data)
    print(text)
#!--------------------------------------------------------------------------Duyệt
# %%
'''Speech-to-text'''
#-Nhận diện ngôn ngữ
import speech_recognition as sr
#-Convert audio content to conformity  
from moviepy.editor import *
#-Send API of website
import requests
#-Interactive systems
import os

# the audio content of customer  
url = 'https://cdn.fbsbx.com/v/t59.3654-21/273435150_630569734868930_5045159025695793697_n.mp4/audioclip-1644285883000-2810.mp4?_nc_cat=104&ccb=1-5&_nc_sid=7272a8&_nc_ohc=YMt5zfXNsrAAX91XOm9&_nc_ht=cdn.fbsbx.com&oh=03_AVI4Pdo8xhUyNTTuEa8_lD5cRP3E05AvK9zF3Jy_r4AX_g&oe=6203A2A6'
# take the audio by URL
r = requests.get(url)
# Open content and convert to wav
with open("voice.wav", "wb") as handle:
    for data in r.iter_content():
        handle.write(data)
# concentrate(nén) audio and convert to conformity type
sound = AudioFileClip("voice.wav")
sound.write_audiofile("voice.wav", 44100, 2, 2000,"pcm_s16le")
# initialize(khởi động) the recognizer(nhận diện)
r = sr.Recognizer()
# open the file
with sr.AudioFile("voice.wav") as source:
    # listen for the data (load audio to memory)
    audio_data = r.record(source)
    # recognize (convert from speech to text) -> Result
    text = r.recognize_google(audio_data,language="vi-VI")
    

os.remove("voice.wav")



    # %%
