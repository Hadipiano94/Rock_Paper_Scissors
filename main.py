import random
import graphics


user_choice = int(input('What do you choose? \n0 = Rock \n1 = Paper \n2 = Scissors\n'))
computer_choice = random.randint(0, 2)
print(f'Your choice:\n{graphics.list_rps[user_choice]}')
print(f'Computer\'s choice:\n{graphics.list_rps[computer_choice]}')
if user_choice == computer_choice:
    print('Draw!')
elif user_choice == 0 and computer_choice == 2:
    print('You WON!')
elif user_choice == 1 and computer_choice == 0:
    print('You WON!')
elif user_choice == 2 and computer_choice == 1:
    print('You WON!')
else:
    print('You LOSTTT!!!!!')
