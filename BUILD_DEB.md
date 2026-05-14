# How to Build the .deb Package

This guide explains how to build the Debian package for the gamecode-launcher.

## Prerequisites

Install the required build tools:

```bash
sudo apt-get update
sudo apt-get install -y build-essential debhelper python3 devscripts
```

## Step 1: Clone and Checkout the Branch

```bash
git clone https://github.com/SevenW-CPHS/Helll.git
cd Helll
git checkout deb-packaging
```

## Step 2: Build the Package

### Option A: Using dpkg-buildpackage (Recommended)

```bash
# Navigate to the repository root
cd Helll

# Build the package
dpkg-buildpackage -us -uc

# The .deb file will be created in the parent directory
ls ../*.deb
```

### Option B: Using debuild

```bash
cd Helll
debuild -us -uc
```

### Option C: Manual Build with debhelper

```bash
cd Helll
debian/rules clean
debian/rules build
debian/rules binary
```

## Step 3: Install the Package

Once built, install the `.deb` file:

```bash
# Find the generated .deb file
cd ..
ls gamecode-launcher_*.deb

# Install it
sudo dpkg -i gamecode-launcher_1.0.0_all.deb
```

## Step 4: Verify Installation

Test that the package installed correctly:

```bash
# Check if the package is installed
dpkg -l | grep gamecode-launcher

# Run the launcher
gamecode-launcher

# Or find it in your applications menu
```

## Package Contents

After installation, the package will provide:

- **Executable**: `/usr/bin/gamecode-launcher` - Command to launch the game
- **Game Files**: `/opt/gamecode/gamecode.py` - The actual game code
- **Desktop Entry**: `/usr/share/applications/gamecode-launcher.desktop` - Application menu shortcut

## Uninstall

To remove the package:

```bash
sudo dpkg -r gamecode-launcher
```

Or with apt:

```bash
sudo apt remove gamecode-launcher
```

## Troubleshooting

### Missing build-essential
```bash
sudo apt-get install build-essential
```

### Permission denied when building
Make sure you have write permissions in the repository directory:
```bash
sudo chown -R $(whoami):$(whoami) Helll/
```

### Python3 not found
Install Python3:
```bash
sudo apt-get install python3
```

### Clean build files
To clean up and start fresh:
```bash
cd Helll
debian/rules clean
rm -rf debian/gamecode-launcher/
```

## Build Output

Successful build will create:
- `gamecode-launcher_1.0.0_all.deb` - The installable package
- `gamecode-launcher_1.0.0_all.changes` - Build metadata
- `gamecode-launcher_1.0.0.tar.gz` - Source archive

---

For more information on Debian packaging, visit: https://www.debian.org/doc/manuals/debmake-doc/
