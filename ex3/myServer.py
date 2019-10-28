import sys
import time
from ex3utils import Server


class myServer(Server):

    def onStart(self):
        self.clientCount = 0
        self.ClArray = {}
        print "Server has started"

    def onStop(self):
        print "Server has stopped"

    def onConnect(self, socket):
        socket.connectionTime = time.time()
        print "Welcome to the server"
        socket.send("Your name is registered")
        socket.username = ""

        self.clientCount += 1
        print "Total number of clients active: " + str(self.clientCount)

    def onMessage(self, socket, message):
        (command, sep, parameter) = message.strip().partition(' ')


        # Acting on message
        if command == "REGISTER":
            socket.userName = parameter
            self.ClArray[parameter] = socket
            print "Username is set as: " + socket.userName
        elif command == "MESSAGE":
            for user, sockets in self.ClArray.iteritems():
                sockets.send(socket.userName + ": " + parameter)
        elif command == "PRIVATEMESSAGE":
            (usertoMessage, sep, message) = parameter.strip().partition(' ')
            if usertoMessage in self.ClArray:
                self.ClArray[usertoMessage].send("Private message from " + socket.userName + ": " + message)
            else:
                socket.send("User doesn't exist")
        return True

    def onDisconnect(self, socket):
        socket.disconnectionTime = time.time()
        self.clientCount -= 1
        print "Total number of clients active: " + str(self.clientCount)
        print "Goodbye"


# ip and port setting using arguments
ip = sys.argv[1]
port = int(sys.argv[2])
# creating server using myServer call
server = myServer()
# starting server
server.start(ip, port)
