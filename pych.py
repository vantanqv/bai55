import random

guessesTaken = 0

print('Xin chao! Ban ten la gi?')
myName = input()

number = random.randint(1, 20)
print('Hey, ' + myName + ', to dang nghi 1 con so tu 1 cho den 20')

while guessesTaken < 6:
    print('Moi ban doan.')
    guess = input()

    guess = int(guess)
    guessesTaken += 1

    if guess < number:
        print('Ban doan nho hon roi.')
    elif guess > number:
        print('Ban doan lon hon roi.')
    else:
        break

if guess == number:
    print('Ban doan dung roi! Ban doan mat ' + str(guessesTaken) + " de doan.")
else:
    print('Ban doan sai roi. Con so to dang nghi trong dau la ' + str(number) + " co.")

