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

    def enterauctionhouse():
        # Search and enter the auction house
        global start

        loop1 = True
        while loop1 == True: # Allows the program to loop
            print("starting program")
            time.sleep(.9)
            ahsearch = pyautogui.pixel(ahsearchx, ahsearchy)
            while ahsearch == (255,0,134):
                #searchah = pyautogui.pixel(searchahx, searchahy)
                #while searchah != (255, 0, 134):
                #    print("Make sure you have the search auction house selected")
                #    searchah = pyautogui.pixel(searchahx, searchahy)
                #    time.sleep(.5)
                start = time.time()
                keyboard.press(Key.enter) # Enters auction house menu
                keyboard.release(Key.enter)
                print("Entering Auction House")
                ahsearch = pyautogui.pixel(ahsearchx, ahsearchy)
                time.sleep(.01)
            time.sleep(.5) 
            loop2 = True
            while loop2 == True:
                print("Line: 66")
                sconfirm = pyautogui.pixel(sconfirmx, sconfirmy)
                if sconfirm == (255,0,134):     # Confirms if you are in ah search menu
                    print("Checking if you are currently in ah")
                    keyboard.press(Key.enter) # Searches the auction house
                    keyboard.release(Key.enter)
                    loop2 = False
                    break # ################################################################### might work or might not work
                loop1 = False
                break

            checkforauction()
    
    def checkforauction():
        # Checks the auction house for an available auction
        auctionavailable = False

        printer = True
        Rear_Window = pyautogui.pixel(Rear_Windowx, Rear_Windowy)
        while Rear_Window != (255,222,57):
            if printer == True:                
                print("Checking if there are any cars up for auction")
                printer = False
            Rear_Window = pyautogui.pixel(Rear_Windowx, Rear_Windowy) # Checks to see if you are in the auction house - viewing the cars up for auction
        #if Rear_Window == (255,222,57):
        time.sleep(.52)
        car = pyautogui.pixel(carx, cary) # Search for the image of the auctionhouse details of the desired car on your screen
        if car == (52,23,53):
            auctionavailable = True
            time.sleep(0.1)
            px = pyautogui.pixel(pxx, pxy)
            if px == (247,247,247):
                listingloading = 1
                printer = True
                while listingloading == 1:
                    if printer == True:
                        print("Line: 84")
                        printer = False
                    David_Joesph = pyautogui.pixel(David_Joesphx, David_Joesphy) # Gets the RGB Values for the pixel at the location X:873 Y:234
                    print(David_Joesph) # Prints the RGB Values for the pixel at the location X:873 Y:234
                    if David_Joesph != (247,247,247): # Checks if the RGB values are not equal to RGB(247,247,247)
                        auctionavailable = True
                        listingloading = 0
                        break # ################################################################### might work or might not work
        else: # If there is no car avaliable for purchase on the auction house
            auctionavailable = False

        
        if auctionavailable == True:
            attemptbuyout()
        else:
            returntostart()
    
    def attemptbuyout():
        # Attempts to buyout the car
