"""
성적이 낮은 순서로 학생 출력하기
"""

N = int(input())

student_list = []

for student in range(N):
    name, grade = input().split()
    student_list.append((name,int(grade)))

student_list = sorted(student_list, key=lambda student:student[1])

for student in student_list:
    print(student[0], end=' ')