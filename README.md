# ed.py
Okay, so it's not a rewrite of the original `ed`. It's just in the spirit of it.

To use it, run the Python file (Python 3 required), name a file, then start typing.

Commands:
- `~save` - Save the file and exit.
- `~exit` - Exit without saving.
- `~show` - Show the contents of the file and buffer.
- `~del` - Remove the last line from the file buffer.

Example:
```
~$ python ./ed.py
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
~$
```
