f=int(input())
list=input().split()
l=[]
for i in range(0,f):
   list.insert(i,int(list[i]))
   list.remove(list[i+1])
   
list.sort(reverse=True)
for i in range(0,f):
   l.append(str(list[i]))

l=''.join(l)

while l[0] == "0":
    if(len(l)==1):
      break
    l = l[1:]

print(l)
