import random
rock =''' _ _ _ _ _ 
----'_ _ _ _ _ _ _)
     (_ _ _ _ _ _)
      (_ _ _ _ _)
       (_ _ _ _)
----,_ _ _ _(_ _ _)

'''
paper = '''  _ _ _ _ _ _
----'_ _ _ _)_ _ _ _
        _ _ _ _)
      _ _ _ _)
    _ _ _ _)
---,_ _ _ _)

'''
scissers='''_ _ _ _
    ----'_ _ _'_ _ _
        _ _ _ _ _ _)
    _ _ _ _ _ _ _)
    (_ _ _ _ )
----,_ _ _ (_ _ _)

'''
game_image=[rock,paper,scissers]
user_choice=int(input('Enter Your Choice: Type 0 for Rock,1 for Pepar,2 for scissers:-'))
if user_choice > 3 or user_choice <0:
    print('You entered invalid number you lose,') 
else:
    print(game_image[user_choice])
    computer_choice=random.randint(0,2)
    print('Computer Chose')
    print(game_image[computer_choice])
    if computer_choice == user_choice:
        print('its a draw')
    elif computer_choice ==0 and user_choice==2:
        print('You Lose')
    elif user_choice ==0 and computer_choice==2:
        print('You win')
    elif computer_choice>user_choice:
        print('You Lose')
    elif user_choice>computer_choice:
        print('You win') 
