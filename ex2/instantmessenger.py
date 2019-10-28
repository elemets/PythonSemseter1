import im
import time
import urllib
import fnmatch


server = im.IMServerProxy('http://webdev.cs.manchester.ac.uk/~w81454af/IMServer.php')

def sendMessage():
	server.__delitem__('message')
	if len(server.keys()) == 4:
		message = raw_input('Type your message here: ')
		server['message'] = message
	waitingForMessageUser2()



def waitingForMessageUser2():
	time.sleep(4)
	while server['message'] == '\r\n':
		print('waiting for message')
		time.sleep(2)
	print(server['message'])
	sendMessage()





if len(server.keys()) == 1:
	server['state'] = '0'
# Clear the server


# if the state is zero (start state) then go
# while server.keys == 0 (no messages sent) then look for a message from someone
if server['state'] == "0\r\n":
	# state now equals one as its been intialised
	# asking user 1 for username and setting it on server
	print (server['state'])
	server['state'] = '1'
	print ('Hello there, what is your name?')
	user1 = raw_input('Type your name: ')
	server['username1'] = user1
	while len(server.keys()) == 3:
		print('Waiting for next user')
		time.sleep(1)
	print('You are chatting with ' + server['username2'])
	message = raw_input('Type your message: ')
	server['message'] = message
	waitingForMessageUser2()


elif server['state'] == '1\r\n':
	print (server['state'])
	print ('Hello there what is your name?')
	user2 = raw_input('Type your name: ')
	server['username2'] = user2
	while len(server.keys()) == 3:
		print('Waiting for next user')
		time.sleep(1)
	print('You are chatting with ' + server['username1'])
	waitingForMessageUser2()



server.clear()

	#while server['message2'] == null:
