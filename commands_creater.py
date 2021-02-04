def Arduino_commands():

# Arduino Commands

    arduino_commands = open("commands_data/Arduino_commands.txt", "r").readlines()
    arduino_command_names = []
    arduino_cmd_key_and_value = {} # Dictionary

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

            arduino_cmd_data_unrefined_1 = ard_comd.replace("\n","").split(" > ") # [on port three][03 : 1]
            arduino_command_names += [arduino_cmd_data_unrefined_1[0]] # ["on port three"]

            arduino_cmd_key_and_value = arduino_cmd_data_unrefined_1[1].split(" : ") # [03][1]
            arduino_cmd_key = arduino_cmd_key_and_value[0] # 03
            arduino_cmd_value = arduino_cmd_key_and_value[1] # 1


            # Create Dictionary

            arduino_cmd_key_and_value.update({arduino_cmd_data_unrefined_1[0]:{arduino_cmd_key:arduino_cmd_value}}) # {{"on port three":{03:1}}}

    return [arduino_command_names, arduino_cmd_key_and_value]

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

def AI_name_calling_lst():

    # List of supported name calling names for the AI

    ai_name_calling_lst = open("commands_data/ai_calling_data.txt", "r").readlines()
    ai_name_list = []
    for ai_calling_name in ai_name_calling_lst:

        if ai_calling_name[0] == "#":
            continue

        elif ai_calling_name[0] != "#":

            ai_name_list += [ai_calling_name.replace("\n", "")]

    return ai_calling_name # list of all calling names for the ai