# The Two-Level System

## Simple Hierarchy

```
┌─────────────────────────────────────────────────────────┐
│ Level 1: BASE RECIPES (Most General)                   │
│ recipes/graphene-contacts/ti-au-standard.md            │
│                                                         │
│ • Complete process for standard substrate (Si/SiO2)    │
│ • Version controlled, gets DOI                         │
│ • Comprehensive documentation                          │
└─────────────────────────────────────────────────────────┘
                        ↓
┌─────────────────────────────────────────────────────────┐
│ Level 2a: FIRST DEVICE (Full Documentation)            │
│ devices/2025-01-10-graphene-albn-ti-au/                │
│                                                         │
│ • Full documentation of AlBN adaptation                │
│ • IS the template (no separate template file)          │
│ • Listed in TEMPLATES.md registry                      │
└─────────────────────────────────────────────────────────┘
                        ↓
┌─────────────────────────────────────────────────────────┐
│ Level 2b: VARIANT DEVICES (Just the Diff)              │
│ devices/2025-01-11-graphene-albn-cr-au.md              │
│                                                         │
│ • Points to 2025-01-10 device                          │
│ • Only documents what's different                      │
│ • ~20 lines                                            │
└─────────────────────────────────────────────────────────┘
```

## No Redundancy

**Base Recipe** → One place  
**First Successful Device** → One place (IS the template)  
**TEMPLATES.md** → Just pointers to successful devices  
**Variant Devices** → Just diffs  

**Total:** No information is duplicated anywhere.

## Example Flow

### Step 1: Make First AlBN Device
```
devices/2025-01-10-graphene-albn-ti-au/
├── README.md (full doc)
├── recipe-used.md
└── ...
```

### Step 2: Register It
Add to `templates/TEMPLATES.md`:
```markdown
### Graphene Contacts on AlBN
- **Device**: 2025-01-10-graphene-albn-ti-au
```

### Step 3: Make Variants
`devices/2025-01-11-graphene-albn-cr-au.md`:
```markdown
**Template**: 2025-01-10-graphene-albn-ti-au
**Diff**: Cr/Au instead of Ti/Au
```

## Why No Separate Template Files?

Because they would duplicate information from the first device.

**The first successful device already contains:**
- Substrate-specific adaptations
- Validated parameters
- Known issues
- Typical results

**Why duplicate it?** Just point to it.

## What If the Template Device Changes?

If you update the first device (e.g., improve the process), all variant devices automatically see the update since they're just pointing to it.

This is a **feature**, not a bug.

## Summary

Two levels:
1. **Base recipes** - General processes
2. **Devices** - Some are full docs (templates), some are diffs (variants)

**TEMPLATES.md** = Index of which devices make good templates

**That's it.** No extra layer, no duplication.
