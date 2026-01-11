# Materials Directory

This directory tracks consumable materials used in device fabrication - photoresists, developers, solvents, deposition materials, etc.

## Purpose

Track material batches to help identify when:
- A resist batch goes bad
- Deposition material needs replacement
- Performance changes correlate with new material batches

## Organization

```
materials/
├── photoresists/
│   ├── s1813-tracker.md
│   ├── az5214e-tracker.md
│   ├── pmma-tracker.md
│   └── ...
├── developers/
│   ├── mf-319-tracker.md
│   └── ...
├── metals/
│   ├── ti-pellets-tracker.md
│   ├── au-pellets-tracker.md
│   └── ...
└── [other-categories]/
```

## How to Use

### When opening a new batch:

1. Find or create the tracker file for that material
2. Add an entry with:
   - Batch ID (create one if vendor doesn't provide)
   - Date opened
   - Who opened it
   - Storage location
   - Expiration date

### When using a batch:

1. Reference it in your device run:
   ```markdown
   **Materials used:**
   - Photoresist: [S1813 batch 2024-12](../../materials/photoresists/s1813-tracker.md#s1813-2024-12)
   ```

2. If you notice performance issues:
   - Document in the batch-specific notes
   - This helps identify whether it's the process or the material

### When a batch is exhausted:

1. Move it to "Archived Batches"
2. Add final performance notes
3. This history helps with troubleshooting

## Example: Tracking Resist Age Effects

If multiple people notice their S1813 liftoff getting worse:
1. Check the batch tracker
2. See when the bottle was opened
3. Realize it's 5 months old and starting to degrade
4. Open a fresh bottle
5. Document the observation so others know the shelf life

## Tips

- **Be consistent with batch IDs**: Use format like `[material]-YYYY-MM` for simplicity
- **Link from device runs**: Makes it easy to trace back issues
- **Update expiration dates**: Based on actual shelf life observed, not just manufacturer specs
- **Note storage conditions**: Temperature, light exposure matter for some materials
