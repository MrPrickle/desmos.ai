def mainUI():
    # print("Welcome to Desmos.ai")
    printMenu()
    


if __name__ == "__main__":
    mainUI()

userPageOn = ""

def getUser():
    option = input("PLEASE TYPE TO SELECT AN OPTION(CASE-SENSITIVE): ")

    if option == "START":
        printHelp()
    elif option == "HELP":
        printHelp()
    elif option == "CONTRIBUTE":
        printHelp()
    elif option == "EXIT":
        print("BYE!")
    elif option == "BACK"  and userPageOn != "MENU":
        printMenu()
    else:
        print("ERROR, NOT AN OPTION!")
        getUser()

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
            [START]                   [HELP]                   [CONTRIBUTE]                   [EXIT]          
        """)
    
    userPageOn = "MENU"

    getUser()
    


def printHelp():

    print("DESMOS.AI IS A PYTHON SCRIPT THAT GENERATES THE PROMPT THAT YOU TYPE INTO AN IMAGE ON THE DESMOS GRAPHING CALCULATOR.")

    print(r"""
            [START]                   [BACK]                   [CONTRIBUTE]                   [EXIT]          
        """)

    print("STILL STUCK? PLEASE EMAIL ME AT RAYFORD.li@GMAIL.COM. ")
    getUser()