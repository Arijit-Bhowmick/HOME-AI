import time
import json
import pyttsx3
import speech_recognizer
import arduino_controller
import chatbot
import commands_creater


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
    
    #command = speech_recognizer.speech_2_text()
    command = "Hey Friday, turn off light"

    print(command)

    ai_name_calling_lst = commands_creater.AI_name_calling_lst() # AI Names list

    # Sample Command -> Hey Friday, turn off light
        


    for ai_call_name in ai_name_calling_lst:

        if (ai_call_name in command.upper()) == True:

            

    #if (("OK FRIDAY" in command.upper()) == True) or (("HELLO FRIDAY" in command.upper()) == True):

        #print("PLEASE PROVIDE A COMMAND TO CONTINUE\nTalk")

        #command = speech_recognizer.speech_2_text()
        #command = "on port eight"
        #command = 
        
            for saved_arduino_command in arduino_commands_names:

            
            #print(command)

            ## Arduino Command Area

                if (saved_arduino_command in command) == True:

                # return pin_number and pin_state to initilize

                    return [arduino_key_value_dict[saved_arduino_command], "arduino"] # format -> [{03:1}, "arduino"]
                else:
                    continue

## *****************************************************************

            # For bot command Action

            for saved_bot_command in bot_commands_names:

                if (saved_bot_command in command) == True:

                    return [bot_key_value_dict[saved_bot_command], "bot_system_command"] # Format -> ["exit()", "bot_system_command"]
                else:
                    continue

            
#################################################################################

            # If both of the above doesn't work then it will be
            # redirected to Chatbot, and the chatbot will result
            # the output if any.

            ## Chatbot command area


                # return command to initilize in chatbot
            command = command
            response = chatbot.chatbot_response(command)

            return [response, "chatbot"] # format -> ["response_from_chat_bot"]

        else:
            
            # return command to initilize in chatbot

            #response = chatbot.chatbot_response(command.replace(ai_call_name, "")) # Removes the First ai calling command from the string

            #return [response, "chatbot"]

            continue



            #return ["nothing", "NONE"]



        # print("Time over, thanks")

    else:
        
        return ["nothing", "NONE"]

def init_arduino_func(filter_command):

    arduino_pin_details = filter_command
    arduino_pin_data = arduino_pin_details[0] # Dictionary data

    # arduino_pin_data.keys() -> pin number
    # arduino_pin_data.values() -> pin state

    #arduino_pin_number = arduino_pin_data

# Recognizing the commands as arduino commands

    if arduino_pin_details[1] == "arduino":

        # commiting the pin state

        arduino_controller.init_pin(arduino_pin_data)


        

def chatbot_response_audio(filter_command):

    chatbot_command_details = filter_command
    command_identifier = chatbot_command_details[1]
    command = chatbot_command_details[0]

    if command_identifier == "chatbot":

        # pass the command to chatbot and it will provide a response

        #chatbot_response_text = chatbot.chatbot_response(command)
        #pyttsx3.speak(chatbot_response_text)
        pyttsx3.speak(command)

def main():

    try :


        filter_data = filter_command()

        if filter_data[1] == "arduino":

            init_arduino_func(filter_data)

        elif filter_data[1] == "chatbot":


            chatbot_response_audio(filter_data)

        else:
            print("none heard")

    except KeyboardInterrupt:

        print("Thankyou For USing ME !!!")
        exit()


if __name__ == "__main__":
    main()