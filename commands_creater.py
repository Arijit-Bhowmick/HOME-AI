def Arduino_commands():

# Arduino Commands

    arduino_commands = open("commands_data/Arduino_commands.txt", "r").readlines()
    arduino_command_names = []
    arduino_cmd_key_and_value_dict = {} # Dictionary

    for ard_comd in arduino_commands:
        # Example List
        # 
        #   [on port three][03 : 1]
        #  
        # 
        #
        if ard_comd[0] == "#":

            continue


        elif ard_comd[0] != "#":

            arduino_cmd_data_unrefined_1 = ard_comd.replace("\n","").split(" > ") # ["on port three"]["3 : 1"]
            arduino_command_names += [arduino_cmd_data_unrefined_1[0]] # ["on port three"]

            arduino_cmd_key_and_value = arduino_cmd_data_unrefined_1[1].split(" : ") # ["3"]["1"]
            arduino_cmd_key = arduino_cmd_key_and_value[0] # "3"
            arduino_cmd_value = arduino_cmd_key_and_value[1] # "1"


            # Create Dictionary
            print()
            arduino_cmd_key_and_value_dict.update({arduino_cmd_data_unrefined_1[0]:{arduino_cmd_key:arduino_cmd_value}}) # {{"on port three":{"3":"1"}}}

    return [arduino_command_names, arduino_cmd_key_and_value_dict]

def Bot_commands():
    
# bot Commands

    bot_commands = open("commands_data/bot_commands.txt", "r").readlines()
    bot_command_names = []
    bot_system_command = []
    bot_cmd_key_and_value = {} # Dictionary

    for bot_comd in bot_commands:
        # Example List
        # 
        # Shutdown yourself : exit()  
        #  
        # 
        #
        if bot_comd[0] == "#":
            continue

        elif bot_comd[0] != "#":

            bot_cmd_data_unrefined_1 = bot_comd.replace("\n","").split(" : ") # ["Shutdown yourself"],["exit()"]
            bot_command_names += [bot_cmd_data_unrefined_1[0]] # ["Shutdown yourself"]

            # System commands list 
            bot_system_command += bot_cmd_data_unrefined_1[1] # ["exit()"]


            # Create Dictionary
            
            bot_cmd_key_and_value.update({bot_cmd_data_unrefined_1[0]:bot_cmd_data_unrefined_1[1]}) # {"Shutdown yourself":"exit()"}

    return [bot_command_names, bot_system_command, bot_cmd_key_and_value]

def arduino_previous_pin_state():

    # List of all pin states of arduino

    arduino_pre_pin_state = open("commands_data/arduino_previous_pin_state.txt", "r").readlines()
    
    arduino_pin_state_dict = {}

    for pin_state in arduino_pre_pin_state:

        if pin_state[0] == "#":
            continue

        elif pin_state[0] != "#":

            # Example data
            # "3 : 0" --> String Value

            pin_num_and_state = pin_state.replace("\n", "").split(" : ") # result -> ["3", "0"]

            arduino_pin_state_dict.update({pin_num_and_state[0]:pin_num_and_state[1]}) # {"3":"0"}
    
    # Return the dictionary of pin number and it's state
    #print(f"readed from file -> {arduino_pin_state_dict}")
    return arduino_pin_state_dict # Dictionary {"key":"value"}

def ai_name_parse():

    # Read the Name of the AI that you want to use in this project

    ai_name_list = open("commands_data/ai_name.txt", "r").readlines()
    ai_name_line_counter = 0
    for ai_name_identifier in ai_name_list:

        ai_name_line_counter += 1 # Count the unwanted lines from the ai_name.txt

        if ai_name_identifier.startswith("ai_name"):


            # if the line start sith ai_name then only 
            # the AI name is accepted
            #
            # Format -> "ai_name = F.R.I.D.A.Y"

            ai_name = ai_name_identifier.replace("\n", "").split(" = ")
            return(ai_name[1]) # Return : "F.R.I.D.A.Y"

        else:

            if ai_name_line_counter == len(ai_name_list):

                # If no supported ai_name variable is setup
                # the it will return "AI" as the name of AI

                return("AI") # If "AI" as the name of the AI

            else:

                continue

def AI_name_calling_lst():

    # List of supported name calling names for the AI

    ai_name_calling_lst = open("commands_data/ai_calling_data.txt", "r").readlines()
    ai_name_list = []
    for ai_calling_name in ai_name_calling_lst:

        if ai_calling_name[0] == "#":
            continue

        elif ai_calling_name[0] != "#":

            ai_name_list += [ai_calling_name.replace("\n", "")]
#    print(ai_name_list)

    return ai_name_list # list of all calling names for the ai


def banner():

    # The banner that is to be used in the Project

    print("""
██╗  ██╗ ██████╗ ███╗   ███╗███████╗               █████╗ ██╗
██║  ██║██╔═══██╗████╗ ████║██╔════╝              ██╔══██╗██║
███████║██║   ██║██╔████╔██║█████╗      █████╗    ███████║██║
██╔══██║██║   ██║██║╚██╔╝██║██╔══╝      ╚════╝    ██╔══██║██║
██║  ██║╚██████╔╝██║ ╚═╝ ██║███████╗              ██║  ██║██║
╚═╝  ╚═╝ ╚═════╝ ╚═╝     ╚═╝╚══════╝              ╚═╝  ╚═╝╚═╝

Project is available on : https://github.com/Arijit-Bhowmick/HOME-AI

- BY

ARIJIT BHOWMICK [https://github.com/Arijit-Bhowmick]
MADHAV BHARGAVA [https://github.com/madhavbhargava]
VIDHI PATEL     [https://github.com/VidhiPattel]
OSHEEN RAWAT    [https://github.com/osheen-rawat]
PRATYUSHA GIRI  [https://github.com/2002pratyusha]
    
    """)