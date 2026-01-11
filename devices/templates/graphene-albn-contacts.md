# Template: Graphene Contacts on AlBN Substrate

**Based on**: [Ti/Au standard recipe](../../recipes/graphene-contacts/ti-au-standard.md) v1.0  
**First successful run**: [2025-01-10-graphene-albn-ti-au](../2025-01-10-graphene-albn-ti-au/)  
**Use this template for**: Any graphene contact fabrication on AlBN substrates

## What This Template Includes

Standard process for making contacts on graphene/AlBN that has been validated to work:
- AlBN substrate handling
- Optical identification on AlBN
- HMDS prime (critical for AlBN)
- Standard photolithography
- Metal deposition parameters
- Liftoff procedure

## Standard Parameters

**Substrate**: AlBN  
**Optical ID**: Adjust filters for AlBN contrast (different from SiO2)  
**HMDS Prime**: 150°C, 5 min (YES HMDS oven)  
**Resist**: S1813, 4000 rpm → 1.3 μm  
**Exposure**: Quintel Q4000, ~8s contact mode  
**Development**: MF-319, 60s  
**Liftoff**: Acetone 50°C, 1hr typical, gentle agitation

## Standard Instruments
- E-beam evaporator: [Thermionics SB60A](../../instruments/ebeam-evaporators/thermionics-ebeam-sb60a.md)
- Mask aligner: [Quintel Q4000](../../instruments/lithography/quintel-q4000.md)
- HMDS: [YES HMDS Oven](../../instruments/lithography/yes-hmds-cleanroom.md)

## Standard Materials
- Photoresist: S1813 (current batch tracker [here](../../materials/photoresists/s1813-tracker.md))

## Known Issues & Solutions
- **AlBN optical contrast**: Use polarizers, adjust illumination angle
- **Resist adhesion**: HMDS prime is essential, don't skip
- **Charging during e-beam**: Not typically a problem, but ground if needed

## Typical Results
- Contact resistance: 500-2000 Ω·μm (depends on metal stack)
- Liftoff success rate: >90% with HMDS prime
- Device yield: High if graphene quality is good

## When Creating New Device Using This Template

Only document:
1. **What's different** from this template (different metals, thicknesses, etc.)
2. **Process deviations** that occurred
3. **Results** (especially if comparing to previous devices)

See example: [2025-01-11-graphene-albn-cr-au](../2025-01-11-graphene-albn-cr-au-simple.md)

## Devices Using This Template
- [2025-01-10-graphene-albn-ti-au](../2025-01-10-graphene-albn-ti-au/) - Original/baseline Ti/Au
- [2025-01-11-graphene-albn-cr-au](../2025-01-11-graphene-albn-cr-au-simple.md) - Cr/Au variant
- (Add new devices here)
