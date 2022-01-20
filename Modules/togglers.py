import __main__ as main

def toggleDateStamp():
	main.globals['youWantDateStamp'] = False if main.globals['youWantDateStamp'] == True else True # Ternary Operator in Python

def toggleForcedOnePerDay():
	main.globals['oneRecPerDayForced'] = False if main.globals['oneRecPerDayForced'] == True else True
