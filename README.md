# qBObsidian

A minimal dark theme for qBittorrent.

## Preview

Dark, clean interface with warm orange accents on a charcoal background.

### Color Palette

- **Background**: `#1d2021` (dark gray-black)
- **Secondary**: `#282828` (medium gray)
- **Borders**: `#3c3836` (subtle gray)
- **Text**: `#ebdbb2` (warm off-white)
- **Secondary Text**: `#a89984` (muted tan)
- **Accent**: `#d79921` (warm orange/yellow)
- **Selection**: `#504945` (muted brown-gray)

## Installation

### Method 1: Direct Installation

1. Download `qbobsidian.qbtheme` from the `dist/` folder
2. Open qBittorrent
3. Go to **Tools** → **Options** → **Behavior**
4. Under **Interface**, click **Use custom UI Theme**
5. Browse and select `qbobsidian.qbtheme`
6. Restart qBittorrent

### Method 2: Manual Installation (macOS)

```bash
# Copy theme to qBittorrent config directory
cp dist/qbobsidian.qbtheme ~/Library/Application\ Support/qBittorrent/
```

Then follow steps 2-6 from Method 1.

### Method 3: Manual Installation (Linux)

```bash
# Copy theme to qBittorrent config directory
cp dist/qbobsidian.qbtheme ~/.config/qBittorrent/
```

Then follow steps 2-6 from Method 1.

### Method 4: Manual Installation (Windows)

```powershell
# Copy theme to qBittorrent config directory
copy dist\qbobsidian.qbtheme %APPDATA%\qBittorrent\
```

Then follow steps 2-6 from Method 1.

## Building from Source

If you want to modify the theme:

1. Edit files in the `src/qbobsidian/` directory:
   - `config.json` - Theme metadata and color palette
   - `stylesheet.qss` - Qt stylesheet (CSS-like syntax)
   - `icons/*.svg` - UI icons

2. Rebuild the theme:
   ```bash
   python3 scripts/build.py
   ```

3. The new `qbobsidian.qbtheme` file will be generated in `dist/`

## Project Structure

```
qbobsidian/
├── dist/                    # Built theme files
│   └── qbobsidian.qbtheme  # Ready-to-use theme file
├── src/                     # Source files
│   └── qbobsidian/
│       ├── config.json      # Theme configuration
│       ├── stylesheet.qss   # Main stylesheet
│       └── icons/           # SVG icons
│           ├── arrow_down.svg
│           ├── arrow_down_disabled.svg
│           ├── branch_closed.svg
│           ├── branch_open.svg
│           ├── check.svg
│           ├── checkbox_checked.svg
│           ├── checkbox_indeterminate.svg
│           ├── checkbox_unchecked.svg
│           ├── chevron_down.svg
│           ├── chevron_down_disabled.svg
│           ├── chevron_up.svg
│           └── chevron_up_disabled.svg
├── scripts/                 # Build scripts
│   └── build.py            # Theme builder
└── README.md               # Documentation
```

## Features

- Minimal, clean dark interface
- Warm color palette with orange accents
- Consistent styling across all UI elements
- Custom SVG icons matching the theme
- Low eye strain with muted colors
- Professional appearance

## Customization

### Changing Colors

Edit `src/qbobsidian/config.json` and `src/qbobsidian/stylesheet.qss` to customize colors:

```json
{
  "colors": {
    "Palette": {
      "Window": "#1d2021",        // Main background
      "Text": "#ebdbb2",          // Primary text
      "Highlight": "#504945",     // Selection background
      "HighlightedText": "#d79921" // Accent color
    }
  }
}
```

In the stylesheet, search and replace color values:
- `#1d2021` - Dark background
- `#282828` - Medium background
- `#3c3836` - Borders
- `#ebdbb2` - Primary text
- `#d79921` - Accent/highlight

### Changing Icons

Replace the SVG files in `src/qbobsidian/icons/` with your own. Keep the same filenames and ensure they're valid SVG format. After making changes, rebuild using `python3 scripts/build.py`.

## License

Free to use and modify.

## Credits

Created by xianmalik