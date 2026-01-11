# 2D Materials Device Fabrication Recipes

A version-controlled library of device fabrication recipes for 2D materials research, with DOI-able process flows.

**Quick Links:** [How It Works](#how-is-it-organized) | [Creating a Device](#the-workflow) | [Tracking Instruments](#tracking-instruments-and-materials) | [Creating Recipes](#creating-a-new-base-recipe)

---

## What is this repository?

This repository is a version-controlled library of device fabrication recipes for 2D materials research. Think of it as a lab notebook that's:
- **Shared** - everyone can see what processes worked (or didn't)
- **Versioned** - we track changes and can cite specific versions
- **Organized** - recipes are standardized and easy to compare
- **Permanent** - recipes get DOIs so they can be cited in papers

We maintain standardized fabrication recipes for:
- Electrical contacts to 2D materials
- Encapsulation methods
- Transfer techniques
- Device patterning procedures

---

## How is it organized?

The repository has four main parts:

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

### 3. Instruments (`instruments/` directory)

Lab-specific tracking for fabrication equipment:
- Tooling factors and calibrations
- Material batches currently loaded
- Performance quirks and tips
- Links to [official NFCF pages](https://www.nano.pitt.edu/facilities)

See [instruments/README.md](instruments/README.md) for complete list.

### 4. Materials (`materials/` directory)

Tracking consumable batches:
- When bottles were opened
- Batch/lot numbers
- Performance notes
- When exhausted

See [materials/README.md](materials/README.md) for details.

---

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

### Referencing Instruments and Materials

In your device README, after the Quick Summary, add:

```markdown
**Instruments used:**
- E-beam evaporator: [Thermionics SB60A](../../instruments/ebeam-evaporators/thermionics-ebeam-sb60a.md)
- Mask aligner: [Quintel Q4000](../../instruments/lithography/quintel-q4000.md)

**Materials used:**
- Photoresist: [S1813 batch 2024-12](../../materials/photoresists/s1813-tracker.md#s1813-2024-12)
- Ti pellets: [Lesker lot #12345](../../instruments/ebeam-evaporators/thermionics-ebeam-sb60a.md#ti-pellets)
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
   
2. **Update instrument files** with:
   - Tooling factors (if you measured actual vs nominal thickness)
   - Any issues or quirks you noticed
   - A link back to your device run
   
3. **Commit and push** your changes to GitHub

4. **Link to related devices** if you're comparing or iterating

---

## Using Templates for Efficiency (Advanced)

Once you've successfully made a device on a **new substrate or device type**, you can register it as a template to make future variants even easier.

### The Two-Level System

1. **Base Recipes** (most general) - Complete process for standard substrates  
   Example: `recipes/graphene-contacts/ti-au-standard.md`

2. **Devices** - Two types:
   - **2a. First device** (full doc) - Becomes the template  
     Example: `devices/2025-01-10-graphene-albn-ti-au/`
   - **2b. Variants** (diff only) - Just what's different  
     Example: `devices/2025-01-11-graphene-albn-cr-au.md` (single file, ~20 lines)

### How It Works

**First device on new substrate** - Document everything:
```
devices/2025-01-10-graphene-albn-ti-au/
├── README.md (full documentation)
├── recipe-used.md
└── ...
```

**After success** - Register as template in `devices/templates/TEMPLATES.md`:
```markdown
### Graphene Contacts on AlBN
- **Device**: [2025-01-10-graphene-albn-ti-au](../2025-01-10-graphene-albn-ti-au/)
- **Good for**: Any contacts on graphene/AlBN
```

**The device folder IS the template** - no separate template file needed.

**Future variants** - Just document the diff (single file):
```markdown
# Device: 2025-01-11 Graphene/AlBN Cr/Au

**Template**: [2025-01-10-graphene-albn-ti-au](../2025-01-10-graphene-albn-ti-au/)

## Diff from Template
- Metal: Cr/Au (5/60nm) instead of Ti/Au (5/30nm)

## Results
- Rc: 800 Ω·μm (vs 1200 for Ti/Au)
```

**Benefits**:
- First device: 150 lines (full doc, becomes the template)
- TEMPLATES.md: Just a pointer, no duplication
- Variants: 20 lines each
- 10 variants = 300 lines total vs 1500 without templates

**Key insight:** Once you have a template example, AI can generate variant files following the same conventions for different processes.

See [devices/templates/](devices/templates/) for the template registry and examples.

---

## Why this structure?

**Efficiency**: You don't need to copy the entire recipe every time. Just reference the base recipe and note what's different.

**Clarity**: Anyone (including future you) can quickly understand what you did by reading the Quick Summary.

**Comparability**: When devices use the same base recipe, it's easy to see what changed between runs.

**Citability**: Base recipes get DOIs, so you can cite them in papers.

**Reproducibility**: Tracking instruments and materials helps identify why nominally identical processes give different results.

---

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

See the [complete instrument list](instruments/README.md) organized by category:
- Metal deposition (e-beam, thermal, sputtering)
- Dielectric deposition (CVD, ALD, parylene)
- Lithography (e-beam, photo, 3D)
- Etching (RIE, ICP-RIE, plasma)
- Thermal processing (RTA, furnaces)
- Characterization (FIB/SEM, profilometry, thin film analysis)

### Materials

The `materials/` directory tracks consumable batches:
- When bottles were opened
- Batch/lot numbers
- Performance notes
- When exhausted

This helps identify when performance changes are due to aged materials vs. process variations.

See [materials/README.md](materials/README.md) for tracking system details.

### Best practices for linking

- **Link liberally** - instruments, materials, related devices
- **Update as you go** - add tooling factors and notes while it's fresh
- **Check existing files first** - see if someone already documented the quirk you noticed
- **Use anchor links** for specific batches: `#s1813-2024-12`

---

## Creating a new base recipe

If you're developing a new process:

1. Create a file in the appropriate `recipes/[category]/` directory
2. Follow the format of existing recipes (see `ti-au-standard.md` as a template)
3. Include metadata at the top (YAML frontmatter):
   ```yaml
   ---
   recipe_id: your-recipe-id
   version: 1.0
   doi: [To be assigned by Zenodo]
   date: YYYY-MM-DD
   materials: [list, of, materials]
   geometry: Description
   substrate: Substrate type
   ---
   ```
4. Add a Mermaid flowchart showing the process flow
5. Document detailed steps, expected results, and troubleshooting

When the recipe is stable and ready for others to use:
1. Tag it: `git tag [recipe-id]-v1.0`
2. Push the tag: `git push --tags`
3. Create a GitHub release
4. Zenodo will automatically generate a DOI
5. Update the recipe metadata with the DOI

---

## Creating a DOI for a Recipe or Device

1. Finalize the recipe or device documentation
2. Tag it: `git tag [recipe-id]-v[version]` or `git tag device-[date]-[name]`
3. Push tag: `git push --tags`
4. Create a GitHub release from the tag
5. Zenodo automatically generates a DOI
6. Update metadata with DOI

**When to create DOIs:**
- Base recipes: When finalized and ready for team use
- Device runs: When used in a publication

---

## Tips for new users

- **Start simple**: Use an existing base recipe for your first device run
- **Keep summaries concise**: Focus on what's different, not what's the same
- **Document as you go**: It's easier than trying to remember everything later
- **Link everything**: Instruments, materials, related devices - liberal linking creates a traceable web
- **Ask questions**: If you're unsure about something, ask the team or check existing device runs for examples

---

## Repository Structure

```
recipes/
├── README.md              # This file
├── recipes/               # Base recipes
│   ├── graphene-contacts/
│   │   ├── ti-au-standard.md
│   │   └── README.md
│   └── hBN-encapsulation/
│       └── README.md
├── devices/               # Specific device runs
│   ├── templates/         # Template registry (pointers only)
│   │   ├── TEMPLATES.md   # List of template devices
│   │   └── README.md
│   ├── 2025-01-10-graphene-albn-ti-au/  # Full device (can be template)
│   │   ├── README.md
│   │   ├── recipe-used.md
│   │   ├── gds/
│   │   ├── images/
│   │   └── data/
│   └── 2025-01-11-graphene-albn-cr-au.md  # Variant (diff only)
├── instruments/           # Equipment tracking
│   ├── README.md
│   ├── ebeam-evaporators/
│   ├── lithography/
│   └── [other-categories]/
├── materials/             # Consumable tracking
│   ├── README.md
│   └── photoresists/
├── metadata/
│   └── recipe-index.yaml
└── CITATION.cff
```

---

## Contributing

This repository is for team use. Team members should:
1. Create device runs following the structure above
2. Update instrument and material files after use
3. Follow the templates and examples
4. Commit and push regularly
5. Create base recipes for new processes

---

## License

[Specify license - e.g., CC-BY-4.0 for methods]

---

## Questions or Suggestions?

This is a living system - if you have suggestions for improvements, let's discuss them!

**Contact**: Jeremy Levy, University of Pittsburgh
