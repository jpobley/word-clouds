# Word Cloud Parser

A small script to combine multiple world cloud CSVs into one file.

## Requirements

The script was writtng using Python 2.7 and requires the following modules (generally available in the standard library):
* os
* csv
* re
* argparse

## Installation

Download the `combine-clouds.py` file and place it in the same directory as the CSV files you wish to process.

## Usage

The script should be run from the command line. 

First, navigate to the folder where you placed the script.

Next, you can run the script on OSX and Linux by typing:

    python combine-clouds.py
    
On Windows, typing `python` in the command line will only work if you have set your path variable accordingly. Othwerwise, the default install for the python.exe file is `c:\Python27\python`. So try the following line for Windows:

    c:\Python27\python combine-clouds.py
    
Simpy calling this script, though, won't produce any output. To produce some output you should pass some flags to the file.

#### Available Flags
