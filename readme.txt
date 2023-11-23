Last Updated: 2023

This readme covers all projects in this practiceproject repository, one .py file at a

Peter

_______________

8QueensProblemGame.py

N-Queens Problem Solver

Introduction

This Python script provides a solution to the N-Queens problem, a classic chess puzzle where N queens must be placed on an N×N chessboard in such a way that no two queens threaten each other. The script outputs all possible solutions for a given board size.

Usage

1. Set the BOARD_SIZE variable to the desired size of the chessboard. For example, if you want to solve the 8-Queens problem, set BOARD_SIZE = 8.

BOARD_SIZE = 8

2. Run the script.

python n_queens_solver.py

3. The script will print all solutions for the specified board size, with each solution represented as a list of coordinates (row, column) for each queen.

Code Explanation

- under_attack(col, queens): Checks if placing a queen in a given column col will result in an attack. It considers both diagonals and the same row.

- solve(n): Recursively finds all solutions for placing n queens on the chessboard. It uses backtracking to explore all possibilities.

- for answer in solve(BOARD_SIZE): print(answer): Prints all solutions for the specified BOARD_SIZE.

Example Output

For BOARD_SIZE = 8, the output will contain all unique solutions for placing 8 queens on an 8×8 chessboard.

[(1, 1), (2, 5), (3, 8), (4, 6), (5, 3), (6, 7), (7, 2), (8, 4)]
[(1, 1), (2, 6), (3, 8), (4, 3), (5, 7), (6, 4), (7, 2), (8, 5)]
...

Feel free to modify the script for different board sizes or integrate it into other projects.

_____________________

app.py

# Loop Program

This simple Python script demonstrates a loop that increases a value until it reaches 10 and then decreases it. The user is prompted to continue the loop or stop the process.

## Usage

1. Run the script.

python loop_program.py

2. The program will display the value of x as it increments until it reaches 10. Afterward, it will decrease by a specified reduction value.

## Code Explanation

- The script initializes variables for increment (diff) and reduction (reduction) values.

- The valueChange function increments the global variable x until it reaches 10, then decreases it by the reduction value.

- The decide function prompts the user to continue the loop (Y or y) or stop the process (N or n). Invalid responses trigger an error message.

## Example Output

Hello, welcome to this program that doesn't fucking work

The Value of X is currently: 1
The Value of X is currently: 2
...
The Value of X is currently: 10
The Value of X is above 10, specifically it is: 11
X has been reduced by: 15, The Value of X is currently: -4
Do you wish to run the loop again, type Y or N:

Feel free to modify the script for different increment and reduction values or integrate it into other projects.


_________

area_calculator.py

Shape Area Calculator

This Python script calculates the area of a shape specified by the user. The supported shapes are rectangle, circle, and triangle.

Usage

1. Run the script.

python shape_area_calculator.py

2. The program will prompt you to choose a shape (rectangle, circle, or triangle) and input the required parameters.

3. The script will calculate and display the area of the chosen shape.

Functions

- area_of_rectangle(length, width): Calculates the area of a rectangle.
- area_of_circle(radius): Calculates the area of a circle.
- area_of_triangle(base, height): Calculates the area of a triangle.

Main Program

1. The user is prompted to choose a shape (rectangle, circle, or triangle).

2. Based on the chosen shape, the script prompts for the necessary parameters (length and width for a rectangle, radius for a circle, base and height for a triangle).

3. The script then calculates and displays the area of the chosen shape.

4. If an invalid shape is chosen, the script displays an error message.

Example

Choose a shape (rectangle, circle, or triangle): rectangle
Enter the length: 5
Enter the width: 3
The area of the rectangle is: 15.0

Feel free to modify the script for additional shapes or integrate it into other projects.

_______________

count_evens.py

Count Evens in Array

This Python script counts the number of even integers in a given array.

Usage

1. Copy the code.

python count_evens.py

2. The program defines a function count_evens(lst) that takes a list as input and prints the count of even numbers in the list.

3. An example list list_a is provided, and the count_evens function is called with this list.

4. The script prints the result, indicating the number of even numbers in the provided list.

