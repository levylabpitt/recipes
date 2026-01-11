# Device Run Created: 2025-01-11-graphene-albn-cr-au

## What Was Created

A complete device run folder for testing Cr/Au contacts (instead of Ti/Au) on AlBN substrate with doubled Au thickness.

## Directory Structure

```
devices/2025-01-11-graphene-albn-cr-au/
├── README.md              # Quick summary and process tracking
├── recipe-used.md         # Full recipe with Cr/Au modifications
├── gds/
│   └── README.md         # GDS file placeholder
├── images/
│   └── README.md         # Image directory guide
└── data/
    └── README.md         # Data directory guide
```

## Key Features

### Quick Summary
- References base Ti/Au recipe
- Highlights TWO modifications:
  1. AlBN substrate (same as yesterday's device)
  2. Cr/Au metal stack with 2× thicker Au
- Links to yesterday's Ti/Au device for comparison
- Lists expected challenges specific to Cr and thicker Au

### Process Flow
- Mermaid diagram updated for Cr/Au stack
- Added HMDS prime step for AlBN
- Noted extended liftoff time for thicker metal

### Detailed Recipe
- Complete step-by-step adapted from Ti/Au standard
- Cr-specific notes (oxidation, work function)
- Thicker Au considerations (liftoff difficulty)
- Troubleshooting section
- Comparison metrics with Ti/Au device

### Organization
- Same structure as previous device
- Direct comparison links
- Placeholder READMEs in subdirectories

## Next Steps

1. **Copy GDS files** from 2025-01-10 device (using same patterns)
2. **As you fabricate**, update the Process Notes section in README.md
3. **Check off** process status items as completed
4. **Add images** with descriptive names as you go
5. **Record data** in the data directory
6. **Update instrument files** after using equipment:
   - Record Cr and Au tooling factors
   - Note any issues with thicker Au deposition
7. **Compare results** with Ti/Au device from 2025-01-10

## How This Demonstrates the System

This device run shows:
- ✅ Building on previous work (references 2025-01-10 device)
- ✅ Systematic variation (Cr vs Ti, thick vs thin Au)
- ✅ Clear documentation of modifications
- ✅ Comparison framework built in
- ✅ Anticipating challenges specific to changes
- ✅ Linking between related devices

## Simulated LLM Conversation

**You**: "I am making a device similar to https://github.com/levylabpitt/recipes/tree/main/devices/2025-01-10-graphene-albn-ti-au. But I am going to try Cr/Au contacts this time and I want to make the Au twice as thick."

**LLM**: "Great! I'll create a new device run for you. Let me set up:
- New device folder: 2025-01-11-graphene-albn-cr-au
- Modified recipe using Cr instead of Ti
- Au thickness increased to 60nm
- Links to yesterday's device for comparison
- Notes about expected challenges with Cr oxidation and thicker Au liftoff

I've created the complete folder structure with:
- README with Quick Summary highlighting your modifications
- Full recipe-used.md with Cr/Au specific notes
- Process tracking checklists
- Comparison framework with Ti/Au device
- Subdirectories for GDS, images, and data

Ready to start fabrication! The main things to watch are:
1. HMDS prime may be critical on AlBN
2. Cr oxidation - handle carefully
3. Longer liftoff time with 60nm Au
4. Direct comparison with yesterday's Ti/Au contacts"

---

**Files are ready at:**
`C:\Users\jerem\github\recipes\devices\2025-01-11-graphene-albn-cr-au\`

**To add to GitHub:**
```bash
cd C:\Users\jerem\github\recipes
git add devices/2025-01-11-graphene-albn-cr-au
git commit -m "Add device run 2025-01-11: Cr/Au contacts on AlBN with 2x Au thickness"
git push
```
