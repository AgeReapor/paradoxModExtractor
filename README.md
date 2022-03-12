# paradoxModExtractor
Helper app I made to extract and tweak paradox mod zips manually

Helper app I made to extract and tweak paradox mod zips manually

Iteratively does the following for every .zip in the working directory:

1. Extract to /Processed/
2. Gets mod name from descriptor.mod
3. Replace descriptor.mod file name and mod folder name with mod name
4. Adds path to the mod folder in the renamed .mod file
5. Moves the .mod out to /Processed/
