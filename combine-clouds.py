#!/usr/bin/env python
#combine-clouds.py

"""
A script for combining multiple word cloud CSV files into a single file
Author: JP Obley
Date: 2013
"""
import os, csv, re, argparse

class CloudCombiner:
    """Class for accepting keywords and combining respective CSV files"""

    def __init__(self, all=False, keywords=None, sources=None):
        """
        :param keywords: The list of words to look for.
        :type keywords: list
        """

        #The list of sources to use
        self.sources = sources if sources else [ "blog", "forum", "traditional media", "twitter" ]

        #The list of keywords to use
        self.keywords = self._generate_keywords() if all else keywords

        #Keep track of successes and failures
        self.success = []
        self.error = []

        print
        print "Starting up..."
        print "Using %d keyword(s): %s" % ( len(self.keywords), ", ".join(self.keywords) )
        print "Using %d source(s): %s" % ( len(self.sources), ", ".join(self.sources) )

    def _generate_keywords(self):
        """Generate list of all keywords based on files in current directory"""

        #Set of unique words for keywords
        keywords = set()

        #Get al the CSV files in this directory
        files = [ f for f in os.listdir(".") if f.endswith(".csv") ]

        #Parse the file names to get unique keywords (i.e. abortion, gun control) and their respective sources (i.e. twitter, blog)
        for filename in files:
            for source in self.sources:
                if re.search(source, filename):
                    kw = filename.split(source)[0].strip()
                    keywords.add(kw)

        return list(keywords)

    def combine(self):
        """Open respective CSV files and combine into one CSV based on keyword"""

        #Open each file for each keyword and grab the value
        for kw in self.keywords:
            print
            print "Processing files for '%s'..." % kw
            datalist = []
            words = {}
            output_filename = "%s combined.csv" % kw
            kw_files = [ filename for filename in os.listdir(".") if filename.startswith(kw) and filename.endswith(".csv") ]
            print "%d file(s) found: %s" % ( len(kw_files), ", ".join(kw_files) )
            for kwf in kw_files:
                isFirstLine = True
                source = None
                for src in self.sources:
                    if re.search(src, kwf):
                        source = src
                if source:
                    print "Reading %s..." % kwf
                    source = [ source for source in self.sources if re.search(source, kwf)][0]
                    try:
                        with open(kwf, "rU") as csvfile:
                            reader = csv.reader(csvfile)
                            for line in reader:
                                if isFirstLine:
                                    isFirstLine = False
                                else:
                                    word = line[0].strip()
                                    value = line[1].strip()
                                    if word not in words:
                                        words[word] = {}
                                    words[word][source] = value
                    except:
                        self.error.append("Unable to open %s." % kwf)
             
            #Create list for DictWriter class
            for each in words:
                data = words[each]
                data["word"] = each
                datalist.append(data)
            datalist.sort(key=lambda x: x["word"])

            #Create headers for csv file
            headers = [ s for s in self.sources ]
            headers.insert(0, "word")

            #Write out
            print "Saving %s to %s..." % ( output_filename, os.getcwd() )
            try:
                with open(output_filename, "wb") as out:
                    writer = csv.DictWriter(out, headers,  restval="0%",dialect="excel")
                    writer.writeheader()
                    writer.writerows(datalist)
                self.success.append(output_filename)
            except:
                self.error.append("Unable to save %s." % output_filename)

        print
        print "%d file(s) were created using the keyword(s) %s:" % ( len(self.success), ", ".join(self.keywords) )
        if len(self.success) > 0:
            for succ in self.success:
                print "\t%s" % succ
        print "There were %d error(s)." % len(self.error)
        if len(self.error) > 0:
            for err in self.error:
                print "\t%s" % err
        print

def main():
    parser = argparse.ArgumentParser()
    
    #Process all files
    parser.add_argument("-a", "--all",
                        help="Process all CSV files in this directory using 'blog', 'twitter', 'traditional media', and 'forum' as sources.",
                        action="store_true")
    
    #Change from default sources
    parser.add_argument("-s", "--sources",
                        help="Alternative sources to 'blog', 'twitter', 'traditional media', and 'forum'. List should quoted words separated by spaces. For example, 'blog' 'twitter' 'traditional media'.",
                        nargs="+")

    #Identify keywords
    parser.add_argument("-k", "--keywords",
                        help="List of keywords to process. Ignored if used with -a/--all flag. List should be quote words separted by a space. For example, 'abortion' 'gun control' 'school'.",
                        nargs="+")

    args = parser.parse_args()
    combiner = CloudCombiner(all=args.all, keywords=args.keywords, sources=args.sources)
    combiner.combine()

if __name__ == "__main__":
    main()