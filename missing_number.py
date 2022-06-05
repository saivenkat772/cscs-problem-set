"""https://cses.fi/problemset/task/1083"""
n=int(input())
l=list(map(int,input().split()))
s=sum(l)
a=(n*(n+1))//2
print(a-s)