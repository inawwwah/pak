import scipy.io
from scipy.io import wavfile
import os

def read_newlabfile(filename, newfile):
    ## Reading label file
    f = open(filename, "r")
    fr=f.readlines()

    for line in fr:
        if "junk" or "lab1" in line:
            fr.remove(line)

    newfile = open(newfile, "w")  
    for line in fr:
        newfile.write(line)
    newfile.close()   
    f.close()
    print("Done")

def convert_points(seconds):
     bits=seconds*samplerate
     return round(bits)

def extract_audio(wav, labfile, newfolder):
    global samplerate
    samplerate, data = wavfile.read(wav)
    sf = open(labfile, "r")
    sfr=sf.readlines()

    sfr_new=[]
    for line in sfr:
        list=[]
        list=line.split(" ")
        sfr_new.append(list)

    save_path=f'/Users/julieyiu/Downloads/pak/{newfolder}'
    for lines in sfr_new:
        filename=lines[2].replace('\n', '')
        completeName = os.path.join(save_path, filename)
        startframe=convert_points(float(lines[0]))
        endframe=convert_points(float(lines[1]))
        wavfile.write(f"{completeName}.wav", samplerate, data[startframe:endframe])

    print("Done")

#execute one by one

#read_newlabfile("4.lab", "n4.lab")
extract_audio("4.wav", "n4.lab", "4wav")

