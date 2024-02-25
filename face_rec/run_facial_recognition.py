"""
Main Face Recognition Class File
"""

import face_recognition
import os
from colorama import init, Fore, Style
import sys

# import class
from FaceRec import FaceRec


def user_io():
	"""
	Manages user input and output.
	"""
	while True:
		user_input = input(
			"Enter \n'1' to Play / Pause, \n'2' to start a blank file, \n'3' to export raw data to CSV, JSON, HTML\n'4' Export Nicely to CSV, JSON, HTML \n'5' to Enable/Disable Idle Detection\n'6' to Exit: \n\n\n"
		)

		try:
			if user_input == "0":
				app.print_db()
			elif user_input == "1":
				app.pause_or_resume()
				if app.get_record() == True:
					print("Recording ...")
				else:
					print("Paused")
			elif user_input == "2":
				app.start_fresh()
			elif user_input == "3":
				app.export_raw()
			elif user_input == "4":
				app.export_collaborative_data()
			elif user_input == "5":
				app.flip_idle_detection()
				print(
					"Idle detection is",
					(
						"Enabled. If you cursor doesnt move for 5 mins, you are idle. "
						if app.get_idle_detection()
						else "Disabled"
					),
				)
			elif user_input == "6":
				# End the application
				app.finish = True
				break
			else:
				print("Invalid input. Please try again.")
		except Exception as e:
			print(e)
			print(e.with_traceback())
	app.cleanup()


if __name__ == "__main__":
	# initialize colorama
	init()

	# create an instance of the FaceRec class
	face_rec = FaceRec()

	# make a simple menu for the user
	print("Welcome to the facial recognition program (Local Edition)")
	print(Fore.BLUE
	      + Style.BRIGHT
	      + """
			 __    __     _                            _           __                    __           
			/ / /\ \ \___| | ___ ___  _ __ ___   ___  | |_ ___    / _| __ _  ___ ___    /__\ ___  ___ 
			\ \/  \/ / _ \ |/ __/ _ \| '_ ` _ \ / _ \ | __/ _ \  | |_ / _` |/ __/ _ \  / \/// _ \/ __|
			 \  /\  /  __/ | (_| (_) | | | | | |  __/ | || (_) | |  _| (_| | (_|  __/ / _  \  __/ (__ 
			  \/  \/ \___|_|\___\___/|_| |_| |_|\___|  \__\___/  |_|  \__,_|\___\___| \/ \_/\___|\___|
				""")

	# load the known face images
	face_rec.load_known_faces()
	print("Known Face images have been loaded from the images/known_faces directory...")
	print("Please select an option from the following list")
	print("1. Create Encodings for all images in the known_faces directory")
	print("2. Run facial recognition on all images in the test directory")
	print("3. Run facial recognition on a single image from absolute path")
	print("4. Exit")
