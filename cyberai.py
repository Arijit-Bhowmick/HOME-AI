import time
import json
import pyttsx3
import speech_recognizer
import arduino_controller
import chatbot


# Environmental Commands

json_command_data_open = open("environmental_commands.json", "r")
json_command_data = json_command_data_open.read()
json_command_data_open.close()

# Arduino Commands

json_command_data_open = open("environmental_arduino_commands.json", "r")
json_arduino_command_data = json_command_data_open.read()
json_command_data_open.close()

# Chatbot Commands

json_command_data_open = open("environmental_chatbot_commands.json", "r")
json_chatbot_command_data = json_command_data_open.read()
json_command_data_open.close()

# Load json data

command_data = json.loads(json_command_data)

# Load Arduino commands data

arduino_command_data = json.loads(json_arduino_command_data)

# Load Chatbot commands data

chatbot_command_data = json.loads(json_chatbot_command_data)

#################

def filter_command():

    #while True:
    
    #command = speech_recognizer.speech_2_text()
    command = "hello Friday"

    print(command)

    if (("OK FRIDAY" in command.upper()) == True) or (("HELLO FRIDAY" in command.upper()) == True):

        print("PLEASE PROVIDE A COMMAND TO CONTINUE\nTalk")

        command = speech_recognizer.speech_2_text()
        command = "on port eight"
        #command = "off port eight"
        if (command in command_data) == True:

            
            print(command)

            ## Arduino Command Area

            if (command in arduino_command_data) == True:

                # return pin_number and pin_state to initilize

                return [arduino_command_data[command], "arduino"]

## *****************************************************************


            

            ## Chatbot command area

            else:

                # return command to initilize in chatbot

                response = chatbot.chatbot_response(command)

                return [response, "chatbot"]

        else:
            
            # return command to initilize in chatbot

            response = chatbot.chatbot_response(command)

            return [response, "chatbot"]



            #return ["nothing", "NONE"]



        print("Time over, thanks")

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