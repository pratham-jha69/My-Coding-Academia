r1=["1","2","3"]
r2=["4","5","6"]
r3=["7","8","9"]
r4=["*","0","#"]
num_pad=[r1,r2,r3,r4]
for row in num_pad:
    for num in row:
        print(num,end=" ")
    print()