import random
def comp():
    return random.choice(["rock","paper","scissor"])
hscore=0
cscore=0
while True:
    ab=["rock","paper","scissor"]
    print("\n== Rock Paper Scissor ==")
    hum=input("Enter your choice (rock,paper,scissor):").lower()
    while hum not in ab:
        print("Invalid choice.")
        hum=input("Enter your choice (rock,paper,scissor)").lower()
    com=comp()
    if hum==com:
        print("\nIt is tie.\n")
        print("You:",hscore,"\nComputer:",cscore)
    elif ((hum=='rock' and com=='scissor') or (hum=='paper' and com =='rock') or (hum=='scissor' and com=='paper')):
        print("\nYou won!!\n")
        hscore+=1
        print("You:",hscore,"\nComputer:",cscore)
    else:
        print("\nComputer wins!!\n")
        cscore+=1
        print("You:",hscore,"\nComputer:",cscore)
    a=input("Would you like to continue (yes or no):").lower()
    while a not in ['yes','y','no','n']:
        print("Invalid choice.Enter correct choice")
        a=input("Would you like to continue (yes or no):").lower()
    if a=='yes' or a=='y':
        continue
    else:
        print("Thank You !!!")
        break
