from time import sleep as sleep
import os.path as file

INPUT_PATH = input("TYPE your input file path or DRAG here the input file, the press ENTER:\n")
OUTPUT_PATH = "md_toc_output.txt"

if not file.exists(INPUT_PATH):
    print(f"File '{INPUT_PATH}' was not found")
    sleep(5)
    quit()

with open(INPUT_PATH, "r") as f:
    lines = f.readlines()

contents = []

"""
'isInCodeBlock' is a flag used to handle scenarios where the markdown file contains a code snippet with a '#' in it.
In that case the paragraph won't be registered
"""
isInCodeBlock = False

# iterate for each line and register the paragraphs (identified by the '#')
for line in lines:
    # if the line starts with '#' and the current line is not part of any code snippet then it's a paragraph definition line
    if line.startswith("#") and not isInCodeBlock:
        # counting the '#' chars to also memorize the heading level, thus enabling the TOC to also visualise nested paragraphs (subparagraphs)
        headingLevel = -1
        headingName = ""
        for char in line:
            if char == "#":
                headingLevel += 1
            else:
                # getting the paragraph name
                headingName = line.replace("#", "").strip()
                # append the paragraph data
                contents.append((headingName, headingLevel))
                # break from the 'chat in line' for loop and continue with the 'line in lines' for loop
                break
    # check if the current line starts a code snippet
    elif line.startswith("```"):
        isInCodeBlock = not isInCodeBlock

import string
specialChars = string.punctuation

# build the table of contents based on the found paragraphs
tableOfContents = ""
for content in contents:
    tabs = "\t" * content[1]
    headingName = content[0]
    for char in specialChars: headingName = headingName.replace(char, "")
    link = headingName.replace(" ", "-").lower()
    tableOfContents += f"\n{tabs}+ [{headingName}](#{link})"
tableOfContents = tableOfContents.strip()

# write TOC to an output text file
with open(OUTPUT_PATH, "w") as f:
    f.write("**Table of Contents**\n")
    f.write(tableOfContents)
print(f"\nSaved table of contents to '{OUTPUT_PATH}'\nThanks for using the tool. Have a nice day! :D")
import webbrowser
webbrowser.open(OUTPUT_PATH)
sleep(5)
quit()
