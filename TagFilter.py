#!/usr/bin/env python3

from bs4 import BeautifulSoup
from urllib.request import urlopen
import itertools
from colorama import Fore

print(Fore.CYAN)
print("""
╔════╗───────╔═══╗╔╗╔╗
║╔╗╔╗║───────║╔══╝║╠╝╚╗
╚╝║║╠╩═╦══╗──║╚══╦╣╠╗╔╬══╦═╗
──║║║╔╗║╔╗╠══╣╔══╬╣║║║║║═╣╔╝
──║║║╔╗║╚╝╠══╣║──║║╚╣╚╣║═╣║
──╚╝╚╝╚╩═╗║──╚╝──╚╩═╩═╩══╩╝
───────╔═╝║
───────╚══╝""")
print("Filter through website tags quickly.")

def menu():

    print()
    print(Fore.RED)
    add = str(input("Add website url here: "))
    url = urlopen(add)
    print()
    soup = BeautifulSoup(url.read(), 'lxml')

    for i in itertools.count(1,1):
        print(Fore.CYAN)
        tag = str(input("Add html tag here: "))
        print()
        print("Examples of tags are: 'a', 'p', 'div', etc.")
        print(Fore.RED)
        link = soup.find_all(f'{tag}')
        print(link)
        print()

menu()
