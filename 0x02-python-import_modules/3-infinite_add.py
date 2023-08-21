#!/usr/bin/python3

if __name__ == "__main__":
    """Print the addition of all arguements."""
    import sys
    total = 0
for s in range(len(sys.argv) - 1):
    total += int(sys.arg[s + 1])
print("{}".format(total))
