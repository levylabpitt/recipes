# Device Documentation Hierarchy

## Three Levels of Abstraction

```
┌─────────────────────────────────────────────────────────┐
│ Level 1: BASE RECIPES (Most General)                   │
│ recipes/graphene-contacts/ti-au-standard.md            │
│                                                         │
│ • Complete process for standard substrate (Si/SiO2)    │
│ • Version controlled, gets DOI                         │
│ • Hundreds of lines, comprehensive                     │
│ • Used across many substrate types                     │
└─────────────────────────────────────────────────────────┘
                        ↓
┌─────────────────────────────────────────────────────────┐
│ Level 2: DEVICE TEMPLATES (Substrate/Context Specific) │
│ devices/templates/graphene-albn-contacts.md            │
│                                                         │
│ • Adapted for specific substrate (AlBN)                │
│ • Captures what's different from base recipe           │
│ • Validated by first successful run                    │
│ • ~100 lines, focused on substrate-specific details    │
│ • Reused for all AlBN contact devices                  │
└─────────────────────────────────────────────────────────┘
                        ↓
┌─────────────────────────────────────────────────────────┐
│ Level 3: DEVICE RUNS (Just the Diff)                   │
│ devices/2025-01-11-graphene-albn-cr-au.md              │
│                                                         │
│ • Only what's different from template                  │
│ • Metal stack change, parameter variations             │
│ • Process deviations that occurred                     │
│ • Results and comparisons                              │
│ • ~20 lines, ultra minimal                             │
└─────────────────────────────────────────────────────────┘
```

## How Information Flows

### Creating First Device on New Substrate
```
You → Full documentation (100+ lines)
     → devices/2025-01-10-graphene-albn-ti-au/README.md
     → Everything documented because it's new
```

### After Success: Create Template
```
You → Extract pattern from successful run
     → devices/templates/graphene-albn-contacts.md
     → "Here's what works for AlBN contacts"
```

### Subsequent Devices: Diff Only
```
You → "Cr/Au instead of Ti/Au, 60nm Au"
Claude → Generates 20-line diff file
You → Commit, done
```

## The Conversation Flow

### Scenario 1: New Substrate (Full Doc)
**You**: "First time making contacts on AlBN, using Ti/Au standard recipe"

**Claude**: "Since this is your first AlBN device, I'll create full documentation. You can turn this into a template after it works."
→ Creates comprehensive device run

### Scenario 2: Create Template
**You**: "Yesterday's AlBN device worked great. Make it a template."

**Claude**: "I'll extract the AlBN-specific details from your device run into a reusable template."
→ Creates `templates/graphene-albn-contacts.md`

### Scenario 3: Use Template (Minimal)
**You**: "New device using AlBN template, but Cr/Au with 60nm Au"

**Claude**: "Just the diff then! What's different and what happened?"
→ Creates 20-line diff-based device file

## Benefits

### For First Device on New Substrate:
- ✅ Full documentation captures everything
- ✅ Becomes reference for future work
- ✅ Can be promoted to template when validated

### For Template:
- ✅ Captures substrate/context-specific knowledge
- ✅ One place to update when process improves
- ✅ New students can reference this
- ✅ Shows typical results and issues

### For Routine Variations:
- ✅ Minimal overhead (~5 minutes)
- ✅ Only record what matters (the diff)
- ✅ Easy comparison across variants
- ✅ Still linked to full context

## Real-World Usage

```
Jan 10: Make first AlBN device
        → Full doc (100 lines)
        → Works! Rc = 1200 Ω·μm

Jan 10: Extract to template
        → Templates/graphene-albn-contacts.md
        → Documents AlBN-specific process

Jan 11: Try Cr/Au variant
        → Diff file (20 lines): "Cr/Au 5/60"
        → Works! Rc = 800 Ω·μm

Jan 15: Try Pd/Au variant  
        → Diff file (20 lines): "Pd/Au 5/40"
        → Result: Rc = 650 Ω·μm

Jan 20: Try 100nm Au
        → Diff file (20 lines): "Ti/Au 5/100"
        → Result: Rc = 700 Ω·μm
```

**Four variants documented in ~100 total lines instead of 400+**

## File Sizes in Practice

- **Base recipe**: 300 lines (comprehensive, reusable)
- **First device**: 150 lines (full documentation)
- **Template**: 100 lines (extracted pattern)
- **Variant devices**: 20 lines each (diff only)

**10 device variants** = 1 template (100) + 10 diffs (200) = **300 lines total**

**Without templates** = 10 × 150 = **1500 lines** with tons of repetition

## The Key Insight

**Don't repeat yourself across devices that share a context.**

- Different substrates → Different templates
- Different device types → Different templates  
- Same substrate, different metals → Use template, just diff
- Same everything, different batch → Ultra-minimal diff

You're capturing **variation**, not **repetition**.
