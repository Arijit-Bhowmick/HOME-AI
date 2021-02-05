import time
import json
import pyttsx3
import speech_recognizer
import arduino_controller
import chatbot
import commands_creater
import command_performer

# Environmental Commands

# Arduino Commands Control

arduino_commands = commands_creater.Arduino_commands() # Only returns two items
arduino_commands_names = arduino_commands[0] # List of Arduino Commands
arduino_key_value_dict = arduino_commands[1] # List of Arduino Commands and Key Values 


# Chatbot Commands

bot_commands = commands_creater.Bot_commands() # Only returns three items
bot_commands_names = bot_commands[0] # List of supported bot Commands
bot_system_commands_names = bot_commands[1] # List of all system commands that the bot can perform
bot_key_value_dict = bot_commands[2] # List of Bot Commands and system_command Values 

# Load json data

#command_data = json.loads(json_command_data)

# Load Arduino commands data

#arduino_command_data = json.loads(json_arduino_command_data)

# Load Chatbot commands data

#chatbot_command_data = json.loads(json_chatbot_command_data)

#################

def filter_command():

    #while True:
    
    command = speech_recognizer.speech_2_text().upper() # For recognizing the voice to perform task
    #command = "Hey Friday, off port three".upper() #testing for aurdino
    #command = "Hey Friday, How are you".upper() # Testing for chat_bot
    #command = "Hey Friday, Open Explorer".upper()

    print(f"USER --> {command}")

    ai_name_calling_lst = commands_creater.AI_name_calling_lst() # AI Names list

    # Sample Command -> Hey Friday, on port three
        
    if command == "NONE":
        # if nothing is said to it
        #print("none command initilized")

        return ["Not Hearing", "nothing"]


    for ai_call_name in ai_name_calling_lst:

        
        if (ai_call_name.upper() in command) == True:
            print("ai_call_name",ai_call_name)

            

    #if (("OK FRIDAY" in command.upper()) == True) or (("HELLO FRIDAY" in command.upper()) == True):

        #print("PLEASE PROVIDE A COMMAND TO CONTINUE\nTalk")

        #command = speech_recognizer.speech_2_text()
        #command = "on port eight"
        #command = 
        
            for saved_arduino_command in arduino_commands_names:

            
            #print(command)

            ## Arduino Command Area

                if (saved_arduino_command.upper() in command) == True:

                # return pin_number and pin_state to initilize
                    print("Arduino command")
                    return [arduino_key_value_dict[saved_arduino_command], "arduino"] # format -> [{03:1}, "arduino"]
                else:
                    continue

## *****************************************************************

            # For bot command Action

            for saved_bot_command in bot_commands_names:

                if (saved_bot_command.upper() in command) == True:

                    #print(bot_key_value_dict[saved_bot_command])

                    return [bot_key_value_dict[saved_bot_command], "bot_system_command"] # Format -> ["exit()", "bot_system_command"]
                else:
                    continue

            
#################################################################################

            # If both of the above doesn't work then it will be
            # redirected to Chatbot, and the chatbot will result
            # the output if any.

            ## Chatbot command area


                # return command to initilize in chatbot
            #command = command.replace(ai_call_name, "") # Removes the AI Calling Name
            response = chatbot.chatbot_response(command.replace(ai_call_name, "")) # Removes the First ai calling command from the string

            return [response, "chatbot"] # format -> ["response_from_chat_bot", "chatbot"]

        else:
            
            # return command to initilize in chatbot

            #response = chatbot.chatbot_response(command.replace(ai_call_name, "")) # Removes the First ai calling command from the string

            #return [response, "chatbot"]

            continue



            #return ["nothing", "NONE"]



        # print("Time over, thanks")

    else:
        
        return ["Not Hearing", "nothing"]



def main():

    try :
        while True:
            # The Data that are to be returned
            # Example:
            # For Arduino it Would be : [{03:1}, "arduino"]
            # For bot_for system functions : ["exit()", "bot_system_command"]
            # For Chat_bot it would be : ["response_from_chat_bot", "chatbot"]
            # For not hearing it would be : ["Not Hearing", "nothing"]
            # 
            command_data = filter_command()

            if command_data[1] == "arduino":

                command_performer.init_arduino_func(command_data)

            elif command_data[1] == "bot_system_command":

                command_performer.bot_system_command_performer(command_data)


            elif command_data[1] == "chatbot":

                command_performer.chatbot_response_audio(command_data)

            elif command_data[1] == "nothing":

                continue
            
            else:
                print("none heard")
            #exit()
    except KeyboardInterrupt:

        print("Thankyou For USing ME !!!")
        exit()


if __name__ == "__main__":
    main()