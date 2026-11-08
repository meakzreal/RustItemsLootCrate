# 🎁 Rust Items Loot Crate

A little Python project where you can open a Rust-inspired loot crate and see what items you get.

I made this to practise using Python's `random` module, working with multiple Python files and adding `.wav` sound effects to make the crate opening feel more realistic.

## What it does
- Opens a Small Crate and generates random loot.
- Shows 5 loot selections with short delays between them.
- Plays a sound effect when opening the crate.
- Has a config file where you can change the crate settings and items.
- Lets you choose whether duplicate items are allowed.

## Configuration

You can change the settings inside `Config.py`, including the crate name, loot amount and duplicate settings.

## Files
- `main.py` – Main menu.
- `Config.py` – Settings and loot pool.
- `SmallCrateScript.py` – Crate opening sequence.
- `SmallCrate.wav` – Opening sound effect.

## Requirements

```bash
pip install pygame
```

Run using:

```bash
python main.py
```

## Author

**Meakz**

Python project – Version 1.0
