input_num = float(input())

while True:
    next_num = float(input())
    if next_num == 999:
        break
    print(f"{next_num-input_num:.2f}")
    input_num = next_num