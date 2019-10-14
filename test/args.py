import argparse

parser = argparse.ArgumentParser()
parser.add_argument("fa_en", type=str)
arg = parser.parse_args()
fa_en = arg.fa_en
if fa_en == "fa":
    print("iran")
if fa_en == "en":
    print("Enghlish")
