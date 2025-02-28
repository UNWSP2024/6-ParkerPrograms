# Nathan Parker
# 2/28/25
# Program #1: Random Dice

#import the random module
import random

#define the main function
def main():
    #set the running total to 0
    running_total = 0

    #call the function to roll the dice 100 times
    for number in range(100):
        sum_of_dice = randDice()
        running_total += sum_of_dice

    #calculate the average
    average = running_total / 100

    #display the average
    print(f'The average of 100 rolls is {average:.2f}.')

#define a function that finds the sum of two random numbers to represent rolling two dice
def randDice():
    num_1 = random.randint(1,6)
    num_2 = random.randint(1,6)
    sum = num_1 + num_2
    return sum

#call the main function
main()
