import pyfirmata
import json

def init_pin(arduino_new_pin_data):


	## Pin number and Pin state

	arduino_states = json.loads(open("current_arduino_state.json", "r").read())
	
	for pin_number in arduino_new_pin_data.keys():
    		
		arduino_states[pin_number] = arduino_new_pin_data[pin_number]

	write_arduino_state_data = open("current_arduino_state.json", "w")
	write_arduino_state_data.write(arduino_states)
	write_arduino_state_data.close()



	# The port that is used by arduino
	# it varies over operating system and available ports

	arduino_port = "COM3" # Here windows port is using

	board = pyfirmata.Arduino(arduino_port)
	#a=[1,0,1,1,0,1,0,1,0,1,0,1,0,1,1,0,0,1,0]
	#b="01010111011001010010000001100001011100100110010100100000011000010110111001101111011011100111100101101101011011110111010101110011"


    		


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


# Write current state in pins

	for pin_num in arduino_states.keys():
		
		board.digital[int(pin_num)].write(int(arduino_states[pin_num]))