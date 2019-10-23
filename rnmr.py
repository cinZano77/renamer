import glob
import os

for unit in glob.glob("/Users/UserName/YourDirectory/SomeFolder/**/*", recursive=True):
    if 'line we need to change ' in unit:
        print(unit)  # this line – just to see in a log what the script founds in the folder
        os.rename(unit, unit.replace('line we need to change ', 'new line (usually left empty)'))

# We put /**/* to scan through an every folder and a file inside them
# New line I usually left empty, just to delete 'line I need to change' from file name 
