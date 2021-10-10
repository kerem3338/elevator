"""
elevator engine is a console game engine written to improve the elevator game
If you found a bug or an error, send an email to zoda@vuhuv.com or diosyazilim@gmail.com
"""
import time
import sys
import os
import platform
from win32api import GetSystemMetrics

t4="\t\t\t\t"
n2="\n\n"
class Engine:
    version = "1.0.0"
    def free_space():
        import psutil

        hdd = psutil.disk_usage('/')
        return (hdd.free / (2**30))
    def clear():
        """clear screen for all os"""
        if os.name == "nt":
            os.system("cls")
        else:
            os.system("clear")

    def draw_text(width, text, spacech=" ", lf="left"):
        if lf == "left":
            print(f"{spacech*width}{text}")
        if lf == "lf":
            print(f"{spacech*width}{text}{spacech*width}")
        else:
            print(f"Invilad mode {lf}")
                
        
    def get_screen_size():
        """return screen size"""
        screen = GetSystemMetrics(0), GetSystemMetrics(1)
        return screen
    def delay_print(text, sleep=0.25):
        for c in text:
            sys.stdout.write(c)
            sys.stdout.flush()
            time.sleep(sleep)


