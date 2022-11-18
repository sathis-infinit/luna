import struct
import pyaudio
import pvporcupine
import pathlib

porcupine = None
pa = None
audio_stream = None

def voice_wake():

    try: 

        parent_path = pathlib.Path(__file__).parent.resolve()
        keyfile_path = str(parent_path)+'/data/luna.ppn'
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
                print("detected")
                audio_stream.close()          
                pa.terminate()           
                return True


    except KeyboardInterrupt:
        print("\nDetected CTRL+C")
        pass             



voice_wake()