# this file imported on main file(RussianRulet.py)
from tqdm import tqdm
from time import sleep
from khayyam import JalaliDate
from colorama import Fore
import sys
import os
import random
from pyfiglet import figlet_format
from rainbowtext import text
import platform

def cl():
    if platform.system() == 'Linux':
        return "clear"
    elif platform.system == 'Windows':
        return "cls"

# var's
data_path = "data/data.txt" # data file path

date_time = JalaliDate.today() # jalali date
#

if __name__ == '__main__': # sey to user
    os.system(cl())
    print(Fore.RED, 'run RussianRulet.py ')
    sleep(6)
    sys.exit()


# funcs

def ReadingData():
    f = open("data/data.txt", "r")
    print(Fore.WHITE)
    print(f.read())
    f.close()


def InstallPip(): # installing pip
    os.system("pip install khayyam")
    os.system("pip install selenium")
    os.system("pip install time")
    os.system("pip install colorama")
    os.system("pip install sys")
    os.system("pip install tqdm")



def loading(a): # loading view 
    for i in tqdm (range (100), 
               desc="Loading ...", 
               ascii=False, ncols=75):
        sleep(a)





rd, gn, lgn, yw, lrd, be, pe = '\033[00;31m', '\033[00;32m', '\033[01;32m', '\033[01;33m', '\033[01;31m', '\033[00;34m', '\033[01;35m'
cn = '\033[00;36m' # colors



def view(a): # app  view
    
    os.system(cl())

    print(Fore.GREEN)
    print(a)

    print(Fore.BLUE)

    print(Fore.YELLOW)
    print("_________________________________________________________________                                                                                             ")

    print(text(figlet_format("amirhosin282", font="slant")))

    print(Fore.YELLOW)
    print("_________________________________________________________________                                                                                             ")

    print(Fore.RED,'    time',Fore.GREEN, a)
    print(Fore.RED,'    email',Fore.GREEN,' amirhosinasdpwr@gmail.com')

    print(Fore.RED,'    by',Fore.BLUE,' amirhosin282')
    print(Fore.WHITE)

    print(Fore.YELLOW)
    print("_________________________________________________________________                                                                                             ")
    
    
    
    
def view2(): # print 1 . 2 . 3
    print(Fore.GREEN)
    sleep(2)
    print("3")
    sleep(2)
    print("2")
    sleep(2)
    print("1")
    print(Fore.YELLOW)
    print("_________________________________________________________________                                                                                             ")
    
    
def exit(a, b): # a func for giving exit from user
    sleep(a)
    print(Fore.RED, "good bye")
    sleep(b)
    sys.exit()
    
    

def numb(a):
    file = open(a, "+r")
    numb = str(file.read())
    file.close()
    return numb


def ChengNumb(a, b):
    os.remove(a)
    file = open(a, "a+")
    file.write(str(int(b) + 1))
    file.close()
    
  
#
