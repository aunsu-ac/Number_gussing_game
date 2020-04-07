import random
win_no = random.randint(1,100) 
# can set this as win_no = 40
guess, game_ov = 1, False
inp = input("entar a number : ")

if inp:
    # convertng input to integer to string
    inp = int(inp)
    while not game_ov:
        if inp==win_no:
            print(f"you win, you tried {guess} times")
            game_ov =True
            input("press enter to close window..!")
            pass
        else:
            # nested if else
            if inp<win_no:
                print(f"{inp} is too low....!")
                pass
            else:
                print(f"{inp} is too high....!")
                pass
            # dry principal 1
            guess += 1
            inp = int(input("try again : "))
        pass
    
    pass
else:
    print("enter something inputs cant be empty")
    pass


