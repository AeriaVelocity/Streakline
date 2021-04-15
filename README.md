# ed.py
Okay, so it's not a rewrite of the original `ed`. All it can do is write to files.

To use it, run the Python file (Python 3 required), name a file, then start typing.

Commands:
- `#save` - Save the file.
- `#exit` - Stop editing. This will not save your changes - use `#save`, then `#exit`.
- `#show` - Show the file contents, and what will be saved when the program quits.

Example:
```
What file name? > youar.e
Warning - this file already exists.
File 'youar.e' opened for writing.
Start typing. Changes will be saved in buffer.
ed > meow :3
ed > #show
Previously stored:
egg
brain
fish
To be saved:
meow :3
ed > #save
File 'youar.e' - 18 bytes saved.
Type #exit to stop editing.
ed > #exit
File 'youar.e' closed.
```
