# ZYA KYNDER TARHATA B. RAFAEL
# 9 BERYLLIUM

# CODE 1
"""
  a. The output of the code will be:
  J
  o
  s
  e
  p
  - This is because the loop runs 5 times using indexes 0-4, so it only prints the first five characters.

  b. An "IndexError: string index out of range" error message pops up because Joseph the Dreamer only has 18 characters, 
  but the program is trying to access 20 characters.

  c. I used minimum function so the loop never goes beyond the length of the name.
"""

def greet_students(name, nChar):
    # len() gets the number of characters in the name
    # min() chooses the smaller number between the nChar and name
    for i in range(min(nChar, len(name))): 
        print(name[i])

name = input("Enter a name: ")
nChar = int(input("Enter any numeric number: "))
greet_students(name, nChar)


# CODE 2
"""
  a. The syntax error is a missing colon (:) after the for loop condition. To fix it I just simply added the colon.
  b. For that, I changed [0:nChar] to [0:i] and range(nChar) to range(nChar, 0, -1) so that I can make the name shorter each iteration.
"""
def greet_students(name, nChar):
    # Starts at nChar and decreases by 1 each iteration.
    # Less characters each loop.
    for i in range(nChar, 0 , -1):
        # This gets the characters from the beginning of the name up to index i.
        print(name[0:i])
name = input("Enter a name: ")
greet_students(name, len(name))


# CODE 3
"""
  a. The function I added is the sum_of_squares function wherein the total starts at 0 and then it loops from 1 until n which is the user's input. 
  Each iteration squares the number through i ** 2 and adds it to the total. The total will be the value to will be returned and printed.
"""
n = 0
def sum_of_squares(n):
    total = 0 # Starts at zero
    # Starts at the number 1 until the user's given number. Adds 1 per iteration.
    for i in range(1, n + 1):
        # Squares the number and adds it to the total.
        total += i ** 2
    return total
  
while n < 1 or n > 100:
    n = int(input("Enter a number between 1 and 100: "))

print("Sum of all squared numbers is" , sum_of_squares(n))
    
