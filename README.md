### A WYGIWYG line mode text editor, inspired by the standard text editor, [ed](https://www.gnu.org/fun/jokes/ed-msg.html)!

#### GNU/Linux instructions
Python will usually already be installed on your distribution. If not, you must install at least Python 3.0.

> The following instructions work for macOS or any other *nix system too.

You can go ahead and just type in `./stline.py` to run Streakline.

If you want to install it (because of course you do) then run the following command as root:

``` sh
cp ./stline.py /usr/local/bin/stline

```

`/usr/local/bin/` will already be in your PATH, so no further setup is required. Just type `stline` into your terminal to start using it. Have fun!

#### Windows instructions
To use the batch script file, you need to be able to run `python.exe` from the command line:

If this is possible, simply type  `stline`  when inside the same directory as the script files and hit Enter.
If not, either add `python` to your PATH, or type `python stline.py`.

To run Streakline anywhere, the folder with both `stline.bat` and `stline.py` should be added to PATH.

#### Commands
- `~save` - Save the file and exit.
- `~exit` - Exit without saving.
- `~show` - Show the contents of the file and buffer.
- `~del` - Remove the last line from the file buffer.

#### Example
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
