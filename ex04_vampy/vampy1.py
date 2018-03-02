#!/usr/bin/python3

# reqs
import vamp
import librosa

# open file
print("Loading audio file...")
data, rate = librosa.load("Rein_-_Occidente.mp3")

# process it
print("Processing audio file...")
chroma = vamp.collect(data, rate, vamp.list_plugins()[0])

# print the results
print(chroma)

# bye!
print("Done!")
