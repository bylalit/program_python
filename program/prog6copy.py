question = ("How many elements are in the periodic table?: ",
            "Which animal lays the largest eggs?: ",
            "What is the most gas in Earth's atmosphere?: ",
            "How many bones are in the human body?: ",
            "Which planet in the solar system is the hottest?: ")

ansewr = (("A. 116", "B. 117", "C. 118", "D. 119"),
          ("A. Whale", "B. Crocodile", "C. Elephant", "D. Ostrich"),
          ("A. Nitrogen", "B. Oxygen", "C. Carbon-Dioxide", "D. Hydrogen"),
          ("A. 206", "B. 207", "C. 208", "D. 209"),
          ("A. Mercury", "B. Venus", "C. Earth", "D. Mars")
          )

ans = ("C", "D", "A", "A", "B")
gusses = []

index_no = 0
for i in range(len(question)):
    print(question[i])
    for j in range(len(ansewr[index_no])):
        print(ansewr[index_no][j])
        index_no +=  1

        # \end{code}
