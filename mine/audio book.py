import pyttsx3
from gtts import gTTS
import os

te="hi how are you"
language= 'en'
out=pyttsx3.init()
# out=gTTS(text=te,lang=language,slow=False)
out.say(te)
out.runAndWait()
