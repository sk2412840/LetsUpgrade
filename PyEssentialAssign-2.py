'''
AUTHOR- AYUSH KUMAR
PURPOSE- DAY-3 ASSIGNMENT-2 PYTHON ESSENTIAL LETSUPGRADE
DATE- 11/12/2020
'''
# QUESTION-1

marks= int(input("Please Enter Your Marks:\n"))
if marks>=90:
    print("You Got A+")
elif marks<90 and marks>=80:
    print("You Have Got A")
elif marks<80 and marks>=70:
    print("You Have Got B+")
elif marks<70 and marks>=60:
    print("You Have Got B")
elif marks<60 and marks>=50:
    print("You Have Got C+")
elif marks<50 and marks>=40:
    print("You Have Got C")
else:
    print("You Have Got FAILED")

# QUESTION-2

for n in range(1,1001):
    if n>1:
        for i in range(2,n):
            if(n%i==0):
                break
        else:
            print(n)

# QUESTION-3

for num in range(1,11):
    for i in range(1,11):
        print(f"{num} * {i} = {num*i}")

# QUESTION- 4

exit= int(input("Enter a number upto which you want to print prime numbers:\n"))
n=1
while n!=exit:
    if n>1:
        for i in range(2,n):
            if n%i==0:
                break
        else:
            print(n)
    n=n+1



                

            
