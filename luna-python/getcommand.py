import speech_recognition as sr

def get_command():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 0.5
        print('Listerning...')

        audio = r.listen(source)

    try:
        print('Thinking...')
        query = r.recognize_google(audio, language='en-in')
        print(f'You Said : {query}\n')
        return query

    except Exception as e:
        print(e)
        print('Try Again...')
        return None

