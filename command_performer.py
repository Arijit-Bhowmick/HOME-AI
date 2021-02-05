import os
import arduino_controller
import pyttsx3

def write_arduino_pin_data(arduino_pin_data):

    # Writes the Data of pin numbers and it's state to arduino_previous_pin_state.txt

    arduino_pin_data_dict_to_str = str(arduino_pin_data).replace("{'", "").replace("'}","").replace("': '", " : ").replace("', '", "\n")
    #print(arduino_pin_data_dict_to_str)
    # Write the new data to the text file

    arduino_pre_pin_state = open("commands_data/arduino_previous_state.txt", "w")
    arduino_pre_pin_state.write(arduino_pin_data_dict_to_str)
    #print(arduino_pin_data_dict_to_str)
    arduino_pre_pin_state.close()



def init_arduino_func(arduino_command_data):
    
    # Identify if the data belongs to arduino
    # if it is for arduino then
    # it initiate the arduino to perform the function

    arduino_pin_details = arduino_command_data
    command_identifier = arduino_pin_details[1]

    if command_identifier == "arduino":
        arduino_pin_data = arduino_pin_details[0] # Dictionary data for pin state setup

    # arduino_pin_data.keys() -> pin number
    # arduino_pin_data.values() -> pin state

    #arduino_pin_number = arduino_pin_data

# Recognizing the commands as arduino commands


        # commiting the pin state
        # process the dictionary data
        # Example pin_dic = {"3": "1"}
        print(arduino_pin_data)

        arduino_controller.init_pin(arduino_pin_data)

def chatbot_response_audio(chatbot_command_data):

    chatbot_command_details = chatbot_command_data # list Example -> ["response_from_chat_bot", "chatbot"]
    command_identifier = chatbot_command_details[1]

    if command_identifier == "chatbot":
    
        chat_bot_reply = chatbot_command_details[0] # Reply from Chat_Bot

    

        # pass the command to chatbot and it will provide a response

        #chatbot_response_text = chatbot.chatbot_response(command)
        #pyttsx3.speak(chatbot_response_text)
        print(chat_bot_reply)

        # Convert the Text to Speech
        # So that it seems to be that
        # the chatbot is speaking

        pyttsx3.speak(chat_bot_reply)

def bot_system_command_performer(bot_system_command_data):

    bot_system_command_details = bot_system_command_data # list Example -> ["exit()", "bot_system_command"]
    command_identifier = bot_system_command_details[1]

    if command_identifier == "bot_system_command":

        # System commands can easily set in the bot_commands.txt file
        # For Linux or Windows systems of the choice
        print("Bot System Command Successfully Performed")
        os.system(bot_system_command_details[0]) # perform System commands