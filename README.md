# Markdown-ToC-Generator
A quick-and-easy 'Table of Contents' generator for your markdown files.

### Table of Contents
- [Markdown-ToC-Generator](#markdowntocgenerator)
    - [Installation Guide](#installation-guide)
        - [Download Executable](#download-executable)
            - [Step 1](#step-1)
                - [Step 2](#step-2)
                - [Step 3 (optional)](#step-3-optional)
            - [Download Python File](#download-python-file)
        - [Usage](#usage)
            - [Choosing ToC Location](#choosing-toc-location)
            - [Running Generator](#running-generator)
        - [Example](#example)


<br>

## Installation Guide
The generator (mdtoc) can either be downloaded as an executable or regular python script.

### Download Executable
> This option is ideal if you want to make the generator globally available.

##### Step 1
Download the `mdtoc` file from this repo.

<br>

##### Step 2
Double check that the executable is *actually* executable by doing where you've downloaded the file.

```
chmod +x mdtoc
```

<br>

##### Step 3 (optional)
If you want to make the generator executable globally on Linux do.

```
mv mdtoc /usr/bin
```
For other operating systems, uhhhhh google it?

<br>

### Download Python File

##### Step 1
Download the `mdtoc` file from this repo and change the file name to `mdtoc.py`

<br>

##### Step 2
Remove the first line of the file.

```
#!/usr/bin/env python3
```

<br>

## Usage
It's pretty simple! Just two steps--indicate where you want the table of contents to go, then run the program!

#### Choosing ToC Location
In the file you want to write your Table of Contents (ToC) in, write the following on its own line:

```
**MD-TOC**
```
This indicates to the generator that the ToC should be placed in that location. Please note that existing content will not be overwritten unless placed on the same line as `**MD-TOC**`.

<br>

#### Running Generator
Once the location has been marked, it's time to run the program. Here's how to do it:

```
mdtoc <source_file> <dest_file>

# or

python mdtoc.py <source_file> <dest_file>
```

- `source_file`= the markdown file the ToC should be generated from

- `dest_file` = the markdown file the ToC should be inserted into

<br>

## Example


