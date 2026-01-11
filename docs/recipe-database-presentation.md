---
marp: true
theme: default
paginate: true
header: 2D Materials Device Fabrication Recipe Database
footer: Levy Lab - University of Pittsburgh
---

<!-- _class: lead -->

# Device Fabrication Recipe Database

**A Version-Controlled System for Reproducible Device Fabrication**

Levy Lab, University of Pittsburgh

---

## The Problem

**Traditional lab notebooks:**
- Hard to search and compare
- Locked in one person's notebook
- Photos scattered across phones/computers
- "How did I make that device 6 months ago?"
- "Which e-beam did Sarah use for her best contacts?"

**Result:** Knowledge is lost, mistakes are repeated, reproducibility is difficult.

---

## Our Solution: Git + GitHub

**A recipe database that is:**
- **Shared** - Everyone sees what worked (and what didn't)
- **Searchable** - Find similar devices instantly
- **Versioned** - Track changes over time
- **Linked** - Connect recipes → devices → instruments → results
- **Permanent** - Recipes get DOIs for citations

Think: **Wikipedia for your lab's fabrication processes**

---

## Repository Organization

```
recipes/                    # General processes (Ti/Au on SiO2)
devices/                    # Specific instances (your actual devices)
  ├── templates/            # Successful patterns to reuse
  ├── 2025-01-10-device/    # Full documentation
  └── 2025-01-11-variant.md # Diff from template
instruments/                # Tool-specific metadata
materials/                  # Batch tracking
```

**Four directories, connected by links**

---

## The Three-Level System

```
┌─────────────────────────────────────┐
│ 1. Base Recipes (Most General)     │
│    recipes/ti-au-standard.md        │
│    • Complete process               │
│    • 300 lines                      │
└─────────────────────────────────────┘
                ↓
┌─────────────────────────────────────┐
│ 2. Template Device (First Success)  │
│    devices/2025-01-10-albn-ti-au/   │
│    • Substrate-specific             │
│    • 150 lines                      │
└─────────────────────────────────────┘
                ↓
┌─────────────────────────────────────┐
│ 3. Variant Devices (Just the Diff) │
│    devices/2025-01-11-cr-au.md      │
│    • Only what's different          │
│    • 20 lines                       │
└─────────────────────────────────────┘
```

---

## Level 1: Base Recipes

**General processes for standard substrates**

`recipes/graphene-contacts/ti-au-standard.md`

- Complete step-by-step instructions
- Process flow diagrams (Mermaid)
- Expected results and troubleshooting
- Version controlled, gets DOI
- Used across many substrate types

**Example:** Ti/Au contacts on Si/SiO2

---

## Level 2: Template Devices

**First successful adaptation to new substrate**

`devices/2025-01-10-graphene-albn-ti-au/`

After your first AlBN device works:
- Full documentation of what's different
- Validated process parameters
- Typical results and known issues
- Becomes reference for future AlBN devices

**Register in:** `devices/templates/TEMPLATES.md`

---

## Level 3: Variant Devices

**Just document the differences**

`devices/2025-01-11-graphene-albn-cr-au.md`

```markdown
# Device: 2025-01-11 Graphene/AlBN Cr/Au

**Template**: 2025-01-10-graphene-albn-ti-au

## Diff from Template
- Metal: Cr/Au (5/60nm) instead of Ti/Au (5/30nm)

## Results
- Rc: 800 Ω·μm (vs 1200 for Ti/Au)
```

**That's it.** Single file, ~20 lines.

---

## Efficiency Gains

**Without templates:**
- 10 device variants = 10 × 150 lines = **1,500 lines**
- Lots of repetition
- Hard to see what actually changed

**With templates:**
- 1 template (150 lines) + 10 diffs (20 lines each) = **350 lines**
- No repetition
- Clear what changed between devices

**→ 77% reduction in documentation overhead**

---

## User Workflow: First Time

**Scenario:** First device on AlBN substrate

1. **Find base recipe:** `recipes/ti-au-standard.md`
2. **Create device folder:** `devices/2025-01-10-graphene-albn-ti-au/`
3. **Document everything:**
   - AlBN-specific adaptations
   - Process notes as you go
   - Images and data
4. **It works!**

**Effort:** Full documentation (~2 hours to set up)

---

## User Workflow: Create Template

**After success:**

Add entry to `devices/templates/TEMPLATES.md`:

```markdown
### Graphene Contacts on AlBN
- **Reference device**: 2025-01-10-graphene-albn-ti-au
- **Use for**: Any contacts on graphene/AlBN
- **Key adaptations**: HMDS prime, optical contrast
```

**That's it** - just a pointer, no duplication.

**Effort:** 5 minutes

---

## User Workflow: Use Template

**Scenario:** Try Cr/Au instead of Ti/Au on AlBN

**Talk to Claude:**
> "New device like 2025-01-10 but with Cr/Au and 60nm Au"

**Claude generates:**
- Single markdown file
- Points to template
- Documents only the diff
- Ready to commit

**Effort:** 5 minutes

---

## The Conversation Approach

**Three ways to create devices:**

1. **Manual** - Create folders and files yourself
2. **Template-based** - Use minimal diff format
3. **Conversation with Claude** - Describe what you want

**All three work.** Choose what fits your workflow.

---

## Example Conversation

**You:**
> "Making graphene device on AlBN, Cr/Au contacts, 60nm Au instead of 30nm. Related to yesterday's device."

**Claude:**
> "Got it! Creating diff-based device file... Which instruments will you use?"

**You:**
> "Same as yesterday - Thermionics e-beam, Quintel aligner"

**Claude:**
> "Here's your device file ready to commit..."

[Outputs complete markdown file]

---

## Linking Everything Together

Every device links to:

- **Base recipe** it's based on
- **Template device** (if using one)
- **Related devices** for comparison
- **Instruments used** (specific tools)
- **Material batches** (resist lot numbers, metal pellets)

**Result:** Traceable web of information

---

## Why Link to Instruments?

**Nominally "identical" recipes give different results because:**
- Different deposition tools (base pressure, calibration)
- Age of photoresist bottle
- When metal pellets were last replaced
- Tool-specific quirks

**By tracking:** Identify patterns, improve reproducibility

---

## Instrument Tracking

**We don't duplicate NFCF documentation!**

Link to official pages: https://www.nano.pitt.edu/facilities

**We add only lab-specific metadata:**
- Tooling factors (measured vs nominal thickness)
- Material batches currently loaded
- Performance quirks we've discovered
- Tips and tricks from experience

---

## Example: E-beam Evaporator

`instruments/ebeam-evaporators/thermionics-ebeam-sb60a.md`

**Tracks:**
- Tooling factors by date and material
- Ti/Au pellet lot numbers
- Base pressure trends
- Rate stability notes
- Links to all devices that used it

**Updated after each use** (~2 minutes)

---

## Material Batch Tracking

`materials/photoresists/s1813-tracker.md`

**Tracks:**
- When bottles were opened
- Batch/lot numbers
- Performance notes
- When exhausted

**Why?** Identify when problems are due to aged materials vs process variations

---

## Benefits: Reproducibility

**Before:**
> "My contacts have 2× higher resistance than Sarah's. Why?"

**After:**
Search shows:
- Sarah used Thermionics e-beam, you used Plassys
- Sarah's S1813 was 1 month old, yours is 4 months old
- Sarah used lot #12345 Ti pellets, you used lot #67890

**Actionable insights.**

---

## Benefits: Knowledge Transfer

**New student joins:**
- Browse `devices/` to see what's been made
- Check `templates/` for validated processes
- Read instrument files for tool quirks
- See typical results and common issues

**No need to ask:** "How do we make contacts on AlBN?"
**Just look:** `templates/TEMPLATES.md`

---

## Benefits: Comparison

**Easy to compare:**
- Ti/Au vs Cr/Au on same substrate
- Same process on different substrates
- Same device over time (batch effects)
- Different people making "same" device

**All linked and searchable.**

---

## Benefits: Publication

**When publishing:**

1. **Cite base recipe** (has DOI from Zenodo)
2. **Link to specific device run** (GitHub URL or DOI)
3. **Reviewers can see** exact process details
4. **Others can reproduce** your work

**Increases credibility and citations**

---

## Benefits: Collaboration

**Repository is public:**
- Collaborators see your methods
- Others can learn from your processes
- Cite your recipes in their papers
- Contribute improvements back

**Private version:** Same benefits within your lab

---

## Real-World Example

```
Jan 10: First AlBN device (Ti/Au)
        → Full doc, 150 lines
        → Works! Rc = 1200 Ω·μm
        → Add to templates

Jan 11: Try Cr/Au variant
        → Diff file, 20 lines
        → Works! Rc = 800 Ω·μm

Jan 15: Try Pd/Au variant  
        → Diff file, 20 lines
        → Result: Rc = 650 Ω·μm

Jan 20: Try 100nm Au
        → Diff file, 20 lines
        → Result: Rc = 700 Ω·μm
```

**4 variants in 4 days, minimal overhead**

---

## Getting Started

1. **Clone the repository**
2. **Read the README** (comprehensive guide)
3. **Look at example devices** (see what others did)
4. **Make your first device:**
   - Use existing recipe
   - Document what's different
   - Add your results
5. **Update instrument files** after using tools

**That's it.**

---

## Three Paths Forward

**Choose your style:**

### Path 1: Full Documentation
- New substrate/device type
- Create complete folders
- Document everything

### Path 2: Template-Based
- Similar to existing device
- Single diff file
- Minimal overhead

### Path 3: Conversation
- Talk to Claude
- Auto-generate files
- Commit and go

---

## Key Principles

1. **Don't repeat yourself** - Use templates and links
2. **Document as you go** - Easier than remembering later
3. **Link everything** - Create traceable web
4. **Only record what's different** - Diff from templates
5. **Update instruments** - Help future you and others

---

## Documentation Overhead

**First device on new substrate:**
- 2 hours to document fully
- Creates reusable template

**Subsequent variants:**
- 5 minutes to create diff file
- Or chat with Claude

**After 10 devices:** 
- Time saved: ~18 hours vs traditional notebooks
- Quality: Much better organized and searchable

---

## Success Metrics

**You'll know it's working when:**

- New students can onboard faster
- You find old device info in seconds
- You understand why results vary
- Collaborators cite your methods
- You use it consistently (low overhead)

---

## Common Questions

**Q: Isn't this a lot of work?**
A: First time yes, but templates make it faster afterward.

**Q: What if I'm not good with Git?**
A: GitHub Desktop makes it point-and-click.

**Q: Do I need to document failed attempts?**
A: Optional, but noting what didn't work can help others.

**Q: Can I use this for other projects?**
A: Yes. The system works for any experimental lab.

---

## Repository Structure (Visual)

```
recipes/
├── Base recipes (Ti/Au standard, etc)
devices/
├── templates/TEMPLATES.md ← Registry of successful patterns
├── 2025-01-10-full-doc/ ← Can become template
└── 2025-01-11-diff.md ← Points to template
instruments/
├── ebeam-evaporators/thermionics-sb60a.md
└── lithography/quintel-q4000.md
materials/
└── photoresists/s1813-tracker.md
```

---

## Live Demo Structure

**Example device:**
https://github.com/levylabpitt/recipes/tree/main/devices/2025-01-10-graphene-albn-ti-au

**Shows:**
- Quick summary (what's different)
- Process notes
- Results
- Links to instruments and materials
- Images and data

---

## The Big Picture

**Traditional approach:**
- Information scattered
- Hard to compare
- Knowledge lost
- Low reproducibility

**Our approach:**
- Centralized and linked
- Easy to compare
- Knowledge preserved
- High reproducibility

**Same effort, much better outcomes**

---

## Implementation Tips

**Start small:**
1. One device run to learn the system
2. Add instruments as you use them
3. Create templates after success
4. Get team buy-in gradually

**Don't:**
- Try to backfill everything at once
- Make it too complicated
- Force rigid structure
- Forget to commit regularly

---

## Future Enhancements

**Possible additions:**
- Automated tooling factor tracking
- Integration with measurement software
- Auto-generated comparison plots
- Machine learning on successful parameters
- Lab equipment calendar integration

**It's a living system.**

---

## Getting Help

**Resources:**
- Repository README (comprehensive)
- Templates directory (examples)
- Existing device runs (patterns)
- Ask Claude (conversation-based)
- Team members (share knowledge)

**Questions?** Open a GitHub issue or ask in lab meeting

---

<!-- _class: lead -->

## Summary

**Recipe Database = Lab Notebook + Version Control + Linking**

- Organized, searchable, permanent
- Everything connected
- Templates minimize overhead
- Knowledge shared across team
- Better science through reproducibility

**Repository:** https://github.com/levylabpitt/recipes

---

<!-- _class: lead -->

# Questions?

**Contact:** Jeremy Levy, University of Pittsburgh

**Repository:** https://github.com/levylabpitt/recipes

**Get started:** Clone it and make your first device.
