#guessing number game
# import random

# def guessing_game():

#     answer = random.randint(0,100)


# while True:
#     user_guess = int(input())
#     if user_guess == answer:
#         print('bingo')
#         break
#     if user_guess < answer:
#         print('too low')
#     else:
#         print("too high")

# guessing_game()


# mysum solution


def mysum(*numbers):
    output = 0 #at the start of operation we iter it to 0
    for number in numbers: #and than for loop we take each element
        output += number
    return output

print(mysum(10,20,30,40))