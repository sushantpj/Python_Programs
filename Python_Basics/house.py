i=int(input())
name = input()
r=0
for i in range(len(name)-1):
    if name[i]=="H" and name[i+1]=="H":
        r=1
        break
    elif name[i]=="H" and name[i]==".":
        name.replace(name[i+1],"B")
    elif name[i]=="." and name[i+1]=="H":
        name.replace(name[i],"B")
    print(name)

if r==1:
    print("NO")

else:
    print("YES\n",name)