#!/usr/bin/python3

import argparse

parser = argparse.ArgumentParser(description='Quick description of script')
parser.add_argument('--stuff', action='store_true', help='Help for --stuff')
parser.add_argument('--text', type=str, required=True, help='Help for --text')
parser.add_argument('--integer', type=int, help='Help for --integer')

args = parser.parse_args()

if (not (args.stuff or args.integer)):
    print("\nYou must enter one of stuff or integer\n")
    parser.print_usage()
    exit()

stuff = args.stuff
text = args.text
integer = args.integer

print("You entered stuff={} text={} integer={}".format(stuff,text,integer))
