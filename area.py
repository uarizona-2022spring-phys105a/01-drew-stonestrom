#!/usr/bin/env python3
from math import pi
import argparse

def area(r):
	return pi * r * r

parser = argparse.ArgumentParser(description='this program computes the area of a circle.')
parser.add_argument("r", type=float, help="the radius of a circle")

args = parser.parse_args()


r = args.r
A = area(r)

print('Area of a circle with radius', r, 'is', A)


