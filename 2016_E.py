from statistics import mode



T = int(input())

for i in range(1, T + 1):
    S = input()
    s,e = map(int, input().split())
    
    b = 0
    for c in S:
        if c == "B":
            b += 1

    b_count = 0

    nearest_start = len(S) - ((s - 1) % len(S))
    for k in range((s - 1) % len(S), len(S)):
        if S[k] == "B":
            b_count += 1
    
    s = s + nearest_start
    completes = (e - s + 1) // len(S)
    b_count += completes * b 

    nearest_end = 



