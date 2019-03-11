#!/usr/bin/env python

import urllib
import fnmatch
url = "http://syllabus.cs.manchester.ac.uk/ugt/2018/COMP18112/page4.html"



# Parsing webpage method (or function if you want)
def parseWebPage(url):
	data = urllib.urlopen(url)
	tokens = data.read().split()
	for token in tokens:
		if token == "<html>":
			token = ""
		elif token == "<head>":
			token = ""
		elif token == "<title>":
			token = ""
		elif token == "</title>":
			token = "\n\n"
		elif token == "</head>":
			token = ""
		elif token == "</html>":
			token = ""
		elif token == "<body>":
			token = ""
		elif token == "<h1>":
			token = "Heading:"
		elif token == "</h1>":
			token = "\n"
		elif token == "<p>":
			token = "Paragraph:"
		elif token == "</p>":
			token = "\n"
		elif token == "<em>":
			token = "\033[1m"
		elif token == "</em>":
			token = "\033[0;0m"
		elif token == "</body>":
			token = ""
		elif token == '<a':
			token = ""
		elif token == 'href="./page4.html">':
			parseWebPage.urlChange1 = token[8:18]
			token = ""
		elif token == '</a>':
			token = ""
		elif token == 'href="./page5.html">':
			parseWebPage.urlChange1 = token[8:18]
			token = ""
		elif token == 'href="./page3.html">':
			parseWebPage.urlChange2 = token[8:18]
			token = ""

		tokens = filter(None, tokens)
		print	token,


def urlChange1():
		url = "http://syllabus.cs.manchester.ac.uk/ugt/2018/COMP18112/" + parseWebPage.urlChange1
		data = urllib.urlopen(url)
		tokens = data.read().split()
		parseWebPage(url)
		print "\n"
		print "1: ./" + parseWebPage.urlChange1
		print "2: ./" + parseWebPage.urlChange2
		myMessage = raw_input('Select a link: ')
		if myMessage == "1":
			urlChange1()
		elif myMessage == "2":
			urlChange2()


def urlChange2():
	url = "http://syllabus.cs.manchester.ac.uk/ugt/2018/COMP18112/" + parseWebPage.urlChange2
	data = urllib.urlopen(url)
	tokens = data.read().split()
	parseWebPage(url)
	print "\n"
	print "1: ./" + parseWebPage.urlChange1
	print "2: ./" + parseWebPage.urlChange2
	myMessage = raw_input('Select a link: ')
	if myMessage == "1":
		urlChange1()
	elif myMessage == "2":
		urlChange2()

# The 'Main' method
parseWebPage(url)

print "\n"
print "1: ./" + parseWebPage.urlChange1
print "2: ./" + parseWebPage.urlChange2
myMessage = raw_input('Select a link: ')
if myMessage == "1":
	urlChange1()
if myMessage == "2":
	urlChange2()
