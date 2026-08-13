from random import randint
from datetime import datetime, timedelta
c = randint(1,101)


print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")


print("Please select the difficulty level:")

print("1. Easy (10 chances)")
print("2. Medium (5 chances)")
print("3. Hard (3 chances)")


b = { 1 : "Easy", 2 : "Medium", 3 : "Hard"}
b1 = { 1 : 10, 2 : 5, 3 : 3}


while True:
    try:
        a = int(input())
        if a in [1, 2, 3]:
            break
        print("Error, please number in [1,2,3]")
    except ValueError:
        print("ValueError, retry")

print(f"Enter your choice {a}")


print(f"Great! You have selected the {b[a]} difficulty level.")

c1 = int(input("Guess the number : "))
count = 1

current_datetime1 = datetime.now()
second1 = current_datetime1.second


while c1 != c:
   
    if count >= b1[a]:
        print("You lose")
        break
        
    if c > c1 :
        print(f"Incorrect! The number is greater than {c1}.")
        
    else:
        print(f"Incorrect! The number is less than {c1}.")

    try:
            c1 = int(input("\nGuess the number : "))
    except ValueError:
            print("\nValueError, retry")
            count -=1
    count += 1
    


current_time2 = datetime.now()
second2 = current_time2.second
second = second2 - second1

print(f"You guessed the number for {second}с")
if c1 == c and count <= b1[a]:
    print(f"Congratulations! You guessed the correct number in {count} attempts.\n")
    print(f"You guessed the number for {second}с")
