# Word Cloud Parser

A small script to combine multiple world cloud CSVs into one file.

## Requirements

The script was writtng using Python 2.7 and requires the following modules (generally available in the standard library):
* os
* csv
* re
* argparse

#### Filename Structure

The script expects all the CSV files that are to be combined to have the following filename structure:

`[keword] [source].csv`

##### Examples
* abortion blog.csv
* gun control twitter.csv
* potus traditional media.csv

Any filename that does not follow this structure will be ignored.

## Installation

Download the `combine-clouds.py` file and place it in the same directory as the CSV files you wish to process.

## Usage

The script should be run from the command line. 

First, navigate to the folder where you placed the script.

Next, you can run the script on OSX and Linux by typing:

    python combine-clouds.py
    
On Windows, typing `python` in the command line will only work if you have set your path variable accordingly. Othwerwise, the default install for the python.exe file is `c:\Python27\python`. So try the following line for Windows:

    c:\Python27\python combine-clouds.py
    
Simply calling this script, though, will only produce a help message. To combine some files you need to pass some flags to the file.

### Available Flags

The script accepts 3 flags

* __-a, --all__
    * This flag overrides all other flags. It tells the script to use process all of the files in the directory. The default sources are "blog", "traditional media", "twitter", and "forum". It uses these sources to parse each filename and determine all of the unique keywords.
    * Example:

        `python combine-clouds.py --all`

* __-k, --keywords__
    * This flag tells the script which keyword to process. It can take *n* keywords, each in quotes, and separated by a space
    * Example:

        `python combine-clouds.py --keywords "abortion" "crime" "gun control"`

* __-s, --sources__
    * This flag sets different sources use when looking through the files. The default sources are "blog", "traditional media", "twitter", and "forum".
    * Example:

        `python combine-clouds.py --sources "news" "televsion" "facebook"`

#### Other usage examples

This command processes all the files for the keyword "gun control" using the default sources ("blog", "traditional media", "twitter", and "forum"):

    python combine-clouds.py -k "gun control"

This command process all of the files in the current directory:

    python combine-clouds.py -a

This command processes all the files for the keywords "gun control" and "election" using the sources "blog", "twitter", and "reddit":

    python combine-clouds.py -k "gun control" "election" -s "blog" "twitter" "reddit