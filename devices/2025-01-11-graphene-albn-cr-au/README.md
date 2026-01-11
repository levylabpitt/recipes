# Device Run: Graphene on AlBN with Cr/Au Contacts

## Quick Summary

Following the Ti/Au standard recipe (graphene-ti-au-standard v1.0) with two modifications: **substrate changed from Si/SiO2 to AlBN** and **metal stack changed from Ti/Au (5nm/30nm) to Cr/Au (5nm/60nm)**. Cr provides alternative adhesion layer chemistry and doubled Au thickness may improve contact resistance. This substrate change introduces uncertainties in optical contrast (may need adjusted lighting/filters), Cr adhesion to AlBN, resist adhesion, and liftoff behavior. Expected challenges include different optical identification conditions, uncharacterized Cr-AlBN interface, and potentially more difficult liftoff with thicker Au. GDS patterns: hallbar-6contact.gds and alignment-marks.gds.

**Date**: 2025-01-11  
**Base Recipe**: [ti-au-standard](../../recipes/graphene-contacts/ti-au-standard.md)  
**Device ID**: 2025-01-11-graphene-albn-cr-au  
**Related Device**: [2025-01-10-graphene-albn-ti-au](../2025-01-10-graphene-albn-ti-au/) - Ti/Au version for comparison

**Instruments used:**
- Mask aligner: [Quintel Q4000](../../instruments/lithography/quintel-q4000.md)
- E-beam evaporator: [Thermionics SB60A](../../instruments/ebeam-evaporators/thermionics-ebeam-sb60a.md)

**Materials used:**
- Photoresist: [S1813 batch 2024-12](../../materials/photoresists/s1813-tracker.md#s1813-2024-12)
- Cr pellets: [Source TBD](../../instruments/ebeam-evaporators/thermionics-ebeam-sb60a.md#cr-pellets)
- Au pellets: [Lesker lot #67890](../../instruments/ebeam-evaporators/thermionics-ebeam-sb60a.md#au-pellets)

## Overview

Testing Cr/Au contact recipe on AlBN substrate with thicker Au layer. This device run explores:
1. Cr vs Ti as adhesion layer on AlBN
2. Effect of thicker Au (60nm vs 30nm) on contact resistance
3. Comparison with Ti/Au version from 2025-01-10

## Key Modifications from Base Recipe

### Metal Stack Changes
- **Adhesion layer**: Cr 5nm (instead of Ti 5nm)
  - Reason: Different work function and interface chemistry may affect contact resistance
  - Concern: Cr adhesion to AlBN not previously characterized
  
- **Contact metal**: Au 60nm (instead of 30nm)
  - Reason: Thicker Au may reduce contact resistance
  - Concern: More difficult liftoff with thicker metal

### Substrate Change
- **Substrate**: AlBN (modified from standard Si/SiO2)
- **Reason**: Closer to actual device structure for hBN-encapsulated devices

## Directory Contents

```
├── README.md           # This file
├── recipe-used.md      # Full recipe with modifications
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
- [ ] HMDS vapor prime (may need for AlBN)
- [ ] Photolithography
- [ ] Metal deposition (Cr 5nm / Au 60nm)
- [ ] Liftoff
- [ ] Initial characterization

## Expected Challenges

1. **Optical contrast on AlBN** - may differ from SiO2
2. **Cr adhesion to AlBN** - not previously characterized
3. **Resist adhesion** - unknown if different on AlBN
4. **Liftoff difficulty** - 60nm Au is twice as thick as standard
5. **Cr oxidation** - Cr more prone to oxidation than Ti

## Comparison with Ti/Au Device

This device will be directly compared with [2025-01-10-graphene-albn-ti-au](../2025-01-10-graphene-albn-ti-au/) to evaluate:
- Contact resistance: Cr/Au vs Ti/Au
- Liftoff quality: Effect of thicker Au
- Long-term stability: Cr vs Ti oxidation

## Results Summary

(Fill in after completion)

### Success Metrics:
- Contact resistance (Ω·μm): 
- Two-terminal resistance: 
- Liftoff quality: 
- Comparison with Ti/Au device: 

### Lessons Learned:
- 

## Process Notes

(Add your observations during fabrication)

### HMDS Prime
- Date:
- Duration:
- Observations:

### Photolithography
- Date:
- Exposure time:
- Development time:
- Quality:

### Metal Deposition
- Date:
- Base pressure:
- Cr deposition rate:
- Au deposition rate:
- Tooling factor check:
- Issues:

### Liftoff
- Date:
- Acetone temperature:
- Soak time:
- Agitation method:
- Success:

### Initial Characterization
- Date:
- Contact resistance measurements:
- Observations:

## Related Devices

- [2025-01-10-graphene-albn-ti-au](../2025-01-10-graphene-albn-ti-au/) - Ti/Au on AlBN for direct comparison
- (Link to future devices using Cr/Au)

## References

- Base recipe: [Ti/Au standard](../../recipes/graphene-contacts/ti-au-standard.md)
- (Add relevant literature on Cr contacts if available)
