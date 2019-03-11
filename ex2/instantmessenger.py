import im
import time

server = http://webdev.cs.manchester.ac.uk/w81454af/IMServer.php?

state = 0

if state == 0
	while server[message1] == null
		state = 1
		myMessage = raw_input('Type your message: ')
		server[message1] = myMessage
		print 'waiting for reply...'
		time.sleep(20)
		if (state == 0)
			print server[message2]
else if state == 1
	while server[message2] == null
		print 'waiting...'
		time.sleep(20)
		state = 1
		myMessage = raw_input('Type your message: ')
		server[message2] = myMessage
