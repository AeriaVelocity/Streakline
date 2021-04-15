import os
filename = ""
line = ""
filebuffer = []
while filename == "":
    filename = input("What file name? > ")
if os.path.exists(filename):
    print("Warning - this file already exists.")
openedfile = open(filename, "a");
filesize = os.path.getsize(filename)
print("File '" + filename + "' opened for writing.")
print("Start typing. Changes will be saved in buffer.")
try:
	while line != "#exit":
		line = input("ed > ")
		if line == "#save":
			for x in range(len(filebuffer)):
				openedfile.write(filebuffer[x] + "\n")
			print("File '" + filename + "' - " + str(filesize) + " bytes saved.")
			print("Type #exit to stop editing.")
			filebuffer = []
		if line == "#show":
			filer = open(filename, 'r')
			if filesize > 0:
				print("Previously stored:")
				print(filer.read(), end='')
			filer.close()
			if len(filebuffer):
				print("To be saved:")
				for x in range(len(filebuffer)):
					print(filebuffer[x])
		if line == "#help":
			print("#save - Save the file.")
			print("#exit - Stop editing. This will not save your changes - use #save, then #exit.")
			print("#show - Show the file contents, and what will be saved when the program quits.")
		if not "#" in line:
			filebuffer.append(line)
except KeyboardInterrupt:
	print()
openedfile.close()
print("File '" + filename + "' closed.")
