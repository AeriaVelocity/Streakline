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
filesize = os.path.getsize(filename)
print("File '" + filename + "' opened for writing.")
print("Start typing. Changes will be saved in buffer.")
try:
	while line != "#exit" and line != "#save":
		line = input("ed > ")
		if line == "#save":
			for x in range(len(filebuffer)):
				openedfile.write(filebuffer[x] + "\n")
		elif line == "#show":
			filer = open(filename, 'r')
			if filesize > 0:
				print("Previously stored:")
				print(filer.read(), end='')
			filer.close()
			if len(filebuffer):
				print("To be saved:")
				for x in range(len(filebuffer)):
					print(filebuffer[x])
		elif line == "#help":
			print("#save - Save the file and exit.")
			print("#exit - Exit without saving.")
			print("#show - Show the file contents, and what will be saved when the program quits.")
		elif "#" in line:
			print(line + " is an unknown command.")
		if not "#" in line:
			filebuffer.append(line)
except KeyboardInterrupt:
	print()
openedfile.close()
if line == "#save":
	print("File '" + filename + "' - " + str(filesize) + " bytes saved.")
elif line == "#exit":
	print("File '" + filename + "' - closed without saving.")
else:
	print("File '" + filename + "' - closed without saving.")
