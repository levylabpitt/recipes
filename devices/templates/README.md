# Templates Directory

This directory contains a **registry of successful device runs** that serve as templates for future work.

## The Key File

**[TEMPLATES.md](TEMPLATES.md)** - The template library

This file lists successful device runs that can be used as templates, with:
- Pointers to the actual device runs (no duplication!)
- Key adaptations from base recipes
- Which devices reference each template

## How It Works

### No Duplication
Templates are just **pointers** to successful device runs, not copies. The actual documentation lives in the device run folder.

### Example Flow

1. **You make a device**: `devices/2025-01-10-graphene-albn-ti-au/` (full doc)
2. **It works!**
3. **Add to template library**: Add entry in `TEMPLATES.md` pointing to it
4. **Future device**: "Like 2025-01-10 but with Cr/Au"
5. **Claude generates**: 20-line diff file that references the template

### What Gets Added to TEMPLATES.md

```markdown
### Graphene Contacts on AlBN
- **Reference device**: [2025-01-10-graphene-albn-ti-au](../2025-01-10-graphene-albn-ti-au/)
- **Use for**: Any contacts on graphene/AlBN
- **Key adaptations**: HMDS prime, optical contrast adjustment
- **Devices using this**: [list of diff-based devices]
```

That's it - just metadata and pointers.

## Files

- **TEMPLATES.md** - The registry (start here!)
- **HIERARCHY-EXPLAINED.md** - Visual guide to the three-level system
- **README.md** - This file

## See Also

- [Main devices directory](../README.md)
- [Base recipes](../../recipes/)
