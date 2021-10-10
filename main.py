import os
import time
import sys
from colorama import init
from termcolor import colored
init()
import json
from pathlib import Path
import datetime
import olaylar
from engine.engine import *
import engine.engine as engine
import random
#Configuration
ver = "1.0"
t4="\t\t\t\t"
n2="\n\n"
random_olay = ["sessiz gun"]


#A1
sourcepath = Path(__file__).parents[0]
bilgiler = {"ad": "kerem"}

bilgiler_dos = os.path.abspath(os.path.join(sourcepath, "bilgiler.json"))
with open(bilgiler_dos, "r+") as bilgiler_dos:
    bilgiler = json.load(bilgiler_dos)
    try:
        if bilgiler["ilk"] == "ilk":
            bilgiler_dos.seek(0)
            bilgiler_dos.truncate() 
            print(f"{t4}Elevator Game Setup")
            ad=input("adınız:")
            veri = {"ad": ad}
            json.dump(veri, bilgiler_dos)
            Engine.clear()
    except KeyError:
        pass

#scene 1 start
def scene_1():
    print(f"""
{t4}/{'-'* 31}\\
{t4}|{t4}|
{t4}|{t4}|
{t4}|{t4}|
{t4}|{t4}|
{t4}|{t4}|
{t4}|{t4}|
{t4}|{t4}|
{t4}|{t4}|
{t4}|{t4}|
{t4}|{t4}|
{t4}|{t4}|
{t4}|{t4}|
{t4}|{t4}|
{t4}|{t4}|
{t4}|{t4}|
{t4}|{t4}|
{t4}|{t4}|
{t4}|{t4}|
{t4}|{t4}|
{t4}|{t4}|
{t4}\{'-'* 31}/""")
    #Formül
    #t4=16 ise 16 yı 2 ile çarparak 32 bulunur
    Engine.delay_print(f"\t\tMerhaba, {bilgiler['ad']} Bu Sessiz sakin 10 katlı apartmana hoşgeldin.\n\t\tGitmek istedğin katın numarasını yazarak o kata gidebilirsin.\n\t\t\tUnutma her kat farklı bir olay bulundurur.\n", sleep=0)
    while True:
        try:
            kat = input("kat:")
            if kat == "1":
                olaylar.kat_animasyonu(kat)

                olaylar.olay(random.choice(random_olay))
            elif kat == "dev-mode":
                olaylar.dev_mode()
            else:
                print(f"Geçersiz kat")
        except KeyboardInterrupt:
            print("\n...")
            exit()
#end of scene 1
#C1
while True:
    now = datetime.datetime.now()

    time = now.strftime("%H")
    
    if time == "04":
        print(f"{t4}Elevator {ver}\nMerhaba, {bilgiler['ad']} herkes uyurken oyun oynamak gibisi yok.{n2}1 yeni oyun")
    elif time == "11":
        print(f"{t4}Elevator {ver}\nMerhaba, {bilgiler['ad']} Yapımcıda oyunu bu saatlerde yapıyordu.{n2}1 yeni oyun")
    elif time == "18":
        print(f"{t4}Elevator {ver}\nMerhaba, {bilgiler['ad']} iyi akşamlar.{n2}1 yeni oyun")
    else:
        print(f"{t4}Elevator {ver}\nMerhaba, {bilgiler['ad']}{n2}1 yeni oyun")

    try:
        secim=input(">")
    except KeyboardInterrupt:
            print(f"\n...")
            exit()

    if secim == "1":
        Engine.clear()
        #sahne başlatılıyor
        scene_1()
