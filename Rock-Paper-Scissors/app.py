import random


def game():
    items = ['ROCK', 'PAPER', 'SCISSORS']
    play = True
    points = 0
    while(play):
        comp_choice = random.choice(items)
        print('Select any from "ROCK", "PAPER", "SCISSORS" ')
        user_choice = input('Enter your choice: ').upper()
        
        print('Your choice: ',user_choice)
        print('Computer choice: ',comp_choice)

        if user_choice == comp_choice:
            print('Draw')
            print('Score: ',points)

            n = input('Still wants to play?(y/n): ')

            if (n == 'y' or n == 'Y'):
                play = True
            else:
                play = False
                print('----Game Over----')
                print('Final score: ', points)

        elif user_choice == 'ROCK':
            if comp_choice == 'SCISSORS':
                print('You Win')
                points = points + 10
                print('Score: ',points)

                n = input('Still wants to play?(y/n): ')
                if (n == 'y' or n == 'Y'):
                    play = True
                else:
                    play = False
                    print('----Game Over----')
                    print('Final score: ', points)

            else:
                print('You Lose')
                points = points - 10
                print('Score: ',points)

                n = input('Still wants to play?(y/n): ')
                if (n == 'y' or n == 'Y'):
                    play = True
                else:
                    play = False
                    print('----Game Over----')
                    print('Final score: ', points)

        elif user_choice == 'PAPER':
            if comp_choice == 'ROCK':
                print('You Win')
                points = points + 10
                print('Score: ',points)

                n = input('Still wants to play?(y/n): ')
                if (n == 'y' or n == 'Y'):
                    play = True
                else:
                    play = False
                    print('----Game Over----')
                    print('Final score: ', points)

            else:
                print('You Lose')
                points = points - 10
                print('Score: ',points)

                n = input('Still wants to play?(y/n): ')
                if (n == 'y' or n == 'Y'):
                    play = True
                else:
                    play = False
                    print('----Game Over----')
                    print('Final score: ', points)

        elif user_choice == 'SCISSORS':
            if comp_choice == 'PAPER':
                print('You Win')
                points = points + 10
                print('Score: ',points)

                n = input('Still wants to play?(y/n): ')
                if (n == 'y' or n == 'Y'):
                    play = True
                else:
                    play = False
                    print('----Game Over----')
                    print('Final score: ', points)

            else:
                print('You Lose')
                points = points - 10
                print('Score: ',points)

                n = input('Still wants to play?(y/n): ')
                if (n == 'y' or n == 'Y'):
                    play = True
                else:
                    play = False
                    print('----Game Over----')
                    print('Final score: ', points)

                        
    

    
game()