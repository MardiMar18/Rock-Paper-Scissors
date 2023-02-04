#  Intro ID: 
import random 
choice_list = ["Rock","Paper","Scissors"]

rock = "Rock"        #  rock = 1 
paper = "Paper"
scissors = "Scissors"  

user_name = ""
win_count = 0 
comp_win_count = 0 
                                                                                                                       # play_again = True    # while play_again is True: 
def show_homepage():
        print("------------------------------------------")
        print("Welcome to the thrilling game of... " )  
        print(  "   Rock, Paper, Scissors! " )  
        print("------------------------------------------")

        print("------------------------------------------")
        print("| 1.    Start Game  | 2.   Exit           |")
        print("------------------------------------------")

        while True:
                home_choice = input("Brave enough to face the Computer? ")
                if home_choice == "1" or home_choice =="Start Game":
                        print("Starting Game...")
                        user_name = input("What is your name? ")
                        user_name = user_name.capitalize()
                        return user_name;
                        
                elif home_choice == "2" or home_choice =="Quit":
                        print("The almighty Computer has spared your life this time coward! ")
                        exit()

                else:
                        print("Invalid option. Please try again.")
                        continue

# Battle Sequence :
def begin_game(user_name):
        global win_count 
        global comp_win_count 

        print("------------------------------------------")
        print(f"           Good Luck, {user_name}.       ")
        print("             You're gonna need it.        ")
        print("------------------------------------------")

        print(f"1. {rock}" ) 
        print(f"2. {paper}" ) 
        print(f"3. {scissors}")
        user_choice = input(f"Choose Wisely, {user_name}. ")
        
        print(f"You have chosen {user_choice}. May the fortunes be in your favor, {user_name}.")

        while True :
                if user_choice == "1" or user_choice =="Rock":
                        user_choice = rock
                        break
            
                elif user_choice == "2" or user_choice =="Paper":
                        user_choice = paper
                        break
            
                elif user_choice == "3" or user_choice == "Scissors":
                        user_choice = scissors
                        break
            
                else:
                        print("Invalid option. Please try again.")
                        begin_game(user_name) 

        comp_choice = random.choice(choice_list)
        print(f"The Computer has chosen: {comp_choice}")
        print("3...2...1... Draw! ")

# Game Rules to determine Results + Save Score  
        if user_choice == comp_choice:
                print(f"Tie Game. Way to waste all of our time, {user_name}.")
                win_count += 0
                comp_win_count += 0
                print(f"User Win Count: {win_count} Computer Win Count: {comp_win_count}") 
            
        elif user_choice == "Rock" and comp_choice == "Scissors":
                print (f"Congrats, {user_name}! I believed in you the whole time!" )
                win_count +=1 
                print(f"User Win Count: {win_count} Computer Win Count: {comp_win_count}") 
            
        elif user_choice == "Paper" and comp_choice == "Rock":
                print (f"Congrats, {user_name}! I believed in you the whole time!" )
                win_count +=1 
                print(f"User Win Count: {win_count} Computer Win Count: {comp_win_count}") 
            
        elif user_choice == "Scissors" and comp_choice == "Paper":
                print (f"Congrats, {user_name}! I believed in you the whole time!" )
                win_count +=1  
                print(f"User Win Count: {win_count} Computer Win Count: {comp_win_count}") 


        elif user_choice == "Rock" and comp_choice == "Paper":
                print (f"Silly {user_name}... You are no match for the Computer!")
                comp_win_count +=1  
                print(f"User Win Count: {win_count} Computer Win Count: {comp_win_count}") 
             
        elif user_choice == "Paper" and comp_choice == "Scissors":
                print (f"Silly {user_name}... You are no match for the Computer!")
                print(f"User Win Count: {win_count} Computer Win Count: {comp_win_count}") 

        elif user_choice == "Scissors" and comp_choice == "Rock":
                print (f"Silly {user_name}... You are no match for the Computer!")
                print(f"User Win Count: {win_count} Computer Win Count: {comp_win_count}") 
        else:
                print(f"Error. How did you manage to mess up a game played by children, {user_name}? ")

# Replay Section :
        while(True):
                replay__choice = input("Play again? Enter 1 to replay or 2 to quit: ")
                if replay__choice == "1":
                        begin_game(user_name)
                        break

                elif replay__choice == "2":
                        print(f" ! FINAL SCORE !  User Win Count: {win_count} Computer Win Count: {comp_win_count}") 
                        print("Goodbye!")
                        exit()
                else:
                        print("Invalid Entry")
                        continue
user_name = show_homepage()
begin_game(user_name)




# T0-Do: 
            # Conditional If - Object Comparison Results :
            #   If user and computer chose the same option, it is a tie. 
            #	If one chose rock, and one chose scissors, rock has won. 
            #	If one chose scissors, and one chose paper, scissors has won. 
            # Announce the winner if there was one, or a tie if not. 

    # Ask the player if they want to try again. 
    # Quit if they say no, and start from the beginning if they say yes. 

# Input Player Name
# Keep Score / Print ScoreBoard 
# Leader Board for "Win Counts"- Dictionary- (User_Name : Win_Count-# )