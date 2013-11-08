#!/usr/local/bin/python

import sys, getopt
from BeautifulSoup import BeautifulSoup


def main(argv):
    inputfile = ''
    outputfile = ''
    try:
        opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
    except getopt.GetoptError:
        print 'tableclean.py -i <inputfile> -o <outputfile>'
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print 'tableclean.py -i <inputfile> -o <outputfile>'
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputfile = arg
        elif opt in ("-o", "--ofile"):
            outputfile = arg

    print 'Input file is "', inputfile
    print 'Output file is "', outputfile

    soup = BeautifulSoup(open(inputfile))

    divfind = soup.findAll('div', attrs={'class': 'rank_arrow_container'})

    for x in divfind:
	   x.extract()

    html = soup.prettify("utf-8")

    with open(outputfile, "wb") as file:
	       file.write(html)

if __name__ == '__main__':
	main(sys.argv[1:])
