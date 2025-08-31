#!/usr/bin/env python3
import argparse

p = argparse.ArgumentParser(description="FizzBuzz with args")
p.add_argument("-n", "--number", type=int, default=100, help="end number (default: 100)")
p.add_argument("--fizz", default="Fizz", help='word for multiples of 3 (default: "Fizz")')
p.add_argument("--buzz", default="Buzz", help='word for multiples of 5 (default: "Buzz")')
args = p.parse_args()

for i in range(1, args.number + 1):
    out = ""
    if i % 3 == 0:
        out += args.fizz
    if i % 5 == 0:
        out += args.buzz
    print(out or i)