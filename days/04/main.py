from solution import solve, Board

# Read input
draw: list[int] = []
boards: list[Board] = []

with open(f"days/04/input.txt", 'r') as f:
    lines = f.read().splitlines()
    # First line is the numbers to draw
    for c in lines[0].split(','):
        draw.append(int(c))
    # Remaining lines are boards separated by a blank line
    i = 1
    raw: list[list[list[int]]] = []
    rows: list[list[int]] = []
    while i < len(lines):
        l = lines[i].strip().split()
        if len(l) > 1:
            row: list[int] = []
            for c in l:
                row.append(int(c))
            rows.append(row)
        if len(rows) == 5:
            raw.append(rows)
            rows = []
        i += 1
    # Construct boards
    for r in raw:
        boards.append(Board(r))


# Code starts here
print(solve(draw, boards))
