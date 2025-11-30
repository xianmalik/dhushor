#!/usr/bin/env python3
"""
Simple Qt Resource (.qbtheme) builder for qBittorrent themes
Based on Qt's RCC binary format
"""

import struct
import zlib
from pathlib import Path

class QRCBuilder:
    def __init__(self):
        self.data_entries = []
        self.names = {}
        self.tree_nodes = []

    def add_file(self, alias, filepath):
        """Add a file to the resource"""
        with open(filepath, 'rb') as f:
            data = f.read()

        # Compress data
        compressed = zlib.compress(data, 9)

        self.data_entries.append({
            'alias': alias,
            'data': data,
            'compressed': compressed
        })

    def build(self, output_path):
        """Build the .qbtheme file"""
        with open(output_path, 'wb') as f:
            # Write header
            f.write(b'qres')  # Magic number
            f.write(struct.pack('>I', 3))  # Version

            # Placeholder for offsets (will be filled later)
            data_offset_pos = f.tell()
            f.write(struct.pack('>I', 0))  # Data section offset

            tree_offset_pos = f.tell()
            f.write(struct.pack('>I', 0))  # Tree section offset

            names_offset_pos = f.tell()
            f.write(struct.pack('>I', 0))  # Names section offset

            # Write data section
            data_section_start = f.tell()
            data_offsets = []

            for entry in self.data_entries:
                data_offsets.append(f.tell() - data_section_start)

                # Write size and compressed data
                original_size = len(entry['data'])
                compressed_data = entry['compressed']

                f.write(struct.pack('>I', original_size))
                f.write(compressed_data)

                # Padding to 4-byte alignment
                while f.tell() % 4:
                    f.write(b'\x00')

            # Write names section
            names_section_start = f.tell()
            name_offsets = {}

            for entry in self.data_entries:
                alias = entry['alias']
                name_offsets[alias] = f.tell() - names_section_start

                # Write name
                name_utf16 = alias.encode('utf-16-be')
                name_len = len(alias)
                name_hash = self._hash_string(alias)

                f.write(struct.pack('>H', name_len))
                f.write(struct.pack('>I', name_hash))
                f.write(name_utf16)

            # Write tree section
            tree_section_start = f.tell()

            # Root node
            f.write(struct.pack('>I', 0))  # Name offset (root has no name)
            f.write(struct.pack('>H', 2))  # Flags: directory
            f.write(struct.pack('>I', len(self.data_entries)))  # Child count
            f.write(struct.pack('>I', 0x14))  # First child offset

            # File nodes
            for i, entry in enumerate(self.data_entries):
                alias = entry['alias']
                f.write(struct.pack('>I', name_offsets[alias]))  # Name offset
                f.write(struct.pack('>H', 1))  # Flags: file
                f.write(struct.pack('>I', 0))  # Country/Language
                f.write(struct.pack('>I', data_offsets[i]))  # Data offset

            # Update section offsets in header
            current_pos = f.tell()

            f.seek(data_offset_pos)
            f.write(struct.pack('>I', data_section_start))

            f.seek(tree_offset_pos)
            f.write(struct.pack('>I', tree_section_start))

            f.seek(names_offset_pos)
            f.write(struct.pack('>I', names_section_start))

            f.seek(current_pos)

    def _hash_string(self, s):
        """Qt's qHash function for strings"""
        h = 0
        for c in s:
            h = (h << 4) + ord(c)
            g = h & 0xF0000000
            if g:
                h ^= g >> 23
            h &= ~g
        return h & 0xFFFFFFFF

def main():
    # Setup paths
    base_dir = Path(__file__).parent.parent
    source_dir = base_dir / 'src' / 'qbobsidian'
    output_file = base_dir / 'dist' / 'qbobsidian.qbtheme'

    # Ensure output directory exists
    output_file.parent.mkdir(parents=True, exist_ok=True)

    # Create builder
    builder = QRCBuilder()

    # Add files
    builder.add_file('config.json', source_dir / 'config.json')
    builder.add_file('stylesheet.qss', source_dir / 'stylesheet.qss')
    builder.add_file('light', source_dir / 'stylesheet.qss')  # Alias for compatibility

    # Add icons
    icons_dir = source_dir / 'icons'
    if icons_dir.exists():
        for icon_file in sorted(icons_dir.glob('*.svg')):
            alias = f'icons/{icon_file.name}'
            builder.add_file(alias, icon_file)

    # Build theme
    builder.build(output_file)

    print(f"✓ Successfully created: {output_file}")
    print(f"✓ Included {len(builder.data_entries)} files")
    print(f"✓ Theme size: {output_file.stat().st_size / 1024:.1f} KB")

if __name__ == '__main__':
    main()
