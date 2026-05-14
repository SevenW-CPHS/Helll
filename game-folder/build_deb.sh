#!/bin/bash
# Build Helll Game .deb package

set -e

echo "Installing build dependencies..."
sudo apt-get update
sudo apt-get install -y build-essential debhelper python3 devscripts

echo "Building .deb package..."
debuild -us -uc

echo ""
echo "✓ Build complete! The .deb file is in the parent directory:"
ls -lh ../*.deb 2>/dev/null || echo "Build may have failed"
