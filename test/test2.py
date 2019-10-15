#!/usr/bin/env python

import argparse
import sys


arg = argparse.ArgumentParser(description="test code ")
arg.add_argument("fan",  type=str,  help=" ok ")
arg.add_argument("-o","--one", action='store_true', help=" 1 ")
arg.add_argument("-t","--tow", action='store_true', help=" 2 ")
arg.add_argument("--name",  type=str,  help=" get name ")

args_Select = arg.parse_args()





def one():
    fname = args_Select.name
    print(fname,"ok")


def tow():
    print("tow")



def main():
    if args_Select.fan == "one":
        one()

    if args_Select.fan == "tow":
        tow()

if __name__ == "__main__":
    main()