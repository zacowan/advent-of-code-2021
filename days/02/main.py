from solution import solve

# Read input
vals = []

with open(f"days/02/input.txt", 'r') as f:
    for line in f.read().splitlines():
        l = line.split()
        key, val = l[0], int(l[1])
        vals.append((key, val))

# Code starts here
print(solve(vals))