####################################################################### replace time.sleeps with pixel checks to attempt to speed up the process

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
            

        buyoutoutcome()
    
    def buyoutoutcome():
        # Waits and checks for the buyout outcome
        print("buyoutoutcome")
        time.sleep(.5)
        printer = True
        buyoutoutcomewait = pyautogui.pixel(buyoutoutcomex, buyoutoutcomey) # Checks to see if the buyout outcome is still loading
        while buyoutoutcomewait != (52,23,53):
            buyoutoutcomewait = pyautogui.pixel(buyoutoutcomex, buyoutoutcomey) # Checks to see if the buyout outcome is still loading
            if printer == True:
                print("Waiting for buyout outcome loading popup")
                printer = False
        printer = True
        buyoutoutcomewait = pyautogui.pixel(buyoutoutcomex, buyoutoutcomey) # Checks to see if the buyout outcome is still loading
        while buyoutoutcomewait == (52,23,53):
            buyoutoutcomewait = pyautogui.pixel(buyoutoutcomex, buyoutoutcomey) # Checks to see if the buyout outcome is still loading
            if printer == True:
                print("Waiting for buyout outcome")
                printer = False
        buyoutoutcomewait = pyautogui.pixel(buyoutoutcomex, buyoutoutcomey) # Checks to see if the buyout outcome is still loading
        if buyoutoutcomewait != (52,23,53):
            print("buyoutoutcomewait not same colour")
            time.sleep(.5)
            #   ################################################ maybe change to use only one pixel check rather than 2 pixel checks
            buyoutfailed = pyautogui.pixel(buyoutfailedx, buyoutfailedy) # Checks if the buyout failed
            buyoutsuccessful = pyautogui.pixel(buyoutx, buyouty) # Checks if the buyout was successful
            if buyoutsuccessful == (52,23,53):
                buyoutoutcomesuccessful()
            elif buyoutfailed == (52,23,53):
                buyoutoutcomefailed()
        else:
            print("buyoutoutcome restart")
            buyoutoutcome()



    def buyoutoutcomesuccessful():
        # Collects car and returns to auction house


        #   Buyout Successful
        print("Buyout Successful")

        keyboard.press(Key.enter) # Backs out of the successful buy-out screen
        keyboard.release(Key.enter)
        print("Line: 157")
        printer = True
        collectcar = pyautogui.pixel(collectcarx, collectcary) # Checks if collect car is currently selected
        while collectcar != (255,0,134):
            collectcar = pyautogui.pixel(collectcarx, collectcary) # Checks if collect car is currently selected
            collectcar = pyautogui.pixel(collectcar1x, collectcar1y) # Checks if collect car is currently selected
            if printer == True:
                print("Car collect option not selected")
                printer = False
            time.sleep(.01)
        if collectcar == (255,0,134):
            print("Collect car is selected")
            time.sleep(.1)
            keyboard.press(Key.enter) # Collects the car
            keyboard.release(Key.enter)
            time.sleep(.5)
            printer = True
            collectcar = pyautogui.pixel(collectcarx, collectcary) # Checks if collect car is currently selected
            while collectcar == (255,0,134):
                collectcar = pyautogui.pixel(collectcarx, collectcary) # Checks if collect car is currently selected
                keyboard.press(Key.enter) # Collects the car
                keyboard.release(Key.enter)
                if printer == True:
                    print("Attempting to collect the car")
                    printer = False
            printer = True
            carcollected = pyautogui.pixel(carcollectedx, carcollectedy) # Checks if collect car is currently selected
            while carcollected != (52, 23, 53):
                carcollected = pyautogui.pixel(carcollectedx, carcollectedy) # Checks if collect car is currently selected
                if printer == True:
                    print("Waiting for car to be collected")
                    printer = False
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


        time.sleep(.7)
        print("Line: 274")
        keyboard.press(Key.esc) # Backs out of the auction house shortcut menu
        keyboard.release(Key.esc)
        print("Line: 277")


        returntostart()
    
    def buyoutoutcomefailed():
        # Exits back to auction house shortcut menu


        #   Buyout Failed                   ####################################################################### replace time.sleeps with pixel checks to attempt to speed up the process
        
        print("Buyout Failed")
        time.sleep(.1)
        keyboard.press(Key.enter) # Backs out of the successful buy-out screen
        keyboard.release(Key.enter)
        print("Line: 272")
        time.sleep(.7)

        time.sleep(.7)
        print("Line: 274")
        keyboard.press(Key.esc) # Backs out of the auction house shortcut menu
        keyboard.release(Key.esc)
        print("Line: 277")

        returntostart()

    def returntostart():
        # Returns from the auction house to the start
        

        print("Line: 163")
        time.sleep(.7)
        Rear_Window = pyautogui.pixel(Rear_Windowx, Rear_Windowy)
        while Rear_Window != (255,222,57):
            if printer == True:                
                print("Checking if there are any cars up for auction")
                printer = False
            Rear_Window = pyautogui.pixel(Rear_Windowx, Rear_Windowy) # Checks to see if you are in the auction house - viewing the cars up for auction
        print("Line: 165")
        keyboard.press(Key.esc) # Returns to start location, before entering the search for the desired car
        keyboard.release(Key.esc)
        print("Line: 169")

        end = time.time()
        print("loop time:", end-start)

        enterauctionhouse()



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
    buyoutoutcomex = int(0.33489583333 * MonitorWidth)        #w:643 h:442
    buyoutoutcomey = int(0.40925925925 * MonitorHeight)
    buyoutx = int(0.3328125 * MonitorWidth)               #w:639 h:460
    buyouty = int(0.42592592592 * MonitorHeight)
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
    buyoutfailedx = int(0.33020833333 * MonitorWidth)             #w:634 h:532
    buyoutfailedy = int(0.49259259259 * MonitorHeight)
    searchahx = int(0.16770833333 * MonitorWidth)
    searchahy = int(0.29074074074 * MonitorHeight)

    time.sleep(2)

    consoleoutput.set("Welcome to the Forza Auction House Sniper Bot\nProgram Running")

    ahsearch = pyautogui.pixel(ahsearchx, ahsearchy) # Search for the image 'ahsearch.png' on your screen 0.171875 * MonitorWidth
    sconfirm = pyautogui.pixel(sconfirmx, sconfirmy) # Search for the image 'searchconfirm.png' on your screen


    enterauctionhouse()


    
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
