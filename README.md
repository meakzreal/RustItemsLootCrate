# 🎁 Rust Items Loot Crate Generator

A Python terminal-based loot crate generator inspired by Rust.

Open a Small Crate and receive randomly selected Rust items, complete with sound effects and configurable loot settings.

I made this project to practise Python's `random` module, working with multiple Python files, configuration settings and `.wav` sound effects to make the experience feel more realistic.

## Features

- **Random Loot Generation** – Randomly selects items from a configurable loot pool.
- **Custom Loot Amount** – Change how many items are generated during each selection.
- **Duplicate Settings** – Choose whether duplicate items are allowed.
- **Custom Crate Names** – Change the displayed crate name.
- **Sound Effects** – Includes an opening sound effect using Pygame.
- **Configuration File** – Customise settings without changing the main program.
- **Terminal Interface** – Simple menu-based interaction.

## Configuration

All customisation is handled through `Config.py`.

| Setting | Description |
|---|---|
| `Small_Crate_Name` | Changes the displayed crate name. |
| `loot_amount` | Controls how many items are selected per loot generation. |
| `duplicate_items` | Allows or prevents duplicates within each selection. |
| `low_number` | Minimum item number setting. |
| `max_number` | Maximum item number setting. |

**Example:**

```python
duplicate_items = False
loot_amount = 1
Small_Crate_Name = "Small Crate"
```

The crate currently runs five loot-generation selections per opening.

## Project Structure

```text
RustItemsLootCrate/
│
├── main.py
├── Config.py
├── SmallCrateScript.py
├── SmallCrate.wav
└── README.md
```

| File | Purpose |
|---|---|
| `main.py` | Main menu and program entry point. |
| `Config.py` | Configuration settings and item selection. |
| `SmallCrateScript.py` | Handles the crate-opening sequence and sound effects. |
| `SmallCrate.wav` | Crate-opening sound effect. |

## Requirements

- Python 3.x
- Pygame

Install Pygame:

```bash
pip install pygame
```

## Running the Project

Clone the repository:

```bash
git clone https://github.com/meakzreal/RustItemsLootCrate.git
```

Run the program:

```bash
python main.py
```

## Built With

- Python
- Random Module
- Pygame
- PyInstaller

## About

**Author:** Meakz  
**Version:** 1.0  
**Created:** 07/11/2026

A personal Python learning project built to explore random item generation, modular scripting, configuration and sound integration.
