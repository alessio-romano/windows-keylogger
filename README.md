# Windows Keylogger
This repository contains a simple windows keylogger written in Python.<br/>
All letters written by the host machine's keyboard while the script is running will be kept in memory.<br/>
Whenever the user writes a certain amount of input characters, or after a specific amount of time is elapsed, all logs will be sent to the target email.<br/>
All scripts are in the ```.pyw``` extension in order to avoid a console popping up while running the keylogger.<br/>


 # Configuration
Before using the script, there are some sections of the code that you might want to modify:<br/>
* In order to send emails containing the logs, the ```mailservice.pyw``` script needs to contain your own email and password, followed by the recipient.<br/>
* The ```keylogger.pyw``` script sends an email _every 2000 input characters or every 15 minutes_ by default. You might want to change that according to your needs.<br/>

To run the script as a standalone, simply run ```cd your/project/path``` followed by ```python keylogger.pyw```.<br/>
That said, most of the times you might want to attach the keylogger to any executable file.<br/>
For that purpose I suggest using [PyInstaller](https://pyinstaller.readthedocs.io/en/stable/) or [Py2Exe](https://pypi.org/project/py2exe/) following their guidelines.<br/>