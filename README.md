# IcoGeneral

IcoGeneral is a portable Windows utility for creating `.ico` files from images, applying custom icons to shortcuts, and setting a folder icon.

## Features

- Convert common image formats into `.ico` files.
- Create desktop shortcuts with a selected icon.
- Set a custom folder icon through `desktop.ini`.
- Store generated icons in the local user application-data directory.

## Requirements

- Python 3
- Pillow
- pywin32

## Run from source

```bash
pip install pillow pywin32
python main.pyw
```

## Downloads

Prebuilt Windows binaries are published under [GitHub Releases](../../releases).

## Build

The included `main.spec` file is intended for PyInstaller builds.

```bash
pyinstaller main.spec
```
