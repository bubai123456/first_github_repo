from random import randint

a = randint(1,99); t = 10; i = 1

def set_difficulty():
    global t
    difficulty = input("Set the difficulty 'e','m','h': ")
    if difficulty == 'e': t = 10
    elif difficulty == 'm': t = 7
    elif difficulty == 'h': t = 5
    else:
        print('Invalid input! Try [e, m, h] to set difficulty.')
        set_difficulty()

def restart():
    global a,i
    inp = input("To play again write 'y': ")
    if inp == 'y':
        a = randint(1,99); i = 1
        set_difficulty()
        return True
    else: print('See you later!')

print('Guess any number between 1 to 100!')
set_difficulty()

while True:
    try:
        x = int(input(f'Enter number({t+1-i} tries): '))
    except:
        print('Invalid input! Please enter an integer number.')
        continue
    if not 0 < x < 100:
        print ('Integer must be between 1 and 100.')
        #if restart (): continue
        #else: break
    elif x == a:
        print(f'Correct! You got it in {i} tries.')
        if restart(): continue
        else : break
    elif i == t:
        print(f'Game Over! It was {a}.')
        if restart(): continue
        else: break
    elif x < a: print('Try larger!'); i += 1
    elif x > a: print('Try smaller!'); i += 1




