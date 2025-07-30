# Guess My Age
secret_age = 38
while True:
    guess = input ("Guess my age : ")
    if not guess.isdigit():
        print ("invalid input! please enter a number ")
        continue
    guess = int(guess)
    if guess > secret_age :
        print ("Too High! Try Again")
    elif guess < secret_age :
        print ("Too Low! Try Again")
    else:
         print ("You got it right ol' chap!") 
         break
