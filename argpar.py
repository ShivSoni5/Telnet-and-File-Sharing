#!/usr/bin/python

import argparse

parser = argparse.ArgumentParser()
"""
parser.add_argument("shiv")
parser.add_argument("square",help="square the given number",type=int)

args = parser.parse_args()
print args.shiv
print args.square**2
"""

parser.add_argument("-v","--verbosity",help="increase output verbosity",action="store_true")
args = parser.parse_args()
if args.verbosity:
	print "verbosity turned on"
