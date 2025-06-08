#--------------Question 1--------------
"""
Write a function reverse_sentence() that 

input: 
takes in a string sentence 

output: 
returns the sentence with the order of the words reversed. 

constraints: 
The sentence will contain only alphabetic characters and spaces 
to separate the words. 

edge case: 
If there is only one word in the sentence, 
the function should return the original string. 
"""

def reverse_sentence(sentence): 
    words = sentence.split()
    reversed_words = reversed(words)
    return ' '.join(reversed_words)

sentence = "tubby little cubby all stuffed with fluff"
print(reverse_sentence(sentence))

sentence = "Pooh"
print(reverse_sentence(sentence))

#--------------Question 2--------------
def goldilocks_approved(nums):
    smallest = min(nums)
    largest = max(nums)

    if len(nums) < 3: 
        return -1

    for num in nums: 
        if num != smallest and num != largest: 
            return num

nums = [3, 2, 1, 4]
print(goldilocks_approved(nums))
nums = [1, 2]
print(goldilocks_approved(nums))
nums = [2, 1, 3]
print(goldilocks_approved(nums))

#--------------Question 3--------------
"""
approach: 
1. create a new list called removed to store the order 
2. while hunny jar size is empty: 
    - find the min value min()
    - append that value to removed
    - remove the value from hunny jar size
3. return removed
"""
def delete_minimum_elements(hunny_jar_sizes):
    removed = []
    while hunny_jar_sizes:  # While the list is not empty
        smallest = min(hunny_jar_sizes)
        removed.append(smallest)
        hunny_jar_sizes.remove(smallest)  # Remove only one occurrence
    return removed
        
hunny_jar_sizes = [5, 3, 2, 4, 1]
print(delete_minimum_elements(hunny_jar_sizes))
hunny_jar_sizes = [5, 2, 1, 8, 2]
print(delete_minimum_elements(hunny_jar_sizes))
#--------------Question 4--------------
"""
input: integer num

output: returns the sum of num's digits
"""
def sum_of_digits(num): 
    total = 0
    while num > 0: 
        digit = num % 10    # get the last digit
        total += digit      # add to total 
        num = num // 10     # remove the last digit 
    return total

num = 423
print(sum_of_digits(num))

num = 4
print(sum_of_digits(num))

#--------------Question 5--------------
def final_value_after_operations(operations):
    tigger = 1
	
    for operation in operations:
        if operation == "bouncy" or operation == "flouncy": 
            tigger += 1
        else: 
            tigger -= 1
    return tigger

operations = ["trouncy", "flouncy", "flouncy"]
print(final_value_after_operations(operations))

operations = ["bouncy", "bouncy", "flouncy"]
print(final_value_after_operations(operations))

#--------------Question 6--------------
def is_acronym(words, s):
    acronym = ""

    for word in words: 
        acronym += word[0]
    return acronym == s
            

words = ["christopher", "robin", "milne"]
s = "crm"
print(is_acronym(words, s))

#--------------Question 7--------------
"""
Write a function make_divisible_by_3() 

input: accepts an integer array nums. 

In one operation, you can add or subtract 1 from any element of nums. 

output: Return the minimum number of operations to make all elements of nums divisible by 3. 

GOAL: 
- for each num in nums: check if it's divisible by 3. 
- if not: either add or subtract 1 to make it divisible. 
- sometimes you will need to do that twice ( 1->0, 2->3)

step by step thinking: 
1. for num in nums: num%3
2. if already 0, do nothing. 
3. if 1 or 2, + or - 1
    - num % 3 == 1 --> (-1)
    - num % 3 == 2 --> (+1)
"""
def make_divisible_by_3(nums):
    operation = 0
    for num in nums: 
        remainder = num % 3

        if remainder == 1: 
            operation += 1
        elif remainder == 2: 
            operation  += 1
    return operation

nums = [1, 2, 3, 4]
print(make_divisible_by_3(nums))

nums = [3, 6, 9]
print(make_divisible_by_3(nums))

#--------------Question 8--------------
"""
Given two lists lst1 and lst2, 

write a function exclusive_elemts() 

returns a new list that contains the elements which 
are in lst1 but not in lst2 and the elements that 
are in lst2 but not in lst1.

"""
def exclusive_elemts(lst1, lst2):
    exclusive_elements = []

    for item in lst1:
        if item not in lst2: 
            exclusive_elements.append(item)
    
    for item in lst2: 
        if item not in lst1: 
            exclusive_elements.append(item)

    return exclusive_elements

lst1 = ["pooh", "roo", "piglet"]
lst2 = ["piglet", "eeyore", "owl"]
print(exclusive_elemts(lst1, lst2))
lst1 = ["pooh", "roo"]
lst2 = ["piglet", "eeyore", "owl", "kanga"]
exclusive_elemts(lst1, lst2)

lst1 = ["pooh", "roo", "piglet"]
lst2 = ["pooh", "roo", "piglet"]
exclusive_elemts(lst1, lst2)

#--------------Question 9--------------
"""
Write a function merge_alternately() 

input: accepts two strings word1 and word2. 

Merge the strings by adding letters in alternating order, 
starting with word1. 

If a string is longer than the other, 
append the additional letters onto the end of the merged string. 

implementation: 
1. merged = []
2. for loop both strings up to the len of shorter one
    - add one character from word1 then word2
3. if one word is longer, append to the rest
"""
def merge_alternately(word1, word2):
    merged = []
    min_len = min(len(word1), len(word2))

    for i in range(min_len): 
        merged.append(word1[i])
        merged.append(word2[i])

    merged.append(word1[min_len:])
    merged.append(word2[min_len:])

    return ''.join(merged)

word1 = "wol"
word2 = "oze"
print(merge_alternately(word1, word2))
word1 = "hfa"
word2 = "eflump"
merge_alternately(word1, word2)

word1 = "eyre"
word2 = "eo"
merge_alternately(word1, word2)

#--------------Question 10--------------
"""
Eeyore has collected two piles of sticks to rebuild his house and 
needs to choose pairs of sticks whose lengths are the right proportion. 

Write a function good_pairs() 

- accepts two integer arrays pile1 and pile2 where each integer represents the length of a stick. 
- The function also accepts a positive integer k. 

- The function should return the number of good pairs.

A pair (i, j) is called good if pile1[i] is divisible by pile2[j] * k. Assume 0 <= i <= len(pile1) - 1 and 0 <= j <= len(pile2) - 1

how to think: 
1. use a for loop over pile1
2. inside loop over pile2
3. for each pair (i,j), check if pile1[i] is divisible by pile2[j] * k
4. if so, increase a count 
"""

def good_pairs(pile1, pile2, k): 
    count = 0

    for i in pile1: 
        for j in pile2: 
            if i % (j * k) == 0: 
                count += 1
    return count

pile1 = [1, 3, 4]
pile2 = [1, 3, 4]
k = 1
print(good_pairs(pile1, pile2, k))

pile1 = [1, 2, 4, 12]
pile2 = [2, 4]
k = 3
print(good_pairs(pile1, pile2, k))
