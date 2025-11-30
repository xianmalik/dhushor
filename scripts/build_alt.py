#!/usr/bin/env python3
"""
Build qBittorrent theme (.qbtheme) file
This script creates a Qt Resource file from the theme files.
"""

import struct
import zlib
import os
from pathlib import Path

def write_qrc_header(f):
    """Write Qt Resource header"""
    f.write(b'qres')  # Magic
    f.write(struct.pack('>I', 3))  # Version

def write_qrc_tree(f, files):
    """Write resource tree structure"""
    # Tree section
    tree_offset = f.tell()

    # Root node
    f.write(struct.pack('>I', 0))  # Name offset (0 for root)
    f.write(struct.pack('>H', 0))  # Flags
    f.write(struct.pack('>I', len(files)))  # Children count
    f.write(struct.pack('>I', 0))  # First child offset (will update)

    return tree_offset

def compress_file(filepath):
    """Compress file data"""
    with open(filepath, 'rb') as f:
        data = f.read()
    compressed = zlib.compress(data, 9)
    return data, compressed

def build_theme(source_dir, output_file):
    """Build .qbtheme file from source directory"""

    # Collect all files
    files = []
    icons_dir = source_dir / 'icons'

    # Add config and stylesheet
    files.append(('config.json', source_dir / 'config.json'))
    files.append(('stylesheet.qss', source_dir / 'stylesheet.qss'))

    # Add icons
    if icons_dir.exists():
        for icon in sorted(icons_dir.glob('*.svg')):
            files.append((f'icons/{icon.name}', icon))

    # Prepare data
    file_data = []
    for name, path in files:
        original, compressed = compress_file(path)
        file_data.append({
            'name': name,
            'original': original,
            'compressed': compressed,
            'path': path
        })

    # Write output file
    with open(output_file, 'wb') as f:
        # Header
        write_qrc_header(f)

        # Data section offset
        data_offset_pos = f.tell()
        f.write(struct.pack('>I', 0))  # Placeholder

        # Tree section offset
        tree_offset_pos = f.tell()
        f.write(struct.pack('>I', 0))  # Placeholder

        # Names section offset
        names_offset_pos = f.tell()
        f.write(struct.pack('>I', 0))  # Placeholder

        # Write data section
        data_offset = f.tell()
        data_entries = []

        for item in file_data:
            entry_offset = f.tell() - data_offset

            # Write compressed data
            compressed = item['compressed']
            original_size = len(item['original'])
            compressed_size = len(compressed)

            # Data entry
            data_entries.append(entry_offset)
            f.write(struct.pack('>I', original_size))
            f.write(compressed)

            # Align to 4 bytes
            while f.tell() % 4 != 0:
                f.write(b'\x00')

        # Write names section
        names_offset = f.tell()
        name_offsets = {}

        for item in file_data:
            name = item['name']
            name_offsets[name] = f.tell() - names_offset

            # Write name length and hash
            name_bytes = name.encode('utf-16-be')
            f.write(struct.pack('>H', len(name)))
            f.write(struct.pack('>I', hash(name) & 0xFFFFFFFF))
            f.write(name_bytes)

        # Write tree section
        tree_offset = f.tell()

        # Root directory
        f.write(struct.pack('>I', 0))  # Name offset
        f.write(struct.pack('>H', 2))  # Flags (directory)
        f.write(struct.pack('>I', len(file_data)))  # Children count
        f.write(struct.pack('>I', 32))  # First child offset

        # File entries
        for i, item in enumerate(file_data):
            name = item['name']
            f.write(struct.pack('>I', name_offsets[name]))  # Name offset
            f.write(struct.pack('>H', 1))  # Flags (file)
            f.write(struct.pack('>I', 1))  # Country
            f.write(struct.pack('>H', 0))  # Language
            f.write(struct.pack('>I', data_entries[i]))  # Data offset

        # Update section offsets in header
        f.seek(data_offset_pos)
        f.write(struct.pack('>I', data_offset))

        f.seek(tree_offset_pos)
        f.write(struct.pack('>I', tree_offset))

        f.seek(names_offset_pos)
        f.write(struct.pack('>I', names_offset))

    print(f"✓ Theme built successfully: {output_file}")
    print(f"✓ Included {len(file_data)} files")

if __name__ == '__main__':
    source_dir = Path(__file__).parent.parent / 'src' / 'qbobsidian'
    output_file = Path(__file__).parent.parent / 'dist' / 'qbobsidian.qbtheme'

    build_theme(source_dir, output_file)
