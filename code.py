import scipy.io
from scipy.io import wavfile
import os

def read_newlabfile(filename, newfile):
    save_path=f'/Users/julieyiu/pak/pak/labfiles/old'
    ## Reading label file
    completeName = os.path.join(save_path, filename)
    f = open(completeName, "r")
    fr=f.readlines()

    for line in fr:
        if "junk" or "lab1" in line:
            fr.remove(line)

    save_path2=f'/Users/julieyiu/pak/pak/labfiles/new'
    completeName2=os.path.join(save_path2, newfile)
    newfile = open(completeName2, "w")  
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
    save_pathWav="/Users/julieyiu/pak/pak/audioraw/wav"
    completeNameWav=os.path.join(save_pathWav, wav)
    samplerate, data = wavfile.read(completeNameWav)

    save_pathLab="/Users/julieyiu/pak/pak/labfiles/new"
    completeNameLab=os.path.join(save_pathLab, labfile)
    sf = open(completeNameLab, "r")
    sfr=sf.readlines()

    sfr_new=[]
    for line in sfr:
        list=[]
        list=line.split(" ")
        sfr_new.append(list)

    save_path=f'/Users/julieyiu/pak/pak/{newfolder}'
    for lines in sfr_new:
        filename=lines[2].replace('\n', '')
        completeName = os.path.join(save_path, filename)
        startframe=convert_points(float(lines[0]))
        endframe=convert_points(float(lines[1]))
        wavfile.write(f"{completeName}.wav", samplerate, data[startframe:endframe])

    print("Done")

#execute one by one
#read_newlabfile("13.lab", "n13.lab")
extract_audio("13.wav", "n13.lab", "13wav")

