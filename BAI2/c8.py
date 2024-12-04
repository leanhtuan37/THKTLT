print("sinh viên : Nguyen Phuoc Hung 205751030110042")
###########################
a,b=1,2
total=0
print(a,end=" ")
while (a <=4000000-1):
    if a%2==0:
        total +=a
    a,b=b,a+b
    print (a,end=" ")
print("\n sum of prime number term in fibonacci seriesL ",total)
