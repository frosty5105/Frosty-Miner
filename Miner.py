import colorama
from colorama import Fore
import string
import requests
import time
from time import sleep
import os
import random




colors = list(vars(colorama.Fore).values())

def gen():
    print("Ctrl + C To Exit")
    Start = True
    while Start == True:
        try:
            str1 = ''.join((random.choice(string.ascii_letters) for x in range(40)))  
            str1 += ''.join((random.choice(string.digits) for x in range(10)))  
        
            sam_list = list(str1) # it converts the string to list.  
            random.shuffle(sam_list) # It uses a random.shuffle() function to shuffle the string.  
            text = ''.join(sam_list)  
            bad_colors = ['BLACK', 'WHITE', 'LIGHTBLACK_EX', 'RESET']
            codes = vars(colorama.Fore)
            colors = [codes[color] for color in codes if color not in bad_colors]
            colored_lines = [random.choice(colors) + line for line in text.split('\n')]
            time.sleep(0.1)
            print('\n'.join(colored_lines) + "| 0.0 BTC")
        except:
            print("Fatal Error Has Occured Or Program was Interrupted")
            print("\nBtc Mined: 0\n")
            print("You Are Using The Free Version So Expect Low Cracking Rates\nFor Extremely Higher Cracking Rates Please Contact _ImFrosty5105 On Discord To Purchase Deluxe Version With Premium Wallets And Faster Cracking Rates")
            input("Press Any Key To Exit:")
            exit()




def start():
  
  os.system('cls' if os.name == 'nt' else 'clear')
  print(colorama.Fore.CYAN, """
  
 /$$$$$$$$                              /$$                     /$$      /$$ /$$                              
| $$_____/                             | $$                    | $$$    /$$$|__/                              
| $$     /$$$$$$   /$$$$$$   /$$$$$$$ /$$$$$$   /$$   /$$      | $$$$  /$$$$ /$$ /$$$$$$$   /$$$$$$   /$$$$$$ 
| $$$$$ /$$__  $$ /$$__  $$ /$$_____/|_  $$_/  | $$  | $$      | $$ $$/$$ $$| $$| $$__  $$ /$$__  $$ /$$__  $$
| $$__/| $$  \__/| $$  \ $$|  $$$$$$   | $$    | $$  | $$      | $$  $$$| $$| $$| $$  \ $$| $$$$$$$$| $$  \__/
| $$   | $$      | $$  | $$ \____  $$  | $$ /$$| $$  | $$      | $$\  $ | $$| $$| $$  | $$| $$_____/| $$      
| $$   | $$      |  $$$$$$/ /$$$$$$$/  |  $$$$/|  $$$$$$$      | $$ \/  | $$| $$| $$  | $$|  $$$$$$$| $$      
|__/   |__/       \______/ |_______/    \___/   \____  $$      |__/     |__/|__/|__/  |__/ \_______/|__/      
                                                /$$  | $$                                                     
                                               |  $$$$$$/                                                     
                                                \______/                                                      

  
  
  """)

def checkinternet():
    print(colorama.Fore.GREEN, "Checking Wifi Connection")
    time.sleep(1)
    print(colorama.Fore.RED, ".")
    time.sleep(1)
    print(colorama.Fore.RED, "..")
    time.sleep(1)
    print(colorama.Fore.RED, "...")
    time.sleep(1)
    print(colorama.Fore.RED, "....")
    time.sleep(1)
    response = requests.get("https://google.com")
    if response.status_code == 200:
        input("Connection Secured, Enter To Continue:")
        gen()
    else:
        input("Connection Failed, Enter To Exit:")
        exit()





start()
checkinternet()