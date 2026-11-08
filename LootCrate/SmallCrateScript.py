import os
import time
import random
import Config
import pygame
pygame.mixer.init()

SmallCrate = pygame.mixer.Sound("SmallCrate.wav")

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
    
    