# ed.py
Okay, so it's not a rewrite of the original `ed`. All it can do is write to files.

To use it, run the Python file (Python 3 required), name a file, then start typing.

Commands:
- `#save` - Save the file and stop editing.
- `#show` - Show the file contents, and what will be saved when the program quits.

Example:
```
What file name? > youar.e
Warning - this file already exists.
Start typing. It'll automatically be saved. Type '#save' to exit.
ed > #show
Previously stored:
egg
brain
ed > fish
ed > #show
Previously stored:
egg
brain
To be saved:
fish
ed > #save
File 'youar.e' - 12 bytes saved.
```
