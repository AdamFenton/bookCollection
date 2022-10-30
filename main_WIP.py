
import speech_recognition
import speech_recognition as sr
from pydub import AudioSegment
import re
filename="/Users/adamfenton/Downloads/rec.m4a"
wav_filename = r"/Users/adamfenton/Downloads/rec.wav"
track = AudioSegment.from_file(filename,  format= 'm4a')
wav_file = track.export(wav_filename, format='wav')

r = sr.Recognizer()
with sr.AudioFile(wav_file) as source:

	audio_data =r.record(source)
	text = r.recognize_google(audio_data)


# print(text)


# authors = re.findall(r'author(.+?)',text)
titles = re.findall(r'break(.+?)break',text.lower())
print(titles)
# for a,t in zip(authors,titles):
# 	print(a,t)
