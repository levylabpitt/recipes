# Templates Directory

## What This Is

A **registry** pointing to successful device runs that work well as templates.

**Not** a directory of template files - those would duplicate information.

## The System

```
Base Recipe (recipes/)
    ↓
First Device on New Substrate (devices/YYYY-MM-DD-name/)
    ← TEMPLATES.md points here
    ↓
Variant Devices (devices/YYYY-MM-DD-variant.md)
    ← Just diff files pointing to first device
```

## Key Files

- **TEMPLATES.md** - List of good template devices (start here)
- **HIERARCHY-EXPLAINED.md** - Visual explanation
- **README.md** - This file

## Philosophy

**The first successful device IS the template.**

No need to copy information - just point to it and document what's different.
