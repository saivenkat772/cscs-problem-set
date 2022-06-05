"""https://cses.fi/problemset/task/1069"""
s=input()
m=0
co=0
for i in range(len(s)-1):
    if s[i]==s[i+1]:
        co+=1
    else:
        co=1
    if co>m:
        m=co 
print(m)