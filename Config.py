import random
import os
# =====================Config============================

max_number = 12 # MAXIMUM ITEM NUMBER - Determines the highest item number that can be selected.
low_number = 1 # MINIMUM ITEM NUMBER - Determines the lowest item number that can be selected.
duplicate_items = False # DUPLICATE ITEMS - True = Allows duplicate items | False = Prevents duplicate items.
loot_amount = 1 # LOOT AMOUNT - 1 = 5 Items | 2 = 10 Items | 3 = 15 Items etc.
Small_Crate_Name = "Small Crate" # CRATE NAME - Determines the displayed name of the crate.
# =======================================================

# Small Crate Items

def pick_item():
    if duplicate_items == True:
        item_choice = random.choices(list(items.keys()), k=loot_amount)
    else:
        item_choice = random.sample(list(items.keys()), k=loot_amount)

    for item in item_choice:
        print(items[item])
    
items = {
    0: "Scrap",
    1: "Pistol",
    2: "Rope",
    3: "Hatchet",
    4: "Tarp",
    5: "Spear",
    6: "Nail Gun",
    7: "Land Mine",
    8: "Chair",
    9: "Fridge",
    10: "Hazmat Suit",
    11: "Revolver",
    12: "Gears"
}
