#1Looping over a range of numbers

for i in [0, 1, 2, 3, 4, 5]:
    print(i**2)

for i in range(6):
    print(i**2)

#2Looping over a collection
colors = ['blue', 'black', 'white', 'green']

for i in range(len(colors)):
    print(colors[i])

colors = ['blue', 'black', 'white', 'green']

for color in colors:
    print(color)

#3Looping over dictionary keys

d = {'matthew': 'blue', 'rachel': 'green', 'raymond': 'red'}

for i in d.keys():
    print(i)
 
d = {'matthew': 'blue', 'rachel': 'green', 'raymond': 'red'}


for i in d.keys():
    if i.startswith('m'):
         print(i)
      
#4looping backwards   
    
colors = ['blue', 'black', 'white', 'green']


for i in range(len(colors)-1,-1,-1):
    print(colors[i])
    
colors = ['blue', 'black', 'white', 'green']
for color in reversed(colors):
    print(color)

#5

names = ['sruthi' , 'priya' , 'shanmukh' , 'suhitha']
colors = ['innocent', 'topper', 'good', 'cute']
n = min(len(names) , len(colors))
for i in range(n):
    print(names[i] , '-->' , colors[i])
   
names = ['sruthi' , 'priya' , 'shanmukh' , 'suhitha']
colors = ['innocent', 'topper', 'good', 'cute']    
for name, color in zip(names, colors):
    print(name, '-->',color)

 
#6sorted list
names = ['sruthi' , 'priya' , 'shanmukh' , 'suhitha']
for names in sorted(names):
    print(names)
   
names = ['sruthi' , 'priya' , 'shanmukh' , 'suhitha']
print(sorted(names, key = len))

#7usiing of list in differnt way

student=("sruthi ", "priya ", "shanmukh ","suhitha " )
print(student[0:3])

student=("sruthi ", "priya ", "shanmukh ","suhitha ")
print(student[:3])

#8
x = int(input("Please enter a number between 1 and 10: "))

if x < 1 or x > 10:
	print("Invalid selection")
else:
	print(x)

x = int(input("Please enter a number between 1 and 10: "))

if x > 0 and x < 11:
	print(x)
else:
	print("Invalid selection")
	
#9	
list1 = [5, 4, 3, 2, 1]
list2 = list1
list1 += [1, 2, 3, 4]
  
print(list1)
print(list2)

list1 = [5, 4, 3, 2, 1]
list1 = list1 + [1, 2, 3, 4]
list2 = list1

print(list1)
print(list2)

#10
colors = ['red', 'green', 'blue', 'yellow']
print (sorted(colors, key=len))

#11

is_generic_name = False
name = 'Harry'
if name == 'Tom' or name == 'Dick' or name == 'Harry':
    is_generic_name = True
    print(is_generic_name)

name = 'Tom'
is_generic_name = name in ('Tom', 'Dick', 'Harry')
print(is_generic_name)

#12

def number_of_evil_robots_attacking():
    return 10
def should_raise_shields():
    return number_of_evil_robots_attacking()
if should_raise_shields() == True:
    raise_shields()
    print('Shields raised')
else:
    print('Safe! No giant robots attacking')



def number_of_evil_robots_attacking():
    return 10
def should_raise_shields():
    return number_of_evil_robots_attacking()
if should_raise_shields()== True:
    raise_shields()
    print('Shields raised')
else:
    print('Safe! No giant robots attacking')

#13
foo = True
value = 0
if foo:
    value = 1
print(value)

foo = True
value = 1 if foo else 0
print(value)

#14
my_container = ['ria', 'sam', 'rashi']
index = 0
for element in my_container:
    print('{} {}'.format(index, element))
index += 1
    

my_container = ['ria', 'sam', 'rashi']
for index, element in enumerate(my_container):
    print('{} {}'.format(index, element))

#15
my_list = ['ria', 'sam', 'rashi']
index = 0
while index < len(my_list):
    print(my_list[index])
    index += 1

my_list = ['ria', 'sam', 'rashi']
for element in my_list:
    print(element)
 
#16
def f(a, L=[]):
    L.append(a)
    return L
print(f(1))
print(f(2))
print(f(3))

def f(a, L=None):
    if L is None:
        L = []
        L.append(a)
        return L
print(f(1))
print(f(2))
print(f(3))


#17
def all_equal(a, b, c):
    result = False
    if a == b == c:
        result = False
        if a == b == c:
            result = True
            return result
        
def all_equal(a, b, c):
return a == b == c

#18
def print_list(list_value, sep):
    print('{}'.format(sep).join(list_value))
the_list = ['a', 'b', 'c']
the_other_list = ['sruthi', 'loves', 'food']
print_list(the_list, ' ')
print_list(the_other_list, ' ')
print_list(the_other_list, ', ')

def print_list(list_value, sep=' '):
    print('{}'.format(sep).join(list_value))
the_list = ['a', 'b', 'c']
the_other_list = ['sruthi', 'loves', 'food']
print_list(the_list)
print_list(the_other_list)
print_list(the_other_list, ', ')

#19
students = ['sruthi' , 'priya' , 'shanmukh' , 'suhitha']
print(students[-1])

students = ['sruthi' , 'priya' , 'shanmukh' , 'suhitha']
print(students[-1])

#20
def add(x,y):
    return x+y
x=3
y=4
z = add(x,y)
print(z)

adder = lambda x,y: x+y
print(adder(3,4))

'''
