# Guide to the Recipe Database

Welcome! This guide explains how our recipe database works and how to use it effectively for device fabrication.

## What is this database?

This repository is a version-controlled library of device fabrication recipes for 2D materials research. Think of it as a lab notebook that's:
- **Shared** - everyone can see what processes worked (or didn't)
- **Versioned** - we track changes and can cite specific versions
- **Organized** - recipes are standardized and easy to compare
- **Permanent** - recipes get DOIs so they can be cited in papers

## How is it organized?

The repository has two main parts:

### 1. Base Recipes (`recipes/` directory)

These are the **standard, reusable protocols** organized by category:
- `recipes/graphene-contacts/` - contact fabrication methods
- `recipes/hBN-encapsulation/` - encapsulation techniques
- (more categories as needed)

Each base recipe contains:
- Complete step-by-step instructions
- Process flow diagram (Mermaid format)
- Expected results and troubleshooting tips
- Metadata (materials, geometry, substrate, version)

**Example**: `recipes/graphene-contacts/ti-au-standard.md` is our standard Ti/Au contact recipe for graphene on Si/SiO2.

### 2. Device Runs (`devices/` directory)

These are **specific instances** where you used a recipe to make a device. Each device run:
- References a base recipe
- Documents what you changed (if anything)
- Tracks your process notes and results
- Stores related files (GDS patterns, images, data)

**Example**: `devices/2025-01-10-graphene-albn-ti-au/` documents using the Ti/Au standard recipe with an AlBN substrate instead of Si/SiO2.

## The workflow

### When you're planning to make a device:

1. **Find or create a base recipe** in `recipes/[category]/`
   - If a recipe exists for what you want, use it
   - If you're doing something new, create a new base recipe
   
2. **Create a device run folder** in `devices/`
   - Name it: `YYYY-MM-DD-brief-description`
   - Example: `2025-01-10-graphene-albn-ti-au`

3. **Set up the device folder** with this structure:
   ```
   devices/2025-01-10-your-device/
   ├── README.md           # Quick summary and status
   ├── recipe-used.md      # Full recipe with your modifications
   ├── gds/                # Lithography patterns
   ├── images/             # Optical/SEM/AFM images
   └── data/               # Measurement data
   ```

### Writing the Quick Summary

The most important part of your device README is the **Quick Summary** section at the top. This should be a single paragraph that:
- References the base recipe you're using
- Highlights **only what's different** from the base recipe
- Notes expected challenges or unknowns
- Lists key files (GDS patterns, etc.)

**Template**:
```markdown
## Quick Summary

Following the [base recipe name] ([recipe-id] v[version]) with [number] modification(s): 
**[key change 1]**, **[key change 2]**. [Brief rationale]. This introduces uncertainties 
in [specific concerns]. Expected challenges include [list challenges]. GDS patterns: 
[pattern-names.gds].
```

**Example**:
```markdown
## Quick Summary

Following the Ti/Au standard recipe (graphene-ti-au-standard v1.0) with one modification: 
**substrate changed from Si/SiO2 to AlBN** to match the target device structure. This 
substrate change introduces uncertainties in optical contrast (may need adjusted 
lighting/filters), Ti adhesion characteristics, resist adhesion, and liftoff behavior 
on AlBN. Expected challenges include different optical identification conditions and 
uncharacterized surface interactions. GDS patterns: hallbar-6contact.gds and 
alignment-marks.gds.
```

### As you're fabricating:

1. **Update the process status checklist** in your device README
2. **Add process notes** as you go - deviations, observations, problems
3. **Save files** in the appropriate subdirectories:
   - GDS files → `gds/`
   - Images → `images/`
   - Data → `data/`

### After fabrication:

1. **Fill in the Results Summary** with:
   - Contact resistance, device functionality
   - What worked, what didn't
   - Lessons learned
   
2. **Commit and push** your changes to GitHub

3. **Link to related devices** if you're comparing or iterating

## Why this structure?

**Efficiency**: You don't need to copy the entire recipe every time. Just reference the base recipe and note what's different.

**Clarity**: Anyone (including future you) can quickly understand what you did by reading the Quick Summary.

**Comparability**: When devices use the same base recipe, it's easy to see what changed between runs.

**Citability**: Base recipes get DOIs, so you can cite them in papers.

## Tips for new users

- **Start simple**: Use an existing base recipe for your first device run
- **Keep summaries concise**: Focus on what's different, not what's the same
- **Document as you go**: It's easier than trying to remember everything later
- **Ask questions**: If you're unsure about something, ask the team or check existing device runs for examples

## Tracking Instruments and Materials

### Why track instruments?

Nominally "identical" recipes can give different results depending on:
- Which deposition tool you used (different base pressures, calibrations)
- How old the photoresist is
- When metal pellets were last replaced
- Tool-specific quirks and calibrations

By tracking these details, we can identify patterns and improve reproducibility.

### Instruments

The `instruments/` directory tracks lab-specific information about equipment:
- Tooling factors and calibrations
- Material batches currently loaded
- Performance quirks
- Tips and tricks

**We don't duplicate NFCF documentation.** Instead, we link to the [official NFCF pages](https://www.nano.pitt.edu/facilities) and add only our lab-specific notes.

**In your device run**, reference specific instruments:
```markdown
**Instruments used:**
- E-beam evaporator: [Thermionics SB60A](../../instruments/ebeam-evaporators/thermionics-ebeam-sb60a.md)
- Mask aligner: [Quintel Q4000](../../instruments/lithography/quintel-q4000.md)
```

**After using an instrument**, update its file with:
- Tooling factors (if you measured actual vs nominal thickness)
- Any issues or quirks you noticed
- A link back to your device run

### Materials

The `materials/` directory tracks consumable batches:
- When bottles were opened
- Batch/lot numbers
- Performance notes
- When exhausted

**In your device run**, reference specific batches:
```markdown
**Materials used:**
- Photoresist: [S1813 batch 2024-12](../../materials/photoresists/s1813-tracker.md#s1813-2024-12)
- Ti pellets: [Lesker lot #12345](../../materials/metals/ti-pellets-tracker.md#lot-12345)
```

This helps identify when performance changes are due to aged materials vs. process variations.

### Best practices for linking

- **Link liberally** - instruments, materials, related devices
- **Update as you go** - add tooling factors and notes while it's fresh
- **Check existing files first** - see if someone already documented the quirk you noticed
- **Use anchor links** for specific batches: `#s1813-2024-12`

## Creating a new base recipe

If you're developing a new process:

1. Create a file in the appropriate `recipes/[category]/` directory
2. Follow the format of existing recipes (see `ti-au-standard.md` as a template)
3. Include metadata at the top (YAML frontmatter)
4. Add a Mermaid flowchart showing the process flow
5. Document detailed steps, expected results, and troubleshooting

When the recipe is stable and ready for others to use:
1. Tag it: `git tag [recipe-id]-v1.0`
2. Push the tag: `git push --tags`
3. Create a GitHub release
4. Zenodo will automatically generate a DOI

## Questions?

This is a living system - if you have suggestions for improvements, let's discuss them!

Contact: Jeremy Levy
