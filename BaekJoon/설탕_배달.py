# N킬로그램 설탕 / 3킬로그램, 5킬로그램 봉지

sugar_weight = int(input())

bag_count = 0

while True:
    if sugar_weight % 5 == 0:
        bag_count = bag_count + (sugar_weight//5)
        print(bag_count)
        break
    elif sugar_weight < 0:
        print(-1)
        break
    elif sugar_weight == 0:
        print(bag_count)
        break
    else:
        sugar_weight -= 3
        bag_count += 1