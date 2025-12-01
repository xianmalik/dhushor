# Dhūshor

A minimalistic monochrome theme for qBittorrent.

## Preview

Ultra-minimal interface with pure black, gray, and white color scheme.

### Color Palette

- **Background**: `#0a0a0a` (pure black)
- **Secondary Background**: `#1a1a1a` (dark gray)
- **Tertiary Background**: `#2a2a2a` (medium gray)
- **Borders/Separators**: `#1a1a1a` to `#333333` (subtle grays)
- **Text**: `#e0e0e0` (light gray)
- **Highlighted Text**: `#ffffff` (white)
- **Disabled Text**: `#666666` (muted gray)
- **Accent/Selection**: `#555555` (medium gray)

## Installation

### Method 1: Direct Installation

1. Download `dhushor.qbtheme` from the `dist/` folder
2. Open qBittorrent
3. Go to **Tools** → **Options** → **Behavior**
4. Under **Interface**, click **Use custom UI Theme**
5. Browse and select `dhushor.qbtheme`
6. Restart qBittorrent

### Method 2: Manual Installation (macOS)

```bash
# Copy theme to qBittorrent config directory
cp dist/dhushor.qbtheme ~/Library/Application\ Support/qBittorrent/
```

Then follow steps 2-6 from Method 1.

### Method 3: Manual Installation (Linux)

```bash
# Copy theme to qBittorrent config directory
cp dist/dhushor.qbtheme ~/.config/qBittorrent/
```

Then follow steps 2-6 from Method 1.

### Method 4: Manual Installation (Windows)

```powershell
# Copy theme to qBittorrent config directory
copy dist\dhushor.qbtheme %APPDATA%\qBittorrent\
```

Then follow steps 2-6 from Method 1.

## Building from Source

If you want to modify the theme:

1. Edit files in the `src/` directory:
   - `config.json` - Theme color configuration
   - `stylesheet.qss` - Qt stylesheet (CSS-like syntax)
   - `resources.qrc` - Resource file listing
   - `icons/*.svg` - UI icons

2. Rebuild the theme:
   ```bash
   # Using Make (recommended)
   make build

   # Or using the shell script directly
   ./scripts/build.sh

   # Or using Python (fallback)
   python3 scripts/build.py
   ```

3. The new `dhushor.qbtheme` file will be generated in `dist/`

### Quick Install

```bash
# Build and install in one command (macOS/Linux)
make install
```

## Project Structure

```
dhushor/
├── dist/                    # Built theme files
│   └── dhushor.qbtheme     # Ready-to-use theme file
├── src/                     # Source files (flat structure)
│   ├── config.json          # Theme color configuration
│   ├── stylesheet.qss       # Main stylesheet
│   ├── resources.qrc        # Qt resource file
│   └── icons/               # SVG icons
│       ├── arrow_down.svg
│       ├── arrow_down_disabled.svg
│       ├── branch_closed.svg
│       ├── branch_open.svg
│       ├── check.svg
│       ├── checkbox_checked.svg
│       ├── checkbox_indeterminate.svg
│       ├── checkbox_unchecked.svg
│       ├── chevron_down.svg
│       ├── chevron_down_disabled.svg
│       ├── chevron_up.svg
│       └── chevron_up_disabled.svg
├── scripts/                 # Build scripts
│   ├── build.sh            # Shell build script (recommended)
│   ├── build.py            # Python build script (fallback)
│   └── build_alt.py        # Alternative Python builder
├── Makefile                # Build automation
└── README.md               # Documentation
```

## Features

- Ultra-minimal monochrome interface
- Pure black, gray, and white color scheme
- Consistent styling across all UI elements
- Custom SVG icons matching the theme
- Zero visual distractions - focus on content
- Professional, clean aesthetic

## Customization

### Changing Colors

Edit `src/config.json` to customize colors. The config uses dot notation for palette colors:

```json
{
  "colors": {
      "Palette.Window": "#1d2021",
      "Palette.WindowText": "#ebdbb2",
      "Palette.Highlight": "#504945",
      "TransferList.Downloading": "#b8bb26",
      "TransferList.Uploading": "#83a598"
  }
}
```

You can also customize colors in `src/stylesheet.qss` by searching and replacing hex values.

### Changing Icons

Replace the SVG files in `src/icons/` with your own. Keep the same filenames and ensure they're valid SVG format. After making changes, rebuild using `python3 scripts/build.py`.

## Troubleshooting

### Theme Not Loading

If the theme doesn't work in qBittorrent:

1. **Check qBittorrent version**: This theme requires qBittorrent v4.1.0 or higher
2. **Verify installation**: Make sure you selected the correct `.qbtheme` file
3. **Restart qBittorrent**: The theme only applies after a full restart
4. **Check logs**: Look for theme-related errors in qBittorrent's console/logs
5. **Rebuild theme**: Run `python3 scripts/build.py` to rebuild with Qt's rcc tool

### Building Requirements

The build script automatically uses Qt's `rcc` compiler if available (recommended). If Qt is not installed, it will fall back to a Python implementation, which may have compatibility issues.

To install Qt (macOS with Homebrew):
```bash
brew install qt
```

## License

Free to use and modify.

## Credits

Created by xianmalik