# Q3. Install an external module and use it to perform an operation of your interest.  
# Whether we want to create a virtual assistant or simply make our program more engaging, pyttsx3 is a library used for converting text into speech. This offline tool offers flexibility with male and female voice options and different TTS engines.
# pip install pyttsx3

import pyttsx3
engine = pyttsx3.init()
engine.say("I will speak the text. This is Text to speech converter.")
engine.runAndWait()