quest = ("How many elements are in the periodic table ?: ",
         "Which animal lays the largest eggs ?: ",
         "What is the most abundant gas in Earth's atmosphere ?: ",
         "How many bones are in the human body ?: ",
         "Which planet in the solar system is the hottest ?: ")
options = (("A. 116", "B. 117", "C. 118", "D. 119"),
           ("A. Whale", "B. Crocodile", "C. Elephant", "D. Ostrich"),
           ("A. Nitrogen", "B. Oxygen", "C. Carbon-Dioxide", "D. Hydrogen"),
           ("A. 206", "B. 207", "C. 208", "D. 209"),
           ("A. Mercury", "B. Venus", "C. Earth", "D. Mars"))
ans=("C", "D", "A", "A", "B")
guesses=[]
score=0
que_num=0

for ques in quest:
    print("-"*20)
    print(ques)
    for option in options[que_num]:
        print(option)
    guess = input("Enter your answer: ").upper()
    guesses.append(guess)
    if guess== ans[que_num]:
        print("Correct!")
        score+=1
    else:
        print("Incorrect!")
        print("The correct answer is", ans[que_num])
    que_num+=1

print("-------------------------------------")
print("               Results               ")
print("-------------------------------------")
print("Your answers: ", end="")
for answer in ans:
    print(answer, end=" ")
print()

print("Your guesses: ", end="")
for guess in guesses:
    print(guess, end=" ")
print()

score = int((score/len(quest))*100)
print("Your score is: ", score, "%")