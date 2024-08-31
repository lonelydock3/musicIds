# format document properly from work laptop email

import os

INPUT_FOLDER    = 'fromWorkLaptop'
INPUT_FILE      = 'workLaptopTunes.txt' 

OUTPUT_FILE     = 'formattedWorkLaptopTunes.txt'

categories = ['clubbin', 'chill', 'trance', 'techno']

# read in input file 
with open(os.path.join(INPUT_FOLDER, INPUT_FILE), 'r', encoding='utf8') as fr:
    lines = fr.readlines()

# remove blank lines in between 
filteredLines = []
for lineIdx, line in enumerate(lines):
    if not(line == '\n'):
        filteredLines.append(line)

# add in a blank line above each category
outputLines = []
for filteredLineIdx, filteredLine in enumerate(filteredLines):
    if filteredLine in categories:
        addBlank = ['\n', filteredLine]
        outputLines = outputLines + addBlank
    else:
        outputLines.append(filteredLine)

# write to output file
with open(os.path.join(INPUT_FOLDER, OUTPUT_FILE), 'w', encoding='utf8') as fw:
    fw.writelines(outputLines)
    print('File written to: ', os.path.join(INPUT_FOLDER, OUTPUT_FILE))
