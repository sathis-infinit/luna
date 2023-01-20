from posixpath import split
import time
import datetime
from speakcontent import speak_content
from getcommand import get_command
from duckduckgo import ddgs
from telegramcall import telegram_call
from getweather import get_weather
# from switchcontrol import switchcontrol


contacts = {'yamuna':'1827945413'}
 
def command_control(command):
    
    if command == 'shutdown' or command == 'exit' or command == 'quit' or command == 'close' or command == 'shut down':
        speak_content('Shutdown Initiated')
        import time
        time.sleep(2)
        speak_content('please confirm , say yes or no')
        command = get_command()
        if command == 'yes':
            speak_content('All Systems are shutting down')
            print('All systems are shutting down')
            import time
            time.sleep(3)
            speak_content('luna is now offline !')
            print('luna is now offline !')
            exit()

    if command == 'hello' or command == 'hi' or command == 'hai' or command == 'hey' or command == 'hi there':
        speak_content('Hi , how can I help you ?')
        print('Hello')
        command = get_command()
        # command_control(command)


    if command == 'time' or command == 'what time is it' or command == 'what is the time' or command == 'tell me the time':
        import time
        t = time.strftime(" it is %I:%M %p")
        print(t)
        speak_content(t)  


    if command == 'date' or command == 'what date is it' or command == 'what is the date' or command == 'tell me the date': 
        
        now = datetime.datetime.now()
        print(now.strftime("%d/%m/%Y"))
        speak_content(now.strftime(" Today's Date is %d/%m/%Y"))


    if command == 'what is going on' or command == "what's up" or command == 'what is happening' or command == 'WhatsApp' or command == 'what is up':

        speak_content('Nothing Much ! , looking forward to your next command !')
        print('Nothing Much ! , looking forward to your next command !')



    if command == 'who are you' or command == 'name' or command == 'your name':
        speak_content('Central A.I of raven system, Name is Luna')
        print('I am luna , Central a i of raven system.')

    if command == 'who made you' or command == 'who created you' or command == 'who is your creator':
        speak_content('I am created by Satheesh !,some codes are from open source!.')
        print('I am created by Satheesh !') 

    if command == 'what are you doing' or command == 'what are you doing now' or command == 'what doing':
        speak_content('I am listening to your command')
        print('I am listening to your command')

    if command =='what is the weather' or command == 'tell me the weather' or command =='weather':
        speak_content('for which location ?')
        place = get_command()
        forecast = get_weather(place)
        speak_content("forecast for "+place+" is "+forecast)    

    # if command == 'turn on light':
    #     switchcontrol()

    # if 'call' in command:
    #     # speak_content('Who do you want to call ?')
    #     # command = get_command()
    #     # if command !=None:

    #         command = command.lower()
    #         id = command.split(' ')[1]

    #         speak_content('Calling '+id)
    #         print('Calling '+id)

    #         telegram_call(contacts[id])  
    #         import time
    #         time.sleep(10)

    elif(command != None):
        desc = ddgs(command)
        speak_content(desc[0]['body'])
        speak_content("do you want to hear next result ?")
        yn = get_command()
        if (yn=='okay sure'):
            speak_content(desc[1]['body'])
        else:
            pass    
 
    elif(command == None):
        print("Going Sleep Mode !")
    else:
        pass    

        