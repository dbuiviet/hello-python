#!/usr/local/bin/python3
import sys  #import sys library

print(sys.platform)

#msg = "hello python"
#print(msg)
#msg.capitalize()
mystring = "Hello"
myfloat = 10.0
myint = 20

#testing code
if mystring == "Hello":
    print("String: %s" %mystring)

if isinstance(myfloat,float) and myfloat == 10.0:
    print("Float : %f" %myfloat)

if isinstance(myint,int) and myint == 20:
    print("Integer : %d" %myint)

mylist = []
mylist.append(1)
mylist.append(2)
mylist.append(3)
#mylist = [1,2,3]

#print(mylist[0])
#print(mylist[1])
#print(mylist[2])

for x in mylist:
    print(x)


numbers = [1,2,3]
strings = ["a","b","c"]
names = ["Dũng","Hạnh", "Hòa"]

second_name = names[1]

for x in numbers:
    print(x)

for x in strings:
    print(x)

print("The second name in the name list is %s" %second_name)

number = 1+2*3/4
#print(number)

remainder = 11%3
#print(remainder)

squared = 7**2
#print(squared)

cubed = 2**3
#print(cubed)

manyhellos = "Hello"*10
#print(manyhellos)

odd_numbers = [1,3,5,7]
even_numbers = [2,4,6,8]

all_numbers = odd_numbers+even_numbers
#print(all_numbers)
#print([1,2,3]*2)

x = object()
y = object()

x_list = [x]
y_list = [y]
big_list = [x,y]

i = 1
while i < 10:
    x_list.append(x)
    big_list.append(x)
    y_list.append(y)
    big_list.append(y)
    i += 1

print("x_list contains %d objects" % len(x_list))
print("y_list contains %d objects" % len(y_list))
print("big_list contains %d objects" % len(big_list))

if x_list.count(x) == 10 and y_list.count(y) == 10:
    print("Almost there...")
if big_list.count(x) == 10 and big_list.count(y) == 10:
    print("Great!")

name = "Dũng"
age = 38
print("%s is %d years old." % (name, age))

data = ("John", "Doe", 53.44)
#print(len(data))
format_string = "Hello, %s %s, your current balance is $%.4f"

print(format_string %data)

astring = "Hello World!"
print(len(astring))
print("The first occurence of letter 'o' in astring is located at %dth" %astring.index("o"))
print(astring.count("l"))
print(astring[3:7])

print("This is a new text to push to git")