Code Explanation

- The count_evens function initializes a counter and iterates through the given list, checking for even numbers.

- For each even number found, the counter is incremented.

- The final count is printed to the console.

Example Output

There are 6 even numbers in this list

Feel free to modify the script or integrate it into other projects.


_________________

count_vowels_and_reverse_string.py

String Operations

This Python script performs operations on a user-entered string. It counts the number of vowels and reverses the string.

Usage

1. Copy the code.

python string_operations.py

2. The program defines two functions:
   - count_vowels(input_string): Counts the number of vowels in a given string.
   - reverse_string(input_string): Reverses the characters in a string.

3. The main program prompts the user to enter a string.

4. The script uses the count_vowels function to count the vowels and the reverse_string function to reverse the string.

5. The results, including the original string, vowel count, and reversed string, are printed to the console.

Functions

count_vowels(input_string)

Counts the number of vowels (case-insensitive) in the input string.

reverse_string(input_string)

Reverses the characters in the input string.

Example Output

Enter a string: Hello, World!
Original String: Hello, World!
Vowel Count: 3
Reversed String: !dlroW ,olleH

Feel free to modify the script or integrate it into other projects.


______________

double_char.py

Double Character String

This Python script doubles every character in a given string.

Usage

1. Copy the code.

python double_char.py

2. The program defines a function double_char(str) that takes a string as input and returns a new string where each character in the original string is doubled.

3. The function is then called with an example string "ABC".

4. The script prints the result, showing the string with each character doubled.

Function

double_char(str)

Returns a new string where each character in the input string is doubled.

Example Output

Input String: ABC
Doubled String: AABBCC

Feel free to modify the script or integrate it into other projects.


_____________

EvenNumbers.py

Even Numbers Counter

This Python script prints even numbers between 1 and 10 and then displays the count of even numbers.

Usage

1. Copy the code.

python even_numbers_counter.py

2. The program defines a function main() that iterates through numbers from 1 to 10, prints the even numbers, and counts their occurrences.

3. The script is executed by calling the main() function.

4. The script prints the even numbers and the count of even numbers.

Function

main()

Iterates through numbers from 1 to 10, prints even numbers, and counts their occurrences.

Example Output

2
4
6
8
There are 4 even numbers

Feel free to modify the script or integrate it into other projects.


______

filter_add_num.py

Even Numbers Filter

This Python script creates and returns a new list containing only the even numbers from an initial list.

Usage

1. Copy the code.

python even_numbers_filter.py

2. The program defines a function filter_odd_numbers(input_list) that takes a list as input and returns a new list containing only the even numbers from the input list.

3. The main program initializes an example list initial_list.

4. The script uses the filter_odd_numbers function to create a new list containing only the even numbers.

5. The results, including the original list and the filtered list with even numbers only, are printed to the console.

Function

filter_odd_numbers(input_list)

Returns a new list containing only the even numbers from the input list.

Example Output

Original List: [1, 5, 8, 3, 10, 7, 12]
Filtered List (Even Numbers Only): [8, 10, 12]

Feel free to modify the script or integrate it into other projects.


________________________

First_last6.py

# First and Last Appearance of 6 Checker

This Python script checks if the number 6 appears as either the first or last number in an array of integers.

Usage

1. Copy the code.

python six_appearance_checker.py

2. The program defines a function first_last(lst) that takes an array of integers as input and returns True if 6 appears as either the first or last number in the array, otherwise False.

3. The script initializes four example lists: list_a, list_b, list_c, and list_d.

4. The script uses the first_last function to check if 6 appears as either the first or last number in each list.

5. The results are printed to the console.

Function

first_last(lst)

Returns True if 6 appears as either the first or last number in the array, otherwise False.

Example Output

List A: [3, 6, 4, 7, 6]
Result A: True

List B: [6, 6, 4, 7, 0]
Result B: True

List C: [3, 6, 4, 7, 4]
Result C: True

List D: [3, 6, 4, 7, 2]
Result D: True

Feel free to modify the script or integrate it into other projects.


_____________

guessingGame.py

Number Guessing Game

