# Shipley S1813 Photoresist Batch Tracker

**Material**: Shipley S1813 Positive Photoresist  
**Type**: Novolac-based positive tone  
**Typical Use**: General photolithography, metal liftoff  
**Storage**: Yellow room, <75°F

## Active Batches

| Batch ID | Date Opened | Opened By | Location | Expiration | Status | Notes |
|----------|-------------|-----------|----------|------------|--------|-------|
| S1813-2024-12 | 2024-12-15 | JDoe | Yellow room shelf 2 | 2025-06-15 | Active | Fresh bottle |
| S1813-2024-09 | 2024-09-01 | JSmith | Yellow room shelf 2 | 2025-03-01 | Low | ~25% remaining |

## Archived Batches

| Batch ID | Date Opened | Date Exhausted/Disposed | Performance Notes |
|----------|-------------|-------------------------|-------------------|
| S1813-2024-06 | 2024-06-01 | 2024-11-30 | Consistent performance throughout |
| S1813-2024-03 | 2024-03-15 | 2024-08-20 | Some yellowing near end, still usable |

## Typical Performance Parameters

**Spin Coating** (using [specific spin coater](../../instruments/)):
- 4000 rpm, 45s → ~1.3 μm thickness
- 5000 rpm, 45s → ~1.1 μm thickness
- 3000 rpm, 45s → ~1.6 μm thickness

**Soft Bake**:
- 115°C, 90s on hotplate

**Exposure** (Quintel Q4000):
- 7-10 seconds contact mode
- Adjust based on feature size

**Development**:
- MF-319 developer, 60s typical
- Watch for complete development (no rainbow film)

## Batch-Specific Notes

### S1813-2024-12
- Opened: 2024-12-15
- Spins very uniformly at 4000 rpm
- No issues observed
- Used in: [2025-01-10-graphene-albn-ti-au](../../devices/2025-01-10-graphene-albn-ti-au/)

### S1813-2024-09
- Opened: 2024-09-01
- Starting to show some edge beading
- May need slightly longer development time (65s vs 60s)
- Used in: [device links]

## Known Issues Across Batches

| Date Reported | Batch | Issue | Cause/Resolution |
|---------------|-------|-------|------------------|
| 2024-10-15 | S1813-2024-09 | Poor adhesion on AlBN | Added HMDS prime before spin |
| 2024-08-01 | S1813-2024-06 | Incomplete liftoff | Increased soft bake to 120°C |

## Storage and Handling Best Practices

- Store in yellow room at controlled temperature
- Always allow bottle to reach room temperature before opening
- Use within 6 months of opening
- Check for yellowing or sediment before use
- Dispense via syringe/filter if contamination suspected

## Related Materials

- Developer: [MF-319](../developers/mf-319.md)
- HMDS: [HMDS batch tracker](../adhesion-promoters/hmds.md)

## Device Runs Using This Material

*Automatically populated from device runs, or add manually*

- [2025-01-10-graphene-albn-ti-au](../../devices/2025-01-10-graphene-albn-ti-au/) - S1813-2024-12
