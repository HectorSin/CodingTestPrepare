# 2s, 256mb
import sys
input = sys.stdin.readline

N, M = map(int,input().split()) # 1~100,000

poke_list = []
poke_dict = {}

for i in range(N): # 포켓몬 입력
    name = input().rstrip()
    poke_list.append(name)
    poke_dict[name] = i+1
    

for _ in range(M): # 문제 개수 M만큼 진행
    prob = input().rstrip()

    if prob.isdigit():
        print(poke_list[int(prob)-1])

    else:
        print(poke_dict[prob])