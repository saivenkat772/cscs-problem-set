"""https://cses.fi/problemset/task/1755"""
s=input()
l=list(set(s))
co=[]
os=""
osi=0
for i in l:
    co.append(s.count(i))
oc=0
for i in range(len(co)):
    if co[i]%2==1:
        oc+=1
        os=l[i]
        osi=i
if oc>1:
    print("NO SOLUTION")
elif oc==1:
    ans=""
    for i in range(len(l)):
        if l[i]!=os:
            ans+=l[i]*(co[i]//2)
    ans=ans+l[osi]*co[osi]+ans[::-1]
    print(ans)
else:
    ans=""
    for i in range(len(l)):
        ans+=l[i]*(co[i]//2)
    ans=ans+ans[::-1]
    print(ans)