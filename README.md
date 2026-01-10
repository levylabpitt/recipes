# 2D Materials Device Fabrication Recipes

A version-controlled library of device fabrication recipes for 2D materials research, with DOI-able process flows.

## Purpose

This repository maintains standardized fabrication recipes for:
- Electrical contacts to 2D materials
- Encapsulation methods
- Transfer techniques
- Device patterning procedures

Each recipe is version-controlled and can be assigned a permanent DOI via Zenodo for citation in publications.

## Repository Structure

```
recipes/
├── recipes/
│   ├── graphene-contacts/
│   │   ├── ti-au-standard.md
│   │   └── README.md
│   ├── hBN-encapsulation/
│   │   └── README.md
│   └── ...
├── metadata/
│   └── recipe-index.yaml
└── CITATION.cff
```

## How to Use

1. **Browse recipes**: Navigate to `recipes/[category]/` directories
2. **View process flows**: Each recipe contains a Mermaid flowchart (renders automatically on GitHub)
3. **Cite a recipe**: Use the DOI from the recipe metadata (assigned via Zenodo releases)

## Contributing

This is a private repository for team use. Team members:
1. Create new recipes in appropriate category directories
2. Follow the template format (see existing recipes)
3. Update `metadata/recipe-index.yaml` with new entries
4. Create a git tag when recipe is ready for DOI assignment

## Creating a DOI for a Recipe

1. Finalize the recipe
2. Tag it: `git tag [recipe-id]-v[version]`
3. Push tag: `git push --tags`
4. Create a GitHub release from the tag
5. Zenodo automatically generates a DOI
6. Update recipe metadata with DOI

## License

[Specify license - e.g., CC-BY-4.0 for methods]

## Contact

Jeremy Levy, University of Pittsburgh
