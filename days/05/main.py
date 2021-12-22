from solution import solve

# Read input
transforms: list[tuple[tuple[int, int], tuple[int, int]]] = []

with open(f"days/05/input.txt", 'r') as f:
    lines = f.read().splitlines()
    for l in lines:
        sides = l.split('->')
        left = sides[0].strip().split(',')
        right = sides[1].strip().split(',')

        # From
        f = (int(left[0]), int(left[1]))
        # To
        t = (int(right[0]), int(right[1]))
        transforms.append((f, t))


# Code starts here
print(solve(transforms))
