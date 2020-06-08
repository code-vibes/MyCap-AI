# 1.assigning elements to different tupple:
list1=[1,"two",(3,),{4},{5:"five"}]
list2=list(input())
list2.append(input())
print(list1+list2) #or list1.extend(list2)

# 2.accessimg elements from a tupple:
tup="HELLO world"
print(tup[0],tup[6:]) #output: H world

# 3.deleting different dictionary elements:
di={}
di[1]="one"
di[2]="two"
di["hello"]="world"
print(di)
del di["hello"]
print(di)
