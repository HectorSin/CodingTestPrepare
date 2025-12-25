tugriks = int(input())

result = (tugriks/100)+25
final_reuslt = min(2000, max(100,result))

print(f"{final_reuslt:.2f}")