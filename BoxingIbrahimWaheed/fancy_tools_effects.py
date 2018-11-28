import pyttsx3 #https://pyttsx3.readthedocs.io/en/latest/ for the TextToSpeech Effect
# maybe instead of pyttsx3 could have use gttsx a google cloud base text to speech'
# google one require internet!
# the below import is for the fancy typo effect!
import wikipedia # will allow the bot to search on wikipedia
import sys #importing system
from time import sleep
# Below import is for the news api




# importing audio module will need for text to speech week4
import vlc








# The text to speech module is using a third party module from Pyttx3
# I just created a function which can be used by the team
# The problem with the pyttsx3 is that it relies on the system native text to speech voices
# Therefore voices will be different on different os -
# This function is good for cmd/GUI desktop base apps
# It might not work with facebook/twitter API sevices
# All comments must be transfer to git repo
def tts_typoEffect(text):
    # the below is the fancy text typo effect
    for char in text:#
        sleep(0.01)#for testing put 0.01
        sys.stdout.write(char)
        sys.stdout.flush()
    print("\n")
    # below is the tts= test to speech effect
    speech_engine = pyttsx3.init()#invoking the pyttsx engine
    voice = speech_engine.getProperty('voices')
    speech_engine.setProperty('voice', voice[2].id)
    speech_engine.say(text)# passing the parameter text ( which would be used on the various chatbots convos)
    speech_engine.runAndWait()


def bg_tts(text):
    '''To play sound but no typo effect'''
    speech_engine = pyttsx3.init()  # invoking the pyttsx engine
    voice = speech_engine.getProperty('voices')
    speech_engine.setProperty('voice', voice[2].id)
    speech_engine.say(text)  # passing the parameter text ( which would be used on the various chatbot)
    speech_engine.runAndWait()

# fix for the TypeError: bg_tts() takes 1 positional argument but 2 were given
#https://wikipedia.readthedocs.io/en/latest/code.html THE BEST API ON THE PLANET
def WikiSearch(text):
    '''Will allow the bot to grab data from wikipedia and say it to the user!'''
    try:
     tts_typoEffect(wikipedia.summary(text,sentences=1))
    except wikipedia.DisambiguationError:
        tts_typoEffect("Not found !")
    #might have to create a force string for individual topic



### Any more function effect will be below


def PlaySportRadio():
    '''This will play sport radio'''

    # the above link really helped me understand how the mediaplay works!

    radio = vlc.MediaPlayer('talksport2.m3u')# This used the vlc mediaplayer -
    #mp3 that is listed
    while True:
        radio.play()





