#!/usr/bin/env python3
"""
Convert all GDS files in the repository to SVG format for preview on GitHub.
This script is designed to be run by GitHub Actions automatically.
"""

import os
import sys
from pathlib import Path

try:
    import gdstk
except ImportError:
    print("Error: gdstk not installed. Run: pip install gdstk")
    sys.exit(1)


def convert_gds_to_svg(gds_path):
    """Convert a single GDS file to SVG format."""
    try:
        # Read the GDS file
        library = gdstk.read_gds(str(gds_path))
        
        if not library.cells:
            print(f"Warning: No cells found in {gds_path}")
            return False
            
        # Get the top-level cell (main design)
        top_cells = library.top_level()
        if not top_cells:
            print(f"Warning: No top-level cells in {gds_path}")
            return False
            
        cell = top_cells[0]
        
        # Generate SVG filename
        svg_path = gds_path.with_suffix('.svg')
        
        # Write SVG
        cell.write_svg(str(svg_path))
        
        print(f"✓ Converted: {gds_path.name} → {svg_path.name}")
        return True
        
    except Exception as e:
        print(f"✗ Error converting {gds_path}: {e}")
        return False


def find_all_gds_files(root_dir='.'):
    """Find all GDS files in the repository."""
    root = Path(root_dir)
    gds_files = list(root.rglob('*.gds'))
    return gds_files


def main():
    """Main conversion routine."""
    print("=" * 60)
    print("GDS to SVG Converter")
    print("=" * 60)
    
    # Find all GDS files
    gds_files = find_all_gds_files()
    
    if not gds_files:
        print("No GDS files found in repository.")
        return 0
        
    print(f"\nFound {len(gds_files)} GDS file(s):\n")
    
    # Convert each file
    success_count = 0
    for gds_file in gds_files:
        if convert_gds_to_svg(gds_file):
            success_count += 1
            
    print("\n" + "=" * 60)
    print(f"Conversion complete: {success_count}/{len(gds_files)} successful")
    print("=" * 60)
    
    return 0 if success_count == len(gds_files) else 1


if __name__ == "__main__":
    sys.exit(main())
