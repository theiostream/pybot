# botty.py -- pybot usage example.

import pybot

sp = ' '
endl = '\r\n'

pybot.name = 'botty3'
pybot.owner = 'theiostream'
pybot.prefix = '@'

pybot.server = 'irc.evilpengu.in'
pybot.channels = ['#talk', '#fr0st']

pybot.notAllowHarmful = 1
pybot.allowedHarmfulFor = ['botty-tester']
pybot.ignoredByBot = ['botty-tester-fail']

# remember nspass!

pybot.connect()

while True:
	pybot.run()