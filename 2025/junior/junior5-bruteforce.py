# Connecting Territories

r = int(input())
c = int(input())
m = int(input())

grid = []
tile = 1
for _ in range(r):
    row = []
    for _ in range(c):
        row.append(tile)
        tile = tile % m + 1
    grid.append(row)


def find_min(i, j):
    if i == 0:
        return grid[i][j]
    mm = find_min(i - 1, j)
    if j > 0:
        mm = min(mm, find_min(i - 1, j - 1))
    if j < c - 1:
        mm = min(mm, find_min(i - 1, j + 1))
    return mm + grid[i][j]

row = [] * c

for i in range(c):
    row.append(find_min(r - 1, i))

print(min(row))