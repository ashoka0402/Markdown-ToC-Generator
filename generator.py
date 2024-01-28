import argparse
import os
from typing import Dict, Tuple
from pathlib import Path
import string


def get_markdown(file_name: str) -> str:
    """Opens the markdown content from the file with the
    given name, and returns its content as a single string.

    Args:
        file_name: name of the `.md` file to read in
    Returns:
        the contents of the `.md` file
    """
    data = Path(file_name).read_text()
    return data


def get_headings(markdown: str) -> Dict[str, int]:
    """Reads the given string of markdown and identifies
    each of the headings (#, ##, ###, etc) and their 
    nesting level. 

    Args:
        markdown: the markdown content
    Returns:
        a dictionary where the keys are the headings and the
        values are the nest/indentation levels.
    """
    headings = dict()
    in_code_block = False

    for line in markdown.splitlines():
        curr_level = 0
        # inside a code block, so ignore comments
        if line.startswith("```"):
            in_code_block = not in_code_block

        if line.startswith("#") and not in_code_block:
            # count how many hashtags
            for char in line:
                if char == "#": curr_level += 1
                else: break

            # remove hashtags + add to dict
            heading = line[curr_level + 1:]
            headings[heading] = curr_level

    return headings



def format_heading(heading: str) -> str:
    """Formats the given heading to match the following:
        - [Heading Name](#link-to-heading)

    Args:
        heading: the markdown heading to be formatted
    Returns:
        the formatted heading
    """
    formatted = ""
    formatted += f"- [{heading}](#" # ADD BACK END
    heading = heading.lower()

    # ignore punctuation + replace "&" +  add dashes
    for i, char in enumerate(heading):
        if char == "&":
            formatted += "--"

        elif char == " ":
            if (heading[i + 1] and heading[i + 1] == "&")\
                    or (heading[i - 1] and heading[i -  1] == "&"):
                continue
            else:
                formatted += "-"
        
        elif char in string.ascii_lowercase or char.isnumeric():
            formatted += char
        else:
            continue

    formatted += ")\n"
    return formatted



def generate_toc(headings: Dict[str, int]) -> str:
    """Formats the given headers using their nesting levels
    as a guide, in order to create a Table of Contents.

    Args:
        headings: each of the headings (#, ##, etc) and their nesting
        level
    Returns:
        the table of contents as a single string
    """
    toc_text = ""
    curr_indent = 0

    for heading, level in headings.items():
        txt = format_heading(heading)
        # regular h1 headings
        if level == 1:
            toc_text += txt 
            curr_indent = 1

        else:
            # determine amount of tab space for 
            # nested layers
            if level > curr_indent:
                curr_indent += 1
            elif level < curr_indent:
                curr_indent -= 1
            
            tab_space = "    " * (curr_indent - 1)
            toc_text += tab_space
            toc_text += txt
             
    return toc_text


def read_args() -> Tuple[str, str]:
    """Read in the command-line arguments to determine the
    source and destination file

    Returns:
        a tuple where the first item is the source file location,
        and the second is the destination file location.
    """
    files = tuple()
    return files



if __name__ == "__main__":
    #source_file, dest_file = read_args()
    markdown = get_markdown("sample.md")
    headings = get_headings(markdown)
    toc = generate_toc(headings)
