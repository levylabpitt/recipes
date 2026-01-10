---
recipe_id: graphene-ti-au-standard
version: 1.0
doi: [To be assigned by Zenodo]
date: 2025-01-10
materials: [graphene, Ti, Au]
geometry: Hall bar (6 contacts)
substrate: AlBN (modified from Si/SiO2)
device_id: 2025-01-10-graphene-albn-ti-au
---

# Graphene Hall Bar Contacts - Ti/Au on AlBN Substrate

**Base Recipe**: [ti-au-standard.md](../../recipes/graphene-contacts/ti-au-standard.md)

**Substrate Modification**: Using AlBN instead of Si/SiO2

## Process Flow

```mermaid
graph TD
    A[Exfoliate graphene onto AlBN substrate] --> B[Optical identification]
    B --> C{Monolayer or bilayer?}
    C -->|Yes| D[Mark coordinates]
    C -->|No| B
    D --> E[Spin photoresist<br/>e.g., S1813, 4000rpm]
    E --> F[Soft bake<br/>115°C, 90s]
    F --> G[Photolithography<br/>Hall bar pattern, 6 contacts]
    G --> H[Develop<br/>MF-319, ~60s]
    H --> I[Descum<br/>O2 plasma, 10s]
    I --> J[Metal deposition<br/>Ti 5nm / Au 30nm<br/>e-beam evaporation]
    J --> K[Liftoff<br/>Acetone bath, 50°C<br/>gentle agitation, ~1hr]
    K --> L[IPA rinse + N2 dry]
    L --> M[Optical inspection]
```

## Substrate-Specific Considerations

### AlBN vs SiO2 Differences:
1. **Optical contrast**: Different from standard SiO2 - may need adjusted lighting/filters
2. **Surface properties**: AlBN may have different wetting/adhesion characteristics
3. **Charging**: Consider conductivity differences during e-beam deposition

### Potential Process Adjustments:
- Monitor photoresist adhesion on AlBN
- Check if Ti adhesion layer thickness needs adjustment
- Verify liftoff characteristics on AlBN surface

## Detailed Steps

[Same steps as base recipe - see linked recipe above]

## Process Log

### Pre-fabrication:
- Date started: 
- Substrate batch: 
- Graphene source: 
- Flake ID: 

### Deviations from base recipe:
- [ ] None
- [ ] (Document any changes here)

### Process notes:
(Add observations during fabrication)

## Results

### Device Characteristics:
- Contact resistance: 
- Two-terminal resistance: 
- Gate response: 

### Images:
- See `images/` directory

### Data:
- See `data/` directory

## GDS Files

Pattern used: `gds/hallbar-6contact.gds` (add your file here)
