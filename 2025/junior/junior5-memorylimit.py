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


for i in range(r - 2, -1, -1):
    for j in range(c):
        mm = grid[i + 1][j]
        if j > 0:
            mm = min(mm, grid[i + 1][j - 1])
        if j < c - 1:
            mm = min(mm, grid[i + 1][j + 1])
        grid[i][j] += mm

print(min(grid[0]))
