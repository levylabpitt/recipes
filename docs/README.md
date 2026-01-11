# Recipe Database Presentation

This directory contains presentations about the recipe database system.

## Files

- **recipe-database-presentation.md** - Marp presentation explaining the entire system

## Viewing the Presentation

### Option 1: Marp CLI (Recommended)

Install Marp CLI:
```bash
npm install -g @marp-team/marp-cli
```

Generate HTML:
```bash
marp recipe-database-presentation.md -o presentation.html
```

Or generate PDF:
```bash
marp recipe-database-presentation.md -o presentation.pdf
```

### Option 2: VS Code Extension

1. Install the [Marp for VS Code extension](https://marketplace.visualstudio.com/items?itemName=marp-team.marp-vscode)
2. Open `recipe-database-presentation.md` in VS Code
3. Click the Marp icon to preview
4. Export to HTML or PDF

### Option 3: Online Viewer

1. Copy the markdown content
2. Paste into [Marp Web](https://web.marp.app/)
3. Present or export

## Presentation Content

**Covers:**
- The problem with traditional lab notebooks
- How the recipe database solves it
- The three-level abstraction system
- User workflows (manual, template, conversation)
- Benefits (reproducibility, knowledge transfer, comparison)
- Getting started guide

**Slides:** 35 slides, ~25 minute presentation

## Customization

Edit the header and footer in the YAML frontmatter:
```yaml
header: 'Your Header Text'
footer: 'Your Footer Text'
```

Change theme:
```yaml
theme: default  # or: gaia, uncover
```

## Tips for Presenting

- Use presenter mode (press `P` in browser)
- Navigate with arrow keys or spacebar
- Press `F` for fullscreen
- Press `Esc` to exit fullscreen
