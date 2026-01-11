# Device Templates Library

## What This Is

A **registry** of successful device runs that serve as templates for future work. These are pointers to actual device runs, not copies.

## Active Templates

### Graphene Contacts on AlBN
- **Reference device**: [2025-01-10-graphene-albn-ti-au](../2025-01-10-graphene-albn-ti-au/)
- **Use for**: Any contacts on graphene/AlBN substrate
- **Key adaptations from base recipe**:
  - HMDS prime required (150°C, 5min)
  - Optical contrast different - adjust filters
  - Standard liftoff: 1hr at 50°C
- **Typical Rc**: 500-2000 Ω·μm depending on metal stack
- **Devices using this template**:
  - [2025-01-11-graphene-albn-cr-au](../2025-01-11-graphene-albn-cr-au-minimal.md) - Cr/Au variant

### [Add More Templates As They're Validated]

---

## How to Use This

### When making a new device similar to an existing one:

**You tell Claude:**
> "New device like 2025-01-10-graphene-albn-ti-au but with Cr/Au 60nm"

**Claude:**
1. Looks at the reference device
2. Generates a minimal diff file
3. Points back to the reference device

**Result:** 20-line file instead of 150

### When to add a template here:

After a device run succeeds and you think "I'll probably make more like this":
1. Add entry to this file
2. Point to the successful device
3. Note key adaptations
4. List future devices that use it

**Don't copy anything** - just point and annotate.

---

## Template Entry Format

```markdown
### [Device Type Name]
- **Reference device**: [link to actual device run]
- **Use for**: [when to use this as template]
- **Key adaptations from base recipe**: 
  - [bullet points of important differences]
- **Typical results**: [expected performance]
- **Devices using this template**:
  - [links to devices that reference this]
```

---

## See Also

- [HIERARCHY-EXPLAINED.md](HIERARCHY-EXPLAINED.md) - How the three-level system works
