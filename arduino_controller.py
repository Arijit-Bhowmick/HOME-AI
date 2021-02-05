import pyfirmata
import json
import commands_creater
import command_performer
import pyttsx3

arduino_port = "COM3" # The port which the Arduino is using
board = pyfirmata.Arduino(arduino_port)

def init_pin(arduino_new_pin_data):

	# arduino_new_pin_data is a dict example {"3":"1"}
	## Pin number and Pin state

	arduino_states = commands_creater.arduino_previous_pin_state() # List of all the state of pins and it's number in dict format
	
	
	
	#print(f"in arduino controller --> {arduino_states}")

	for pre_pin_number in arduino_new_pin_data.keys():
    	
		#print(type(pre_pin_number))
    		
		if (pre_pin_number in arduino_states) == True:

			# Checks if the new pin is in the arduino previous pin data
			#print(f"Arduino pin data {arduino_new_pin_data}\nArduino pin state --> {arduino_states}")
			#if arduino_states[pre_pin_number] == arduino_new_pin_data[pre_pin_number]:
    		#			# if previous pin state is equals current pin state
			#	print(f"error area  {arduino_states}")
			#	print("The pin is already functioning with this command")

			#elif (arduino_states[pre_pin_number] != arduino_new_pin_data[pre_pin_number]):
    				
					# Toggle the State of the pins of the pin number

			arduino_states[pre_pin_number] = arduino_new_pin_data[pre_pin_number]
			#print(arduino_states[pre_pin_number])

			arduino_pin_controller([pre_pin_number, arduino_states[pre_pin_number]])
	
	# Forward the dictionary to write it to the text file
	#print(arduino_states)
	pyttsx3.speak("Task Successfully Performed")
	command_performer.write_arduino_pin_data(arduino_states)



def arduino_pin_controller(pin_number_and_state):
    	
	# pin_number_and_state is a list of [pin_number, pin_state]
	# The port that is used by arduino
	# it varies over operating system and available ports

	# arduino_port = "COM3" # The port which the Arduino is using

	# board = pyfirmata.Arduino(arduino_port)
	#a=[1,0,1,1,0,1,0,1,0,1,0,1,0,1,1,0,0,1,0]
	#b="01010111011001010010000001100001011100100110010100100000011000010110111001101111011011100111100101101101011011110111010101110011"

	# Write current state in pins

		
	board.digital[int(pin_number_and_state[0])].write(int(pin_number_and_state[1]))

    		


	#while True:

		#user_input = input("Please enter a sleep time as interger value : >> ")
		#user_input = int(user_input)

	## From here we can on/off a current device state

	#board.digital[int(pin_number)].write(int(pin_state))

	## other detailed works

	## Digital Pins
	
	# board.digital[int(pin_number)].write(int(pin_state))
	# board.digital[int(pin_number)].write(int(pin_state))
	# board.digital[int(pin_number)].write(int(pin_state))
	# board.digital[int(pin_number)].write(int(pin_state))
	# board.digital[int(pin_number)].write(int(pin_state))
	# board.digital[int(pin_number)].write(int(pin_state))
	# board.digital[int(pin_number)].write(int(pin_state))
	# board.digital[int(pin_number)].write(int(pin_state))
	# board.digital[int(pin_number)].write(int(pin_state))

	# board.digital[int(pin_number)].write(int(pin_state))
	# board.digital[int(pin_number)].write(int(pin_state))
	# board.digital[int(pin_number)].write(int(pin_state))
	# board.digital[int(pin_number)].write(int(pin_state))
	# board.digital[int(pin_number)].write(int(pin_state))
	# board.digital[int(pin_number)].write(int(pin_state))
	# board.digital[int(pin_number)].write(int(pin_state))
	# board.digital[int(pin_number)].write(int(pin_state))
	# board.digital[int(pin_number)].write(int(pin_state))