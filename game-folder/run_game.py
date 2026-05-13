"""
Game Launcher
This script imports and runs gamecode.py
"""
import sys
import os

# Add the game folder to the path so we can import gamecode
game_folder = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, game_folder)

# Import and run the game
import gamecode
