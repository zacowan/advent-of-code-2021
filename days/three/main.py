from solution import solve_p2

# Read input
vals = []

with open(f"days/three/input.txt", 'r') as f:
    vals = f.read().splitlines()

# Code starts here
print(solve_p2(vals))
