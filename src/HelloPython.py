#!/usr/local/bin/python3
import sys  #import sys library
from sys import argv
from os.path import exists

print(sys.platform)

msg = "hello python"
#msg = msg.capitalize()
print(msg)
print(msg.upper())
print(msg.lower())
print(msg.title())

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
names = ["Dũng", "Hạnh", "Hòa", "Hiếu", "Hà"]
print(names[-1]) #Prints the last element in the list
names.insert(1,"Vinh")
print(names)
del names[1]
print(names)
names.remove(names[2])
print(names)
poped_name = names.pop(1)
poped_name_last = names.pop()
print(poped_name)
print(poped_name_last)

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

#error
print("Happy " + str(age) + "th Birthday, " + name)
#print("Happy %dth Birthday, %s" %(age,name))

data = ("Donald", "Trump", 53.44)
#print(len(data))
format_string = "Hello, %s %s, your current balance is $%.4f"
print(format_string %data)
name = "John"
if name in ["John", "Doe"]:
    print("Your name is John or Doe")

astring = "Hello World!"
print(len(astring))
print("The first occurence of letter 'o' in astring is located at %dth" %astring.index("o"))
print(astring.count("l"))
print(astring[3:7])

print("This is a test text to push to git")

#list
x = [1,2,3]
y = [1,2,3]
print(x == y) # Prints out True
print(x is y) # Prints out False, because 'is' compares instances instead of values

#for x in range(5):
#    print(x) #print 0,1,2,3,4

#for x in range(3,6):
#    print(x) #print 3,4,5

#for x in range(3,8,2):
#    print(x) #print 3,5,7

count = 0
#while count < 5:
#    print(count)
#    count += 1
while True:
    print(count)
    count += 1
    if count >= 5:
        break

for x in range(10):
    if (x%2) == 0:
        continue
    print(x)

count2 = 0
while (count2 < 5):
    print(count2)
    count2 += 1
else:
    print("count2 value reached %d" %count2)

print("""
There's something going on here.
With the three double-quotes.
We'll be able to type as much as we like.
Even 4 lines if we want,or 5,or 6.
""")

#print("How old are you? ", end='')
#your_age = input()
your_age = input("How old are you? ")
#print("How tall are you? ", end='')
#your_height = input()
your_height = input("How tall are you? ")
#print("How much do you weigh? ", end='')
#your_weight = input()
your_weight = input("How much do you weigh? ")
print(f"So, you are {your_age} old, {your_height} tall and {your_weight} heavy.")

# pylint: disable=unbalanced-tuple-unpacking
# script_name, user_name, file_name = argv
# prompt = '> '

# print(f"Hi {user_name}, I'm the {script_name} script.")
# print("I'd like to ask you a few questions.")
# print(f"Do you like me {user_name}?")
# likes = input(prompt)

# print(f"Where do you live {user_name}?")
# lives = input(prompt)

# print("What kind of computer do you have?")
# computer = input(prompt)

# print(f"""
# Alright, so you said {likes} about liking me.
# You live in {lives}.  Not sure where that is.
# And you have a {computer} computer.  Nice.
# """)

# txt = open(file_name,'r')
# print(f"Here's your file name: {file_name}")
# print("And it's content is: \n")
# print(txt.read())
# txt = open(file_name,'w') #'w' mode for writing
# print("Let's delete the old content.")
# txt.truncate()
# print("Now write some new text")
# line1 = input("Line 1: ")
# line2 = input("Line 2: ")
# line3 = input("Line 3: ")
#txt.write(line1)
#txt.write('\n')
#txt.write(line2)
#txt.write('\n')
#txt.write(line3)
#txt.write('\n')
# txt.write(f"{line1}\n{line2}\n {line3}\n")
# print("Now close/save the file")
# txt.close() #always to close the opened file

#copy content from a file to a file
script_name, from_file, to_file = argv
print(f"We are writing from {from_file} to {to_file}")
temp_file = open(from_file, 'r')
temp_data = temp_file.read()
print(f"The input file has {len(temp_data)} bytes long")
temp_file.close()

print(f"Does the output file exist? {exists(to_file)}")
print("Ready, hit Return to continue, Ctrl-C to abort")
input() #waiting user keystroke to continue
temp_file = open(to_file,'w')
temp_file.write(temp_data)
temp_file.close()
print(f"We are done with writing, check the files out!")

def cheese_and_crackers(cheese_count, box_of_crackers):
    print(f"You have {cheese_count} cheese")
    print(f"You have {box_of_crackers} box of crackers")
    print(f"That's enough for the weekend party.")

amount_cheese = input("How many cheese you want? ")
amount_box_crackers = input("How many box of crackers are there? ")
cheese_and_crackers(int(amount_cheese), int(amount_box_crackers))

