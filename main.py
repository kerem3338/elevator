import os
import time
import sys
from colorama import init
from termcolor import colored
init()
import json
from pathlib import Path
import datetime

#Configuration
ver = "1.0"
t4="\t\t\t\t"
n2="\n\n"

def clear():
    """clear screen for all os"""
    if os.name == "Windows":
        
        os.system("cls")
    else:
        os.system("clear")
#A1
sourcepath = Path(__file__).parents[1]
bilgiler_dos = os.path.abspath(os.path.join(sourcepath, "bilgi.json")).replace("\\", "\\\\")
with open(bilgiler_dos, "r+") as bilgiler:
    try:
        bilgiler = json.load(bilgiler)
    except json.decoder.JSONDecodeError:
        print(f"{t4}Elevator Game Setup")
        ad=input("adınız:")
        veri = {"ad": ad}
        json.dump(veri, bilgiler)
        clear()

#B1
def scene_1():
    print(f"""
{t4}/{'-'* 31}\
{t4}|{t4}|
{t4}|{t4}|
{t4}|{t4}|
{t4}\{'-'* 31}/""")
#Formül
#t4=16 ise 16 yı 2 ile çarparak 32 bulunur


#C1
while True:
    now = datetime.datetime.now()

    time = now.strftime("%H")
    
    if time == "04":
        print(f"{t4}Elevator 1.0\nMerhaba, {bilgiler['ad']} herkes uyurken oyun oynamak gibisi yok.{n2}1 yeni oyun")
    elif time == "18":
        print(f"{t4}Elevator 1.0\nMerhaba, {bilgiler['ad']} iyi akşamlar.{n2}1 yeni oyun")
    else:
        print(f"{t4}Elevator 1.0\nMerhaba, {bilgiler['ad']}{n2}1 yeni oyun")
    secim=input(">")
    if secim == "1":
        clear()
        #sahne başlatılıyor
        scene_1()
