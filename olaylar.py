import os
import os
import time
import sys
from colorama import init
from termcolor import colored
from engine.engine import Engine
import random
try:
    import playsound
except:
    print("playsound kütüphanesi bulunamadı!")

remzi = """
     #######
    ##: _ :##
    #########
     #######
    #########
   ###########
   ###########
   ###########
   ###########
   ###########
   ###########
   ###########
    ##     ##
    ##     ##
    ##     ##
   ###     ###
"""

yilmaz = """
    ##########
   ############
   ###: __ :###
   ###########
    #########
   ###########
  #############
  #############
#################
#################
#################
#################
  #############
  #############
   ##       ##
   ##       ##
   ##       ##
   ##       ##
  ###       ###
"""
#Configuration
ver = "1.0"
t4="\t\t\t\t"
n2="\n\n"

def kat_animasyonu(kat):
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
{t4}|\t      Kat {kat}\t\t|
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
    playsound.playsound("sounds/ding.mp3")
    Engine.clear()

def dev_mode():
    Engine.clear()
    print(f"{t4}Elevator Game Developer/Test mode")
    print("Engine version: " + Engine.version)
#No archiment Mode
def olay(olay):
    if olay == "sessiz gun":
        print(remzi)
        Engine.delay_print("*tak* *tak*\n-Merhaba efendim ben yan komuşunuz, yatmaya çalışıyorum ama evinizden çok ses geliyor.", sleep=0.10)
        time.sleep(1)
        Engine.clear()
        print(yilmaz)
        Engine.delay_print("+Evet ne olmuş yani ses geliyorsa.", sleep=0.10)
        time.sleep(1)
        Engine.clear()
        print(remzi)
        Engine.delay_print("-Yatamayıyoruz, kabalık etmek gibi olmasında öküz gibi gecenin bu saatinde müzik dinliyorsunuz.\n", sleep=0.10)
        time.sleep(1)
        Engine.clear()
        print(yilmaz)
        Engine.delay_print("+Sen bana ne cüretle öküz dersin lan sen!\n", sleep=0.10)
        playsound.playsound("sounds/shoot.mp3")
        time.sleep(2)
        Engine.delay_print("...")
        Engine.clear()
        Engine.delay_print("Sanırım burada göreceğimizi gördük.\n")