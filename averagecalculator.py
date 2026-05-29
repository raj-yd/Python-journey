print("Average Calculator\n")
n=int(input("Enter Number of Subject:"))
marks=[]
for i in range(1,n+1):
    print("Enter marks of subject ",i)
    a=int(input())
    marks.append(a)
sum=sum(marks)
print("Average = ",sum/n)