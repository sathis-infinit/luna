###################################################################################################

def sound_player(sound_file):
    from playsound import playsound
    playsound(sound_file)

###################################################################################################


def find_file(name, path="."):
    import os
    for dirpath, dirname, filename in os.walk(path):
        if name in filename:
            return os.path.join(dirpath, name)

###################################################################################################

def skill_manager(skill_name,skill_parameters):

    skill_name = skill_name[0]
    skill_parameters = skill_parameters[0]
    importline = "import skill."+skill_name+" as skill"
    exec(importline)
    
    if not skill_name == None:
        runline = "skill." + skill_name + "(" +"'"+ skill_parameters + "'" + ")"
        exec(runline)


###################################################################################################

# Load JSON data
def load_json(file):
    import json
    with open(file) as bot_responses:
        return json.load(bot_responses)

###################################################################################################