# Quiz Game

questions = (
    "Who is this game created? ",
    "How many friends in this person? ",
    "What is the name of this game? ",
    "Which god pray this game oner? ",
    "Which is your favarate game? "
)

options = (
    ("A: Rahul",  "B: Lalit", "C: Ravi", "D: Rakesh"),
    ("A: 3", "B: 2", "C: 1", "D: Not countable"),
    ("A: Quiz Game", "B: Ludo", "C: Chess", "D: Carrom"),
    ("A: Vishnu", "B: Ganesh", "C: Shiva", "D: Brahma"),
    ("A: Cricket", "B: Football", "C: Hockey", "D: All"),
)

def game():
    answer = ('B', 'D', 'A', 'C', 'D')
    guess = []
    score = 0
    index_num = 0
    for question in questions:
        print("---------------------------")
        print(f"{index_num + 1}. {question}")
        for option in options[index_num]:
            print(option)
            
        guesses = input("Enter your answer (A/B/C/D): ").upper()
        guess.append(guesses)
        # print(guesses)
        # print(answer[index_num])
        if guesses == answer[index_num]:
            print("Correct answer!")
            score += 1
        else:
            print("Incorecct answer")
            print(f"{answer[index_num]} is a correct answer")
        print()
        
        index_num += 1

    print(f"Your score is {score} out of {len(questions)}")
    
if __name__ == "__main__":    
    game()