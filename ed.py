import os
filename = ""
line = ""
while filename == "":
    filename = input("What file name? > ")
openedfile = open(filename, "a");
print("Start typing. It'll automatically be saved. Type '#~#' to exit.")
while line != "#~#":
    line = input("ed > ")
    if line != "#~#":
        openedfile.write(line + "\n")
filesize = os.path.getsize(filename)
print(filesize)
print("File '" + filename + "' - " + str(filesize) + " bytes saved.")
