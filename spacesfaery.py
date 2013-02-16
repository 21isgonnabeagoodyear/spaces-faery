#!/usr/bin/env python

import sys

if len(sys.argv) < 3 or "--help" in sys.argv or "-h" in sys.argv:
	print "usage: "+sys.argv[0]+" filename fileout"
thefile = sys.stdin
if sys.argv[1] != "-":
	thefile = open(sys.argv[1], "r")
outfile = sys.stdout
if sys.argv[2] != "-":
	outfile = open(sys.argv[2], "w")
numparens = 0
for line in thefile:
	#print numparens*" " + line.lstrip()
	if len(line.rstrip().lstrip()) > 0 and line.rstrip().lstrip()[0] == ")":
		outfile.write((numparens-1)*" " + line.rstrip().lstrip()+"\n")
	else:
		outfile.write(numparens*" " + line.rstrip().lstrip()+"\n")
	numparens += len(filter(lambda l:l in "[(", line.partition(";")[0]))
	numparens -= len(filter(lambda l:l in ")]", line.partition(";")[0]))
#print ";#this file has been visited by the spaces faery"
outfile.write(";#this file has been visited by the spaces faery")
