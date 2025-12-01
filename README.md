<p align="center">
  <img src="./assets/dhushor-light.svg" />
</p>

<p align="center">
    <img alt="Version" src="https://img.shields.io/badge/Version-2.0.0-pink?style=for-the-badge&labelColor=302D41&logo=git&logoColor=D9E0EE">
</p>
<p align="center">
    A minimalistic monochrome theme for qBittorrent
</p>

<p align="center">
    <!-- <a href="https://github.com/xianmalik/dhushor/issues">
        <img alt="Issues" src="https://img.shields.io/github/issues/xianmalik/dhushor?style=for-the-badge&logo=bilibili&color=F5E0DC&logoColor=D9E0EE&labelColor=302D41"></a> -->
    <a href="https://github.com/xianmalik/dhushor">
        <img alt="Repo Size" src="https://img.shields.io/github/repo-size/xianmalik/dhushor?color=%23DDB6F2&label=SIZE&logo=square&style=for-the-badge&logoColor=D9E0EE&labelColor=302D41"/></a>
    <a href="https://github.com/xianmalik/dhushor/stargazers">
        <img alt="Stars" src="https://img.shields.io/github/stars/xianmalik/dhushor?style=for-the-badge&logo=starship&color=C9CBFF&logoColor=D9E0EE&labelColor=302D41"></a>
</p>

<hr />

<p align="center">
    <h2 align="center">Tech Stack</h2>
</p>

<p align="center">
    <a href="https://www.qt.io/"><img src="https://img.shields.io/badge/Qt-302D41?style=for-the-badge&logo=qt&logoColor=4285F4" /></a>
    <a href="https://doc.qt.io/qt-5/stylesheet-reference.html"><img src="https://img.shields.io/badge/Qt_Stylesheet-302D41.svg?logo=css3&logoColor=white&style=for-the-badge" /></a>
    <a href="https://www.w3.org/TR/SVG/"><img src="https://img.shields.io/badge/SVG-302D41?logo=svg&logoColor=4285F4&style=for-the-badge" /></a>
    <a href="https://www.gnu.org/software/make/manual/make.html"><img src="https://img.shields.io/badge/Make-302D41?logo=gnu&logoColor=D9E0EE&style=for-the-badge"/></a>
</p>

<hr />

<p align="center">
    <h2 align="center">Quick Start</h2>
    <small>Ultra-minimal monochrome qBittorrent theme: build & install.</small>
</p>

```bash
# 1) Clone the repository
git clone https://github.com/xianmalik/dhushor.git
cd dhushor

# 2) Build the theme
make build

# 3) Install the theme
make install

# Or build and install in one command
make all
```

<p align="center">
    <h2 align="center">Project Structure</h2>
</p>

```
├── dist/                      # Built theme files
│   └── dhushor.qbtheme       # Ready-to-use theme file
├── src/                       # Source files (edit these)
│   ├── config.json            # Theme color configuration
│   ├── stylesheet.qss         # Main Qt stylesheet
│   ├── resources.qrc          # Qt resource file
│   └── icons/                 # SVG icons
│       ├── arrow_down.svg
│       ├── checkbox_checked.svg
│       ├── checkbox_indeterminate.svg
│       ├── checkbox_unchecked.svg
│       └── ...                 # All theme icons
├── scripts/                   # Build & automation scripts
│   └── build.sh               # Shell build script
├── Makefile                   # Build automation
└── README.md                  # Documentation
```

<p align="center">
    <h2 align="center">Features</h2>
</p>

- **Ultra-minimal design**: Pure black, gray, and white color scheme
- **Consistent styling**: Uniform look across all UI elements
- **Custom SVG icons**: Matching the monochrome aesthetic
- **Zero distractions**: Focus on functionality over visual elements
- **Professional aesthetic**: Clean, modern interface

<p align="center">
    <h2 align="center">Requirements</h2>
</p>

- Qt5 development tools (for `rcc` compiler) - optional, fallback included
- Python 3.6+ (for fallback Python implementation)
- Make (for build automation)

<p align="center">
    <h2 align="center">Usage</h2>
</p>

1. **Build the theme**
```bash
make build
```

2. **Install the theme**
```bash
make install
```

3. **Apply the theme in qBittorrent**
   - Open qBittorrent
   - Go to **Tools** → **Options** → **Behavior**
   - Under **Interface**, click **Use custom UI Theme**
   - Browse and select `dhushor.qbtheme` from the `dist/` folder
   - Restart qBittorrent

4. **Output**
- Theme file: `dist/dhushor.qbtheme`

<p align="center">
    <h2 align="center">Customization</h2>
</p>

- **Colors**: Edit accent/text colors in `src/config.json`
- **Icons**: Replace SVG files in `src/icons/` with custom designs
- **Styles**: Adjust Qt stylesheet in `src/stylesheet.qss`
- **Layout**: Modify UI elements via CSS-like syntax in stylesheet

<p align="center">
    <h2 align="center">License</h2>
</p>

<p align="center">
This project is open source and available under the <a href="LICENSE">MIT License</a>.
</p>

<p align="center">
    <h2 align="center">Author</h2>
</p>

<p align="center">
    <strong>Malik Zubayer Ul Haider</strong><br>
    <a href="https://xianmalik.com">Website</a> •
    <a href="https://github.com/xianmalik">GitHub</a> •
    <a href="https://linkedin.com/in/xianmalik">LinkedIn</a>
</p>