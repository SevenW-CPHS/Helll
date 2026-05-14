# Installing Build Tools for .deb Package

This guide covers how to install the necessary tools to build a Debian (.deb) package from the Helll project.

## Prerequisites

- Ubuntu, Debian, or any Debian-based Linux distribution
- Administrator (sudo) access
- Internet connection

---

## Step 1: Update Package Manager

First, update your package manager cache:

```bash
sudo apt-get update
```

This ensures you get the latest versions of packages.

---

## Step 2: Install Build Tools

### Option A: Install All Required Tools at Once (Recommended)

```bash
sudo apt-get install -y build-essential debhelper python3 devscripts
```

**What each tool does:**
- **build-essential** - GCC compiler, make, and development libraries
- **debhelper** - Simplifies Debian package creation
- **python3** - Required to run gamecode.py
- **devscripts** - Additional Debian packaging utilities

### Option B: Install Individually

If you prefer to install tools one at a time:

```bash
# Install build essentials (compiler, make, etc.)
sudo apt-get install -y build-essential

# Install debhelper
sudo apt-get install -y debhelper

# Install Python 3
sudo apt-get install -y python3

# Install devscripts
sudo apt-get install -y devscripts
```

---

## Step 3: Verify Installation

Check that all tools are installed correctly:

```bash
# Check GCC (part of build-essential)
gcc --version

# Check make (part of build-essential)
make --version

# Check debhelper
dh --version

# Check Python 3
python3 --version

# Check devscripts
dpkg-buildpackage --version
```

You should see version numbers for each command.

---

## Step 4: Clone and Prepare the Repository

```bash
# Clone the repository
git clone https://github.com/SevenW-CPHS/Helll.git
cd Helll

# Switch to the deb-packaging branch
git checkout deb-packaging

# Verify the debian folder exists
ls -la debian/
```

---

## Step 5: Build the .deb Package

Now you're ready to build:

```bash
# Build the package (no signing)
dpkg-buildpackage -us -uc
```

The `.deb` file will be created in the parent directory:

```bash
cd ..
ls -lah gamecode-launcher_*.deb
```

---

## Step 6: Install the Package

```bash
# Install the built .deb file
sudo dpkg -i gamecode-launcher_1.0.0_all.deb
```

---

## Step 7: Run the Game

```bash
# Launch from command line
gamecode-launcher

# Or find "Gamecode" in your applications menu
```

---

## Troubleshooting

### "E: Unable to locate package build-essential"

**Solution:** Run update first:
```bash
sudo apt-get update
sudo apt-get install -y build-essential
```

### "command not found: dpkg-buildpackage"

**Solution:** Install devscripts:
```bash
sudo apt-get install -y devscripts
```

### "Permission denied" error

**Solution:** Make sure you use `sudo` for installation commands:
```bash
sudo apt-get install -y build-essential debhelper python3 devscripts
```

### "ImportError" when running gamecode.py

**Solution:** Your game may require additional Python libraries. Install them:
```bash
pip3 install <library_name>
# or
sudo apt-get install python3-<library_name>
```

---

## Complete One-Liner Installation

If you want to do everything at once:

```bash
sudo apt-get update && sudo apt-get install -y build-essential debhelper python3 devscripts && git clone https://github.com/SevenW-CPHS/Helll.git && cd Helll && git checkout deb-packaging && dpkg-buildpackage -us -uc
```

---

## Summary

| Tool | Purpose | Install Command |
|------|---------|-----------------|
| build-essential | Compiler & dev tools | `sudo apt-get install -y build-essential` |
| debhelper | Debian packaging helper | `sudo apt-get install -y debhelper` |
| python3 | Python interpreter | `sudo apt-get install -y python3` |
| devscripts | Packaging utilities | `sudo apt-get install -y devscripts` |

Once installed, you can build the .deb package with:
```bash
dpkg-buildpackage -us -uc
```

