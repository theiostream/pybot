# safety.py -- by theiostream
# -- checks if an action from action.py can be executed, as there might be limitations for bot usage on yourbot.py
# Part of PyBot, (C) 2011 Matoe Productions LLC

import arr

def checkIfCanExecuteAggressive():
	
	import pybot
	
	if pybot.notAllowHarmful==0:
		return True
		
	if arr.checkIfReal(pybot.allowedHarmfulFor):
		for x in pybot.allowedHarmfulFor:
			if pybot.data[1:pybot.data.index('!')]==x:
				return True
			if pybot.data[1:pybot.data.index('!')]==pybot.owner:
				return True
				
	return False
	

def checkIfPersonIsIgnoredByBot():
	
	import pybot
	
	if arr.checkIfReal(pybot.ignoredByBot):
		for x in pybot.ignoredByBot:
			if pybot.data[1:pybot.data.index('!')]==x:
				return True
				
	return False
	
