
def skill_datetime(param="datetime",*args):

    import core.luna_core as coremodules
    import core.luna_utils as lunautils    
    from datetime import datetime

    now = datetime.now()

    if param == "raw":
        coremodules.luna_speak(datetime.now())

    if param == "datetime" and format == "default":

        hour = now.strftime("%I")
        minute = now.strftime("%M")
        day_of_week = now.strftime("%A")
        month = now.strftime("%B")
        year = now.strftime("%Y")
        coremodules.luna_speak("It is " + hour+ " " +minute + " in the " + day_of_week + " of " + month + " " + year)

    if param == "time":
        
        coremodules.luna_speak("It is " + now.strftime("%I:%M %p"))

    if param == "date":
        
        day_of_week = now.strftime("%A")
        month = now.strftime("%B")
        year = now.strftime("%Y")
        coremodules.luna_speak("Today is " + day_of_week + " of " + month + " " + year)
    

