---
marp: true
theme: default
paginate: true
header: 2D Materials Device Fabrication Recipe Database
footer: Levy Lab - University of Pittsburgh
---

<!-- _class: lead -->

# Device Fabrication Recipe Database

**A Version-Controlled System for Reproducible Device Fabrication**

Levy Lab, University of Pittsburgh

---

## What It Is

A Git repository for tracking device fabrication:

```
recipes/                    # General processes
devices/                    # Your actual devices
  ├── templates/            # Registry of good templates
  ├── 2025-01-10-device/    # Full documentation
  └── 2025-01-11-variant.md # Diff from template
instruments/                # Tool-specific metadata
materials/                  # Batch tracking
```

---

## The Two-Level System

```
┌─────────────────────────────────────┐
│ 1. Base Recipes (Most General)     │
│    recipes/ti-au-standard.md        │
│    • Complete process               │
│    • ~300 lines                     │
└─────────────────────────────────────┘
                ↓
┌─────────────────────────────────────┐
│ 2a. First Device (Full Doc)         │
│     devices/2025-01-10-albn-ti-au/  │
│     • Substrate-specific            │
│     • ~150 lines                    │
│     • IS the template               │
└─────────────────────────────────────┘
                ↓
┌─────────────────────────────────────┐
│ 2b. Variant Devices (Just Diff)     │
│     devices/2025-01-11-cr-au.md     │
│     • Points to first device        │
│     • ~20 lines                     │
└─────────────────────────────────────┘
```

---

## Base Recipes

**General processes for standard substrates**

`recipes/graphene-contacts/ti-au-standard.md`

- Complete step-by-step instructions
- Process flow diagrams
- Expected results and troubleshooting
- Version controlled, gets DOI

---

## First Device (Full Documentation)

**When working on a new substrate:**

`devices/2025-01-10-graphene-albn-ti-au/`

```
├── README.md           # Quick summary
├── recipe-used.md      # Full adapted recipe
├── gds/                # Patterns
├── images/             # Microscopy
└── data/               # Measurements
```

**This becomes the template** - no separate file needed.

---

## Registering as Template

Add to `devices/templates/TEMPLATES.md`:

```markdown
### Graphene Contacts on AlBN
- **Device**: 2025-01-10-graphene-albn-ti-au
- **Good for**: Any contacts on graphene/AlBN
```

Just a pointer - the actual documentation stays in the device folder.

---

## Variant Devices

**When making similar devices:**

`devices/2025-01-11-graphene-albn-cr-au.md`

```markdown
# Device: 2025-01-11 Graphene/AlBN Cr/Au

**Template**: 2025-01-10-graphene-albn-ti-au

## Diff from Template
- Metal: Cr/Au (5/60nm) instead of Ti/Au (5/30nm)

## Results
- Rc: 800 Ω·μm (vs 1200 for Ti/Au)
```

Single file, ~20 lines.

---

## Three Ways to Create Devices

1. **Manual** - Create folders and files yourself
2. **Template-based** - Single diff file (~20 lines)
3. **AI-assisted** - Describe to Claude, it generates the file

**Key:** Once you have a template example, AI can generate variant files following the same conventions.

---

## Linking System

Every device links to:

- **Base recipe** it's based on
- **Template device** (if using one)
- **Related devices** for comparison
- **Instruments used**
- **Material batches**

Creates a traceable web of information.

---

## Instrument Tracking

`instruments/ebeam-evaporators/thermionics-ebeam-sb60a.md`

Tracks:
- Tooling factors (measured vs nominal thickness)
- Material batches currently loaded
- Performance quirks
- Links to devices that used it

Links to official NFCF pages - we only add lab-specific metadata.

---

## Material Tracking

`materials/photoresists/s1813-tracker.md`

Tracks:
- When bottles were opened
- Batch/lot numbers
- Performance notes
- When exhausted

Helps identify when problems are due to aged materials vs process.

---

## Example: Real Usage

```
Jan 10: First AlBN device (Ti/Au)
        → Full doc, 150 lines
        → Works! Rc = 1200 Ω·μm
        → Register as template

Jan 11: Try Cr/Au variant
        → Diff file, 20 lines
        → Works! Rc = 800 Ω·μm

Jan 15: Try Pd/Au variant  
        → Diff file, 20 lines
        → Result: Rc = 650 Ω·μm
```

---

## Repository Structure

```
recipes/
├── Base recipes (Ti/Au standard, etc)
devices/
├── templates/TEMPLATES.md ← Registry
├── 2025-01-10-full-doc/ ← Template device
└── 2025-01-11-diff.md ← Variant
instruments/
├── ebeam-evaporators/
└── lithography/
materials/
└── photoresists/
```

---

## Key Principles

1. **No duplication** - First device IS the template
2. **Document differences** - Variants are just diffs
3. **Link everything** - Create traceable web
4. **Update instruments** - Track tool-specific factors
5. **Use AI** - Templates guide AI to generate compliant files

---

## Getting Started

1. Clone the repository
2. Read the README
3. Look at example devices
4. Make your first device
5. Update instrument files after use

**Repository:** https://github.com/levylabpitt/recipes

---

<!-- _class: lead -->

# Questions?

**Contact:** Jeremy Levy, University of Pittsburgh

**Repository:** https://github.com/levylabpitt/recipes
