# Automation Scripts

This directory contains scripts used by GitHub Actions and local development.

## convert_gds_to_svg.py

Automatically converts all GDS files in the repository to SVG format for easy preview on GitHub.

**Usage (local):**
```bash
pip install gdstk
python scripts/convert_gds_to_svg.py
```

**Automatic usage:**
This script runs automatically via GitHub Actions whenever a `.gds` file is pushed to the repository.

**What it does:**
- Finds all `.gds` files in the repo
- Converts each to `.svg` format
- Places SVG next to original GDS file
- SVGs are committed back to the repo automatically

**Manual trigger:**
You can also manually trigger the conversion:
1. Go to GitHub → Actions tab
2. Select "Convert GDS to SVG" workflow
3. Click "Run workflow"
