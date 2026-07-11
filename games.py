import random

while True:
    print("\n===== GAME HUB =====")
    print("1. Number Guessing Game")
    print("2. Rock Paper Scissors")
    print("3. Quiz Game")
    print("4. Exit")

    choice = input("Enter your choice: ")

    # Number Guessing Game
    if choice == "1":
        print("\n--- Number Guessing Game ---")
        secret = random.randint(1, 100)

        while True:
            guess = int(input("Guess a number (1-100): "))

            if guess == secret:
                print("🎉 Correct! You Won!")
                break
            elif guess < secret:
                print("📉 Too Low!")
            else:
                print("📈 Too High!")

    # Rock Paper Scissors
    elif choice == "2":
        print("\n--- Rock Paper Scissors ---")

        options = ["rock", "paper", "scissors"]

        player = input("Enter rock, paper, or scissors: ").lower()
        computer = random.choice(options)

        print("Computer chose:", computer)

        if player == computer:
            print("🤝 It's a Tie!")
        elif (
            (player == "rock" and computer == "scissors")
            or (player == "paper" and computer == "rock")
            or (player == "scissors" and computer == "paper")
        ):
            print("🎉 You Win!")
        else:
            print("😢 Computer Wins!")

    # Quiz Game
    elif choice == "3":
        print("\n--- Quiz Game ---")

        score = 0

        q1 = input("1. What is the capital of India? ")
        if q1.lower() == "new delhi":
            score += 1

        q2 = input("2. How many days are there in a week? ")
        if q2 == "7":
            score += 1

        q3 = input("3. Which programming language are you learning? ")
        if q3.lower() == "python":
            score += 1

        print("\nYour Score:", score, "/ 3")

        if score == 3:
            print("🏆 Excellent!")
        elif score == 2:
            print("👍 Good Job!")
        else:
            print("📚 Keep Practicing!")

    # Exit
    elif choice == "4":
        print("Thank You For Playing!")
        break

    else:
        print("❌ Invalid Choice!")