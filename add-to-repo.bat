@echo off
REM Script to add the presentation and all new files to the repository

cd C:\Users\jerem\github\recipes

echo Adding new files to git...

REM Add the presentation files
git add docs/

REM Add the templates directory
git add devices/templates/

REM Add the simplified device examples
git add devices/2025-01-11-graphene-albn-cr-au-simple.md
git add devices/2025-01-11-graphene-albn-cr-au-minimal.md

REM Check status
echo.
echo Files staged for commit:
git status

echo.
echo Ready to commit! Run:
echo git commit -m "Add Marp presentation, template system, and device examples"
echo git push

pause
