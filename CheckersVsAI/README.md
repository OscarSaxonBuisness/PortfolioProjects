# Checkers vs AI

A fully playable Checkers game written in Python, featuring a Tkinter GUI and an AI opponent powered by the Minimax algorithm with Alpha-Beta pruning.

## Features

- 8×8 graphical board rendered with Tkinter and piece sprites
- Click a piece to highlight valid moves in red
- AI opponent using Minimax with Alpha-Beta pruning across three difficulty levels
- King promotion — pieces reaching the opposite end move in all four diagonal directions
- Multi-jump captures detected recursively
- Win, Draw, and Lose screens on game completion
- Difficulty selection on the start menu (Easy, Medium, Hard)

## Requirements

- Python 3.x
- Pillow

```bash
pip install Pillow
```

## How to Run

Place `checkers.py`, `white.png`, and `black.png` in the same folder, then run:

```bash
python checkers.py
```

## AI — How It Works

The AI uses Minimax with Alpha-Beta pruning to search ahead through possible game states. A static evaluation function scores positions based on piece count, back-row control, and centre control.

| Difficulty | Search Depth |
|------------|-------------|
| Easy | 3 |
| Medium | 5 |
| Hard | 7 |
