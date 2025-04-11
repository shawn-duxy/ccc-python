# Sunny Days

n = int(input())

s = ""
for _ in range(n):
    s += input()

max_sunny = 0

has_p = False
for i in range(n):
    if s[i] == 'P':
        has_p = True
        sunny_before = 0
        sunny_after = 0
        j = i - 1
        while j >= 0 and s[j] == 'S':
            sunny_before += 1
            j -= 1
        j = i + 1
        while j < n and s[j] == 'S':
            sunny_after += 1
            j += 1
        max_sunny = max(max_sunny, 1 + sunny_before + sunny_after)

print(max_sunny if has_p else n - 1)
