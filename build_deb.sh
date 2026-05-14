#!/bin/bash
# Build script for creating the .deb package

set -e

echo "Building Helll Game .deb package..."

# Install build dependencies if not present
sudo apt-get update
sudo apt-get install -y build-essential debhelper python3 devscripts

# Build the package
echo "Running debuild..."
debuild -us -uc

echo ""
echo "Build complete! The .deb file should be in the parent directory."
ls -lh ../*.deb 2>/dev/null || echo "No .deb files found"
