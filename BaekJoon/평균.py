N = int(input())
grade_list = list(map(int,input().split()))

total_false_grade = 0
max_grade = max(grade_list)

for i in range(N):
    total_false_grade += (grade_list[i] / max_grade) * 100

print(total_false_grade/N)