
import os
import aiml

def chatbot_response(command):

	BRAIN_FILE="brain_dump/brain.dump"

	k = aiml.Kernel()

	# To increase the startup speed of the bot it is
	# possible to save the parsed aiml files as a
	# dump. This code checks if a dump exists and
	# otherwise loads the aiml from the xml files
	# and saves the brain dump.
	if os.path.exists(BRAIN_FILE):
		print("Loading from brain file: " + BRAIN_FILE)
		k.loadBrain(BRAIN_FILE)
	else:
		print("Parsing aiml files")
		k.bootstrap(learnFiles="xml_file/std-startup.aiml", commands="load aiml b")
		print("Saving brain file: " + BRAIN_FILE)
		k.saveBrain(BRAIN_FILE)

	# Endless loop which passes the input to the bot and prints
	# its response
	#while True:
	try:
		#input_text = input("USER --> ")
		input_text = command

		if (("exit" in input_text.lower()) == True) or (("close" in input_text.lower()) == True):
    			return ("break")
		else:
			response = k.respond(input_text)
			print("F.R.I.D.A.Y  --> ", response)
			
			return response

	except KeyboardInterrupt:
		print("EXIT\nThankyou for using me")
		exit()