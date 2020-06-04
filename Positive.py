print("Enter nummbers to be appended to list.\nEnter non-integer character to end input")
a=0
output=[]
while(True):
    a=input("enter : ")
    try:
        a=int(a)
        if(a>=0):
            output.append(int(a))
    except ValueError:
        break
print("Output : ",output)
