kantite_not=int(input("tape kantite not ou vle klkile mwayen pou yo a: \n"))
i=0
lis_not=[]
for i in range(kantite_not):
    not_yo=float(input("Tape not: \n"))
    lis_not.append(not_yo)

Kantite=sum(lis_not)
mwayen= Kantite/kantite_not

print ("Men lis not yo :", lis_not)

if (mwayen>=90):
    print ("\nE mwayenn not yo se: ", mwayen)
    print ("\nA")
elif(mwayen>=80 and mwayen<90):
    print ("E mwayenn not yo se: ", mwayen)
    print ("\nB")
elif(mwayen>=70 and mwayen<80):
    print ("E mwayenn not yo se: ", mwayen)
    print ("\nC")
elif(mwayen>=60 and mwayen<70):
    print ("E mwayenn not yo se: ", mwayen)
    print ("\nD")
else:
    print ("E mwayenn not yo se: ", mwayen)
    print ("\nF")
