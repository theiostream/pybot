# action.py -- by theiostream
# -- executes bot actions, selected by parse.py
# Part of PyBot, (C) 2011 Matoe Productions LLC

import socket
import pybot
import safety

sp = ' '
endl = '\r\n'

# -- make life easier
# QuickSend
def send(message, obj=pybot.irc):
	obj.send(message)
# --

# Channel Actions
def kick(channel, person, reason, sender):
	if safety.checkIfCanExecuteAggressive()==False:
		return
	send('KICK '+channel+sp+person+sp+reason+endl)

# PM Actions
# TODO: maybe add a separate file to handle PM actions?

def say(channel, message):
	send('PRIVMSG '+channel+sp+message+endl)
