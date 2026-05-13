"""
Build script to create an executable from the game code.
Requires: pip install pyinstaller
"""
import PyInstaller.__main__
import sys
import os

# Get the absolute path to the game folder
game_folder = os.path.join(os.path.dirname(__file__), 'game-folder')
game_script = os.path.join(game_folder, 'run_game.py')

# Build the executable
PyInstaller.__main__.run([
    game_script,
    '--name=Hell_Game',  # Name of the executable
    '--onefile',  # Create a single executable file
    '--windowed',  # Remove console window (optional, remove this line if you want the console)
    '--icon=NONE',  # Add --icon=path/to/icon.ico if you have an icon file
    '--distpath=./dist',  # Output directory
    f'--workpath=./build',  # Build directory
    '--specpath=./build',  # Spec file directory
])

print("Executable created! Look in the 'dist' folder for 'Hell_Game.exe'")
