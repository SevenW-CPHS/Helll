# Creating an Executable (.exe) for Your Game

## Option 1: Using PyInstaller (Recommended)

### Prerequisites
Install PyInstaller:
```bash
pip install pyinstaller
```

### Build Steps
1. Open your terminal/command prompt in the repository folder
2. Run the build script:
   ```bash
   python build_exe.py
   ```
3. The executable will be created in the `dist` folder as `Hell_Game.exe`

## Option 2: Manual PyInstaller Command

If you prefer to build manually:
```bash
pyinstaller game-folder/run_game.py --name=Hell_Game --onefile --windowed --distpath=./dist
```

### Flags Explanation
- `--onefile` - Creates a single .exe file (vs. a folder with many files)
- `--windowed` - Removes the console window (optional; remove if you want to see debug output)
- `--distpath=./dist` - Output folder for the executable
- `--icon=path/to/icon.ico` - (Optional) Add a custom icon to your .exe

## Option 3: Using auto-py-to-exe (GUI Tool)

If you prefer a graphical interface:
```bash
pip install auto-py-to-exe
auto-py-to-exe
```

Then select `game-folder/run_game.py` as your script and configure the options.

## What's Included

- **run_game.py** - Launcher script that imports and runs gamecode.py
- **build_exe.py** - Automated build script using PyInstaller

## Notes

- The first build may take 1-2 minutes as PyInstaller bundles Python and all dependencies
- The resulting .exe will be larger (50-100MB+) because it includes the Python runtime
- Your game requires the CMU graphics library, so make sure it's installed: `pip install cmu_graphics`
- If your game uses internet resources (CMU images/sounds), ensure they remain accessible

## Sharing Your Game

Once built, you can share the `Hell_Game.exe` file. Users don't need to install Python to run it!

**Note**: Some antivirus software may flag PyInstaller executables. This is normal - they're false positives.
