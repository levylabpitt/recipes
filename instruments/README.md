# Instruments Directory

This directory tracks lab-specific information about fabrication equipment. 

**For official specs, SOPs, and training**: See [NFCF Facilities Page](https://www.nano.pitt.edu/facilities)  
**For equipment booking**: Use [FOM](https://fom.nano.pitt.edu/fom/)

## Purpose of This Directory

The NFCF maintains comprehensive documentation and SOPs for all equipment. **We don't duplicate that information here.**

Instead, this directory tracks:
- **Tooling factors and calibrations** specific to your processes
- **Material batches** and when they were loaded/replaced
- **Performance quirks** you've discovered through use
- **Links to device runs** that used each instrument
- **Tips and tricks** from your experience

## Organization

```
instruments/
├── ebeam-evaporators/
│   ├── thermionics-ebeam-sb60a.md
│   ├── plassys-ebeam-cleanroom.md
│   └── ...
├── lithography/
│   ├── raith-eline.md
│   ├── quintel-q4000.md
│   └── ...
└── [other-categories]/
```

## Complete Instrument List

### Metal Deposition

#### E-beam Evaporation
- [Thermionics E-beam Evaporator](ebeam-evaporators/thermionics-ebeam-sb60a.md) - SB60A (no cleanroom)
  - [NFCF Page](https://www.nano.pitt.edu/eBeamTherm)
- [Plassys E-beam System](ebeam-evaporators/plassys-ebeam-cleanroom.md) - Cleanroom
  - [NFCF Page](https://www.nano.pitt.edu/Plassys)

#### Thermal Evaporation
- [Angstrom COVAP Thermal Evaporator](thermal-evaporators/angstrom-thermal-cleanroom.md) - Cleanroom
  - [NFCF Page](https://www.nano.pitt.edu/AngstThermal)

#### Sputtering
- [Angstrom Sputtering System](sputtering/angstrom-sputter-cleanroom.md) - Cleanroom
  - [NFCF Page](https://www.nano.pitt.edu/angstromsputter)

### Dielectric Deposition

#### CVD/PECVD
- [Plasma Enhanced CVD (PECVD)](cvd-ald/pecvd-cleanroom.md) - Cleanroom
  - [NFCF Page](https://www.nano.pitt.edu/PECVD)

#### Atomic Layer Deposition
- [Plasma Enhanced ALD (PE-ALD)](cvd-ald/peald-cleanroom.md) - Cleanroom
  - [NFCF Page](https://www.nano.pitt.edu/ald)
- [Anric AT410 Thermal ALD](cvd-ald/anric-ald-cleanroom.md) - Cleanroom
  - [NFCF Page](https://www.nano.pitt.edu/AnricALD)

#### Parylene
- [Parylene Deposition Coater PDS 2010](cvd-ald/parylene-coater-sb60a.md) - SB60A (no cleanroom)
  - [NFCF Page](https://www.nano.pitt.edu/Parylene)

### Lithography

#### Electron Beam Lithography
- [Raith EBPG5150 (100kV)](lithography/raith-ebpg5150.md) - Cleanroom
  - [NFCF Page](https://www.nano.pitt.edu/EBPG)
- [Raith e-LiNE](lithography/raith-eline.md) - Cleanroom
  - [NFCF Page](https://www.nano.pitt.edu/RaithEBL)

#### Photolithography
- [Quintel Q4000 Mask Aligner](lithography/quintel-q4000.md) - Cleanroom
  - [NFCF Page](https://www.nano.pitt.edu/QuintelMaskAligner)
- [Heidelberg MLA150](lithography/heidelberg-mla150.md) - Cleanroom
  - [NFCF Page](https://www.nano.pitt.edu/MLA150)
- [Heidelberg MLA100](lithography/heidelberg-mla100.md) - Cleanroom
  - [NFCF Page](https://www.nano.pitt.edu/MLA100)

#### 3D Lithography
- [Nanoscribe 3D Lithography](lithography/nanoscribe-cleanroom.md) - Cleanroom
  - [NFCF Page](https://www.nano.pitt.edu/Nanoscribe)

#### Surface Treatment
- [YES HMDS Oven](lithography/yes-hmds-cleanroom.md) - Cleanroom
  - [NFCF Page](https://www.nano.pitt.edu/yesoven)

### Etching

#### Dry Etching
- [Trion Reactive Ion Etcher (RIE)](etching/trion-rie-cleanroom.md) - Cleanroom
  - [NFCF Page](https://www.nano.pitt.edu/RIE)
- [APEX ICP-RIE Chlorine](etching/apex-icprie-cl-cleanroom.md) - Cleanroom
  - [NFCF Page](https://www.nano.pitt.edu/facilities/ICP-RIE-Cl)
- [APEX ICP-RIE Fluorine](etching/apex-icprie-f-cleanroom.md) - Cleanroom
  - [NFCF Page](https://www.nano.pitt.edu/facilities/ICP-RIE-F)

#### Plasma Cleaning
- [March 500 Plasma Asher](etching/march-asher-cleanroom.md) - Cleanroom
  - [NFCF Page](https://www.nano.pitt.edu/plasmaasher)

### Thermal Processing

- [Rapid Thermal Annealer (Solaris 100)](thermal-processing/rta-solaris-cleanroom.md) - Cleanroom
  - [NFCF Page](https://www.nano.pitt.edu/rta)
- [Oxidation/Annealing Tube Furnace](thermal-processing/tube-furnace-cleanroom.md) - Cleanroom
  - [NFCF Page](https://www.nano.pitt.edu/facilities/OxFurnace)

### Characterization

#### Electron Microscopy
- [FEI Scios Dual Beam (FIB/SEM)](characterization/fei-scios-dualbeam-sb06.md) - SB06 Lab
  - [NFCF Page](https://www.nano.pitt.edu/DualBeam)
- [Zeiss Gemini FE-SEM 360](characterization/zeiss-gemini-sem-cleanroom.md) - Cleanroom
  - [NFCF Page](https://www.nano.pitt.edu/InspSEM)

#### Thin Film Metrology
- [Bruker DektakXT Profiler](characterization/dektak-profiler-cleanroom.md) - Cleanroom
  - [NFCF Page](https://www.nano.pitt.edu/DektakProfiler)
- [Filmetrics F40 Thin Film Analyzer](characterization/filmetrics-f40-cleanroom.md) - Cleanroom
  - [NFCF Page](https://www.nano.pitt.edu/F40)

### Other

- [ADT 7122 Wafer Dicer](other/adt-dicer-sb02a.md) - SB02A (no cleanroom)
  - [NFCF Page](https://www.nano.pitt.edu/dicer)

## Quick Reference: NFCF Equipment

### Metal Deposition
- [Thermionics E-beam Evaporator](https://www.nano.pitt.edu/eBeamTherm) - SB60A (no cleanroom)
- [Plassys E-beam](https://www.nano.pitt.edu/Plassys) - Cleanroom
- [Angstrom Thermal Evaporator](https://www.nano.pitt.edu/AngstThermal) - Cleanroom
- [Angstrom Sputtering System](https://www.nano.pitt.edu/angstromsputter) - Cleanroom

### Lithography
- [Raith e-LiNE EBL](https://www.nano.pitt.edu/RaithEBL) - Cleanroom
- [Raith EBPG5150 EBL](https://www.nano.pitt.edu/EBPG) - Cleanroom
- [Heidelberg MLA150](https://www.nano.pitt.edu/MLA150) - Cleanroom
- [Heidelberg MLA100](https://www.nano.pitt.edu/MLA100) - Cleanroom
- [Quintel Q4000 Mask Aligner](https://www.nano.pitt.edu/QuintelMaskAligner) - Cleanroom

### Etching
- [Trion RIE](https://www.nano.pitt.edu/RIE) - Cleanroom
- [APEX ICP-RIE (Cl)](https://www.nano.pitt.edu/facilities/ICP-RIE-Cl) - Cleanroom
- [APEX ICP-RIE (F)](https://www.nano.pitt.edu/facilities/ICP-RIE-F) - Cleanroom

### Characterization (Cleanroom)
- [Zeiss Gemini FE-SEM 360](https://www.nano.pitt.edu/InspSEM)
- [Filmetrics F40](https://www.nano.pitt.edu/F40)
- [Bruker DektakXT Profiler](https://www.nano.pitt.edu/DektakProfiler)
- [Keyence VK-X3000 3D Profiler](https://www.nano.pitt.edu/VK_X3000)

### Characterization (SB06 Lab)
- [FEI Scios Dual Beam FIB/SEM](https://www.nano.pitt.edu/DualBeam)
- [Dimension Icon AFM](https://www.nano.pitt.edu/SPM_AFM)
- [LabRAM Soleil Raman](https://www.nano.pitt.edu/Raman)
- [Multiple SEMs, TEMs, XRD, etc.](https://www.nano.pitt.edu/facilities)

## How to Use This Directory

### When fabricating a device:

1. **Reference the instrument** in your device run README:
   ```markdown
   **Instruments used:**
   - E-beam evaporator: [Thermionics SB60A](../../instruments/ebeam-evaporators/thermionics-ebeam-sb60a.md)
   ```

2. **After deposition/processing**, update the instrument file with:
   - Tooling factors (if you measured actual thickness)
   - Any issues encountered
   - Material batch information
   - Add a link to your device run

3. **Over time**, the instrument files build up institutional knowledge about what works and what doesn't

### Creating a new instrument file:

1. Use an existing file as a template
2. Fill in the NFCF link and basic info
3. Leave most sections empty - they'll fill in as people use the tool
4. Track only what's relevant to your group's use

## Tips

- **Don't duplicate NFCF docs** - just link to them
- **Do track variations** between nominally identical processes
- **Do record calibrations** you've measured
- **Do share tricks** that helped you succeed
- **Link liberally** between instruments, materials, and device runs
