from game_data import data
import random
import os

score = 0
random_choice_a = random.choice(data)
game_not_over = False
print("logo")
while not game_not_over:
    random_choice_b = random.choice(data)
    if random_choice_b == random_choice_a:
        random_choice_b = random.choice(data)
    # just to check the answers     
    ## print(f"com a {random_choice_a['follower_count']}")
    ## print(f"com b {random_choice_b['follower_count']}")
    print(f"Compare A: {random_choice_a['name']}, {random_choice_a['description']}, {random_choice_a['country']}")
    print("Vs")
    print(f"Against B: {random_choice_b['name']}, {random_choice_b['description']}, {random_choice_b['country']}")
    user_choice = input("who has more followers?Type 'A' or 'B': ").lower()
    if user_choice == "a":
        if random_choice_a['follower_count'] > random_choice_b['follower_count']:
            score += 1
            random_choice_a = random_choice_b
        else:
            game_not_over = True
    elif user_choice == "b":
        if random_choice_b['follower_count'] > random_choice_a['follower_count']:
            score += 1
            random_choice_a = random_choice_b
        else:
            game_not_over = True
    else:
        print("Enter a correct choice 'A' or 'B'")
    os.system("cls")
    if game_not_over:
        print(f"sorry, that's wrong.Final score :{score}")
    else:    
        print("logo")
        print(f"You are right current score :{score}")
    
    
