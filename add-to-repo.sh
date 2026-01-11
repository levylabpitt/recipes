#!/bin/bash

# Script to add the presentation and all new files to the repository

cd "C:\Users\jerem\github\recipes"

echo "Adding new files to git..."

# Add the presentation files
git add docs/

# Add the templates directory
git add devices/templates/

# Add the simplified device examples
git add devices/2025-01-11-graphene-albn-cr-au-simple.md
git add devices/2025-01-11-graphene-albn-cr-au-minimal.md

# Check status
echo ""
echo "Files staged for commit:"
git status

echo ""
echo "Ready to commit! Run:"
echo "git commit -m 'Add Marp presentation, template system, and device examples'"
echo "git push"
