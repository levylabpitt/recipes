# Device Templates Registry

## What This Is

A **simple list** of successful device runs that can be used as templates. Just pointers - the actual documentation lives in the device folders.

## How to Use

When you make a device similar to an existing one, just reference it:

```markdown
**Template**: [2025-01-10-graphene-albn-ti-au](../2025-01-10-graphene-albn-ti-au/)
```

Then document only what's different.

## Current Templates

### Graphene Contacts on AlBN
- **Device**: [2025-01-10-graphene-albn-ti-au](../2025-01-10-graphene-albn-ti-au/)
- **Good for**: Any contacts on graphene/AlBN substrate
- **Key details**: HMDS prime required, different optical contrast than SiO2
- **Variants**:
  - [2025-01-11-graphene-albn-cr-au](../2025-01-11-graphene-albn-cr-au-minimal.md) - Cr/Au instead of Ti/Au

---

## Adding to This Registry

After a successful device on a **new substrate or device type**, add it here:

```markdown
### [Device Type Name]
- **Device**: [link to device folder]
- **Good for**: [when to use this as template]
- **Key details**: [important adaptations]
- **Variants**: [links as they're made]
```

That's it - just metadata, no duplication.
