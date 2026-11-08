## ==========================================
## Project: LOOT GENERATOR
## Author: Meakz
## Purpose: Learn the Random Module through Loot Generation, with .WAV sound effects for a more of an immersive experience WITH A CONFIG!.
## ------------------------------------------
## Version: 1.0
## Created: 07/11/2026
## ==========================================


import os
import time
import SmallCrateScript
import pygame
import Config

pygame.mixer.init()
loot_amount = Config.loot_amount
Small_Crate_Name = Config.Small_Crate_Name
duplicate_items = Config.duplicate_items
SmallCrate = pygame.mixer.Sound("SmallCrate.wav")


def open_config():
    global Small_Crate_Name,duplicate_items,loot_amount
    print(f"Crate Name = {Small_Crate_Name}")
    print(f"duplicate items = {duplicate_items}")
    print(f"Loot Multiplier = {loot_amount}")
    time.sleep(5)
    main_screen_terminal()
    
def main_screen_terminal():
    global choice_ost, Small_Crate_Name
    os.system("cls")
    print(f"1. Loot {Small_Crate_Name} ")
    
    choice_ost = input(">> ").lower()
    
    if choice_ost == "1":
        SmallCrateScript.found_crate_load_sound()
        time.sleep(1.4)
        main_screen_terminal()
        
    elif choice_ost == "config":
        open_config()
        
    else:
        print("Invalid, Please Use Numbers or type 'Config' To See Some Values!")
        time.sleep(1.4)
        input("Press Enter to retry! (Any text is fine!) >> ")
        time.sleep(1)
        main_screen_terminal()
    

main_screen_terminal()
    



    




