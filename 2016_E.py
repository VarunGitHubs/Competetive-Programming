T = int(input())

for i in range(1, T + 1):
  S = input()
  s,e = map(int, input().split())
  
  b = 0
  for c in S:
    if c == "B":
      b += 1

  b_count = 0

  if s - e + 1 < len(S):
    for k in range(s%len(S) - 1, len(S)):
      if S[k % len(S) - 1] == "B":
        b_count += 1
  print("B count: " + str(b_count))
  
  else:
    nearest_start = len(S) - ((s - 1) % len(S))
    for k in range(s, nearest_start):
      if S[k%len(S) - 1] == "B":
        b_count += 1
    
    s = s + nearest_start
    print("Start: " + str(s))
    completes = (e - s + 1) // len(S)
    b_count += completes * b 
  
    nearest_end = e - (e % len(S))
    print("NE: " + str(nearest_end))
    for g in range(nearest_end, e):
      if S[(g) % len(S) - 1] == "B":
        b_count += 1 
    print("Case #{}: {}".format(i, b_count))



