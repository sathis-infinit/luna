

def central_control():

    import core.core_modules as lunacore

    wake_check = lunacore.luna_wake()
    if wake_check == True:
        active()
        central_control()


def active():

    import core.core_modules as lunacore

    command = lunacore.luna_listern()
    print('Command: ', command)
    lunacore.luna_think(command)
    command_check(command)


def command_check(command):
    import core.core_modules as lunacore
    import core.luna_utils as lunautils

    if command == None:
        # sound_player(find_file('speechoff.mp3'))
        lunautils.sound_player(lunautils.find_file("speechoff.mp3"))
        central_control()
    else:
        active()

central_control()
