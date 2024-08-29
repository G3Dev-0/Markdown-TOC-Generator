from time import sleep as sleep
import os.path as file
import webbrowser

INPUT_PATH = "md_toc_input.txt"
OUTPUT_PATH = "md_toc_output.txt"

if not file.exists(INPUT_PATH):
    print(f"Paste your Markdown content into '{INPUT_PATH}'")
    # create file
    with open(INPUT_PATH, "w") as f:
        f.write("")
    webbrowser.open(INPUT_PATH)
    sleep(2.5)
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
    f.write(tableOfContents)
print(f"Saved table of contents to '{OUTPUT_PATH}'\nThanks for using the tool. Have a nice day! :D")
webbrowser.open(OUTPUT_PATH)
sleep(2.5)
quit()
