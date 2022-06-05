"""https://cses.fi/problemset/task/1069"""
s=input()
if len(s)==1:
    print(1)
else:
    m=0
    co=1
    for i in range(len(s)-1):
        if s[i]==s[i+1]:
            co+=1
        else:
            co=1
        if co>m:
            m=co 
    print(m)
