a,b = map(int,input().split())

def refnit(input):
    count = 1
    result = 0
    for i in range(input):
        result += count
        count = 10*count
    return result

print(refnit(a) + refnit(b))
