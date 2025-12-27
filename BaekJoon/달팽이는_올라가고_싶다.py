A, B, V = map(int,input().split())

day = 0

daily_climb = A - B

print((((V-A)+daily_climb-1) // daily_climb) + 1)