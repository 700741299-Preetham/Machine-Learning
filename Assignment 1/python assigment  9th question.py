N = int(input("Enter number of students "))
in_lbs=[]
in_kgs=[]
print("Enter weight of "+str(N)+" studens")
for i in range(N):
    #assinging input to temp
    temp=int(input(str(i+1)+". Student weight :"))
    in_lbs.append(temp)
    #we know 1lb=0.453kg
    in_kgs.append(float("{:.2f}".format(temp*0.453)))
print("Weight in lbs :",in_lbs)
print("Weight in kgs : ",in_kgs)
