# 1.5s 4mb

import sys
input = sys.stdin.readline

M = int(input())

S = [0] * 21 # 비어있는 공집합

def num_action(method, num=0):
    global S

    if method == "add":
        if S[num] == 0:
            S[num] = 1
    elif method == "remove":
        if S[num] != 0:
            S[num] = 0
    elif method == "check":
        if S[num] == 0:
            print(0)
        else:
            print(1)
    elif method == "toggle":
        if S[num] == 0:
            S[num] = 1
        else:
            S[num] = 0
    elif method == "all":
        for i in range(1,21):
            S[i] = 1
    elif method == "empty":
        S = [0] * 21



for _ in range(M):
    in_method = input().rstrip()
    if in_method in ("empty", "all"):
        method = in_method
        num_action(method)
    else:
        method, num = in_method.split()
        num = int(num)
        num_action(method, num)