import mingus
import time
import pandas as pd
import random
import mingus.core.chords as chords
from mingus.containers import NoteContainer
from mingus.containers import Bar
from mingus.containers import Track
from mingus.containers import Composition
from mingus.midi import midi_file_out
from mingus.containers.instrument import Instrument, Piano, Guitar



md=pd.read_csv("melody.csv",dtype=object)
md[md == " "] = None
#print(md)
bs=pd.read_csv("bass.csv")
#print(bs)




print(">>>>>>>>>>>>>>>>> Welcome to Melodify (Alpha v0.0.1) <<<<<<<<<<<<<<<<<<")
print()
print("Melodify is our try at giving you the best musical experience based on your current mood.")
print("It is an open source AI Music generator which creates melodies based on your present state of mind in a")
print("matter of seconds. So, indulge your emotions and vibe on!!")


time.sleep(5)

print()

print()

input("Press enter to continue")

print()

print("Hello There! I am Melodify, I can create a melody in seconds just for you.?")

time.sleep(3)

print()

mood=input("What kind of melody would you like to listen to?(happy/sad) ")

print()

bars_total=int(input("How many bars of melody do you want to generate? (4/8/16/32) (Recommended:16 bars)  "))

print()


user_inp_mel= md[mood].tolist()
user_inp_bass= bs[mood].tolist()

#extracting lists based upon user's mood

file_name=input("File name : ")

print()

loading_statement=["Unfolding Compositions...","Almost there...","Tuning the guitar...","Just a moment...","Sit back and relax..."]

print(random.choice(loading_statement))

print()



bars=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","a1","a2","a3","a4","a5","a6"]

bars=bars[0:bars_total]

#the length of the melody ie 8 bars

y=0

ca= NoteContainer(['C-4', 'E-4', 'G-4'])
ci= NoteContainer(['C-4','Eb-4','G-4'])
da= NoteContainer(['D-4', 'F#-4', 'A-4'])
di= NoteContainer(['D-4', 'F-4', 'A-4'])
dba= NoteContainer(['C#-4', 'G-4', 'A#-4'])
dbi= NoteContainer(['D#-4', 'F#-4', 'A#-4'])
ea= NoteContainer(['E-4', 'G#-4', 'B-4'])
ei= NoteContainer(['E-4', 'G-4', 'B-4'])
eba= NoteContainer(['Eb-4', 'G-4', 'Bb-4'])
ebi= NoteContainer(['Eb-4', 'Gb-4', 'Bb-4'])
fa= NoteContainer(['F-4', 'A-4', 'C-5'])
fi= NoteContainer(['F-4', 'Ab-4', 'C-5'])
ga= NoteContainer(['G-4', 'B-4', 'D-5'])
gi= NoteContainer(['G-4', 'Bb-4', 'D-5'])
gba= NoteContainer(['G-4', 'B-4', 'D-5'])
gbi= NoteContainer(['G-4', 'Bb-4', 'D-5'])
aa= NoteContainer(['A-4', 'C#-4', 'E-4'])
ai= NoteContainer(['A-4', 'C-4', 'E-4'])
aba= NoteContainer(['A-4', 'C#-4', 'E-4'])
abi= NoteContainer(['A-4', 'C-4', 'E-4'])
ba= NoteContainer(['B-4', 'D-4', 'F-5'])
bi= NoteContainer(['B-4', 'D-4', 'F-5'])
bba= NoteContainer(['B-4', 'D-4', 'F-5'])
bbi= NoteContainer(['B-4', 'D-4', 'F-5'])

r=NoteContainer([])

#making chords out of notes

happy_chords=[ca,di,ei,fa,ga]
sad_chords=[ai,ga,fa,ei,di]

if mood == 'happy' :
    user_inp_harm = happy_chords
if mood == 'sad' :
    user_inp_harm = sad_chords

c=Composition()
t=Track()
t2=Track()
t3=Track()

#creating tracks to save midi data

for x in bars:
    x1=random.choice(user_inp_mel)
    x2=random.choice(user_inp_mel)
    x3=random.choice(user_inp_mel)
    x4=random.choice(user_inp_mel)
    chord=random.choice(user_inp_harm)
    bass_note=random.choice(user_inp_bass)
    bass_bar=Bar()
    bass_bar.place_notes(bass_note, 1)
    bars[y]=Bar()
    bars[y] + x1
    bars[y] + x2
    bars[y] + x3
    bars[y] + x4
    t + bars[y]
    t2 + chord
    t2 + r
    t2 + r
    t2 + r
    t3 + bass_bar
    #print()
    y=y+1

#this for loop generates a single bar and keeps on generating until it genrates 8 bars of melody, chords, bass

y=0
c + t
c + t2
c +t3
t=0

#print(c)


"""import time
from progress.bar import ChargingBar
secs = [1,2,3,4,5]
bar = ChargingBar('Composing', max = len(secs))
for item in secs:
    bar.next()
    time.sleep(1)
bar.finish()
"""
#the code for prgress bars

print()

print("Your melody is ready , search ",file_name+".mid","on your computer ")

print()

midi_file_out.write_Composition(file_name + ".mid",c)

input("Press any key to exit")
