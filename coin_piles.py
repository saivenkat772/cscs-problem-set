"""https://cses.fi/problemset/task/1754"""
for t in range(int(input())):
    a,b=map(int,input().split())
    if (min(a,b)*2>=max(a,b)) and (a+b)%3==0:
        print("YES")
    else:
        print("NO")