#--------------Question 1--------------
def welcome() :
    print("Welcome to the Hundred Arcre Wood!")

welcome()

#--------------Question 2--------------
def greetings(name) :
    print("Welcome to the Hundred Arcre Wood " + name + "!")

greetings("Michael")
greetings("Winnie the Pooh")

#--------------Question 3--------------
def print_catchphrase(character): 
    if character == "Pooh": 
        print("Oh bother!")
    elif character == "Tigger": 
        print("TTFN: Ta-ta for now!")
    else: 
        print("Sorry! I don't know " + character + "'s chatchprhase! ") 

character = "Pooh"
print_catchphrase(character)

#--------------Question 4--------------
def get_item(items, x): 
    if len(items) > 0 and x < len(items):
        print(items[x])
    else:
        print("None")
items = ["piglet", "pooh", "roo", "rabbit"]
x = 2
get_item(items, x)

items = ["piglet", "pooh", "roo", "rabbit"]
x = 5
get_item(items, x)

#--------------Question 5--------------
def sum_honey(hunny_jars):
    total = 0
    for hunny in hunny_jars:
        total += hunny
    print(total)

hunny_jars = [2, 3, 4, 5]
sum_honey(hunny_jars)

hunny_jars = []
sum_honey(hunny_jars)

#--------------Question 6--------------
"""
Help Winnie the Pooh double his honey! Write a function doubled() 
that accepts a list of integers hunny_jars as a parameter and 
multiplies each element in the list by two. 
Return the doubled list.
"""
def doubled(hunny_jars):
    doubled_list = []
    for hunny in hunny_jars:
        doubled_list.append(hunny * 2)
    return doubled_list

hunny_jars = [1, 2, 3]
print(doubled(hunny_jars))

#--------------Question 7--------------
"""
Winnie the Pooh and his friends are playing a game 
called Poohsticks where they drop sticks in a stream 
and race them. They time how long it takes each player's 
stick to float under Poohsticks Bridge to score each round.

Write a function count_less_than() to help Pooh and his 
friends determine how many players should move on to the next 
round of Poohsticks. count_less_than() should accept a list 
of integers race_times and an integer threshold and return the 
number of race times less than threshold.
"""

def count_less_than(race_times, threshold): 
    count = 0
    for time in race_times:
        if time < threshold:
            count += 1
    return count

race_times = [1, 2, 3, 4, 5, 6]
threshold = 4
print(count_less_than(race_times, threshold))

race_times = []
threshold = 4
print(count_less_than(race_times, threshold))

#--------------Question 8--------------
"""
Write a function print_todo_list() that accepts a list of 
strings named tasks. The function should then number and 
print each task on a new line using the format:

Pooh's To Dos:
1. Task 1
2. Task 2
...
"""
def print_todo_list(tasks):
    print("Pooh's To Dos:")
    for i in range(len(tasks)):
        print(f"{i+1}. {tasks[i]}")

tasks = ["Count all the bees in the hive", "Chase all the clouds from the sky", "Think", "Stoutness Exercises"]
print_todo_list(tasks)

tasks = []
print_todo_list(tasks)
    
#--------------Question 9--------------
"""
Situation: Rabbit is very particular about his belongings and wants to 
own an **even** number of each thing he owns. 

Things to do: Write a function can_pair()
- accepts a list of integers item_quantities. 
- Return True if each number in item_quantities is even. 
- Return False otherwise.
"""
def can_pair(item_quantities): 
    for item in item_quantities:
        if item % 2 != 0:
            return False
    return True

item_quantities = [2, 4, 6, 8]
print(can_pair(item_quantities))

item_quantities = [1, 2, 3, 4]
print(can_pair(item_quantities))

item_quantities = []
print(can_pair(item_quantities))

#--------------Question 10--------------
"""
Piglet's has collected a big pile of his favorite food, 
haycorns, and wants to split them evenly amongst his friends. 

Write a function split_haycorns() 
- help Piglet determine the number of ways he can split his 
haycorns into even groups. split_haycorns() accepts a positive 
integer quantity as a parameter
returns a list of all divisors of quantity.
"""
def split_haycorns(quantity):
    divisors = []
    for i in range(1, quantity + 1):
        if quantity % i == 0:
            divisors.append(i)
    return divisors

quantity = 6
print(split_haycorns(quantity))

quantity = 1
print(split_haycorns(quantity))

#--------------Question 11--------------
"""
Signs in the Hundred Acre Wood have been losing letters as 
Tigger bounces around stealing any letters he needs to spell 
out his name. 

Write a function tiggerfy()
- accepts a string s,

- returns a new string with the letters t, i, g, e, 
and r removed from it.

"""
def tiggerfy(s):
    result = ""
    for char in s:
        if char.lower() not in "tiger":
            result += char
    return result

s = "suspicerous"
print(tiggerfy(s))

s = "Trigger"
print(tiggerfy(s))

s = "Hunny"
print(tiggerfy(s))

#--------------Question 12--------------
"""
Pooh, Piglet, and Roo are looking for thistles to gift their 
friend Eeyore. 

Write a function locate_thistles()

input: takes in a list of strings items

output: returns a list of the indices of any elements with value "thistle". 

constraints: The indices in the resulting list should be ordered 
from least to greatest. 

Implementation: 
1. for loop with range() or enumerate() 
2. empty list to store indices
3. if statement to check whether thistle or not. 
"""
def locate_thistles(items):
    thistle_indices = []
    for index,value in enumerate(items): 
        if value == "thistle": 
            thistle_indices.append(index)
    return thistle_indices

items = ["thistle", "stick", "carrot", "thistle", "eeyore's tail"]
print(locate_thistles(items))

items = ["book", "bouncy ball", "leaf", "red balloon"]
print(locate_thistles(items))
