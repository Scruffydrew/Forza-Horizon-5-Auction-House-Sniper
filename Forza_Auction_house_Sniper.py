from python_imagesearch.imagesearch import *
from pynput.keyboard import Key, Controller
from datetime import datetime
import time, sys, pyautogui
import keyboard as keyboardlistener
from threading import Thread
from tkinter import Label, PhotoImage, Button
import tkinter as tk
from win32gui import GetWindowText, GetForegroundWindow

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

# Stop the print command from showing up in the console
def blockPrint():
    sys.stdout = open(os.devnull, 'w')

class Logger(object):
    def __init__(self):
        self.terminal = sys.stdout
        self.log = open("logfile.log", "a")
    def write(self, message):
        self.terminal.write(message)
        self.log.write(message)  
    def flush(self):
        # this flush method is needed for python 3 compatibility.
        # this handles the flush command by doing nothing.
        # you might want to specify some extra behavior here.
        pass    

sys.stdout = Logger()

def closeprog():
    consoleoutput.set("Welcome to the Forza Auction House Sniper Bot\nClosing Program")
    time.sleep(1)
    sys.exit()

# Activates the print block function
#blockPrint()

def sniperscript():
    # Start of Code
    print("Welcome to the Forza Auction House Sniper Bot")
    consoleoutput.set("Welcome to the Forza Auction House Sniper Bot")
    time.sleep(2)
    print("Starting program")
    consoleoutput.set("Welcome to the Forza Auction House Sniper Bot\nStarting program")
    time.sleep(2)
    activewin = 0
    while activewin == 0:
        print(GetWindowText(GetForegroundWindow()))
        if GetWindowText(GetForegroundWindow()) == "Forza Horizon 5":
            activewin = 1

    consoleoutput.set("Welcome to the Forza Auction House Sniper Bot\nProgram Running")

    keyboard = Controller()

    keyy = "y" # Used to press down and release the 'y' key
    kdown = "down" # Used to press down and release the 'down arrow' key
    keyenter = "enter" # Used to press down and release the 'enter' key

    ahsearch = pyautogui.pixel(330, 249) # Search for the image 'ahsearch.png' on your screen
    sconfirm = pyautogui.pixel(609, 732) # Search for the image 'searchconfirm.png' on your screen

    cat = 0 # Used to make the program loop
    turbo = 0 # Used to enter the ah menu
    Immortal_Snail = 1 # Used to confirm the settings chosen in the auction house menu
    supercharger = 1 # Used to select the car and purchase it from the auction house
    chinas_population = 0 # Used to back out of the buy-out screen and return to the start of the script
    listingloading = 0 # Used to loop checking pixel colour while waiting for Austion House listings to load

    while cat == 0: # Allows the program to loop
        print("Line: 50")
        time.sleep(.9)
        while turbo == 0 and ahsearch == (255,0,134):
            start = time.time()
            print("Line: 58")
            keyboard.press(Key.enter) # Enters auction house menu
            keyboard.release(Key.enter)
            Immortal_Snail = 0 # Allows the 'while Immortal_Snail == 0:' and following lines of code to run
            turbo = 1 # Stops the 'while turbo == 0 and ahsearch[0] != -1:' and following lines of code from running
        while Immortal_Snail == 0:
            print("Line: 66")
            sconfirm = pyautogui.pixel(609, 732)
            if sconfirm == (255,0,134):
                print("Line: 69")
                keyboard.press(Key.enter) # Confirms if you are in ah and searches for a car
                keyboard.release(Key.enter)
                supercharger = 0 # Allows the 'while supercharger == 0:' and following lines of code to run
                Immortal_Snail = 1 # Stops the 'while Immortal_Snail == 0:' and following lines of code from running
        while supercharger == 0:
            print("Line: 77")
            Rear_Window = pyautogui.pixel(411, 172)
            if Rear_Window == (255,222,57):
                time.sleep(.52)
                car = pyautogui.pixel(990, 231)
                if car == (52,23,53):
                    time.sleep(0.1)
                    px = pyautogui.pixel(873, 234)
                    if px == (247,247,247):
                        listingloading = 1
                        while listingloading == 1:
                            print("Line: 84")
                            David_Joesph = pyautogui.pixel(873, 234) # Gets the RGB Values for the pixel at the location X:873 Y:234
                            print(David_Joesph) # Prints the RGB Values for the pixel at the location X:873 Y:234
                            if David_Joesph != (247,247,247): # Checks if the RGB values are not equal to RGB(247,247,247)
                                listingloading = 0
                    David_Joesph = pyautogui.pixel(873, 234) # Gets the RGB Values for the pixel at the location X:873 Y:234
                    if David_Joesph != (247,247,247): # Checks if the RGB values are not equal to RGB(247,247,247)
                        keyboard.press(keyy) # Auction house options
                        keyboard.release(keyy)
                        print("Line: 90")
                        time.sleep(.25)
                        keyboard.press(Key.down) # Move to Buy-out
                        keyboard.release(Key.down)
                        print("Line: 94")
                        time.sleep(.12)
                        keyboard.press(Key.enter) # Opens Buy-out
                        keyboard.release(Key.enter)
                        print("Line: 98")
                        time.sleep(0.5)
                        Budget_Shaeden = pyautogui.pixel(627, 572)
                        if Budget_Shaeden == (255,0,134):
                            print("Line: 101")
                            keyboard.press(Key.enter) # Buys the car
                            keyboard.release(Key.enter)
                            purchase = time.time()
                            print("Line: 105")
                            supercharger = 1 # Stops the 'while supercharger == 0:' and following lines of code from running
                            chinas_population = 1 # Allows the 'while chinas_population == 1:' and following lines of code to run
                    else: # If there is no car avaliable for purchase on the auction house
                        print("Line: 109")
                        print("image not found")
                        keyboard.press(Key.esc) # Backs out of the auction house, to allow it to have another go at searching
                        keyboard.release(Key.esc)
                        print("Line: 113")
                        # Resets all variables that are stopping previous lines of code from running
                        turbo = 0
                        Immortal_Snail = 1
                        chinas_population = 0
                        supercharger = 1
                else: # If there is no car avaliable for purchase on the auction house
                        print("Line: 120")
                        print("image not found")
                        keyboard.press(Key.esc) # Backs out of the auction house, to allow it to have another go at searching
                        keyboard.release(Key.esc)
                        print("Line: 124")
                        # Resets all variables that are stopping previous lines of code from running
                        turbo = 0
                        Immortal_Snail = 1
                        chinas_population = 0
                        supercharger = 1
            while chinas_population == 1:
                print("Line: 131")
                time.sleep(1.8)
                print("Line: 133")
                buyout = pyautogui.pixel(637, 458)
                if buyout == (52,23,53):
                    print("Line: 152")
                    time.sleep(3)
                    keyboard.press(Key.enter) # Backs out of the successful buy-out screen
                    keyboard.release(Key.enter)
                    print("Line: 157")
                    time.sleep(.7)
                    print("Line: 159")
                    keyboard.press(Key.esc) # Backs out of the auction house buy menu
                    keyboard.release(Key.esc)
                    print("Line: 163")
                    time.sleep(.7)
                    print("Line: 165")
                    keyboard.press(Key.esc) # Returns to start location, before entering the search for the desired car
                    keyboard.release(Key.esc)
                    print("Line: 169")
                    # Resets all variables that are stopping previous lines of code from running
                    turbo = 0
                    Immortal_Snail = 1
                    supercharger = 1
                    chinas_population = 0
                    cat = 0
                    print("Line: 176")
                    # Restarts the script
                    continue
                else:
                    buyoutfailed = pyautogui.pixel(641, 477)
                    if buyoutfailed == (52,23,53):
                        print("Line: 152")
                        time.sleep(2)
                        keyboard.press(Key.enter) # Backs out of the successful buy-out screen
                        keyboard.release(Key.enter)
                        print("Line: 157")
                        time.sleep(.7)
                        print("Line: 159")
                        keyboard.press(Key.esc) # Backs out of the auction house buy menu
                        keyboard.release(Key.esc)
                        print("Line: 163")
                        time.sleep(.7)
                        print("Line: 165")
                        keyboard.press(Key.esc) # Returns to start location, before entering the search for the desired car
                        keyboard.release(Key.esc)
                        print("Line: 169")
                        # Resets all variables that are stopping previous lines of code from running
                        turbo = 0
                        Immortal_Snail = 1
                        supercharger = 1
                        chinas_population = 0
                        cat = 0
                        print("Line: 176")
                        # Restarts the script
                        continue
root = tk.Tk()
consoleoutput = tk.StringVar()
consoleoutput.set("")
lastoutput = tk.StringVar()
lastoutput.set("")

width, height= pyautogui.size()

root.title("Forza Horizon 5 Sniper") # names the Tk root window  
root.overrideredirect(1) # removes title bar from window
root.geometry(("%dx%d" % (width, height)))
root.configure(bg='grey')
root.wm_attributes("-topmost", True)
root.wm_attributes("-transparentcolor", "grey")

ConsoleOutput=Label(textvariable=consoleoutput, fg='#ffffff', bg='grey')
ConsoleOutput.grid(sticky="NE")
LastOutput=Label(textvariable=lastoutput, fg='#ffffff', bg='grey')
LastOutput.grid()
overlayimg=PhotoImage(file=resource_path('overlay.png'))
overlay=Button(root, image=overlayimg, bg='grey', highlightbackground = "grey", highlightthickness = 0, bd=0, activebackground = "grey", command = closeprog)
X=width-120
Y=height-31
overlay.place(x=X, y=Y)

Script = Thread(target=sniperscript)
Script.setDaemon(True)
Script.start()
root.mainloop()