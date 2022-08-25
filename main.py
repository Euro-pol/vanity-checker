import requests
from colorama import Fore, init
import datetime
import time
init()
delay = float(input("Input delay: "))
choice = input("1. Check random words\n2. Check specific words from file\nInput choice: ")
filename = "session-" + datetime.datetime.now().strftime("%H-%M-%S") + ".txt"

def write(word):
    with open(filename, "a") as f:
        f.write(word + "\n")

def check(checkstring):
    r = requests.get("https://discord.com/api/v9/invites/" + checkstring)
    if (r.status_code == 200):
        print(Fore.RED + "discord.gg/" + checkstring + " is taken!")
    elif (r.status_code == 404):
        write("discord.gg/" + checkstring)
        print(Fore.GREEN + "discord.gg/" + checkstring + " is free!")
    elif (r.status_code == 429):
        print(Fore.RED + "Too many requests, waiting...")
        time.sleep(1)
        check(checkstring)

def checkfile():
    with open("words.txt", "r") as f:
        for line in f.read().splitlines():
            check(line)

            time.sleep(delay)

def checkwords():
    word = requests.get("https://random-word-api.herokuapp.com/word").json()[0]
    check(word)
    time.sleep(delay)

if __name__ == "__main__":
    if (choice == "1"):
        while True:
            checkwords()
    elif (choice == "2"):
        checkfile()
