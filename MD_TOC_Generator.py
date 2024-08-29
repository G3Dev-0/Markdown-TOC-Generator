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

isInCodeBlock = False

for line in lines:
    if line.startswith("#") and not isInCodeBlock:
        headingLevel = -1
        headingName = ""
        for char in line:
            if char == "#":
                headingLevel += 1
            else:
                headingName = line.replace("#", "").strip()
                contents.append((headingName, headingLevel))
                break
    elif line.startswith("```"):
        isInCodeBlock = not isInCodeBlock

import string
specialChars = string.punctuation

tableOfContents = ""
for content in contents:
    tabs = "\t" * content[1]
    headingName = content[0]
    for char in specialChars: headingName = headingName.replace(char, "")
    link = headingName.replace(" ", "-").lower()
    tableOfContents += f"\n{tabs}+ [{headingName}](#{link})"
tableOfContents = tableOfContents.strip()

with open(OUTPUT_PATH, "w") as f:
    f.write("**Table of Contents**\n")
    f.write(tableOfContents)
print(f"\nSaved table of contents to '{OUTPUT_PATH}'\nThanks for using the tool. Have a nice day! :D")
import webbrowser
webbrowser.open(OUTPUT_PATH)
sleep(5)
quit()
