#Hacker Rank Collections Shoe Problems
from collections import Counter
X = int(input())
S = Counter(map(int,input().split()))
N = int(input())
rearn = 0
for customer in range(N):
    size, x = map(int,input().split())
    if size in S and S[size] > 0:
        S[size] -= 1
        rearn =rearn+x
            
print(rearn)
