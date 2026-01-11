# Device: 2025-01-11 Graphene/AlBN Cr/Au

**Template**: [graphene-albn-contacts](templates/graphene-albn-contacts.md)  
**Date**: 2025-01-11

## Diff from Template
- **Metal stack**: Cr/Au (5nm/60nm) instead of Ti/Au (5nm/30nm)
- **Rationale**: Testing Cr adhesion chemistry, thicker Au for lower Rc

## Process Deviations
- **Liftoff time**: 2hr (vs 1hr standard) - thicker Au needed longer soak
- **Cr deposition rate**: 0.8 Å/s - stable

## Results
- **Contact resistance**: 800 Ω·μm
- **vs Ti/Au baseline**: 33% improvement (1200 → 800 Ω·μm)
- **Liftoff quality**: Good despite thicker metal
- **Observations**: Slight Cr discoloration after 24hr in air (oxidation)

## Files
- Images: `images/2025-01-11/`
- Data: `data/2025-01-11-resistance.csv`

## Next
Try 100nm Au to see if Rc improves further, or test Cr oxidation mitigation (immediate vacuum storage).
