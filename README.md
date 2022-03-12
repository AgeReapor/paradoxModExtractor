# paradoxModExtractor
Helper app I randomly made to extract and tweak paradox mod zips manually
- Only works for mods from http://steamworkshop.download/
- "Processing/" directory needs to be deleted/emptied from the working directory if it exists before running 

How to use:

1. Put in folder with only the mod files in zip (expected to be named as numbers like 9999999999.zip)
2. Open latest executable version
3. A "Processing/" directory should be created/filled up
4. You can now copy all the files in "Processing/" to the respective mod folder of the paradox game (expected to be in C:\Users\USER_NAME\Documents\Paradox Interactive\GAME_NAME\mod)


I'm too lazy to add more functionality. I only did this because I was annoyed of doing above manually over 20 times in a row.

Iteratively does the following for every .zip in the working directory:

1. Extract to /Processed/
2. Gets mod name from descriptor.mod
3. Replace descriptor.mod file name and mod folder name with mod name
4. Adds path to the mod folder in the renamed .mod file
5. Moves the .mod out to /Processed/

Method of extraction credited to AlpaxLP, from ff. video: 
https://www.youtube.com/watch?v=HnUYIVWePFo
