#!/usr/bin/env python3
import argparse
import sys

def add(a, b): return a + b
def sub(a, b): return a - b
def mul(a, b): return a * b
def div(a, b):
    if b == 0:
        raise ValueError("Division by zero")
    return a / b

OPS = {
    'add': add,
    'sub': sub,
    'mul': mul,
    'div': div
}

def main():
    parser = argparse.ArgumentParser(description="Simple Calculator CLI")
    parser.add_argument('op', choices=OPS.keys(), help='operation: add, sub, mul, div')
    parser.add_argument('a', type=float, help='first operand')
    parser.add_argument('b', type=float, help='second operand')
    args = parser.parse_args()

    try:
        result = OPS[args.op](args.a, args.b)
        # If integer result, print as int
        if result == int(result):
            print(int(result))
        else:
            print(result)
    except Exception as e:
        print(f"ERROR: {e}", file=sys.stderr)
        sys.exit(2)

if __name__ == '__main__':
    main()
