						IoT Group 12

################################################################################################

Script Folder:  Contains all PDDL files and Plans 
	csv_ai_planner_1.py - Subscriber file 
	ai_planner_2.py - API for AI planner 
	init.py - reset all actuators of RPi


AI Planning and MQTT Branch: Publisher Subscriber &  AI planning generator
	publisher.py - Exected from Rpi
	Subscriber.py - Exected on laptop 1

Dashboard Branch: Smart healthcare Unit GUI and CSV writer
	csv_writer.py - Executed on laptop 2
	dashboard.py -  Executed on laptop 2 for Main UI screen

Note: Change path of the CSV writer as per the new path of the csv file in a different machine

################################################################################################



