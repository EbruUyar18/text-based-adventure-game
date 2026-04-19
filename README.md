
# Text-Based Adventure Game (Python)

This project is a text-based adventure game developed in Python.  
The game allows players to make choices that directly affect the storyline and outcome.

## Features

-  Branching storyline based on player decisions
-  Multiple endings (win/lose scenarios)
-  Clue collection system that affects game progression
-  Object-Oriented Programming (OOP) structure
-  Slow text printing effect for immersive storytelling
-  Replayable game flow with different paths

## Technologies Used

- Python
- Object-Oriented Programming (OOP)
- Functions & Control Structures

## Project Structure

- `Karakter` class: Base class for characters
- `Oyuncu` class: Inherits from `Karakter`, manages clues
- Game functions:
  - `giris()` → Introduction and story setup
  - `orman_gorevi()` → First decision phase
  - `secim()` → Mid-game branching
  - `son_gorev()` → Final decisions
  - `kapı_sifre()` → Ending mechanism
  - `oyunu_baslat()` → Game loop

## Gameplay Logic

- Player navigates through a story using input choices
- Choices affect:
  - Story progression
  - Clues collected
  - Final outcome
- The game includes multiple endings depending on decisions

## Known Issue

- One path may not continue due to a missing clue hint  
  (Example path: `sağ → 1 → 2 → 2 → 2`)

## 🚀 How to Run

1. Make sure Python is installed
2. Run the script:

```bash
python adventure_game.py
