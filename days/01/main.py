from solution_p2 import solve

# Read input
vals = []

with open(f"days/01/input.txt", 'r') as f:
    vals = f.read().splitlines()

for i in range(len(vals)):
    vals[i] = int(vals[i])

# Code starts here
print(solve(vals))
