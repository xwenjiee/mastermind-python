
# Game banner and instructions
def banner():
    print('--------------------------------------------------------------------------------')
    print("Welcome to Wen Jie's Mastermind Game!")
    print('--------------------------------------------------------------------------------')
    print('How the game works:')
    print('1. There are a total of 4 colours: Red, Yellow, Green, and Blue in random sequence.')
    print('2. Each colour may appear more than once in the sequence.')
    print('3. You need to guess the sequence correctly in order to win!')
    print("4. Don't worry, you may have unlimited guesses.")
    print("5. For your convenience, you may enter 'r' for Red, 'y' for Yellow, 'g' for Green, and 'b' for Blue.")
    print()
    print('   Good luck, have fun!')
    print('--------------------------------------------------------------------------------')

# End of the game
def end():
    
    print('--------------------------------------------------------------------------------')
    print('Game closed.')
    print('--------------------------------------------------------------------------------')
    
# Check if letter entered is valid and assign the full name of the colour accordingly
def colourCheck(colour,invalidOrNot):

    if colour.lower() == 'r':
        colour = 'Red'
        invalidOrNot = False
        
    elif colour.lower() == 'y':
        colour = 'Yellow'
        invalidOrNot = False
        
    elif colour.lower() == 'b':
        colour = 'Blue'
        invalidOrNot = False
        
    elif colour.lower() == 'g':
        colour = 'Green'
        invalidOrNot = False

    # Display error message if input other than r/y/g/b is entered and ask user to input again    
    else:
        print('Invalid guess!')
        
    return[colour, invalidOrNot]

start = True

while start == True:
    
    # Let the player choose if they want to start the game
    print('Do you wish to start playing?')
    start_game = input("Type 'Y' for Yes and 'N' for No [Y/N]: ")
    
    if start_game.upper()=='Y':
        break
    elif start_game.upper()=='N':
        break
    
    # Display error message if input other than Y/N is entered and ask user to input again
    else:
        print()
        print('Invalid selection!')

# Start game if user enters 'Y'
if start_game.upper()=='Y':
    
    restart = 'Y'
    
    # start game
    while restart.upper() == 'Y':

        # List of possible colours
        colour_list = ['Red','Yellow','Green','Blue']

        # Generate random sequence of colours
        import random
  
        correctAnswer = random.choices(colour_list, k=4)
        banner()
        guesses = []
        tries = 0
        print('Start guessing!')

        # Loop if the player's guess is not correct
        while guesses!= correctAnswer:

            print()
            # Ask the player to guess the sequence
            invalid = True
            while invalid == True:
                
                firstColour = input('Guess the first colour: ')
                i = colourCheck(firstColour,invalid)
                firstColour = i[0]
                invalid = i[1]
                
            invalid2 = True
            while invalid2 == True:
                
                secondColour = input('Guess the second colour: ')
                i = colourCheck(secondColour,invalid2)
                secondColour = i[0]
                invalid2 = i[1]
            
            invalid3 = True
            while invalid3 == True:
                    
                thirdColour = input('Guess the third colour: ')
                i = colourCheck(thirdColour,invalid3)
                thirdColour = i[0]
                invalid3 = i[1]
                
            invalid4 = True
            while invalid4 == True:
                    
                fourthColour = input('Guess the fourth colour: ')
                i = colourCheck(fourthColour,invalid4)
                fourthColour = i[0]
                invalid4 = i[1]
                
            guesses = [firstColour, secondColour, thirdColour, fourthColour]

            # Show the player their guesses
            print()
            print('Your guess was:',guesses)
            print()
            
            correctGuess = 0
            wrongGuess = 0

            # Show the player which colour they got correct and wrong
            for i in range(0,4):
                if i == 0:
                    position = 'first'
                elif i == 1:
                    position = 'second'
                elif i == 2:
                    position = 'third'
                elif i == 3:
                    position = 'fourth'

                if guesses[i] == correctAnswer[i] :

                    print('The '+position+' colour is correct.')
                    correctGuess +=1
                        
                elif (guesses[i]!= correctAnswer[i]):

                    print('The '+position+' colour is wrong.')
                    wrongGuess +=1
                    
            # Show the player the total number of correct and wrong guesses they got
            print()                                   
            print('Correct guesses:', correctGuess)
            print('Wrong guesses:', wrongGuess)
            print()
            print('--------------------------------------------------------------------------------')
            
            tries +=1
            
        # Display congratulations message when the player has guessed the sequence correctly
        # along with the number of tries they took
        print()
        print('Congratulations! You have guessed the sequence correctly!')
        print('You took a total of',tries,'try(s).')
        print()
        
        # Ask if the player wants to play again
        sure = False
        while sure == False:
            askRestart = input('Do you wish to play again? [Y/N]: ')
            
            if askRestart.upper() == 'Y' or askRestart.upper() == 'N':
                
                while askRestart.upper() == 'Y':
                    
                    # Reconfirm the player's selection
                    reconfirm = input('Are you sure? [Y/N]: ')
                    if reconfirm.upper() == 'Y':
                        sure = True
                        break
                    
                    elif reconfirm.upper() == 'N':
                        break

                    # Display error message if input other than Y/N is entered and ask user to input again
                    else:
                        print()
                        print('Invalid selection!')
                        
                while askRestart.upper() == 'N':

                    # Reconfirm the player's selection
                    reconfirm = input('Are you sure? [Y/N]: ')
                    if reconfirm.upper() == 'Y':
                        restart = 'N'
                        sure = True
                        break
                    
                    elif reconfirm.upper() == 'N':
                        break
                    
                    # Display error message if input other than Y/N is entered and ask user to input again
                    else:
                        print()
                        print('Invalid selection!')
                        
            # Display error message if input other than Y/N is entered and ask user to input again
            else:
                print()
                print('Invalid selection!')
        
    end()
    
# Close the game if the player chooses not to play    
elif start_game.upper()=='N':
    end()  
