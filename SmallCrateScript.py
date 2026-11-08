import os
import time
import random
import Config
import pygame
import sys
def resource_path(filename):
    if getattr(sys, 'frozen', False):
        base_path = sys._MEIPASS
    else:
        base_path = os.path.dirname(os.path.abspath(__file__))

    return os.path.join(base_path, filename)

pygame.mixer.init()

SmallCrate = pygame.mixer.Sound(resource_path("SmallCrate.wav"))

def found_crate_load_sound():
    print("Opening Crate!")
    SmallCrate.play()
    time.sleep(2)
    os.system("cls")
    time.sleep(1)
    load_crate()
    
def load_crate():
    global exit_leave
    Config.pick_item()
    time.sleep(0.5)
    Config.pick_item()
    time.sleep(0.4)
    Config.pick_item()
    time.sleep(0.3)
    Config.pick_item()
    time.sleep(0.2)
    Config.pick_item()
    time.sleep(1)
    exit_leave = input("Press Enter To Loot All >> ")
    if exit_leave == "":
        return True
        
    else:
        return True
    
    