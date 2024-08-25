questions = ("What is my name ?",
             "What is my age ?",
             "What i like you ?",
             "Which one is my best friend ?",
             "Which drink is my favarote ?",
)


answers = (
            ("A. Rakesh", "B. Mahesh", "C. Lalit", "D. Shubham"),
            ("A. 65", "B. 20", "C. 17", "D. 22"),
            ("A. Rain", "B. Summer", "C. Winter", "D. Noting"),
            ("A. Music", "B. Books", "C. Games", "D. Mobil"),
            ("A. Tea", "B. Water", "C. Juice", "D. Coffee"),
        )

ans = ("C", "B", "C", "A", "D")
gusses = []

index_num = 0
score = 0

print(ans[index_num])

        
for question in questions:
    print(question)
    for answer in answers[index_num]:
        print(answer)
        
    guess = input("Please Chosses one  of the above option : ").upper()
    print(guess)
    gusses.append(guess)
    
    if guess == ans[index_num]:
        print("Right Ans")
        score += 1
    else:
        print("Wrong Ans")

    
    print("\n") 
    index_num += 1
    
print(f"{score} out of {len(questions)} ")