'''AUTHOR- AYUSH KUMAR
PURPOSE- ASSIGNMENT-3 DAY-4 PYESSENTIAL 101 LETSUPGRADE
DATE- 13/12/2020
'''
# Question-1
#Write down a program in Python for Opening a File and Writing " I Love LetsUpgrade" And close
#it, and read it back again, and then append some data to it and close it.

f= open("file1.txt", 'w')
f.write("I Love LetsUpgrade.")
f.close()

f= open("file1.txt",'r+')
a = f.read()
print(a)
f.write(" Learning python is fun.")
f.close()

#Question 2
#Write a function which can return a Factorial of any numbers as INT, given in the argument

def fact(num):
    if(num==1):
        return num
    else:
        return num*fact(num-1)

if __name__ == "__main__":
    n= int(input("Enter A Number:\n"))
    if n<0:
        print("Invalid Input")
    elif n==0:
        print("Factorial of 0 is 1")
    else:
        print(f"Factorial of {n} is {fact(n)}")
            



