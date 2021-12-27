from gtts import gTTS
from playsound import playsound


# Get Input from the user
name = str(input("What's your name? "))
# Format text
text = f"Hello, {name}!______This is a text to speech test____This is Google translate voice over______Goodbye"
# Turn text to speech and save
tts = gTTS(text)
tts.save('test.mp3')
# Play Sound
playsound('test.mp3')
