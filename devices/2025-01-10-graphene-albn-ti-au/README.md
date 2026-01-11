# Device Run: Graphene on AlBN with Ti/Au Contacts

## Quick Summary

Following the Ti/Au standard recipe (graphene-ti-au-standard v1.0) with one modification: **substrate changed from Si/SiO2 to AlBN** to match the target device structure. This substrate change introduces uncertainties in optical contrast (may need adjusted lighting/filters), Ti adhesion characteristics, resist adhesion, and liftoff behavior on AlBN. Expected challenges include different optical identification conditions and uncharacterized surface interactions. GDS patterns: hallbar-6contact.gds and alignment-marks.gds.

**Date**: 2025-01-10  
**Base Recipe**: [ti-au-standard](../../recipes/graphene-contacts/ti-au-standard.md)  
**Device ID**: 2025-01-10-graphene-albn-ti-au

**Instruments used:**
- Mask aligner: [Quintel Q4000](../../instruments/lithography/quintel-q4000.md)
- E-beam evaporator: [Thermionics SB60A](../../instruments/ebeam-evaporators/thermionics-ebeam-sb60a.md)

**Materials used:**
- Photoresist: [S1813 batch 2024-12](../../materials/photoresists/s1813-tracker.md#s1813-2024-12)
- Ti pellets: [Lesker lot #12345](../../instruments/ebeam-evaporators/thermionics-ebeam-sb60a.md#ti-pellets)
- Au pellets: [Lesker lot #67890](../../instruments/ebeam-evaporators/thermionics-ebeam-sb60a.md#au-pellets)

## Overview

Testing Ti/Au contact recipe on AlBN substrate instead of standard Si/SiO2.

## Key Modification

- **Substrate**: AlBN (modified from standard Si/SiO2)
- **Reason**: This is closer to the actual device structure we want.

## Directory Contents

```
├── README.md           # This file
├── recipe-used.md      # Full recipe with AlBN modifications
├── gds/                # Lithography patterns
│   └── (add your .gds files here)
├── images/             # Optical/SEM/AFM images
│   └── (add images as you go)
└── data/               # Measurement data
    └── (add data files here)
```

## Process Status

- [ ] Graphene exfoliation
- [ ] Optical identification
- [ ] Photolithography
- [ ] Metal deposition
- [ ] Liftoff
- [ ] Initial characterization

## Expected Challenges

1. Optical contrast on AlBN may differ from SiO2
2. Ti adhesion to AlBN not yet characterized
3. Unknown if resist adhesion differs

## Results Summary

(Fill in after completion)

### Success Metrics:
- Contact resistance: 
- Device functionality: 
- Lessons learned: 

## Related Devices

(Link to similar device runs for comparison)

## Notes

(Add your process notes here as you go)
