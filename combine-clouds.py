#!/usr/bin/env python
#combine-clouds.py

"""
A script for combining multiple word cloud CSV files into a single file

Author: JP Obley
Date: 2013
"""
import os, sys, csv, re

class CloudCombiner:
    """Class for accepting keywords and combining respective CSV files"""

    def __init__(self, keywords=None):
        """
        :param keywords: The list of words to look for.
        :type keyords: list
        """
        self.keywords = keywords if keywords else self._generate_keywords()

    def _generate_keywords(self):
        """Generate list of all keywords based on files in current directory"""

        #Get al the CSV files in this directory
        files = [ f for f in os.listdir(".") if f.endswith(".csv") ]

        #Parse the file names to get unique keywords (i.e. abortion, gun control) and their respective sources (i.e. twitter, blog)
        splitter = re.compile(r'\w+.csv$')
        #Create dictionary with keywords as 
        return keywords

    def create_csv(self, filenames):
        """
        Open respective CSV files and combine into one CSV

        :param filenames: A list of filenames to combine
        :type filenames: list
        """


if __name__ == "__main__":

    if len(sys.argv) == 1:
        files = [ f for f in os.listdir(".") if f.endswith(".csv") ]
        combiner = CloudCombiner(files)
    else:
        combiner = CloudCombiner(sys.argv[1:])

    print combiner.keywords