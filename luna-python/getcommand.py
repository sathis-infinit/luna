import speech_recognition as sr
from soundplayer import sound_player
from findfile import find_file

def get_command():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        r.dynamic_energy_threshold = True 
        r.pause_threshold = 0.6
        print('Listerning...')
        speechon_sound = find_file('speechon.mp3')
        sound_player(speechon_sound)

        audio = r.listen(source)

    try:
        print('Thinking...')
        query = r.recognize_google(audio, language='en-in')
        print(f'You Said : {query}\n')
        return query

    except Exception as e:
        print(e)
        print('Something Went Wrong...')
        return None 

