#!/usr/bin/env python3
import argparse
from PIL import Image
from rembg import remove

parser = argparse.ArgumentParser(
    prog=r'Image Background Remover',
    description=r'A small CLI to remove background of an image.'
)

parser.add_argument(
    '-i', '--infile',
    help=r'Path of input file.', 
    required=True
)

parser.add_argument(
    '-o', '--outfile',
    help=r"Path to store new file, eg: '/home/user/Pictures/portrait.png'.",
    required=True
)

args = parser.parse_args()

img_in = args.infile
img_out = args.outfile

try:
    infile = Image.open(img_in)
    outfile = remove(infile)
    outfile.save(img_out)
    print(f"[Success] Output file saved to: '{img_out}'")
except Exception as e:
    print(e)
