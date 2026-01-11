---
instrument_id: thermionics-ebeam-sb60a
instrument_type: electron_beam_evaporator
nfcf_link: https://www.nano.pitt.edu/eBeamTherm
location: Benedum Hall SB60A
---

# Thermionics Electron Beam Evaporator (SB60A)

**Official NFCF Page**: [Thermionics EBE](https://www.nano.pitt.edu/eBeamTherm)  
**Location**: Benedum Hall, Room SB60A (does not require cleanroom access)  
**FOM Equipment Page**: [Login to view schedule/book time](https://fom.nano.pitt.edu/fom/)

*For system specifications, training requirements, and SOPs, see the official NFCF page above.*

## Lab-Specific Notes

### Known Quirks and Calibrations

#### Tooling Factor History
Track how the quartz crystal monitor compares to actual deposited thickness:

| Date | Material | Nominal (QCM) | Measured | Tooling Factor | Method | User |
|------|----------|---------------|----------|----------------|--------|------|
| 2024-12-15 | Ti | 5 nm | 6.2 nm | 124% | Profilometer | JDoe |
| 2024-11-20 | Au | 50 nm | 48 nm | 96% | XRR | JSmith |

*Tooling factor = (Measured / Nominal) × 100%*

#### Source Status

| Source | Material | Purity | Last Refilled | Approximate Remaining | Notes |
|--------|----------|--------|---------------|----------------------|-------|
| 1 | Ti | 99.995% | 2024-12-01 | 75% | - |
| 2 | Au | 99.99% | 2024-11-15 | 50% | - |
| 3 | Cr | 99.95% | 2024-10-01 | 80% | - |
| 4 | - | - | - | Empty | - |

#### Performance Notes
- Ti deposition: Rate tends to spike in first 20-30s, wait for stabilization
- Au deposition: Very stable between 1-2 Å/s
- Base pressure typically 3-5×10⁻⁷ Torr
- [Add your observations here]

### Recent Issues/Maintenance

| Date | Issue/Maintenance | Resolution | Impact | Reported By |
|------|-------------------|------------|--------|-------------|
| 2024-11-15 | High base pressure | Pump service by NFCF | 3 days downtime | JSmith |
| 2024-10-01 | QCM erratic readings | Crystal replaced | - | JDoe |

*For official maintenance records, contact NFCF staff*

## Material Batches Used

### Ti Pellets
| Batch/Lot | Vendor | Purity | Date Opened | Date Exhausted | Notes |
|-----------|--------|--------|-------------|----------------|-------|
| Lesker #12345 | Kurt J. Lesker | 99.995% | 2024-12-01 | - | Current |
| Lesker #11234 | Kurt J. Lesker | 99.995% | 2024-08-15 | 2024-11-30 | Gave consistent results |

### Au Pellets
| Batch/Lot | Vendor | Purity | Date Opened | Date Exhausted | Notes |
|-----------|--------|--------|-------------|----------------|-------|
| Lesker #67890 | Kurt J. Lesker | 99.99% | 2024-11-15 | - | Current |

## Device Runs Using This Instrument

*Add links to device runs as they're completed*

- [2025-01-10-graphene-albn-ti-au](../../devices/2025-01-10-graphene-albn-ti-au/) - Ti/Au deposition
- 

## Tips and Tricks

*Share your experience and institutional knowledge here*

- For Ti/Au contacts on graphene: 0.5 Å/s Ti, 1.5 Å/s Au works well
- Always wait for rate stabilization before opening shutter
- [Your tips here]
