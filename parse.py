# parse.py -- by theiostream
# -- gets stuff from pybot.py, reads data and selects what will be executed from class.py
# Part of PyBot, (C) 2011 Matoe Productions LLC

import pybot
import arr
import safety

# ===== make life easier
# QuickFind
def find(obj, whatever):
	if obj.find(whatever)!=-1:
		return True
	
	return False
# =====

def parsePRIVMSG(msg):
	import action
	if safety.checkIfPersonIsIgnoredByBot():
		return
	
	# ==== what you need to make your own bot commands:
	useful = msg[(msg.index('PRIVMSG')+8):]
	chan = useful[0:(useful.index(':')-1)]
	message = useful[useful.index(chan)+(len(chan)+2):]
	person = msg[1:msg.index('!')]
	# ====
	
	thing = message.split(' ', 2)
	
	if find(message, pybot.prefix+'k'):
		if arr.checkIfThereIsIndex(thing, 2):
			action.kick(chan, thing[1], thing[2], person)
		else:
			print pybot.stdkickreason
			action.kick(chan, thing[1], pybot.stdkickreason, person)
	