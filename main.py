#Quratul Ain
#2022
#password cracker using random

import random

print("\n\t****welcome to the password cracker****\n")
#taking input from user
user_pass=input("\n\t please enter your password :")
#storing letters of the alphabet to
password=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',]
guess=""#initialzing an empty string
#using while loop to generate many until one of them
#them matches user_pass
while(guess != user_pass):
  guess=""
  for letter in range(len(user_pass)):
    guess_letter=password[random.randint(0,25)]
    guess=str(guess_letter)+str(guess)
    #printing guessed password
    print(guess)
    #printing the matched password
    print("\n your password is", guess)
                