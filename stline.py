#!/usr/bin/env python
import os
filename = ""
line = ""
filebuffer = []
try:
	while filename == "":
		filename = input("What file name? > ")
except KeyboardInterrupt:
	print("\nQuitting.")
	exit(0)
if os.path.exists(filename):
    print("Warning - this file already exists.")
openedfile = open(filename, "a");
filesize = os.path.getsize(openedfile.name)
print("File '" + filename + "' opened for writing.")
print("Start typing. Changes will be saved in buffer.")
try:
	while line != "~exit" and line != "~save":
		line = input(filename + " > ")
		if line == "~save":
			for x in range(len(filebuffer)):
				openedfile.write(filebuffer[x] + "\n")
		elif line == "~show":
			filer = open(filename, 'r')
			if filesize > 0:
				print("Previously stored:")
				print(filer.read(), end='')
			filer.close()
			if len(filebuffer):
				print("To be saved:")
				for x in range(len(filebuffer)):
					print(filebuffer[x])
		elif line == "~help":
			print("~save - Save the file and exit.")
			print("~exit - Exit without saving.")
			print("~show - Show the contents of the file and buffer.")
			print("~del - Remove the last line from the file buffer.")
		elif line == "~exit":
			pass
		elif line == "~del":
			if len(filebuffer) < 1:
				print("Nothing to delete.")
			else:
				print("Previous line deleted.")
				filebuffer.pop()
		elif "~" in line:
			print(line + " is an unknown command.")
		if not "~" in line:
			filebuffer.append(line)
except KeyboardInterrupt:
	print()
openedfile.flush()
os.fsync(openedfile.fileno())
filesize = os.path.getsize(openedfile.name)
if line == "~save":
	print("File '" + filename + "' - " + str(filesize) + " bytes saved.")
elif line == "~exit":
	print("File '" + filename + "' - closed without saving.")
	if filesize < 1:
		os.remove(filename)
else:
	print("File '" + filename + "' - closed without saving.")
	if filesize < 1:
		os.remove(filename)
openedfile.close()
