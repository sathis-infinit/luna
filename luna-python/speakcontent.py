import pyttsx3;

def speak_content(speech_content):
    engine = pyttsx3.init();
    voice = engine.getProperty('voices')
    engine.setProperty('voice', voice[28].id);
    engine.say(speech_content);
    engine.runAndWait() ;






# import os
# import pathlib
# from gtts import gTTS 
# from playsound import playsound 

# def speak_content(speech_content):
#     parent_path = pathlib.Path(__file__).parent.resolve()
#     speech_file_path = str(parent_path)+'/temp/speechaudio.mp3'
#     speechaudio = gTTS(text = speech_content,lang = 'en') 
#     speechaudio.save(speech_file_path) 
#     playsound(speech_file_path)
#     os.remove(speech_file_path)

# speak_content('Welcome !')     
