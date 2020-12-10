'''AUTHOR: AYUSH KUMAR
PURPOSE: ASSIGNMENT-1 DAY-2 PYTHON ESSENTIAL LETSUPGRADE
DATE- 10/12/2020
 '''

# 5 string functions:

mystr= "welcome to my first PYTHON program"
print("The Original String Is:")
print(mystr)
print("\nOutput Of Different String Functions:")
print(mystr.capitalize())
print(mystr.lower())
print(mystr.upper())
print(mystr.replace("first","second"))
print(mystr.title())

# 5 list functions:

mylist= [5,7,1,5,9,3,2,7,555,4412,21,0,5,5,0,5]
print("\nThe Original List Is:")
print(mylist)
print("\nOutput Of Different List Functions:")
print(mylist.index(7))
print(mylist.count(5))
mylist.extend([1,2,5,9])
print(mylist)
mylist.pop()
print(mylist)
mylist.clear()
print(mylist)

# 5 Dictionary Functions:

mydict= {
    "Name" : "Ayush",
    "Age" : "20",
    "Course" : "B.Tech",
    "Address" : "Rajajipuram Lucknow"
}
print("\nThe Original Dictionary Is:")
print(mydict)
print("\nOutput Of Different Dictionary Functions:")
print(mydict.items())
print(mydict.keys())
print(mydict.values())
mydict.update({"Phone" : "84xxxxxx05"})
print(mydict)
mydict.popitem()
print(mydict)