This Python script implements a simple number guessing game. The computer randomly selects a number between 1 and 20, and the player has 6 attempts to guess it.

Usage:

1. Copy the code.

```bash
python number_guessing_game.py



__________________

HellName.py

# Personalized Greeting

This Python script prompts the user for their name and then generates a personalized greeting. The greeting is of the form "Hello, [Name]!".

Usage:

1. Copy the code.

python personalized_greeting.py

2. The program prompts the user to enter their name.

3. The user inputs their name.

4. The program prints a personalized greeting in the format "Hello, [Name]!"

Example Output:

What is your name? Alice
Hello, Alice!

Feel free to modify the script or integrate it into other projects.


________________________

list_manipulator.py

# List Modification

This Python script modifies a list with the following operations:
1. Add 10 to the end of the list.
2. Remove the first occurrence of 5.
3. Double each element in the list.

## Usage

1. Copy the code.

python modify_list.py

2. The program initializes an example list.

3. The `modify_list` function is applied to perform the specified operations.

4. The program prints the original and updated lists.

## Example Output

Original List: [2, 5, 8, 3, 5, 7]
Updated List: [4, 16, 6, 14, 20, 10]

Feel free to modify the script or integrate it into other projects.


____________________


# maze.py - under construction


___________________

reverse_and_capitalise.py

Reverse and Capitalize String

This Python script takes a user input string, reverses it, and then converts it to uppercase.

Usage:

1. Copy the code.

2. Run the script:

   python reverse_and_capitalize.py

3. The program prompts the user to enter a string.

4. The `reverse_and_capitalize` function is applied to reverse and capitalize the input string.

5. The program prints the original and reversed capitalized strings.

Example Output:

Enter a string: example
Original String: example
Reversed String: ELPMAXE

Feel free to modify the script or integrate it into other projects.


________________

rock_paper_scissors.py


Rock, Paper, Scissors Game

This Python script is a simple implementation of the classic Rock, Paper, Scissors game.

Usage:

1. Copy the code.

2. Run the script:

   python rock_paper_scissors.py

3. The program prompts the user to choose Rock (1), Paper (2), Scissors (3), or Exit (4).

4. The user's choice is compared with the randomly generated opponent's choice.

5. The winner is determined based on the game rules.

6. The user can play multiple rounds until choosing to exit.

Note:

- If the user selects Exit (4), the game terminates.

Feel free to modify the script or integrate it into other projects.


_________________

# Sleepin.py - under construction

_________________

star_wars_names.py

Star Wars Name Generator

This Python program converts your name into a Star Wars-themed name by providing background information such as Religion, Home Planet, and Lightsaber Color.

Instructions:

1. Run the script:

   python star_wars_name_generator.py

2. Enter your full name when prompted.

3. The program generates your Star Wars name based on the first letter of your name and its length.

4. It assigns a religious affiliation (Jedi, Sith, or None), a Lightsaber color, and a home planet.

5. The results are displayed, including your original name, Star Wars name, religion, Lightsaber color, and home planet.

6. Optionally, you can try another name or exit the program.

Note:

- The Lightsaber extension (turtle graphics) is currently disabled (commented out). Uncomment the relevant lines in the extend_saber function to enable it.

Feel free to modify the script or integrate it into other projects.


______________

StinrgTimes.py  <-- Yes, this file name is mistyped, I was tired...

String Times Program

This Python script takes a word and a non-negative integer as input and returns a larger string than the original by repeating the word.

Instructions:

1. Run the script:

   python string_times.py

2. Enter a word when prompted.

3. Enter a non-negative integer indicating how many times to repeat the word.

4. The program will display the resulting larger string.

Feel free to use this script in your projects or modify it as needed.


_______________________

test_score_calculator.py

Grade Calculator Program

This Python script calculates the average score from three tests and assigns a grade based on the result.

Instructions:

1. Run the script:

   python grade_calculator.py

2. Enter the quiz score when prompted.

3. Enter the midterm score when prompted.

4. Enter the final score when prompted.

5. The program will display the calculated average score.

6. The program will display the corresponding grade based on the average score.

Feel free to use this script in your educational activities or modify it as needed.


