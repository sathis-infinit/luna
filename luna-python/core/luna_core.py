###################################################################################################

def luna_wake():

    import struct
    import pyaudio
    import pvporcupine
    import pathlib
    import core.luna_utils as lunautils

    porcupine = None
    pa = None
    audio_stream = None

    try:

        # parent_path = pathlib.Path(__file__).parent.resolve()
        # keyfile_path = str(parent_path)+'/data/voicedata/luna.ppn'
        keyfile_path = lunautils.find_file("luna.ppn")
        porcupine = pvporcupine.create(access_key='S2vwjyUTZTYjvnPzyg9RF2SoLmk1tSKuqL5TB2FcvFzu935a2GDc6Q==',
                                       keywords=["luna"],
                                       keyword_paths=[keyfile_path])

        pa = pyaudio.PyAudio()

        audio_stream = pa.open(
            rate=porcupine.sample_rate,
            channels=1,
            format=pyaudio.paInt16,
            input=True,
            frames_per_buffer=porcupine.frame_length)

        while True:

            pcm = audio_stream.read(porcupine.frame_length)
            pcm = struct.unpack_from("h" * porcupine.frame_length, pcm)

            keyword_index = porcupine.process(pcm)

            if keyword_index >= 0:
                audio_stream.close()
                pa.terminate()
                print("detected")
                return True

    except KeyboardInterrupt:
        print("\nDetected CTRL+C   EXITING ...   ")
        exit()

###################################################################################################

def luna_listern():

    import speech_recognition as sr
    import core.luna_utils as lunautils

    r = sr.Recognizer()

    with sr.Microphone() as source:

        r.adjust_for_ambient_noise(source)
        r.dynamic_energy_threshold = True
        r.pause_threshold = 0.8
        print('Listerning...')
        lunautils.sound_player(lunautils.find_file("speechon.mp3"))
        
        
        audio = r.listen(source)

    try:
        print('Thinking...')
        return r.recognize_google(audio, language='en-in')

    except Exception as e:
        print(e)
        print('Something Went Wrong...')
        return None

###################################################################################################

def luna_speak(speech_content):

    import pyttsx3

    engine = pyttsx3.init()
    voice = engine.getProperty('voices')
    engine.setProperty('voice', voice[28].id)

    print(speech_content)
    engine.say(speech_content)
    engine.runAndWait() 

###################################################################################################

def luna_think(input_string):

    import core.luna_utils as luna_utils
    import re
    import random
    # Store JSON data
    response_data = luna_utils.load_json( "/Users/sathishkumar/Documents/code/python/workspaces/luna/v2_2/core/luna_brain.json")
    # switch_intent , possible_tags , possible_slots , bot_response , required_tags , run_skill , skill_parameter

    print(input_string)
    if not (input_string == None):
        print(input_string)
        input_words = re.split(r'\s+|[,;?!.-]\s*', input_string.lower())

        score_list = []
        parameter_list = []
        slot_list = []


        for response in response_data:
            required_score = 0
            possible_score = 0

            required_tags = response["required_tags"]
            possible_tags = response["possible_tags"]

            switch_intent = response["switch_intent"]

            if input_string in possible_tags:
                possible_score += 1

            if required_tags:
                for word in input_words:
                    if word in required_tags:
                        required_score = + 1

            if required_score == len(required_tags):
                for word in input_words:
                    if word in possible_tags:
                        possible_score += 1

            score_list.append(possible_score+required_score)
    elif (input_string == None):
        return None

    best_response = max(score_list)
    response_index = score_list.index(best_response)

    if best_response != 0:

        # switch_intent = response_data[response_index]["switch_intent"]
        # possible_tags = response_data[response_index]["possible_tags"]
        possible_slots = response_data[response_index]["possible_slots"]
        bot_response = response_data[response_index]["bot_response"]
        # required_tags = response_data[response_index]["required_tags"]
        run_skill = response_data[response_index]["run_skill"]
        skill_parameter = response_data[response_index]["skill_parameter"]

        if run_skill:

            # if possible_slots:
            #     for word in input_words:
            #         if word in possible_slots:
            #             slot_list.append(word)

            # luna_utils.skill_manager(run_skill, skill_parameter , possible_slots)
            luna_utils.skill_manager(run_skill, skill_parameter)
        else:
            bot_response_length = len(
                response_data[response_index]["bot_response"])
            if bot_response_length != 0:

                list_count = len(response_data[response_index]["bot_response"])
                random_item = random.randrange(list_count)

                luna_speak(
                    response_data[response_index]["bot_response"][random_item])
            else:
                luna_speak("Not sure")

###################################################################################################
