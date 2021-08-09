import random 
 # while True
 #Nhập biến current_player----human-----computer
 #cho current num = 1
 #Khi current num <= 21:---chia 2 trường hợp xử lý----1 là người---2 là máy(random)
 #nếu người nhập ngoài khoảng 123 thì cho nhập lại!(note)
while True:
    current_number  = 1 
    if random.randint(0, 1) == 0:
        current_player = "human"
    else:
        current_player = "computer"
    while current_number <= 21:
        print("The current number is " + str(current_number) + ".")
        print()
        if current_player == "human":
            print("Add 1,2,3 . Dont pass 21. The player who lands on 21 will lose")
            player_choice = int(input("What number you choose? "))
            while player_choice not in range(1,4):
                player_choice
            current_number = current_number + player_choice
            print()
            
            if current_number >= 21:
                print("The current number is " + str(current_number) + ".")
                print()
                print("Sorry, you lose.")
                break
            else:
                current_player = "computer"
        if current_player == "computer":
            computer_choice = random.randint(1,3)
            current_number = current_number + computer_choice
            print("The computer choose "+ str(computer_choice) + ".")
            print()
            if current_number >= 21:
                print("The current number is " + str(current_number) +".")
                print()
                print("Bingo.You won. Congrats!")
                break
            else:
                current_player = "human"

#INPUT xem người chơi có muốn chơi lại
    play_again = input("Do you want to play again?: ")
    if play_again.lower().startswith("y"):
        continue
    else:
        print("goodbye")
        break



