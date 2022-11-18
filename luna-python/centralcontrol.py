from voicewake import voice_wake
from getcommand import get_command
from commandcontrol import command_control
from findfile import find_file
from soundplayer import sound_player

def central_control():
    speechon_sound = find_file('speechon.mp3')
    speechoff_sound = find_file('speechoff.mp3')
    wake_check = voice_wake()
    if wake_check == True:
        active() 
        central_control()

def active():
        speechon_sound = find_file('speechon.mp3')
        speechoff_sound = find_file('speechoff.mp3')

        sound_player(speechon_sound)
        print("Wake up")
        command = get_command()
        print('Command: ',command)
        command_control(command)
        command_check(command)

def command_check(command):
    speechon_sound = find_file('speechon.mp3')
    speechoff_sound = find_file('speechoff.mp3')
    if command == None:
        sound_player(speechoff_sound)
        central_control()
    else:
        active()    

central_control()
