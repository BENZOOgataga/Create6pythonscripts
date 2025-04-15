# Create6pythonscripts
Scripts for modpack makers and developers to check if your mods are compatible with Create 6. You will need an Excel file (see README).

The Excel file was adapted from this community-made one :  
https://docs.google.com/spreadsheets/d/1sEK9lDrp5nT00MzR6mSGFQzcq04kdcioGFuKwIqiavg/edit?gid=0#gid=0

> [!CAUTION]
> Note that these are helper scripts for you to find mods that aren't compatible; you should check the mods the script gives you against the ones on the Excel mentioned above.  

## Command examples:  
Specifying an excel file and changing the threshold:  
`python createsixer.py "C:\Users\mrdar.DESKTOP-B6LKOPF\curseforge\minecraft\Instances\test create 6\mods" --show-incompatible --fuzzy-threshold=75 --excel-file="C:\Users\mrdar.DESKTOP-B6LKOPF\PycharmProjects\PythFinder\c6.xlsx"`  

Show no matches and changing the threshold:  
`python createsixer.py "C:\Users\mrdar.DESKTOP-B6LKOPF\curseforge\minecraft\Instances\test create 6\mods" --show-no-matches --fuzzy-threshold=75`  

Only show incompatible mods:  
`python createsixer.py "C:\Users\mrdar.DESKTOP-B6LKOPF\curseforge\minecraft\Instances\test create 6\mods" --show-incompatible`  

## Available arguments:    
`--show-incompatible` : Show incompatible mods  
`--show-compatible` : Show compatible mods, why would you want that anyway?  
`--show-no-matches` : Show mods with no match found  
`--excel-file` : Excel file with mod names and compatibility  
`--fuzzy-threshold` : Fuzzy match threshold (default: 85)  
