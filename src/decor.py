def mainUI():
	# print("Welcome to Desmos.ai")
	start()



if __name__ == "__main__":
	mainUI()

userPageOn = ""

def start():

	printMenu()
	
	agree = input("DO YOU AGREE TO THE GNU GENERAL PUBLIC LICENSE V3.0? (Y/N) ")

	if agree == "Y":
		getUser()
	elif agree == "N":
		print("Bye!")
	else:
		print("ERROR, NOT AN OPTION!")

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
		getUser()
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



def printHelp():

	print("DESMOS.AI IS A PYTHON SCRIPT THAT GENERATES THE PROMPT THAT YOU TYPE INTO AN IMAGE ON THE DESMOS GRAPHING CALCULATOR.")

	print(r"""
			[START]                   [BACK]                   [CONTRIBUTE]                   [EXIT]          
		""")

	print("STILL STUCK? PLEASE EMAIL ME AT RAYFORD.li@GMAIL.COM. ")
	getUser()