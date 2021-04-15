import os
filename = ""
line = ""
filebuffer = []
while filename == "":
    filename = input("What file name? > ")
filesize = os.path.getsize(filename)
if os.path.exists(filename):
    print("Warning - this file already exists.")
openedfile = open(filename, "a");
print("Start typing. It'll automatically be saved. Type '#save' to exit.")
while line != "#save":
    line = input("ed > ")
    if line == "#save":
        pass
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
    if not "#" in line:
        openedfile.write(line + "\n")
        filebuffer.append(line)
openedfile.close()
print("File '" + filename + "' - " + str(filesize) + " bytes saved.")
