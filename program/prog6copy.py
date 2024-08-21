questions = ("1. How many elements are in the periodic table?: ",
            "2. Which animal lays the largest eggs?: ",
            "3. What is the most gas in Earth's atmosphere?: ",
            "4. How many bones are in the human body?: ",
            "5. Which planet in the solar system is the hottest?: ")

ansewr = (("A. 116", "B. 117", "C. 118", "D. 119"),
          ("A. Whale", "B. Crocodile", "C. Elephant", "D. Ostrich"),
          ("A. Nitrogen", "B. Oxygen", "C. Carbon-Dioxide", "D. Hydrogen"),
          ("A. 206", "B. 207", "C. 208", "D. 209"),
          ("A. Mercury", "B. Venus", "C. Earth", "D. Mars")
          )

anss = ("C", "D", "A", "A", "B")
gusses = []
score = 0
index_no = 0


for question in questions:
    print("------------------------")
    print(question)
    for ans in ansewr[index_no]:
        print(ans)
    
    guss = input("Selecte one option: ").upper()
    gusses.append(guss)   
        
    if guss == anss[index_no]:
        score += 1  
        print("Correct!")
    else:
        print("Wrong!")
  
    index_no += 1

print(anss)
print(gusses)
print(score)