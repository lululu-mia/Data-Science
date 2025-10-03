#1. Write a program that takes a word as an input and print the number of vowels in the word.
def count_vowels():
    word = input("Enter a word: ")
    vowels = set("aeiou")
    count = sum(1 for ch in word.lower() if ch in vowels)
    print(f"The number of vowels in '{word}' is {count}")
count_vowels()

#2. Iterate through the following list of animals and print each one in all caps.
#animals=['tiger', 'elephant', 'monkey', 'zebra', 'panther']
def print_animals():
    animals = ['tiger', 'elephant', 'monkey', 'zebra', 'panther']
    for a in animals:
        print (a.upper())
print_animals()

#3. Write a program that iterates from 1 to 20, printing each number and whether it's odd or even.
def print_nums():
    for i in range(1,21):
        if i % 2 == 0:
            print(f"{i} is even")
        else:
            print(f"{i} is odd")
print_nums()

#4. Write a program to check if a string is a palindrome or not.
def palindrome():
    s = input("Enter a string: ")
    if s == s[::-1]:
        print(f"{s} is palindrome")
    else:
        print(f"{s} is not palindrome")
palindrome()

#5. Write a function sum_of_integers(a, b) that takes two integers as input from the user and returns their sum.
def sum():
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    print(a + b)
sum()