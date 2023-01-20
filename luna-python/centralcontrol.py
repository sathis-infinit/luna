from voicewake import voice_wake
from getcommand import get_command
from commandcontrol import command_control
from findfile import find_file
from soundplayer import sound_player

def central_control():
    wake_check = voice_wake()
    if wake_check == True:
        active() 
        central_control()

def active():
        command = get_command()
        print('Command: ',command)
        command_control(command)
        command_check(command)

def command_check(command):
    speechoff_sound = find_file('speechoff.mp3')
    if command == None:
        sound_player(speechoff_sound)
        central_control()
    else:
        active()    
 
central_control()
