#import library

import speech_recognition as sr
import json

# Initialize recognizer class (for recognizing the speech)

r = sr.Recognizer()

def speech_2_text():
# Reading Microphone as source
# listening the speech and store in audio_text variable
    
    with sr.Microphone() as source:
        #print("PLEASE PROVIDE A COMMAND TO CONTINUE\nTalk")
        audio_text = r.listen(source)
        #print("Time over, thanks")
    # recoginize_() method will throw a request error if the API is unreachable, hence using exception handling
        
        try:
            # using google speech recognition
            command = r.recognize_google(audio_text)

            print("Text: "+command)
            return (command)
        except:
            print("Sorry, I did not get that")
            return ("NONE")

