import time
import sys
import os
import requests
import cv2
import numpy as np

import app
import structure
import desmos_test

# Add the 'src' directory to the Python path

current_dir = os.path.dirname(os.path.abspath(__file__))
print(f"Current directory: {current_dir}")

scripts_dir = os.path.join(current_dir, 'src')
print(f"Scripts directory: {scripts_dir}")

sys.path.insert(0, scripts_dir)

userPageOn = ""

def printMenuWithoutOptions():
    print(r"""
$$$$$$$\  $$$$$$$$\  $$$$$$\  $$\      $$\  $$$$$$\   $$$$$$\                   $$$$$$\  $$$$$$\ 
$$  __$$\ $$  _____|$$  __$$\ $$$\    $$$ |$$  __$$\ $$  __$$\                 $$  __$$\ \_$$  _|
$$ |  $$ |$$ |      $$ /  \__|$$$$\  $$$$ |$$ /  $$ |$$ /  \__|                $$ /  $$ |  $$ |  
$$ |  $$ |$$$$$\    \$$$$$$\  $$\$$\$$ $$ |$$ |  $$ |\$$$$$$\                  $$$$$$$$ |  $$ |  
$$ |  $$ |$$  __|    \____$$\ $$ \$$$  $$ |$$ |  $$ | \____$$\                 $$  __$$ |  $$ |  
$$ |  $$ |$$ |      $$\   $$ |$$ |\$  /$$ |$$ |  $$ |$$\   $$ |                $$ |  $$ |  $$ |  
$$$$$$$  |$$$$$$$$\ \$$$$$$  |$$ | \_/ $$ | $$$$$$  |\$$$$$$  |      $$\       $$ |  $$ |$$$$$$\ 
\_______/ \________| \______/ \__|     \__| \______/  \______/       \__|      \__|  \__|\______|
    """)
	
    print(r"""
    
MrPrickle 2024
https://github.com/MrPrickle/desmos.ai
	
    """)

    print(r"""% COPYRIGHT %""")
    print(r"""
©Copyright MrPrickle 2024. This program is licensed under the [GNU General Public License](https://github.com/MrPrickle/desmos.ai/blob/main/LICENSE). Please provide proper credit to the author (MrPrickle) in any public media that uses this software.""")
	
    print("")

    userPageOn = "MENU"

def printMenu():
    print(r"""
$$$$$$$\  $$$$$$$$\  $$$$$$\  $$\      $$\  $$$$$$\   $$$$$$\                   $$$$$$\  $$$$$$\ 
$$  __$$\ $$  _____|$$  __$$\ $$$\    $$$ |$$  __$$\ $$  __$$\                 $$  __$$\ \_$$  _|
$$ |  $$ |$$ |      $$ /  \__|$$$$\  $$$$ |$$ /  $$ |$$ /  \__|                $$ /  $$ |  $$ |  
$$ |  $$ |$$$$$\    \$$$$$$\  $$\$$\$$ $$ |$$ |  $$ |\$$$$$$\                  $$$$$$$$ |  $$ |  
$$ |  $$ |$$  __|    \____$$\ $$ \$$$  $$ |$$ |  $$ | \____$$\                 $$  __$$ |  $$ |  
$$ |  $$ |$$ |      $$\   $$ |$$ |\$  /$$ |$$ |  $$ |$$\   $$ |                $$ |  $$ |  $$ |  
$$$$$$$  |$$$$$$$$\ \$$$$$$  |$$ | \_/ $$ | $$$$$$  |\$$$$$$  |      $$\       $$ |  $$ |$$$$$$\ 
\_______/ \________| \______/ \__|     \__| \______/  \______/       \__|      \__|  \__|\______|
    """)
	
    print(r"""
    
MrPrickle 2024
https://github.com/MrPrickle/desmos.ai
	
    """)

    # print("% COPYRIGHT %")
    # print("©Copyright MrPrickle 2024. This program is licensed under the [GNU General Public License](https://github.com/MrPrickle/desmos.ai/blob/main/LICENSE). Please provide proper credit to the author (MrPrickle) in any public media that uses this software.")
	
    # print("")

    # print("% End-User License Agreement %")
    # print("By using Desmos.ai, you agree to comply to the [Desmos Terms of Service](https://www.desmos.com/terms). The Software and related documentation are provided “AS IS” and without any warranty of any kind. Desmos.ai is not responsible for any User application or modification that constitutes a breach in terms. User acknowledges and agrees that the use of the Software is at the User's sole risk.")

    printOptions()

    userPageOn = "MENU"

def printOptions():
    print(r"""
[START]                   [HELP]                   [CONTRIBUTE]                   [EXIT]          
		""")
	
def loading():
    for i in range(81):  # Double the number of iterations
        progress = '=' * (i // 2)  # Adjust the progress calculation
        if i == 80:  # When progress reaches maximum
            percentage = 100
        else:
            percentage = (i / 80) * 100  # Calculate the percentage based on the total progress
        sys.stdout.write("\rLOADING: [{}] {:.1f}%".format(progress.ljust(40), percentage))  # Adjust the formatting
        sys.stdout.flush()
        time.sleep(0.05)  # Adjust the delay here to maintain smooth animation

    sys.stdout.write("\n")  # Add a newline after completion
    sys.stdout.flush()

def start():
    printMenuWithoutOptions()
    agree = input("DO YOU AGREE? (Y/N) ")

    if agree == "Y":
        print("PROGRESS:")
        # print("PROGRESS:", end = "")
        # print("[", end = "")
        
        loading()  # Correct indentation for calling loading()
        printOptions()
        getUser()
    elif agree == "N":
        print("Bye!")
    else:
        print("ERROR, NOT AN OPTION!")
        start()
		

def getUser():
    
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")

    option = input("PLEASE TYPE TO SELECT AN OPTION(CASE-SENSITIVE): ")

    if option == "START":
        startCalculations()
    elif option == "HELP":
        printHelp()
    elif option == "CONTRIBUTE":
        printContirbute()
    elif option == "EXIT":
        print("BYE!")
    elif option == "BACK"  and userPageOn != "MENU":
        printMenu()
        getUser()
    else:
        print("ERROR, NOT AN OPTION!")
        getUser()
		
def printHelp():
    
    print("")
    print("")

    print("DESMOS.AI IS A PYTHON SCRIPT THAT GENERATES THE PROMPT THAT YOU TYPE INTO AN IMAGE ON THE DESMOS GRAPHING CALCULATOR.")

    print(r"""
			[START]                   [BACK]                   [CONTRIBUTE]                   [EXIT]          
		""")

    print("STILL STUCK? PLEASE EMAIL ME AT RAYFORD.li@GMAIL.COM. ")
    getUser()
	
def printContirbute():
	
    print("")
    print("")

    print("TODO: Add option to save the photo you generated")

    printOptions()
    getUser()

def mainUI():
	# print("Welcome to Desmos.ai")
    loading()
    start()

def startCalculations():
    print("")
    print("")

    print("Starting... Please wait...")
    time.sleep(2)
    userPrompt = input("What do you want to be drawn on desmos? ")
    app.getPrompt(userPrompt)
    app.startUp()

    print("")
    print("")
    
    print("Please copy and paste latex.txt to desmos!")

if __name__ == "__main__":
	mainUI()