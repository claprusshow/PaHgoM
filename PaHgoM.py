import random
from random import Random, randint
import sys
from time import sleep
from colorama import init
init()
from colorama import Fore, Back, Style

words = '''
 /$$$$$$$            /$$   /$$                     /$$      /$$
| $$__  $$          | $$  | $$                    | $$$    /$$$
| $$  \ $$  /$$$$$$ | $$  | $$  /$$$$$$   /$$$$$$ | $$$$  /$$$$
| $$$$$$$/ |____  $$| $$$$$$$$ /$$__  $$ /$$__  $$| $$ $$/$$ $$
| $$____/   /$$$$$$$| $$__  $$| $$  \ $$| $$  \ $$| $$  $$$| $$
| $$       /$$__  $$| $$  | $$| $$  | $$| $$  | $$| $$\  $ | $$
| $$      |  $$$$$$$| $$  | $$|  $$$$$$$|  $$$$$$/| $$ \/  | $$
|__/       \_______/|__/  |__/ \____  $$ \______/ |__/     |__/
                               /$$  \ $$                       
                              |  $$$$$$/                       
                               \______/                       
                               
                    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
                    |T|G|:| |@|H|A|C|K|E|R|_|P|H|O|N|E|_|V|I|P|
                    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+'''
for char in words:
    sleep(0.007)
    sys.stdout.write(char)
    sys.stdout.flush()

while True:

    print(Fore.WHITE + '\n\n\n► От сколько до скольки нужен рандом?\n')
    print(Fore.WHITE + '1 ⇒  От 1 до 10')
    print(Fore.WHITE + '2 ⇒  От 1 до 100')
    print(Fore.WHITE + '3 ⇒  От 1 до 1000')
    print(Fore.WHITE + '4 ⇒  От 1 до 10000')
    randomm = input('\n► Выбери одну из цифр: ')

    if randomm == '1':
        print(Fore.GREEN + '\n\n✅ Результат: ' + str(random.randint(1, 10)))

    elif randomm == '2':
        print(Fore.MAGENTA + '\n\n✅ Результат: ' + str(random.randint(1, 100)))

    elif randomm == '3':
        print(Fore.YELLOW + '\n\n✅ Результат: ' + str(random.randint(1, 1000)))

    elif randomm == '4':
        print(Fore.BLUE + '\n\n✅ Результат: ' + str(random.randint(1, 10000)))

    print(Fore.WHITE + '\n► Нажми Ctrl + Z чтобы остановить рандом!')
