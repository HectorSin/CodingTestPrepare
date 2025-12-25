num = int(input())

count = 1
found = False

while count <= num:
    pred = count
    for a in str(count):
        pred += int(a)
    if pred == num:
        print(count)
        found = True
        break

    count += 1

if found == False:
    print(0)