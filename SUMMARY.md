# Summary: Recipe Database with Instrument and Material Tracking

## What We've Created

A lightweight system for tracking device fabrication that:
1. **References** the NFCF facility documentation (doesn't duplicate it)
2. **Tracks** lab-specific metadata: tooling factors, material batches, quirks
3. **Links** everything together for easy tracing and troubleshooting

## Key Principle

**Don't reinvent the wheel.** The NFCF maintains comprehensive equipment documentation at https://www.nano.pitt.edu/facilities. We link to their pages and add only what's unique to our lab's experience.

## Directory Structure

```
recipes/
├── GUIDE.md                    # Main documentation (start here!)
├── README.md                   # Overview
├── recipes/                    # Base recipes
│   └── graphene-contacts/
│       └── ti-au-standard.md
├── devices/                    # Specific device runs
│   └── 2025-01-10-graphene-albn-ti-au/
│       ├── README.md           # Quick summary + links
│       ├── recipe-used.md
│       ├── gds/
│       ├── images/
│       └── data/
├── instruments/                # Lab-specific instrument tracking
│   ├── README.md               # How to use this directory
│   ├── ebeam-evaporators/
│   │   ├── thermionics-ebeam-sb60a.md
│   │   └── plassys-ebeam-cleanroom.md
│   └── lithography/
│       ├── raith-eline.md
│       └── quintel-q4000.md
└── materials/                  # Consumable batch tracking
    ├── README.md
    └── photoresists/
        └── s1813-tracker.md
```

## How It Works

### 1. Base Recipes (recipes/)
Complete, reusable protocols for standard processes. These get version numbers and DOIs.

### 2. Device Runs (devices/)
Each device run:
- References a base recipe
- Lists only what's different
- Links to specific instruments and materials used
- Tracks results and lessons learned

### 3. Instruments (instruments/)
Each instrument file:
- Links to official NFCF page
- Tracks tooling factors and calibrations
- Records material batches currently loaded
- Collects tips and tricks
- Lists device runs that used it

### 4. Materials (materials/)
Each material tracker:
- Records when batches were opened/exhausted
- Notes batch-specific performance
- Links to device runs
- Helps identify when problems are due to aged materials

## The Linking Strategy

Everything links to everything:

**Device Run** → references:
- Base recipe
- Specific instruments used
- Specific material batches used

**Instrument file** → links to:
- NFCF official page
- Device runs that used it
- Material batches loaded in it

**Material tracker** → links to:
- Device runs that used it
- Related materials (e.g., resist → developer)

This creates a traceable web of information.

## Example Workflow

### Planning a device:
1. Find base recipe: `recipes/graphene-contacts/ti-au-standard.md`
2. Create device folder: `devices/2025-01-15-my-device/`
3. Write Quick Summary noting any changes from base recipe

### During fabrication:
1. Reference instruments and materials in README
2. Take notes as you go
3. Update process status checklist

### After fabrication:
1. Fill in results
2. Update instrument files with:
   - Tooling factors (if measured)
   - Any quirks noticed
   - Link back to your device
3. Update material trackers if you noticed batch-specific issues

### Over time:
- Instrument files accumulate calibration data
- Material trackers show shelf life patterns
- Device runs build comparative history
- Patterns emerge about what works where

## Benefits

1. **Reproducibility**: Know exactly which tool and batch were used
2. **Troubleshooting**: Quickly identify if issues are process vs. equipment vs. materials
3. **Knowledge transfer**: New students can learn from accumulated tips
4. **Efficiency**: Don't duplicate NFCF docs, just add what's missing
5. **Comparability**: Easy to see what changed between similar devices

## Maintenance

**Low overhead by design:**
- Official specs live on NFCF site (they maintain it)
- You add only what you observe/measure
- Links create connections without duplication
- Empty sections are fine - fill in as you learn

## Getting Started

1. Read `GUIDE.md`
2. Look at existing device run as example
3. When you use an instrument, check if a file exists
4. If not, copy a template and fill in what you know
5. Update as you go, leave blanks for unknown info

## Questions?

This is a living system. Improve it as you use it!

Contact: Jeremy Levy
