x=0
y=1
n=int(input("Enter n value : "))
for i in range(n):
  print(y,sep='',end='')
  if (i!=n-1):
    print(',',sep='',end='')
  temp=x
  x=y
  y+=temp
