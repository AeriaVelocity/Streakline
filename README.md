### A WYGIWYG line mode text editor, inspired by the standard text editor, [ed](https://www.gnu.org/fun/jokes/ed-msg.html)!

To use it, run the Python file (Python 3 required), name a file, then start typing.

Commands:
- `~save` - Save the file and exit.
- `~exit` - Exit without saving.
- `~show` - Show the contents of the file and buffer.
- `~del` - Remove the last line from the file buffer.

Example:
```
~$ python ./stline.py
What file name? > youar.e
Warning - this file already exists.
File 'youar.e' opened for writing.
Start typing. Changes will be saved in buffer.
youar.e > meow :3
youar.e > ~show
Previously stored:
egg
brain
fish
To be saved:
meow :3
youar.e > ~save
File 'youar.e' - 18 bytes saved.
~$
```
