# pybot.py -- by theiostream
# -- main part of the bot, with connect, variables and gets data to parse.py
# Part of PyBot, (C) 2011 Matoe Productions LLC

import sys
import socket
from datetime import datetime

import parse

# variables
sp = ' '
endl = '\r\n'

irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
now = datetime.now()
data = ''

# variables set on your bot
name = ''
owner = ''
prefix = ''

server = ''
channels = []
nspass = ''

stdkickreason = 'Your behaviour is not conductive to the desired environment.' #default, easily changed on yourbot.py

ignoredByBot = []
notAllowHarmful = 0
allowedHarmfulFor = []


def connect():
	irc.connect((server, 6667))
	print irc.recv(4096)
	irc.send('NICK '+name+endl)
	irc.send('USER '+name+' '+name+' '+name+' :Python IRC'+endl) #even I don't get this line :\
	
	if nspass!='':
		irc.send('PRIVMSG NickServ IDENTIFY '+nspass+endl)
	
	for chanl in channels:
		irc.send('JOIN '+chanl+endl)

def run():
	global data
	
	data = irc.recv(4096)
	
	if parse.find(data, 'PING'):
		irc.send('PONG '+ data.split()[1]+endl)
		
	if parse.find(data, 'PRIVMSG'):
		'''if parse.find(data, 'PRIVMSG '+name):
			parse.parsePM(data)
		else:''' # NOT DONE YET...
		parse.parsePRIVMSG(data)
		
	print '['+str(now.hour)+':'+str(now.minute)+':'+str(now.second)+'] '+data