#!/usr/bin/env python
from pydub import AudioSegment
import sys

if len(sys.argv) <= 1:
	print("Parametros invalidos! Use python music.py [ARQUIVO MP3]")
	exit()

mp3 = str(sys.argv[1])
if mp3[-4:] != '.mp3':
	print("Arquivo invalido")
	exit()

sound = AudioSegment.from_file(mp3, format="mp3")
size = len(sound)

q, r = divmod(size, 1000)
totalSegments= q + int(bool(r)) 
n = 0

s = sound[0:0]

pan = float(1.0)
ind = False

while n < (totalSegments * 10):
	firstPart = (totalSegments * n)
	secondPart = (totalSegments * (n + 1))
	s += (sound[firstPart:secondPart].pan(pan))
	if ind:
		pan += 0.100
	else:
		pan -= 0.100
	if pan <= -0.900:
		ind = True
		pan += 0.100
	if pan >= 0.900:
		ind = False
		pan -= 0.100
	n += 1
s.export(mp3[:-4]+'-final.mp3', format="mp3")
print("Processo concluido!")
