from python_imagesearch.imagesearch import *
from pynput.keyboard import Key, Controller
from datetime import datetime
import time, sys, pyautogui, os
import keyboard as keyboardlistener
from threading import Thread
from tkinter import Label, PhotoImage, Button
import tkinter as tk
from win32gui import GetWindowText, GetForegroundWindow
from win32api import GetSystemMetrics

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

    consoleoutput.set("Welcome to the Forza Auction House Sniper Bot\nGetting Monitor info")

    keyboard = Controller()

    keyy = "y" # Used to press down and release the 'y' key
    kdown = "down" # Used to press down and release the 'down arrow' key
    keyenter = "enter" # Used to press down and release the 'enter' key

    MonitorWidth = GetSystemMetrics(0)
    MonitorHeight = GetSystemMetrics(1)

    ahsearchx = int(0.171875 * MonitorWidth)
    ahsearchy = int(0.2305555556 * MonitorHeight)
    sconfirmx = int(0.3171875 * MonitorWidth)
    sconfirmy = int(0.677777778 * MonitorHeight)
    Rear_Windowx = int(0.2140625 * MonitorWidth)
    Rear_Windowy = int(0.159259259 * MonitorHeight)
    carx = int(0.515625 * MonitorWidth)
    cary = int(0.213888889 * MonitorHeight)
    pxx = int(0.4546875 * MonitorWidth)
    pxy = int(0.216666667 * MonitorHeight)
    David_Joesphx = int(0.4546875 * MonitorWidth)
    David_Joesphy = int(0.216666667 * MonitorHeight)
    BuyoutOptionx = int(0.329166667 * MonitorWidth)
    BuyoutOptiony = int(0.492592593 * MonitorHeight)
    Budget_Shaedenx = int(0.3265625 * MonitorWidth)
    Budget_Shaedeny = int(0.52962963 * MonitorHeight)
    buyoutoutcomex = int(0.327083333 * MonitorWidth)
    buyoutoutcomey = int(0.405555556 * MonitorHeight)
    buyoutx = int(0.327604167 * MonitorWidth)
    buyouty = int(0.417592593 * MonitorHeight)
    collectcarx = int(0.32291666666 * MonitorWidth)
    collectcary = int(0.46481481481 * MonitorHeight)
    collectcar1x = int(0.328645833 * MonitorWidth)
    collectcar1y = int(0.490740741 * MonitorHeight)
    carcollectedx = int(0.3296875 * MonitorWidth)
    carcollectedy = int(0.47685185185 * MonitorHeight)
    sellerdetailsx = int(0.327604167 * MonitorWidth)
    sellerdetailsy = int(0.489814815 * MonitorHeight)
    sellerdetails2x = int(0.327604167 * MonitorWidth)
    sellerdetails2y = int(0.514814815 * MonitorHeight)
    auctionhousex = int(0.515625 * MonitorWidth)
    auctionhousey = int(0.213888889 * MonitorHeight)
    buyoutfailedx = int(0.327604167 * MonitorWidth)
    buyoutfailedy = int(0.432407407 * MonitorHeight)
    searchahx = int(0.16770833333 * MonitorWidth)
    searchahy = int(0.29074074074 * MonitorHeight)

    time.sleep(2)

    consoleoutput.set("Welcome to the Forza Auction House Sniper Bot\nProgram Running")

    ahsearch = pyautogui.pixel(ahsearchx, ahsearchy) # Search for the image 'ahsearch.png' on your screen 0.171875 * MonitorWidth
    sconfirm = pyautogui.pixel(sconfirmx, sconfirmy) # Search for the image 'searchconfirm.png' on your screen

    cat = 0 # Used to make the program loop
    turbo = 0 # Used to enter the ah menu
    Immortal_Snail = 1 # Used to confirm the settings chosen in the auction house menu
    supercharger = 1 # Used to select the car and purchase it from the auction house
    chinas_population = 0 # Used to back out of the buy-out screen and return to the start of the script
    listingloading = 0 # Used to loop checking pixel colour while waiting for Austion House listings to load

    while cat == 0: # Allows the program to loop
        print("starting program")
        time.sleep(.9)
        ahsearch = pyautogui.pixel(ahsearchx, ahsearchy)
        while turbo == 0 and ahsearch == (255,0,134):
            searchah = pyautogui.pixel(searchahx, searchahy)
            while searchah != (255, 0, 134):
                print("Please make sure you have the search auction house selected")
                searchah = pyautogui.pixel(searchahx, searchahy)
                time.sleep(.5)
            start = time.time()
            keyboard.press(Key.enter) # Enters auction house menu
            keyboard.release(Key.enter)
            print("Entering Auction House")
            Immortal_Snail = 0 # Allows the 'while Immortal_Snail == 0:' and following lines of code to run
            turbo = 1 # Stops the 'while turbo == 0 and ahsearch[0] != -1:' and following lines of code from running
        while Immortal_Snail == 0:
            print("Line: 66")
            sconfirm = pyautogui.pixel(sconfirmx, sconfirmy)
            if sconfirm == (255,0,134):
                print("Checking if you are currently in ah")
                keyboard.press(Key.enter) # Confirms if you are in ah and searches for a car
                keyboard.release(Key.enter)
                supercharger = 0 # Allows the 'while supercharger == 0:' and following lines of code to run
                Immortal_Snail = 1 # Stops the 'while Immortal_Snail == 0:' and following lines of code from running
        while supercharger == 0:
            print("Checking if there are any cars up for auction")
            Rear_Window = pyautogui.pixel(Rear_Windowx, Rear_Windowy) # Checks to see if you are in the auction house - viewing the cars up for auction
            if Rear_Window == (255,222,57):
                time.sleep(.52)
                car = pyautogui.pixel(carx, cary) # Search for the image of the auctionhouse details of the desired car on your screen
                if car == (52,23,53):
                    time.sleep(0.1)
                    px = pyautogui.pixel(pxx, pxy)
                    if px == (247,247,247):
                        listingloading = 1
                        while listingloading == 1:
                            print("Line: 84")
                            David_Joesph = pyautogui.pixel(David_Joesphx, David_Joesphy) # Gets the RGB Values for the pixel at the location X:873 Y:234
                            print(David_Joesph) # Prints the RGB Values for the pixel at the location X:873 Y:234
                            if David_Joesph != (247,247,247): # Checks if the RGB values are not equal to RGB(247,247,247)
                                listingloading = 0
                    David_Joesph = pyautogui.pixel(David_Joesphx, David_Joesphy) # Gets the RGB Values for the pixel at the location X:873 Y:234
                    if David_Joesph != (247,247,247): # Checks if the RGB values are not equal to RGB(247,247,247)
                        keyboard.press(keyy) # Auction house options
                        keyboard.release(keyy)
                        print("Bringing up shortcut menu to purchase the car")
                        time.sleep(.25)
                        BuyoutOption = pyautogui.pixel(BuyoutOptionx, BuyoutOptiony) # Confirms that the butout option is selected
                        if BuyoutOption != (255,0,134):
                            keyboard.press(Key.down) # Move to Buy-out
                            keyboard.release(Key.down)
                            print("Moved to Buy-Out Button")
                        print("Line: 94")
                        time.sleep(.12)
                        BuyoutOption = pyautogui.pixel(BuyoutOptionx, BuyoutOptiony) # Confirms that the butout option is selected
                        if BuyoutOption != (255,0,134):
                            keyboard.press(Key.down) # Move to Buy-out
                            keyboard.release(Key.down)
                            print("Moved to Buy-Out Button")
                        keyboard.press(Key.enter) # Selects Buy-out
                        keyboard.release(Key.enter)
                        print("Line: 98")
                        time.sleep(0.5)
                        Budget_Shaeden = pyautogui.pixel(Budget_Shaedenx, Budget_Shaedeny) # Search for the image 'placebid.png' on your screen
                        if Budget_Shaeden == (255,0,134):
                            print("Line: 101")
                            keyboard.press(Key.enter) # Buys the car
                            keyboard.release(Key.enter)
                            purchase = time.time()
                            print("Line: 105")
                            print("Car Purchased")
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
                buyoutoutcome = pyautogui.pixel(buyoutoutcomex, buyoutoutcomey) # Checks to see if the buyout outcome is still loading
                while buyoutoutcome == (52,23,53):
                    buyoutoutcome = pyautogui.pixel(buyoutoutcomex, buyoutoutcomey) # Checks to see if the buyout outcome is still loading
                print("Line: 133")
                buyout = pyautogui.pixel(buyoutx, buyouty) # Search for the image 'buyout.png' on your screen
                if buyout == (52,23,53):
                    print("Line: 152")
                    time.sleep(3)
                    keyboard.press(Key.enter) # Backs out of the successful buy-out screen
                    keyboard.release(Key.enter)
                    print("Line: 157")
                    time.sleep(.7)
                    collectcar = pyautogui.pixel(collectcarx, collectcary) # Checks if collect car is currently selected
                    while collectcar != (255,0,134):
                        collectcar = pyautogui.pixel(collectcarx, collectcary) # Checks if collect car is currently selected
                        collectcar = pyautogui.pixel(collectcar1x, collectcar1y) # Checks if collect car is currently selected
                        print("Car collect option not selected")
                        time.sleep(.1)
                    if collectcar == (255,0,134):
                        print("Collect car is selected")
                        time.sleep(.1)
                        keyboard.press(Key.enter) # Collects the car
                        keyboard.release(Key.enter)
                        time.sleep(.5)
                        collectcar = pyautogui.pixel(collectcarx, collectcary) # Checks if collect car is currently selected
                        while collectcar == (255,0,134):
                            collectcar = pyautogui.pixel(collectcarx, collectcary) # Checks if collect car is currently selected
                            keyboard.press(Key.enter) # Collects the car
                            keyboard.release(Key.enter)
                            print("Attempting to collect the car")
                            time.sleep(.1)
                        carcollected = pyautogui.pixel(carcollectedx, carcollectedy) # Checks if collect car is currently selected
                        while carcollected != (52, 23, 53):
                            carcollected = pyautogui.pixel(carcollectedx, carcollectedy) # Checks if collect car is currently selected
                            print("Waiting for car to be collected")
                            time.sleep(.1)
                        print("Car has been collected")
                        time.sleep(.1)
                        keyboard.press(Key.enter) # Collects the car
                        keyboard.release(Key.enter)
                    else:
                        print("Car collect option not selected")
                    print("Line: 159")
                    sellerdetails = pyautogui.pixel(sellerdetailsx, sellerdetailsy) # Search for the image of the seller details of the desired car on your screen
                    while sellerdetails != (255,0,134):
                        sellerdetails = pyautogui.pixel(sellerdetailsx, sellerdetailsy) # Search for the image of the seller details of the desired car on your screen
                        sellerdetails = pyautogui.pixel(sellerdetails2x, sellerdetails2y) # Search for the image of the seller details of the desired car on your screen
                    time.sleep(.2)
                    keyboard.press(Key.esc) # Backs out of the auction house buy menu
                    keyboard.release(Key.esc)
                    print("Line: 163")
                    time.sleep(.7)
                    auctionhouse = pyautogui.pixel(auctionhousex, auctionhousey) # Search for the image of the auctionhouse details of the desired car on your screen
                    while auctionhouse != (52,23,53):
                        auctionhouse = pyautogui.pixel(auctionhousex, auctionhousey) # Search for the image of the auctionhouse details of the desired car on your screen
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
                    buyoutfailed = pyautogui.pixel(buyoutfailedx, buyoutfailedy) # Search for the image 'buyoutfailed.png' on your screen
                    if buyoutfailed == (52,23,53):
                        print("Line: 268")
                        time.sleep(2)
                        keyboard.press(Key.enter) # Backs out of the successful buy-out screen
                        keyboard.release(Key.enter)
                        print("Line: 272")
                        time.sleep(.7)
                        print("Line: 274")
                        keyboard.press(Key.esc) # Backs out of the auction house buy menu
                        keyboard.release(Key.esc)
                        print("Line: 277")
                        time.sleep(.7)
                        print("Line: 279")
                        keyboard.press(Key.esc) # Returns to start location, before entering the search for the desired car
                        keyboard.release(Key.esc)
                        print("Line: 282")
                        # Resets all variables that are stopping previous lines of code from running
                        turbo = 0
                        Immortal_Snail = 1
                        supercharger = 1
                        chinas_population = 0
                        cat = 0
                        print("Line: 289")
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
