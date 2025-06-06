import random
a=['rock','paper','scissor']
print("lets play the game rock,paper,scissor")
your_choice=input("enter your choice")
print(f"your choice:{your_choice}")

comp_choice=random.choice(a)
print(f"computer choice:{comp_choice}")

if your_choice==comp_choice:
    print(f"both coice is {a} : match is tie")
elif your_choice=='rock':
    if comp_choice=='scissor':
        print("rock hits scissor:you win")
    else:
        print("paper covers rock:computer win")
elif your_choice=='paper':
    if comp_choice=='rock':
        print("paper covers rock: you win")
    else:
        print("scissor cuts paper:computer win")
else:
    if comp_choice=='rock':
        print("rock hits scissor: computer win")
    else:
        print("scissor cuts paper: you win")