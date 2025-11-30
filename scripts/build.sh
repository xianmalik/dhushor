#!/usr/bin/env bash
set -euo pipefail

echo "Building qBObsidian theme..."

# Find rcc
RCC=""
if command -v rcc &> /dev/null; then
    RCC="rcc"
elif [ -f "/opt/homebrew/Cellar/qtbase/6.9.3_1/share/qt/libexec/rcc" ]; then
    RCC="/opt/homebrew/Cellar/qtbase/6.9.3_1/share/qt/libexec/rcc"
elif [ -f "/opt/homebrew/Cellar/qt/6.7.3/share/qt/libexec/rcc" ]; then
    RCC="/opt/homebrew/Cellar/qt/6.7.3/share/qt/libexec/rcc"
else
    echo "Error: Qt rcc compiler not found"
    echo "Please install Qt: brew install qt"
    exit 1
fi

echo "Using rcc: $RCC"

# Clean and create dist directory
rm -rf dist
mkdir -p dist

# Build theme (use zlib compression like working gruvbox theme)
cd src
"$RCC" --compress 9 --compress-algo zlib -binary resources.qrc -o ../dist/qbobsidian.qbtheme
cd ..

# Show result
if [ -f "dist/qbobsidian.qbtheme" ]; then
    SIZE=$(du -h dist/qbobsidian.qbtheme | cut -f1)
    echo "✓ Successfully built: dist/qbobsidian.qbtheme ($SIZE)"
else
    echo "✗ Build failed"
    exit 1
fi
